import wtforms

from wtforms import validators


class EventForm(wtforms.form.Form):
    name = wtforms.StringField(validators=[validators.DataRequired()])
    start_date = wtforms.DateField(validators=[validators.DataRequired()])
    end_date = wtforms.DateField(validators=[validators.DataRequired()])
    url = wtforms.URLField()
    notes = wtforms.TextAreaField()
