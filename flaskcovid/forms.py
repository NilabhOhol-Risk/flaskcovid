from flask_wtf import FlaskForm
from wtforms import Form,FloatField, validators
from wtforms.validators import DataRequired, Length, Email


class InputForm(Form):
    input1 = FloatField('Input 1',validators=[validators.InputRequired()])
    input2 = FloatField('Input 2',validators=[validators.InputRequired()])
