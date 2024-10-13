from models import Event, User

event_key = 'some_event_key'
try:
    event = Event.objects.get(event_key=event_key)
    print(event.name, event.description, event.start_time, event.end_time)
except Event.DoesNotExist:
    print("Event not found")