## What is this package? ##

Have you ever needed to take time input from a user, and convert it from their local timezone into UTC?
What a pain. How much nicer if that logic could be handled by the form, letting you validate and store normalized UTC time, and letting
your user only deal with their local timezone. 


## How to install ##

 1. Put the "timeforms" directory somewhere in your python path
 
 2. Done



## How to use ##
   
To automatically localize a form have it subclass either the UTCForm or UTCModelForm class, and pass in a pytz timezone as the timezone kwarg when creating the form instance.

    class MyForm(UTCModelForm):
        """
        Form for editing something rockin
        """
        pass
    form = MyForm(request.POST, timezone=timezone)

That will ensure that submitted and rejected forms are localized. 

To localize a form with intial data, an additional step of calling
form.convert_form_intial_to_local is required.

    form = MyForm(instance=my_instance, timezone=timezone)
    form.convert_form_initial_to_local()

That's it! Enjoy never having to convert time again.


