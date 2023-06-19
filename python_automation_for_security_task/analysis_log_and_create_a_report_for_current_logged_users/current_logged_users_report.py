# sorting key function
def get_event_date(event):
    return event.date

# find out the current users from the events
def current_users(events):
    # sort() events by event date
    events.sort(key = get_event_date)
    # store the logged users machine and user set into the machines dictionary
    machines = {}
    # run for loop through the events and store machine and users name information for logged users and remove the logout users name from 
    # the corresponding set 
    for event in events:
        # check if the event machine exist in the machines dictionary. If not then add machines[event.machine]=set()
        if event.machine not in machines:
            machines[event.machine] = set()
        # check if the event.type == log then add the value to the corresponding machine set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        # check if the user in the corresponding machine set() and type is logout then remove the user from the set()
        if event.user in machines[event.machine] and event.type == 'logout':
            machines[event.machine].remove(event.user)
    return machines


# creat Event class for creating event objects or instances
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# creat a events list by using Event class
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]


# make a report with current logged usrs list:
# the report will look like: macine name: logged_user_name_separated_by_comma

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            log_users = ", ".join(users)
            print("{}: {}".format(machine, log_users))



# Call the generate_report(events) function and test the result. You will get the following result -> webserver.local: lane
generate_report(current_users(events))