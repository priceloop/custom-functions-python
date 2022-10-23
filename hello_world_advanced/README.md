# Hello World Advanced Example

* Create an external function with external dependencies
* Seperate the lambda handler and core logic

Run this to test:

```
python-lambda-local function.py event.json -t 900
```

### Deployment

First install the packages from your `requirements.txt`, zip it and then add your function to the root of the zip file::

```
pip install --target ./package -r requirements.txt
cd package
zip -r ../app.zip .
cd ..
zip -g app.zip *.py
```

Or use this command:

```
./package.sh
```

Once this is done, you can use the `hello_world_app.zip` to push it to our platform.
