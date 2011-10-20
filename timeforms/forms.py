from django import forms
from django.forms import fields

from misc import convert_input_to_utc, convert_initial_to_local

def get_form_full_clean(form_class):
    def form_full_clean(form):
        converted = form.data.copy()
        for name, data in form.data.iteritems():
            if not name in form.fields:
                continue
            if isinstance(form.fields.get(name, None), fields.DateTimeField) or isinstance(form.fields.get(name, None), fields.TimeField):
                value = form.fields[name].widget.value_from_datadict(form.data, form.files, form.add_prefix(name))
                converted[name] = convert_input_to_utc(value, form.timezone)
            else:
                converted[name] = form.data[name]
        form.data = converted
        return super(form_class, form).full_clean()
    return form_full_clean


def convert_form_initial_to_local(form):
    converted = form.initial.copy()
    for name, field in form.fields.iteritems():
        if not name in form.initial:
            continue
        value = form.initial[name]
        if isinstance(field, fields.DateTimeField) or isinstance(field, fields.TimeField):
            value = convert_initial_to_local(value, form.timezone)
        converted[name] = value
    form.initial = converted
    

def get_form_post_clean(form_class):
    def form_post_clean(form, *args, **kwargs):
        if form._errors:
            converted = form.data.copy()
            for name, field in form.fields.iteritems():
                if not name in form.data:
                    continue
                value = form.data[name]
                if isinstance(field, fields.DateTimeField) or isinstance(field, fields.TimeField):
                    value = convert_initial_to_local(value, form.timezone)
                converted[name] = value
            form.data = converted
        super(form_class, form)._post_clean(*args, **kwargs)
    return form_post_clean

class UTCForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.timezone = kwargs.pop('timezone')
        super(UTCForm, self).__init__(*args, **kwargs)

UTCForm.full_clean = get_form_full_clean(UTCForm)
UTCForm._post_clean = get_form_post_clean(UTCForm)
UTCForm.convert_form_initial_to_local = convert_form_initial_to_local

class UTCModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.timezone = kwargs.pop('timezone')
        super(UTCModelForm, self).__init__(*args, **kwargs)

    

UTCModelForm.full_clean = get_form_full_clean(UTCModelForm)
UTCModelForm._post_clean = get_form_post_clean(UTCModelForm)
UTCModelForm.convert_form_initial_to_local = convert_form_initial_to_local
