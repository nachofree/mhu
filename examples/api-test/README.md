Create a Dockerfile that does the following:

 - Based on python:3
 - Exposes port 8080
 - Sets the working directory to `/usr/src/app`
 - copies `requirements.txt` into `./`.
 - Does an `apt update` and installs the package named `fortune`
 - Installs the necessary pip packages `pip install --no-cache-dir -r requirements.txt`
 - Copies `fortune.py` into `./`
 - Runs the following at container launch time `["gunicorn", "-b", "0.0.0.0:8080", "fortune:__hug_wsgi__"]`

See if you can build the image.
See if you can run an instance of the image.
See if you can `curl localhost:8080`.
