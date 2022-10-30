# 🧶 Priceloop NoCode Python External Functions Templates

You can create your own functions and then call them inside our [NoCode table](https://priceloop.ai/nocode), just like a builtin function. Here are some easy examples that you can use to write your own functions. Some of them are also deployed on our platform.

### Deployment

The easiest way to deploy our external functions are via our cli:

```bash
npm install -g @priceloop/cli
```

Once you installed it, let’s login and then create the function via the CLI:

```bash
priceloop login-credentials --username "nocode_username" --password "nocode_password"
priceloop create-external-function --function "my_example" --runtime "python" --return-type "string" --parameter-types "string"
```

Finally, we need update the function:

```bash
priceloop update-external-function --function "my_example" --directory "hello_world"
```

After these steps, your new function will be available inside the specified workspace in [NoCode](https://alpha.priceloop.ai/).

Go to the app and type a new formula: `\my_example('World')`. It should return “Hello World”.

More information on how to deploy it to our platform please also go to our [documentation](https://priceloopai.notion.site/External-Functions-f78d153ab7b94a5f8a2f2cc5baa5e9d3).

### Testing

To test locally please install python-lambda-local:

```
pip install python-lambda-local
```
