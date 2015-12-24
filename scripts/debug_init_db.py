'''
This script builds the additonal entries in the database that are not built
into a deployment database. Fake patients, possibly fake providers, etc.

scripts/init_db.py contains data that is real and should be used in a
deployment environment. This script relies on model entries created by that
script.
'''

from django.contrib.auth.models import User
from pttrack import models
from datetime import date, timedelta

# pylint: disable=invalid-name

user = User.objects.create_superuser('jrporter', 'justinrporter@wustl.edu',
                                     'password')
user.first_name = "Justin"
user.last_name = "Porter"
user.save()

prov = models.Provider.objects.create(
    first_name="Justin",
    last_name="Porter",
    phone="123455",
    gender=models.Gender.objects.all()[0],
    associated_user=user)

for role in models.ProviderType.objects.all():
    prov.clinical_roles.add(role)

# build a patient.
p = models.Patient(first_name="Frankie",
                   middle_name="Lane",
                   last_name="McNath",
                   address="6310 Scott Ave.",
                   date_of_birth=date(year=1989, month=8, day=9),
                   phone="501-233-1234",
                   gender=models.Gender.objects.all()[0],
                   needs_workup=True)
p.save()

p.languages.add(models.Language.objects.all()[0])
p.ethnicities.add(models.Ethnicity.objects.all()[0])

p = models.Patient(first_name="Antonie",
                   last_name="Dodson",
                   address="3223 Main St.",
                   date_of_birth=date(year=1991, month=9, day=7),
                   gender=models.Gender.objects.all()[0])
p.save()

p.languages.add(models.Language.objects.all()[1])
p.ethnicities.add(models.Ethnicity.objects.all()[2])

models.ActionItem.objects.create(
    instruction=models.ActionInstruction.objects.all()[0],
    due_date=date.today()-timedelta(40),
    comments="Somebody really needs to call this guy.",
    patient=p,
    author=prov,
    author_type=prov.clinical_roles.all()[0])


p = models.Patient(first_name="Alan",
                   last_name="Turing",
                   address="85 Albert Embankment",
                   date_of_birth=date(year=1912, month=6, day=23),
                   gender=models.Gender.objects.all()[0])
p.save()

p.languages.add(models.Language.objects.all()[2])
p.ethnicities.add(models.Ethnicity.objects.all()[1])

models.Workup.objects.create(
    author=prov,
    author_type=prov.clinical_roles.all()[0],
    patient=p,
    clinic_day=models.ClinicDate.objects.create(
        clinic_type=models.ClinicType.objects.all()[0],
        clinic_date=date.today()),
    chief_complaint="Depression",
    diagnosis="Dperession",
    HPI="Started becoming depressed after being being found guilty.",
    PMH_PSH="Noncontributory.",
    meds="stilboestrol",
    fam_hx="Noncontributory",
    soc_hx="Few friends?",
    ros="Noncontributory",
    pe="")

print "Done!"
