from aiohttp import web
import socketio
import sys
sys.path.append('/home/nate/ASAP/Log')
sys.path.append('/home/nate/ASAP/DataBase_Scrape/')
from LogASAP import log, setup_log, LogASAP, LOG_ERROR, LOG_INFO
import json
from time import time
import Schedule 
import ScheduleofClasses
from multiprocessing import Process
import asyncio

# Global assignments, plus they need to run first. 
static_path = None
# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)


class User(): # implicit inheritance from object Python 3.x
    """
    defines a user object to store user information while connected to a socket. 
    """
    def __init__(self, sid, address, course_list=None, preferences=None, personal_events=None):
        """
        Parameters:
            sid -- socket id
            course_list -- dict of User course
            preferences -- dict of User course preferences 
        """
        self.sid = sid # socket id 
        self.address = address
        self.course_list = course_list # User selected courses
        self.preferences = preferences # User chosen preferences
        self.personal_events = personal_events # User's personal events
        self.schedule = {} # set by generate schedule
        self.data = []

async def index(request):
    """
    handler for index GET requests
    """
    log('Index requested by {client_address}'.format(client_address=request.remote) )
    with open(static_path+'main.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect')
async def new_connection(sid, environ):
    """
    Sets up a User object for each session. A single computer can have multiple sessions and sockets open.
    """
    address = environ['aiohttp.request'].remote
    await sio.save_session(sid, {'user': User(sid=sid, address=address), 'address' : address}) # save information about the user
    
    log("New session for host: " + address)

@sio.on('disconnect')
async def remove_connection(sid):
    session = await sio.get_session(sid=sid)
    log('Connection ended: ' + session['address'] ) 

@sio.on('message')
async def print_message(sid, message):
    """
    Generic message handler mostly for testing
    """
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    log("Socket ID: "  + sid + ' message: ' + str(message))


@sio.on('generate')
async def receive_schedule(sid, data):
    """
    event handler for when a User attempts to generate a schedule
    """
    session = await sio.get_session(sid)
    log('Generate schedule reqeuest from: ' + session['address'])
    await sio.emit('comfirmation', 'Data Received. Optimizing Schedule...', room=sid) # NOTE typo on the UI for comfirmation, should be confirmation
    user = session['user']
    user.input_data = data
    try:
        sio.start_background_task(target=generate_schedule, args=user) # this library's use of asyncio is questionable. 
    except Exception as e:
        log('Something went wrong', level=LOG_ERROR, err_str=str(e))
    
async def generate_schedule(args):
    """
    Middle man between socket server and Schedule.py. This allows for proper asynchronous calls so we 
    don't slow down the webserver.
    Paremters: 
        input_data: raw data string from the client.
        user: user object pertaining to who requested the schedule
    """
    user = args

    input_dict = json.loads(user.input_data) 
    log('input_dict\n' + str(input_dict))
    user_courses = input_dict['course']
    currentTerm = input_dict['currentTerm']
    personalEvents = input_dict['personalEvent']

    waitlist_okay = False
    if input_dict['waitlistStat'].upper() == 'TRUE':
        waitlist_okay = True

    start_time = time()
    must_haves, could_haves = ScheduleofClasses.get_section_pairings(user_courses=user_courses, termCode=currentTerm, \
        personalEvents=personalEvents, waitlist_okay=waitlist_okay)
    log(message='get_section_pairings took ' + str(round(time()-start_time,5)))

    log('must_haves:\n' + str(must_haves) + '\nwant_to_haves: \n' + str(could_haves) + '\nprefs: \n:' + str(input_dict['preference']))
    
    start_time = time()
    user.schedule = Schedule.generateSchedule(must_haves=must_haves, want_to_haves=could_haves, \
        preferences=input_dict['preference'])
    log(message='generateSchedule took'+ str(round(time()-start_time,5)))
    
    log('Schedule: \n' + str(user.schedule)) # save raw output of schedule

    new_display, new_schedule = convert_schedule(user)

    # test_schedule = json.dumps(test)
    log("Converted Schedule:\n" + str(new_schedule) + '\n' + str(new_display))
    display_schedule = json.dumps({'display': new_display, 'schedule': new_schedule}) # json to string 
    await sio.emit('schedule_ready', display_schedule, room=user.sid)
    log('Sent schedule to: ' + str(user.address))

def convert_schedule(user: User):
    """
    converts a generated schedule into the correct format needed to display it on the UI calendar and table
    """
    dayCodeDict = { 'SU' : 0, 'MO' : 1, 'TU' : 2, 'WE' : 3, 'TH' : 4, 'FR' : 5, 'SA' : 6} # days of the week constants
    new_display = [] 
    new_schedule = []
    test = [{'id': 'personal event', 'meetings': [['MO', 700, 730], ['WE', 700, 730]], 'finals': [], 'midterms': [], 'LE id': 'personal event'}, {'meetings': [['TU', 1100, 1220], ['TH', 1100, 1220], ['MO', 1100, 1150]], 'finals': ['WE', 1130, 1429], 'midterms': [], 'LE id': '016900', 'id': '016901', 'waitlist': False}] 
    '''
   'display': [{name: 'CSE 100',
            'professor': 'Paul Cao',
            'days': 'MWF',
            'start': '9:00 AM',
            'end': '9:50 AM'}], 
    '''
    for course in user.schedule:
        if course['id'] == course['LE id']:
            ids = [course['id']]
        else:
            ids = [course['id'], course['LE id']]
        # get meetings for both
        if ids[0] != 'personal event':
            for ID in ids: 
                if ID != '': # skip this
                    response = ScheduleofClasses.getSectionByID(sectionID=ID)
                    section = response['sections'][0] # only returns a single section
                    title = response['subjectCode'] + ' ' + response['courseCode'] + ' ' + section['instructionType'] +\
                        ' ' + section['sectionCode'] 
                    daysOfWeek = []
                    daysDisplay = []
                    professor = '' # no prof listed
                    staff = True
                    for prof in section['instructors']:
                        staff = False
                        professor += prof['instructorName'] + ' '
                    if staff:
                        professor = 'staff'
                    # professor = section['instructors'][0]['instructorName']
                    for meeting in section['recurringMeetings']:
                        daysDisplay.append(meeting['dayCode'])
                        dayCode = dayCodeDict[meeting['dayCode']] # convert dayCode to a number e.g. SU to 0
                        daysOfWeek.append(dayCode) # separate for debugging
                        startTime = convertTime(meeting['startTime'])
                        endTime = convertTime(meeting['endTime'])
                    # enrolled = section['enrolledQuantity']
                    # capacity = section['capacityQuantity']
                    # print('enrolled: ', enrolled, ' capacity: ', capacity)
                    waitlist = course['waitlist']# (enrolled == capacity) and capacity > 0 # stupid edge cases, I hate Schedule of Classes
                    new_schedule.append({'title': title, 'startTime': startTime, 'endTime': endTime, 'daysOfWeek': daysOfWeek})
                    new_display.append({'name': title, 'professor': professor, 'days':daysDisplay, 'start' : startTime, 'end': endTime, 'waitlisted': waitlist})
        else: #personal event
            dayCode = []
            for meeting in course['meetings']:
                dayCode.append(dayCodeDict[meeting[0]])
                startTime = convertTime(str(meeting[1]))
                endTime = convertTime(str(meeting[2]))
            new_schedule.append({'title': ids[0], 'startTime': startTime, 'endTime': endTime, 'daysOfWeek': dayCode, 'waitlisted': False})
    
    return [new_display, new_schedule]

def convertTime(time: str):
    """
    Converts from Schedule of Classes format e.g. 1200 to 12:00:00
    """
    if len(time) < 4:
        time = time[:1] + ':' + time[1:] + ':00'
    else:
        time = time[:2] + ':' + time[2:] + ':00'
    return time

test = """
    'display': [{name: 'CSE 100',
            'professor': 'Paul Cao',
            'days': 'MWF',
            'start': '9:00 AM',
            'end': '9:50 AM'}],
    'schedule': [{ 'title': 'CSE 110',
                'startTime': '9:00:00',
                'endTime': '9:50:00',
                'daysOfWeek': [1,3,5]}
                ]
}
"""
test = {'display': [{'name' : 'CSE 100', 'professor': 'Paul Cao', 'days' : 'MWF', 'start':'9:00 AM', 'end': '9:50 AM'}],\
        'schedule' : [{'title': 'CSE 110', 'startTime': '9:00:00', 'endTime': '9:50:00', 'daysOfWeek': [1,3, 5]}] }


def main():
    """ 
    prep necessary routes then start the server. 
    """
    setup_log() # default log level is debug
    # router
    global static_path
    static_path = '/var/www/html/src/' # base bath to all of the static files. 
    # static_path = '/home/nate/ASAP/Frontend/'
    app.router.add_get('/', index) # redirect to index on initial visit. 
    app.router.add_static('/', static_path) # automatically add routes for everything else
    # app.add_routes([web.static('/', static_path)]) # this works 
    # We kick off our server
    log('Starting ASAP socket server')
    try:
        web.run_app(app, host='asap.ucsd.edu', port=80) # this is blocking
        # web.run_app(app) # localhost for debugging. Doesn't require root to run
        log('Stoppping ASAP socket server')
    except Exception as e:
        log('The server messed up', level=LOG_ERROR, email=False, err_str=str(e))

if __name__ == '__main__':
    main()
    # must_takes = [[{'meetings': [['TU', 1100, 1220], ['TH', 1100, 1220], ['MO', 1100, 1150]], 'finals': ['WE', 1130, 1429], 'midterms': [], 'LE id': '016900', 'id': '016901'}]]
    # want_to_takes = []
    # preference = {'prof_rating':'false','avg_gpa':'false','avg_time':'true','class_days':'none','time_pref':'none','gap':'none'}
    # schedules = Schedule.generateSchedule(must_takes,want_to_takes,preference)
    # print(schedules)
    # convert_schedule(user=None)