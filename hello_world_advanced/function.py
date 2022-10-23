from main import return_fake_name

def handler(event, context):
  arg_one = list(map(lambda row: return_fake_name(row[0]), event["BatchedArgs"]))
  return arg_one