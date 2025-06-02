#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

company1 = Company(name="RAM", founding_year=2010)
company2 = Company(name="ZORD", founding_year=2013)
company3 = Company(name="AWAG", founding_year=2020)

dev1 = Dev(name="Daud")
dev2 = Dev(name="Gich")
dev3 = Dev(name="Zanaa")

session.add_all([company1, company2, company3, dev1, dev2, dev3])
session.commit()

f1 = Freebie(item_name="OLED GAMING SCREEN", value=50000, dev=dev1, company=company1)
f2 = Freebie(item_name="ROG PHONE", value=70000, dev=dev2, company=company2)
f3 = Freebie(item_name="RAZER MOUSE", value=5000, dev=dev1, company=company2)
f4 = Freebie(item_name="JBL", value=15000, dev=dev3, company=company3)
f5 = Freebie(item_name="BUDS", value=10000, dev=dev2, company=company1)

session.add_all([f1, f2, f3, f4, f5])
session.commit()