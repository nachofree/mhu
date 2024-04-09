### Python/Flask application

Project structure:
```
.
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py

```

- docker build -t friendly-hello .
- docker run -d -p 8000:8000 friendly-hello

Then you should be able to  `curl localhost:8000`.

#### Kubernetes

- kubectl create deployment hello --image=joelongtoe/friendly-hello
- kubectl expose deployment/hello --type="NodePort" --port 8000
- Then you can `curl localhost:<port>`
