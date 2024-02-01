from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField, FloatField
from wtforms import EmailField

from wtforms.validators import DataRequired, Email

class UserFormDistance(Form):
  distanciaX = FloatField('distanciaX')
  distanciaX2 = FloatField('distanciaX2')
  distanciaY = FloatField('distanciaY')
  distanciaY2 = FloatField('distanciaY2')
  