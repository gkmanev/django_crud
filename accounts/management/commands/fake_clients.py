from django.core.management.base import BaseCommand
import csv
import pandas as pd
from faker import Faker
import datetime
import random
from faker.providers import DynamicProvider
from datetime import timedelta
import pytz


class Command(BaseCommand):
    help = 'generate fake clients'

    def handle(self, *args, **kwargs):

        def fake_data_generation(records):
            fake = Faker('en_US')

            clients = []

            for i in range(records):
                firstname = fake.first_name()
                last_name = fake.last_name()
                name = firstname + ' ' + last_name
                created_at = fake.date_time_between(start_date='-1y', end_date="now")
                updated_at = created_at + timedelta(days=1, hours=random.randint(0,24))

                clients.append({
                    "name": name,
                    "created_at":created_at,
                    "updated_at":updated_at,
                    })
            return clients

        df = pd.DataFrame(fake_data_generation(500000))
        df.head()

        df.to_csv('clients.csv')
