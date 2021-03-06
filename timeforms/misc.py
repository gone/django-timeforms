import pytz
import datetime

def convert_input_to_utc(timedate, timezone):
    """ Converts the input datetime into an unstamped UTC datetime"""
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
    """Converts a utc datetime into a stamped localized datetime"""
    if not timezone or not timedate:
        return timedate
    if isinstance(timedate, basestring):
        timedate = datetime.datetime.strptime(timedate, "%m/%d/%Y %H:%M")
    timedate = timedate.replace(tzinfo=pytz.utc)
    timedate = timedate.astimezone(timezone)
    return timedate

def convert_output_to_local(timedate, timezone, format="%m/%d/%Y %H:%M"):
    """Converts a utc datetime into a localized datetime string in the provided format"""
    timedate = convert_initial_to_local(timedate, timezone)
    return datetime.datetime.strftime(timedate, format)

