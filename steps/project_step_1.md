# Project Outline

Our project will be a simple veterinary practice management database.

# Database Outline

## Owners

### Description

Owners will represent people who have pets.

### Attributes

* First name - text (required)
* Last name - text
* Email - text
* Phone - text (required)

### Relationships

An owner will have a many to many relationship with pets.
A pet is not required.
An owner will have a one to many relationship with visits.
A visit is not required.

## Pets

### Description

Pets will represent the animals visiting the veterinary clinic.
The Pet Type will indicate the animal species.
The Comment column will have arbitrary additional notes about the description or living conditions of the animal.

### Attributes

* Name - text (required)
* Birthdate - date (required)
* Pet Type - text (required)
* Comment - text

### Relationships

A Pet will have a many to many relationship with an owner.
An owner is required.
A Pet will have a one to many relationship with vaccinations.
A vaccination is not required.
A Pet will have a one to many relationship with a visit.
A visit is not required.

## Visit

### Description

A visit will encapsulate a consultation involving a single pet and an owner.
If more than one owner is present at a visit, a single owner will be chosen and used.
If more than one pet is brought at a time with a single owner, it will be recorded independently as a visit for each pet.
The notes are arbitrary text encapsulating the details/reasons/results of the visit.

### Attributes

* Visit time - datetime (required)
* Owner ID - int (required)
* Pet ID - int (required)
* Notes - text (required)

### Relationships

A visit has many to one relationship with an owner, an owner is required.
A visit has many to one relationship with a pet, an pet is required.

## Vaccination

### Description

A vaccination records the details of a pet's vaccination.
The vaccination date records the date of vaccine administration and the expiration date records the date at which the vaccine is no longer effective.

### Attributes

* Pet ID - int (required)
* Vaccine - text (required)
* Vaccination Date - date (required)
* Expiration Date - date (required)


# URL to Website