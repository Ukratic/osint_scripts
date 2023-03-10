from faker import Faker
import random

# Create object with randomized locale
locale = random.choice(['it_IT','en_GB','fr_FR','es_ES','de_DE','pl_PL','nl_NL'])
fake = Faker(locale)

# generate fake profile
print({"bdate":fake.date_of_birth(minimum_age=18,maximum_age=80),"name":fake.name_nonbinary(),"email":fake.email(),
           "address":fake.street_address(),"city":fake.city(),"phone":fake.phone_number(),'job':fake.job()})