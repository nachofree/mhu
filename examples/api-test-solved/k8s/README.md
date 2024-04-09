#### Kubernetes yaml files

These files were generated  and executed like:

kubectl create deployment pythonapi --image=joelongtoe/api --dry-run=client -o yaml > api.yaml
kubectl create deployment phpconsumer --image=joelongtoe/phpconsumer --dry-run=client -o yaml > consumer.yaml
kubectl apply -f api.yaml
kubectl apply -f consumer.yaml

kubectl expose deployment pythonapi --type=NodePort --port=8080 --name=pythonapi  --dry-run=client -o yaml > api_svc.yaml
kubectl expose deployment phpconsumer --type=NodePort --port=80 --name=phpconsumer --dry-run=client -o yaml > consumer_svc.yaml

kubectl apply -f api_svc.yaml
kubectl apply -f consumer_svc.yaml
