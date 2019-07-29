from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField,validators, ValidationError
from wtforms.fields.html5 import DateField,DateTimeLocalField
from datetime import datetime

class AddOwnerForm(FlaskForm):
    firstname = TextField("First Name",[validators.Required("First name is required.")])
    lastname = TextField("Last Name",[validators.Required("Last name is required.")])
    email = TextField("Email",
                    [validators.Required("Email address is required."),
                        validators.Email("Enter a valid email address.")])
    phone = TextField("Phone Number",[validators.Required("Phone Number is required.")])

    submit = SubmitField("Send")

class AddPetForm(FlaskForm):
    name = TextField("Name",[validators.Required(" name is required.")])
    birthdate = DateField("Birthday", format='%Y-%m-%d', validators=[validators.DataRequired()])
    type = TextField("Type",[validators.Required("Type is required.")])
    comment = TextField("Phone Number",[validators.Required("comment is required.")])

    submit = SubmitField("Send")


class AddOwnerPetForm(FlaskForm):
    ownerid=IntegerField("Owner ID",[validators.Required("Owner ID is required.")])
    petid=IntegerField("Pet ID",[validators.Required("Pet ID is required.")])
    submit = SubmitField("Send")


class AddVisitForm(FlaskForm):
    ownerid=IntegerField("Owner ID",[validators.Required("Owner ID is required.")])
    petid=IntegerField("Pet ID",[validators.Required("Pet ID is required.")])
    scheduled_time= DateTimeLocalField('Scheduled Time?',
                        format='%Y-%m-%dT%H:%M:%S',
                        default=datetime.today,
                        validators=[validators.DataRequired()])
    submit = SubmitField("Send")


class UpdateVisitCheckinForm(FlaskForm):
    visit_id=IntegerField("Visit ID",[validators.Required("Visit ID is required.")])
    checkin_time= DateTimeLocalField('Checkin Time',
                        format='%Y-%m-%dT%H:%M:%S',
                        default=datetime.today,
                        validators=[validators.DataRequired()])
    submit = SubmitField("Send")


class UpdateVisitNotesForm(FlaskForm):
    visit_id=IntegerField("Visit ID",[validators.Required("Visit ID is required.")])
    notes= TextField("Notes",[validators.Required("Notes is required.")])
    submit = SubmitField("Send")

class AddVaccinationRecordForm(FlaskForm):

    pet_id =IntegerField("Pet ID",[validators.Required("Pet ID is required.")])
    vaccine_name =TextField("Vaccine Name",[validators.Required("Vaccine Name is required.")])
    vaccine_details =TextField("Vaccine Details",[validators.Required("Vaccine Details is required.")])
    vaccination_date = DateField("Vaccine Date", format='%Y-%m-%d', validators=[validators.DataRequired()])
    expiration_date= DateField("Expiration Date Date", format='%Y-%m-%d', validators=[validators.DataRequired()])
    submit = SubmitField("Send")

class OwnerRecordLookupForm(FlaskForm):
    firstname = TextField("First Name",[validators.Required("First name is required.")])
    lastname = TextField("Last Name",[validators.Required("Last name is required.")])
    submit = SubmitField("Send")

class PetLookupForm(FlaskForm):
    petname = TextField("Pet Name",[validators.Required("Pet name is required.")])
    submit = SubmitField("Send")


class PetsForOwnerForm(FlaskForm):
    owner_id =IntegerField("Owner ID",[validators.Required("Owner ID is required.")])
    submit = SubmitField("Send")

class OwnersForAPetForm(FlaskForm):
    pet_id =IntegerField("Pet ID",[validators.Required("Pet ID is required.")])
    submit = SubmitField("Send")


class DeleteAVisitForm(FlaskForm):
    visit_id =IntegerField("Visit ID",[validators.Required("Visit ID is required.")])
    submit = SubmitField("Send")

class DeleteAnOwnerForm(FlaskForm):
    owner_id =IntegerField("Owner ID",[validators.Required("Owner ID is required.")])
    submit = SubmitField("Send")

class DeleteOwnerPetRelationshipForm(FlaskForm):
    pet_id =IntegerField("Pet ID",[validators.Required("Pet ID is required.")])
    owner_id =IntegerField("Owner ID",[validators.Required("Owner ID is required.")])
    submit = SubmitField("Send")
