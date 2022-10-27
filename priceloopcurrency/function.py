from forex_python.converter import CurrencyRates

def return_currency_rates(from_currency: str, to_currency: str) -> float:
  c = CurrencyRates()
  try:
    return str(c.get_rate(from_currency, to_currency))
  except:
    return str(-1)

def handler(event, context):
  return list(map(lambda row: return_currency_rates(row[0], row[1]), event["BatchedArgs"]))