from faker import Faker

fake = Faker()

person = ["first_name", "first_name_female", "first_name_male", "last_name", "last_name_female", "last_name_male", "name"]
address = ["address", "building_number" "city", "city_suffix", "country", "country_code", "postcode", "street_address", "street_name"]
company = ["company"]
job = ["job"]
phone_number = ["phone_number"]
internet = ["company_email", "email", "free_email"]

faker_args = sum([person, address, company, job, phone_number, internet], [])

def return_fake_name(row, faker_provider, valid_args=faker_args):
  if faker_provider in valid_args:
    return eval(f"fake.{faker_provider}()")
  else:
    return fake.name()

def handler(event, context):
  arg_one = list(map(lambda row: return_fake_name(row[0],  row[1]), event["BatchedArgs"]))
  return arg_one