import database
from flask import Flask, render_template, request, flash, redirect
from forms import *

app = Flask(__name__)
# A secret key is required to use wtforms in flask
app.config['SECRET_KEY'] = 'sample-secret-key'

@app.route('/')
def appIndex():
    params = {'welcomeMessage': 'Hello and welcome to the Veterinary Practice Flask App!'}
    return render_template('index.html', params=params)


@app.route('/add_owner', methods = ['GET', 'POST'])
def add_owner():
    form = AddOwnerForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('dbInteractionTemplates/add_owner.html', form = form)
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

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            flash('Successfully added new owner')
            return redirect('/owners')
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/add_owner.html', form = form)


@app.route('/add_pet', methods = ['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/add_pet.html', form = form)
        else:

            mysqlConn = database.connectMySql()
            with mysqlConn.cursor() as cursor:
                insert_stmt = (
                    "insert into pets ( name, birthdate, pet_type, comment)"
                    "values ( %s, %s, %s, %s);"
                )
                data = (request.form["name"],
                        request.form["birthdate"],
                        request.form["type"],
                        request.form["comment"])
                cursor.execute(insert_stmt, data)
            mysqlConn.commit()

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            flash('Successfully added new pet')
            return redirect('/pets')
    elif request.method == 'GET':

        return render_template('dbInteractionTemplates/add_pet.html', form = form)

@app.route('/AddVisit', methods = ['GET', 'POST'])
def AddVisit():
    if request.method == 'POST':
        mysqlConn = database.connectMySql()
        with mysqlConn.cursor() as cursor:
            insert_stmt = (
                "insert into visits ( owner_id, pet_id, scheduled_time)"
                "values ( %s, %s, %s);"
            )
            data = ((request.form["owner_id"]),
                    (request.form["pet_id"]),
                    request.form["scheduled_time"])

            cursor.execute(insert_stmt, data)
        mysqlConn.commit()

    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        cursor.execute('select * from visits')
        visits = cursor.fetchall()

        cursor.execute('select id, name from pets')
        pets = cursor.fetchall()

        cursor.execute('select id, first_name, last_name from owners')
        owners = cursor.fetchall()
    return render_template('dbInteractionTemplates/addVisit.html', visits=visits, pets=pets, owners=owners)

@app.route('/AddOwnerPet', methods = ['GET', 'POST'])
def AddOwnerPet():
    mysqlConn = database.connectMySql()
    form = AddOwnerPetForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            with mysqlConn.cursor() as cursor:
                cursor.execute('select id, first_name, last_name from owners')
                owners = cursor.fetchall()
                cursor.execute('select id, name from pets')
                pets = cursor.fetchall()
            return render_template('dbInteractionTemplates/addOwnerPet.html', form=form, owners=owners, pets=pets)
        else:

            with mysqlConn.cursor() as cursor:
                insert_stmt = (
                    "insert into owners_pets ( owner_id, pet_id)"
                    "values ( %s, %s);"
                )
                data = ((request.form["ownerid"]),
                        (request.form["petid"]))

                cursor.execute(insert_stmt, data)
            mysqlConn.commit()

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':
        with mysqlConn.cursor() as cursor:
            cursor.execute('select id, first_name, last_name from owners')
            owners = cursor.fetchall()
            cursor.execute('select id, name from pets')
            pets = cursor.fetchall()
        return render_template('dbInteractionTemplates/addOwnerPet.html', form = form, owners=owners, pets=pets)



@app.route('/UpdateVisitCheckin', methods = ['GET', 'POST'])
def UpdateVisitCheckin():
    form = UpdateVisitCheckinForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/updateVisitCheckin.html', form = form)
        else:

            mysqlConn = database.connectMySql()
            with mysqlConn.cursor() as cursor:
                update_stmt = (
                    "update visits set checkin_time=%s where id=%s;"
                )
                data = ((request.form["checkin_time"].replace("T"," ")),
                        (request.form["visit_id"]))
                cursor.execute(update_stmt, data)
            mysqlConn.commit()

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':

        mysqlConn = database.connectMySql()
        with mysqlConn.cursor() as cursor:
            sql='select * from visits;'
            cursor.execute(sql)
            result = cursor.fetchall()
            params = result

        return render_template('dbInteractionTemplates/updateVisitCheckin.html', form = form, params=params)


@app.route('/UpdateVisitNotes', methods = ['GET', 'POST'])
def UpdateVisitNotes():
    form = UpdateVisitNotesForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/updateVisitNotes.html', form = form)
        else:

            mysqlConn = database.connectMySql()
            with mysqlConn.cursor() as cursor:
                update_stmt = (
                    "update visits set notes=%s where id=%s;"
                )
                data = ((request.form["notes"]),
                        (request.form["visit_id"]))
                cursor.execute(update_stmt, data)
            mysqlConn.commit()

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':

        mysqlConn = database.connectMySql()
        with mysqlConn.cursor() as cursor:
            sql='select * from visits;'
            cursor.execute(sql)
            result = cursor.fetchall()
            params = result

        return render_template('dbInteractionTemplates/updateVisitNotes.html', form = form, params=params)




@app.route('/AddVaccinationRecord', methods = ['GET', 'POST'])
def AddVaccinationRecord():
    form = AddVaccinationRecordForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/addVaccinationRecord.html', form = form)
        else:

            mysqlConn = database.connectMySql()
            with mysqlConn.cursor() as cursor:
                insert_stmt = (
                    "insert into vaccinations (  pet_id, vaccine_name, vaccine_details, vaccination_date, expiration_date)"
                    "values ( %s, %s, %s, %s, %s);"
                )

                data = (request.form["pet_id"],
                        request.form["vaccine_name"],
                        request.form["vaccine_details"],
                        request.form["vaccination_date"],
                        request.form["expiration_date"])

                cursor.execute(insert_stmt, data)
            mysqlConn.commit()

            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':
        mysqlConn = database.connectMySql()
        with mysqlConn.cursor() as cursor:
            sql='select * from vaccinations;'
            cursor.execute(sql)
            result = cursor.fetchall()
            params = result

        return render_template('dbInteractionTemplates/addVaccinationRecord.html', form = form, params=params)


@app.route('/OwnerRecordLookup', methods = ['GET', 'POST'])
def OwnerRecordLookup():
    form = OwnerRecordLookupForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/ownerRecordLookup.html', form = form)
        else:
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
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
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
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
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
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
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
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
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/deleteAVisit.html', form = form)


@app.route('/delete_owner/<owner_id>')
def delete_owner(owner_id):
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        cursor.execute('delete from owners where id = %s', owner_id)
    mysqlConn.commit()
    flash('Owner deleted')

    return redirect('/owners', code=302)


@app.route('/delete_pet/<pet_id>')
def delete_pet(pet_id):
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        cursor.execute('delete from pets where id = %s', pet_id)
    mysqlConn.commit()
    flash('Pet deleted')

    return redirect('/pets', code=302)


@app.route('/DeleteOwnerPetRelationship', methods = ['GET', 'POST'])
def DeleteOwnerPetRelationship():
    form = DeleteOwnerPetRelationshipForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('dbInteractionTemplates/deleteOwnerPetRelationship.html', form = form)
        else:
            passed_data = request.form.to_dict()
            passed_data.pop("csrf_token")
            return render_template('success.html', passed_form_data=passed_data)
    elif request.method == 'GET':
        return render_template('dbInteractionTemplates/deleteOwnerPetRelationship.html', form = form)


@app.route('/reports/expired_vaccinations')
def ViewExpiredVaccinations():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql='select pets.name as pet_name, vaccinations.* from vaccinations, pets where pets.id=vaccinations.pet_id and expiration_date<=NOW();'
        cursor.execute(sql)
        result = cursor.fetchall()
        params = result

    return render_template('dbInteractionTemplates/expired_vaccinations.html', params=params)


@app.route('/delete_vaccination/<vaccination_id>')
def delete_vaccination(vaccination_id):
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        cursor.execute('delete from vaccinations where id = %s', vaccination_id)
    mysqlConn.commit()

    return redirect('/reports/expired_vaccinations', code=302)


@app.route('/owners')
def owners():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql= """select
                    id, first_name,
                    coalesce(last_name, '') as last_name,
                    (select count(*) from owners_pets where owners_pets.owner_id=owners.id) AS pet_count,
                    (select scheduled_time from visits where visits.owner_id=owners.id AND scheduled_time > NOW() and checkin_time IS NULL ORDER BY scheduled_time ASC LIMIT 1) AS next_visit,
                    (select checkin_time from visits where visits.owner_id=owners.id AND scheduled_time <= NOW() and checkin_time IS NOT NULL ORDER BY checkin_time DESC LIMIT 1) AS last_visit
                from
                    owners"""
        order_by = " order by last_name ASC, first_name ASC"
        filter_id = request.args.get('id', '')
        filter_name = request.args.get('name', '')
        if filter_id != '':
            cursor.execute(sql + ' where id = %s' + order_by, filter_id)
        elif filter_name != '':
            cursor.execute(sql + ' where first_name like %s or last_name like %s' + order_by, ['%' + filter_name + '%', '%' + filter_name + '%'])
        else:
            cursor.execute(sql + order_by)

        result = cursor.fetchall()
        params = result

    return render_template('dbInteractionTemplates/owners.html', params=params, filter_name=filter_name)


@app.route('/pets')
def pets():
    mysqlConn = database.connectMySql()
    with mysqlConn.cursor() as cursor:
        sql= """select
                    id, name, birthdate, pet_type,
                    (select count(*) from owners_pets where owners_pets.pet_id=pets.id) AS owner_count,
                    (select scheduled_time from visits where visits.pet_id=pets.id AND scheduled_time > NOW() and checkin_time IS NULL ORDER BY scheduled_time ASC LIMIT 1) AS next_visit,
                    (select checkin_time from visits where visits.pet_id=pets.id AND scheduled_time <= NOW() and checkin_time IS NOT NULL ORDER BY checkin_time DESC LIMIT 1) AS last_visit
                from
                    pets"""
        order_by = " order by pet_type ASC, name ASC"
        filter_id = request.args.get('id', '')
        filter_name = request.args.get('name', '')
        if filter_id != '':
            cursor.execute(sql + ' where id = %s' + order_by, filter_id)
        elif filter_name != '':
            cursor.execute(sql + ' where name like %s' + order_by, '%' + filter_name + '%')
        else:
            cursor.execute(sql + order_by)

        result = cursor.fetchall()
        params = result

    return render_template('dbInteractionTemplates/pets.html', params=params, filter_name=filter_name)


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
