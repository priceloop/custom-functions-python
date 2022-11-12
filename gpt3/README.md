# GPT3 Example

## Testing locally

1. Go to <https://openai.com/api/> and register an account
2. Get the API key and replace the `<openai-key>` in the `event.json` with your key
3. Run this to test:

```
python-lambda-local function.py event.json -t 900
```
