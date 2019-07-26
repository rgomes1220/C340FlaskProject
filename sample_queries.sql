-- adds an owner to the system
insert into owners values (null, :first_name, :last_name, :email, :phone);

-- adds a pet to the system
insert into pets values (null, :name, :birthdate, :pet_type, :comment);

-- links up an owner with a pet
insert into owners_pets values (null, :owner_id, :pet_id);

-- schedules a new visit
insert into visits (owner_id, pet_id, scheduled_time) values (:owner_id, :pet_id, :scheduled_time);

-- updates a visit with a checkin time
update visits set checkin_time=:checkin_time where id=:visit_id;

-- updates the notes with a visit
update visits set notes=:notes where id=:visit_id;

-- adds a vaccination record
insert into vaccinations values (null, :pet_id, :vaccine_name, :vaccine_details, :vaccination_date, :expiration_date);

-- Looks up an owner record
select * from owners where first_name=:first_name and last_name=:last_name;

-- Looks up a pet name
select * from pets where name like '%:name';

-- Find all of the pets for an owner
select pets.* from pets, owners_pets where pets.id=owners_pets.pet_id and owners_pets.owner_id=:owner_id;

-- List the owners for a pet
select owners.* from pets, owners_pets where owners.id=owners_pets.owner_id and owners_pets.pet_id=:pet_id;

-- Find expired vaccinations
select * from vaccinations where expiration_date<=NOW();
