from faker import Faker

fake = Faker()
def return_fake_name(row):
    return row + " " + fake.name()