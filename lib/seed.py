#!/usr/bin/env python3

# Script goes here!
from models import Company,Dev,Freebie

#company1 = Company(name="ARC", founding_year=2018)
#company2 = Company(name="MANY", founding_year=2020)


#dev1 = Dev(name="Daud")
#dev2 = Dev(name="Allan")

#session.add_all([company1, company2, dev1, dev2])
#session.commit()

f1 = Freebie(item_name="Asus laptop", value=1, dev=dev1, company=company1)
f2 = Freebie(item_name="PS 5", value=10, dev=dev2, company=company2)

session.add_all([f1, f2])
session.commit()
