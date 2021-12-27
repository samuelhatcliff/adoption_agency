from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    '''form to add a new pet. Name required'''
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])  
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)])  
    notes = StringField("Notes", validators=[Optional()])
    
    
class EditPetForm(FlaskForm):
    '''form to edit existing pet. only photo_url, notes, and avalablity can be changed
    to ensure that critical information is not lost'''
    photo_url = StringField("Photo Url", validators=[Optional(), URL()])  
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")