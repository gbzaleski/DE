import csv
from faker import Faker
import random

fake = Faker()
N = int(1e4)
result_file = "data.csv"

with open(result_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Name", "Age", "Profession", "Location", "Email"])
    for _ in range(N):
        writer.writerow([fake.name(), random.randint(20, 60), fake.job(), fake.city(), fake.email()])