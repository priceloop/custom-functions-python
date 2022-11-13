# GPT3 Example

## Testing locally

1. Go to <https://openai.com/api/> and register an account
2. Get the API key and replace the `<openai-key>` in the `event.json` with your key
3. Run this to test:

```
python-lambda-local function.py event.json -t 900
```

## Deployment

1. Log in to your workspace:

```
priceloop login-web
```

2. Register the function:

```
priceloop create-external-function --function gpt3 --runtime python --parameter-types "string,string" --return-type "string"
```

3. Update the function:

```
# from root directory of this repository
priceloop update-external-function --function gpt3 --directory gpt3
```

4. Go to <https://alpha.priceloop.ai/> and try out the function in a formula with `\gpt3(gpt3_input, openai_api_key)`
