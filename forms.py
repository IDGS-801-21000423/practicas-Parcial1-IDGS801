from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField, FloatField, SelectField, RadioField
from wtforms import EmailField

from wtforms.validators import DataRequired, Email

class UserFormDistance(Form):
  distanciaX = FloatField('distanciaX')
  distanciaX2 = FloatField('distanciaX2')
  distanciaY = FloatField('distanciaY')
  distanciaY2 = FloatField('distanciaY2')



class UserFormColors(Form):
  banda1 = SelectField ('banda1', choices=[
    (0, "Negro"),
    (1, "Cafe"),
    (2, "Rojo"),
    (3, "Naranja"),
    (4, "Amarillo"),
    (5, "Verde"),
    (6, "Azul"),
    (7, "Violeta"),
    (8, "Gris"),
    (9, "Blanco")
    ])
  banda2 = SelectField('banda2', choices=[
    (0, "Negro"),
    (1, "Cafe"),
    (2, "Rojo"),
    (3, "Naranja"),
    (4, "Amarillo"),
    (5, "Verde"),
    (6, "Azul"),
    (7, "Violeta"),
    (8, "Gris"),
    (9, "Blanco")
  ])
  banda3 = SelectField('banda3', choices=[
    (1, "Negro (X1)"),
    (10, "Cafe (X10)"),
    (100, "Rojo (X100)"),
    (1000, "Naranja (X1000)"),
    (10000, "Amarillo (X10000)"),
    (100000, "Verde (X100000)"),
    (1000000, "Azul (X1000000)"),
    (10000000, "Violeta (X10000000)"),
    (100000000, "Gris (X100000000)"),
    (1000000000, "Blanco (X1000000000)")
  ])
  tol = RadioField('tol')