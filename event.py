class Schedule:
    def __init__(self,time,desc):
        self.time=time
        self.desc=desc
    def __str__(self):
        print(self.)

class Attendee:
    def __init__(self,a_id,a_name,a_company,a_feedback=None):
        self.a_id=a_id
        self.a_name=a_name
        self.a_company=a_company
        self.a_feedback=a_feedback
    def __str__(self):
        print("ID",self.)
        print("Name :",self.a_name)
        print("Company :",self.a_company)
        print("Feedback :",self.a_feedback if self.a_feedback is not None else)

    def set_feedback(self,feedback):
        self.a_feedback=feedback

class Event:
    def __init__(e_id,e_name,e_start,e_end):
        self.e_id=e_id
        self.e_name=e_name
        self.e_start=e_start
        self.e_end=e_end
        self.schedule=[]
        self.attendes=[]
    def __str__(self):
        print("Event details for :",self.e_id)
        print("Event Name :",self.e_name)
        print("Start at :",self.e_start)
        print("End at :",self.e_end)

        if len(self.schedule)==0:
            print("there is no shedule")
        else:
            print("Event shedules are")
            for Schedule in self.add_shedules:

    def add_shedule(self,time,desc):
        schedule=Schedule(time,desc)
        self.shedule.append(schedule)
    def add_attendee(self,id,name,company,feedback=None):
        attendee=Attendee(id,name,company,feedback)
        self.attendes.append(attendee)

# Bulding all the core functionalites
events={}
# the events is a dict which holds the events that the manager is adding using the key event_id and the values is the object of a event

"""
events={
E_4R5 : {
    e_id:E_4R5,
    e_name:"Grand meetup",
    e_start:"4/05/2025",
    e_end:"6/05/2025",
    schedules:[{"12:00":"Introduction of meeting"},{"01:00":"Given the thanks to imp persons"}],
    attendees:[{id:A_4Y3,name:"Nani",company:"wipro",feedback:"Good developer"},{id:A_4Y4,name:"Jyo",company:"Google",feedback:"Good scrum"}]
}    
}
"""
# Create Event
def create_event(id,name,start,end):
    if id not in events:
        event=Event(id,name,start,end)
        events[id]=
    else:
        raise Exception("Event Already Exists...")
    def show_events():
        for e_id in events:
            print(event[e_id])

create_event("E_4Y5","Developer Camp","04/05/2025","06/05/2025")
show_employees()














# 