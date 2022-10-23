def handler(event, context):
  return list(map(lambda row: "Hello " + row[0], event["BatchedArgs"]))