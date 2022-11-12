import json
import requests

def return_gpt3_results(input, api_key):
    headers = {
        "Authorization": "Bearer {}".format(api_key),
    }

    json_data = {
        "model": "text-davinci-002",
        "prompt": input,
        "temperature": 0.8,
        "max_tokens": 60,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)
    return json.loads(response.content.decode("utf-8"))["choices"][0]["text"]

def handler(event, context):
    api_key = list(map(lambda row: row[1], event["BatchedArgs"]))[0]
    return list(map(lambda row: return_gpt3_results(row[0], api_key), event["BatchedArgs"]))