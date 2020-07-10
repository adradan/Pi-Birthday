from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange, ValidationError


class NumCheck:
    def __init__(self, min_val=0, max_val=0):
        self.min = min_val
        self.max = max_val
        message = f'Only numbers from {self.min} to {self.max} are allowed.'
        self.message = message

    def __call__(self, form, field):
        try:
            usr_str = int(field.data)
            if usr_str < self.min or usr_str > self.max:
                raise ValidationError(self.message)
        except ValueError:
            raise ValidationError(self.message)
