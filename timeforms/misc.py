import new
import pytz
import datetime

def add_method(cls, func, method_name):
    """Patches a class with an instance using the given values"""

    method = new.instancemethod(func, cls, cls)
    name = method_name
    setattr(cls, name, method)    
    return name


def convert_input_to_utc(timedate, timezone):
    if not timezone or not timedate:
        return timedate
    if isinstance(timedate, basestring):
        timedate = datetime.datetime.strptime(timedate, "%m/%d/%Y %H:%M")
    #first make sure the date is represented as the user would see it
    try:
        timedate = timezone.localize(timedate)
    except ValueError:
        pass #this already has a tzz
    # convert that sucker
    timedate = timedate.astimezone(pytz.utc)
    #and finally strip off the timezone, sine mysql won't let us save it with it and we want to be db independent.
    timedate = timedate.replace(tzinfo=None)
    return timedate

def convert_initial_to_local(timedate, timezone):
    if not timezone or not timedate:
        return timedate
    if isinstance(timedate, basestring):
        timedate = datetime.datetime.strptime(timedate, "%m/%d/%Y %H:%M")
    timedate = timedate.replace(tzinfo=pytz.utc)
    timedate = timedate.astimezone(timezone)
    return timedate

def convert_output_to_local(timedate, timezone):
    timedate = convert_initial_to_local(timedate, timezone)
    
    return datetime.datetime.strftime(timedate, "%m/%d/%Y %H:%M")

