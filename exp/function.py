import math

def exp(x):
    try:
        return str(math.exp(float(x[0])))
    except:
        return str(-1)

def handler(event, context):
    return list(map(lambda row: exp(row), event["BatchedArgs"]))