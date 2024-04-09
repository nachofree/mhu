#### Description

A frontend container running php, needs to talk to a backend container that is built with python. The backend container must be resolved via dns at `pythonapi`

#### Instructions

 - Based on python:3
 - Exposes port 8080
 - Sets the working directory to `/usr/src/app`
 - copies the contents of this directory into `./`.
 - Does an `apt update` and installs the package named `fortune`
 - Installs the necessary pip packages `pip install --no-cache-dir -r requirements.txt`
 - Runs the following at container launch time `["gunicorn", "-b", "0.0.0.0:8080", "fortune:__hug_wsgi__"]`

        docker build -t api .
        docker run -d -p 8080:8080 api
        curl localhost:8080/generate/


#### Docker compose

After you bring up both images, you should be able to access `http://localhost/mypage.php`.

docker compose up -d

#### Kubernetes

Remember that two different containers are involved. I think that I would want to control each individually and scale them separately.

kubectl create deployment pythonapi --image=joelongtoe/api
kubectl create deployment phpconsumer --image=joelongtoe/phpconsumer
kubectl expose deployment/pythonapi --type="NodePort" --port 8080
kubectl expose deployment/phpconsumer --type="NodePort" --port 80

Test curl the endpoints:

curl localhost:30538/generate
curl localhost:31914/mypage.php


