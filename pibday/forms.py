from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from pibday.validators import NumCheck


class BdayForm(FlaskForm):
    month_rg = [1, 12]
    day_rg = [1, 31]
    year_rg = [0, 9999]
    month = StringField('Month', validators=[NumCheck(min_val=1, max_val=12), InputRequired()])
    day = StringField('Day', validators=[NumCheck(min_val=1, max_val=31), InputRequired()])
    year = StringField('Year', validators=[NumCheck(min_val=0, max_val=9999), InputRequired()])
    submit = SubmitField('Submit')
