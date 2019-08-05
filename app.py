#! /Users/ryagomes/Desktop/Workspace/PythonEnvironments/CS340Databases/bin/python
import database
from flask import Flask, render_template, request, flash
from forms import *

app = Flask(__name__)
# A secret key is required to use wtforms in flask
app.config['SECRET_KEY'] = 'sample-secret-key'

@app.route('/')
def appIndex():
    # return '<h3>Hello, world from Flask!</h3>'
    params = {'welcomeMessage': 'Hello and welcome to the Veterinary Practice Flask App!'}
    return render_template('index.html', params=params)


@app.route('/AddOwner', methods = ['GET', 'POST'])
def AddOwner():
    form = AddOwnerForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addOwner.html', form = form)
        else:
            # insert into owners values (null, :first_name, :last_name, :email, :phone);
            
            mysqlConn = database.connectMySql()
            with mysqlConn.cursor() as cursor:
                insert_stmt = (
                    "insert into owners ( first_name, last_name, email, phone)"
                    "values ( %s, %s, %s, %s);"
                )
                data = (request.form["firstname"],
                        request.form["lastname"],
                        request.form["email"],
                        request.form["phone"])
                cursor.execute(insert_stmt, data)
            mysqlConn.commit()

            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/addOwner.html', form = form)


@app.route('/AddPet', methods = ['GET', 'POST'])
def AddPet():
    form = AddPetForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addPet.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/addPet.html', form = form)

@app.route('/AddVisit', methods = ['GET', 'POST'])
def AddVisit():
    form = AddVisitForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addVisit.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/addVisit.html', form = form)

@app.route('/AddOwnerPet', methods = ['GET', 'POST'])
def AddOwnerPet():
    form = AddOwnerPetForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addOwnerPet.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/addOwnerPet.html', form = form)



@app.route('/UpdateVisitCheckin', methods = ['GET', 'POST'])
def UpdateVisitCheckin():
    form = UpdateVisitCheckinForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/updateVisitCheckin.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/updateVisitCheckin.html', form = form)


@app.route('/UpdateVisitNotes', methods = ['GET', 'POST'])
def UpdateVisitNotes():
    form = UpdateVisitNotesForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/updateVisitNotes.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/updateVisitNotes.html', form = form)




@app.route('/AddVaccinationRecord', methods = ['GET', 'POST'])
def AddVaccinationRecord():
    form = AddVaccinationRecordForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addVaccinationRecord.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/addVaccinationRecord.html', form = form)


@app.route('/OwnerRecordLookup', methods = ['GET', 'POST'])
def OwnerRecordLookup():
    form = OwnerRecordLookupForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/ownerRecordLookup.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/ownerRecordLookup.html', form = form)


@app.route('/PetLookup', methods = ['GET', 'POST'])
def PetLookup():
    form = PetLookupForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/petLookup.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/petLookup.html', form = form)


@app.route('/PetsForOwner', methods = ['GET', 'POST'])
def PetsForOwner():
    form = PetsForOwnerForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/petsForOwner.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/petsForOwner.html', form = form)


@app.route('/OwnersForAPet', methods = ['GET', 'POST'])
def OwnersForAPet():
    form = OwnersForAPetForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/ownersForAPet.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/ownersForAPet.html', form = form)


@app.route('/DeleteAVisit', methods = ['GET', 'POST'])
def DeleteAVisit():
    form = DeleteAVisitForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/deleteAVisit.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/deleteAVisit.html', form = form)


@app.route('/DeleteAnOwner', methods = ['GET', 'POST'])
def DeleteAnOwner():
    form = DeleteAnOwnerForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/deleteAnOwner.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/deleteAnOwner.html', form = form)


@app.route('/DeleteOwnerPetRelationship', methods = ['GET', 'POST'])
def DeleteOwnerPetRelationship():
    form = DeleteOwnerPetRelationshipForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/deleteOwnerPetRelationship.html', form = form)
        else:
            return render_template('success.html', passed_form_data=request.form)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/deleteOwnerPetRelationship.html', form = form)


@app.route('/ViewExpiredVaccinations')
def ViewExpiredVaccinations():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql='select * from vaccinations where expiration_date<=NOW();'
        cursor.execute(sql)
        result = cursor.fetchall()
        params = result

    return render_template('dbInteractionTemplates/viewExpiredVaccinations.html', params=params)


@app.route('/diagnostic')
def diagnostic():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql='SELECT * FROM diagnostic;'
        cursor.execute(sql)
        result = cursor.fetchall()
    return '<h3>' + str(result) + '</h3>'

if __name__=='__main__':
    # to run with debug=True, add python shebang (#! /path/to/env/python) on top
    # https://stackoverflow.com/a/55272071
    app.run(port=8619, debug=True)

    # to run on flip and access via url, specify host
    #app.run(port=8619, host='flip1.engr.oregonstate.edu')
