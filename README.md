# 🧶 Priceloop NoCode Python External Functions Templates

You can create your own functions and then call them inside our [NoCode table](https://priceloop.ai/nocode), just like a built-in function. Here are some easy examples that you can use to write your own functions. Some of them are also deployed on our platform.

https://user-images.githubusercontent.com/3866530/200024328-ea5cad88-c930-4544-a9d4-9838437978f0.mp4

### Getting Started

Let's start with creating a Python environment first. You can use `virtualenv` or `conda` to do this. At the moment, we only support Python 3.8 due to the pre-built lambda layer:

```bash
conda create -n my_example python=3.8
source activate my_example
```

The easiest way to deploy our external functions is via our cli:

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
