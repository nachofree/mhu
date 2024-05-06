### Presentation @ UMH

------------------------------------------------------------------

#### Intro

- Me
- [Github](https://github.com/nachofree/mhu)

------------------------------------------------------------------

#### What is Docker

- an open platform for developing, shipping and running applications
- separate applications from infrastructure 
- faster time from writing code to deploying

------------------------------------------------------------------

#### More about Docker

- Applications are packaged in a isolated environment called a `container`.
- Containers contain everything needed to run an application, so you don't need to rely on what's installed on the host
- Sharing: Avoid the problem of "it worked on my machine". Everyone gets the same container.

------------------------------------------------------------------

#### More reasons for containers

Containerization is increasingly popular because containers are:

    - Flexible: Even the most complex applications can be containerized.
    - Lightweight: Containers leverage and share the host kernel. Make more efficient use of hardware compared to vm.
    - Interchangeable: You can deploy updates and upgrades on-the-fly.
    - Portable: You can build locally, deploy to the cloud, and run anywhere.
    - Scalable: You can increase and automatically distribute container replicas.

------------------------------------------------------------------

#### CI/CD workflows scenario

- Your developers write code locally and share their work with their colleagues using Docker containers.
- They use Docker to push their applications into a test environment and run automated and manual tests.
- When developers find bugs, they can fix them in the development environment and redeploy them to the test environment for testing and validation.
- When testing is complete, getting the fix to the customer is as simple as pushing the updated image to the production environment.

------------------------------------------------------------------

#### Docker architecture

![](https://docs.docker.com/get-started/images/docker-architecture.webp)

------------------------------------------------------------------

#### Objects you will work with in Docker

- Images
- Containers
- Networks
- Volumes
- Other ...

------------------------------------------------------------------

#### What is a docker image?

A Docker _image_ is a read-only template with instructions for creating a container.

- can be based on another image
- can create your own or use those published in a registry (dockerhub)

------------------------------------------------------------------

#### What are containers

- An image becomes a _container_ at runtime.
- a container will always run the same regardless of infrastructure
- a container isolates software from its environment

------------------------------------------------------------------

#### First Examples

- `docker run hello-world`
- `docker` - indicates to os that we are using this program
- `run` - creates and runs a docker container
- `hello-world` - which image to put in container

------------------------------------------------------------------

#### Another visual

-![](https://training.play-with-docker.com/images/ops-basics-run-details.svg)

------------------------------------------------------------------

#### Docker hub

Find and run the `whalesay` image.

- Visit hub.docker.com
- Search for `whalesay`
- Look at info as to how to run [it](https://hub.docker.com/r/docker/whalesay/)

------------------------------------------------------------------

#### Docker commands

- `docker run`
  * will try to create a container based on an image
- `docker images`
  * Shows images that are installed or available locally to run
- `docker --help`
  * What comands are available to me
- `docker logs`
  * Shows any container output

------------------------------------------------------------------

#### Docker Examples

- `docker run alpine echo "hello world"`
  * Docker has provisioned and launched our container, executed our echo command, and then shut down the container again. If you were to try to do something similar with a traditional VM, you would be waiting several seconds, possibly minutes.
- Containers only run as long as their main process

------------------------------------------------------------------

#### Container isolation

-![](https://training.play-with-docker.com/images/ops-basics-isolation.svg)

------------------------------------------------------------------

#### More docker commands

- `docker run -h foobar -it alpine /bin/sh`
- `docker ps` or `docker ps -a`
- `docker inspect gigantic_leavitt` or whatever the name is
- `docker diff gigantic_leavitt` #what changes have been made
- `docker logs gigantic_leavitt` #cmd history

------------------------------------------------------------------

#### Docker cleanup commands

- `docker container rm -f <containername>` #force remove container
- `docker rm $(docker  ps -aq)` #remove all containers
- `docker rmi <imagename>` #remove image

------------------------------------------------------------------

#### Building an image

Create a Dockerfile

The dockerfile provides instructions as to how to build and run an image. It can map ports to outside world.  Copy stuff into container (your application code). Set environment variables, and more.

------------------------------------------------------------------

#### Dockerfile Example

See the following examples in the git repo:

- friendly-hello 
- the-matrix

------------------------------------------------------------------

#### Dockerfile (From)

This sets the base image for the build process.

        FROM <image>[:<tag>]

The `tag` is optional. If you don't specify then `latest` is assumed.

Example:

        FROM ubuntu:14.04

------------------------------------------------------------------

#### Dockerfile (Copy) 

Copies from the docker host to the filesystem of the new image.

        COPY <src> ... <dst>

Multiple src files can be specified.

        COPY html /var/www/html

------------------------------------------------------------------

#### Dockerfile (ADD) 

Similar to COPY but can handle remote URLs (like wget) and also tarred files:

        ADD <src> ... <dst>

Multiple src files can be specified

------------------------------------------------------------------

#### Dockerfile (ENV) 

This can set an environment variable. An environment variable can be accessed anywhere in the system (by a script or app).

        ENV <key> <value> 
        ENV APACHE_LOG_DIR /var/log/apache

------------------------------------------------------------------

#### Dockerfile (Workdir) 

Kind of like a `cd`. Changes current working directory to that which is specified. 

------------------------------------------------------------------

#### Dockerfile (Expose) 

The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified.  To actually publish the port when running the container, use the `-p` or `-P` flag on `docker run`. Like this `docker run -d -p 80:80 apachephp`

------------------------------------------------------------------

#### Dockerfile (Expose) 

        EXPOSE <port> [<port>/<protocol>...]

        EXPOSE 8080

This will expose 8080 tcp port.

------------------------------------------------------------------

#### Dockerfile (RUN) 

        RUN <command> (or)
        RUN ["executable", "param1", "param2"]

The first command is a shell command always executed at build.
The second does not automatically invoke shell `/bin/sh -c`.

------------------------------------------------------------------

#### Dockerfile (RUN) 

        RUN apt-get update && \
           apt-get install -y apache2 && \
           apt-get clean

------------------------------------------------------------------

#### Dockerfile (CMD) 

RUN executes at build time, CMD executes when the container is launched.

        CMD ["executable","param1","param2"] (exec form) (or)
        CMD command param1 param2 (shell form)

Shell form:

        FROM ubuntu
        CMD echo "This is a test." | wc -

------------------------------------------------------------------

#### Dockerfile (CMD) 

Syntactically, you can add more than one CMD instruction in Dockerfile. However, the build system would ignore all the CMD instructions except for the last one. In other words, in the case of multiple CMD instructions, only the last CMD instruction would be effective.

------------------------------------------------------------------

#### Dockerfile Quiz

Let's spend 5 minutes to see if you can create Dockerfile that will ??

- Look at the `api-test` in the repo for instructions

------------------------------------------------------------------

#### Dockerfile Quiz Solution

- Look at the `api-test-solved` in the repo for solution

------------------------------------------------------------------

#### Push our image to docker hub

- `docker login`
- Build your image with your dockerhub username
  * `docker build -t username/reponame:tag .`
  * `docker build -t joelongtoe/apitest .`
- Push to docker hub
  * `docker push username/reponame:tag`
  * `docker push joelongtoe/apitest`

------------------------------------------------------------------

#### Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

------------------------------------------------------------------

#### Docker compose Example

Look at api-test-solved in the repo examples.

------------------------------------------------------------------

#### More

- The file should be named `docker-compose.yml`
- First make sure to create your Dockerfile
- run `docker compose up`

------------------------------------------------------------------

#### Advantages

- Using a project name, `docker compose` can isolate environments from each other
- Preserve volume data when containers are created
- Recreate only containers that have changed
- Can use variables to make things more dynamic 

------------------------------------------------------------------

#### Other commands with `docker-compose`


- logs -> shows container logs
- ps -> shows running containers
- restart
- rm -> deletes containers
- stop

------------------------------------------------------------------

#### Docker compose quiz

See if you can update the docker compose file in api-test-solved to use the image that you pushed to github.

------------------------------------------------------------------

#### Other important Docker items

We don't have time to cover:

- Networks (how to get containers to connect to one another)
- Volumes (persistent storage for containers)
- How to move to the cloud? (ECS on AWS)

------------------------------------------------------------------

#### Kubernetes - What is it?

Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.  

Review the part about containers [here](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)

------------------------------------------------------------------

#### What can it do?

Remember, it works with our containers and provides:

- load balancing
- storage orchestration: can automatically mount local or cloud or other storage
- automated rollouts and rollbacks
- automatic bin packing: can specify ram and cpu of container, k8s will fit onto your nodes to maximize resource usage
- self-healing: restarts services, containers, etc automatically
- more...

------------------------------------------------------------------

#### Overview

To work with Kubernetes, you use Kubernetes API objects to describe your cluster’s desired state: what applications or other workloads you want to run, what container images they use, the number of replicas, what network and disk resources you want to make available, and more. You set your desired state by creating objects using the Kubernetes API, typically via the command-line interface, kubectl.

------------------------------------------------------------------

#### Kubernetes Clusters

Kubernetes coordinates a highly available cluster of computers that are connected to work as a single unit. The abstractions in Kubernetes allow you to deploy containerized applications to a cluster without tying them specifically to individual machines.

- master node coordinates the cluster
- other nodes run applications

------------------------------------------------------------------

#### What is it?

![](https://d33wubrfki0l68.cloudfront.net/99d9808dcbf2880a996ed50d308a186b5900cec9/40b94/docs/tutorials/kubernetes-basics/public/images/module_01_cluster.svg)

------------------------------------------------------------------

#### Clusters

Each node has a Kubelet (an agent) which manages node and communicates with Kubernetes (K8s) master. They will also have docker installed.

------------------------------------------------------------------

#### Verify installation

From a terminal, you should be able to `kubectl get nodes`.

------------------------------------------------------------------

#### Nodes

- Where the pods run
- can be physical or virtual
- managed by master
- Run a kubelet (an agent that handles comms from master)(Manages pods and containers on a machine)
- Also run a container runtime (like docker)

------------------------------------------------------------------

#### Now what?

We want to put container(ized) applications on the cluster.  Create a k8s configuration file. Master will schedule nodes to run the container.  These containers are monitored. If it goes down, the cluster `self heals` by bringing it up again.

------------------------------------------------------------------

#### How?

![](https://d33wubrfki0l68.cloudfront.net/152c845f25df8e69dd24dd7b0836a289747e258a/4a1d2/docs/tutorials/kubernetes-basics/public/images/module_02_first_app.svg)

------------------------------------------------------------------

#### What is a pod?

A group of one or more (docker) containers, along with their volumes, networks, and other information about the container.  Containers should only be scheduled together in a single Pod if they are tightly coupled and need to share resources such as disk.

Containers within a pod share an IP address and port space, and can find each other via localhost. 
  * So they must coordinate usage of ports

------------------------------------------------------------------

#### Create our first pod

        kubectl run kubernetes-bootcamp --image=docker.io/jocatalin/kubernetes-bootcamp:v1 --port=8080
        kubectl get pods

------------------------------------------------------------------

#### Hmmm??

This command:

- searched for a suitable node where an instance of the application could be run
- scheduled the application to run on that Node

------------------------------------------------------------------

#### Pod scheduling

When a node dies:

- Pods on that node are lost (though your controller might make cluster back to desired state by creation of identical pods on a different host)

------------------------------------------------------------------

#### More about pods

- Containers in different pods have distinct ip addresses
- If a node dies, the pods scheduled to that node are scheduled for deletion, after a timeout period. A given pod (as defined by a UID) is not “rescheduled” to a new node; instead, it can be replaced by an identical pod, with even the same name if desired, but with a new UID

------------------------------------------------------------------

#### Pod Examples

![](https://d33wubrfki0l68.cloudfront.net/fe03f68d8ede9815184852ca2a4fd30325e5d15a/98064/docs/tutorials/kubernetes-basics/public/images/module_03_pods.svg)

------------------------------------------------------------------

#### Another view

![](https://d33wubrfki0l68.cloudfront.net/5cb72d407cbe2755e581b6de757e0d81760d5b86/a9df9/docs/tutorials/kubernetes-basics/public/images/module_03_nodes.svg)

------------------------------------------------------------------

#### More Pod Commands

- `kubectl get pods`
- `kubectl describe pods`
- `kubectl logs $POD_NAME` (only one container inside this pod)
- `kubectl exec -ti $POD_NAME bash`
- `kubectl delete pod $PODNAME`

------------------------------------------------------------------

#### A note about pods

You'll rarely create individual Pods directly in Kubernete. This is because Pods are designed as relatively ephemeral, disposable entities. When a Pod gets created (directly by you, or indirectly by a controller), the new Pod is scheduled to run on a Node in your cluster. The Pod remains on that node until the Pod finishes execution, the Pod object is deleted, the Pod is evicted for lack of resources, or the node fails.

Better to use a deployment.

------------------------------------------------------------------

#### What is a deployment

- A Deployment provides declarative updates for Pods
- You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate.

------------------------------------------------------------------

#### Sample

- `kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml`
- Run `kubectl get deployments`
  * DESIRED = how many we want
  * CURRENT = how many are running
  * UP-TO-DATE = how many replicas were changed to match desired state
  * AVAILABLE = how many are usable right now
- Delete a few containers 

------------------------------------------------------------------

#### How does this relate to pods?

Run `kubectl get pods` to look at what the deployment created.
Also, `kubectl describe deployment`.

------------------------------------------------------------------

#### Kubernetes services (Quick overview)

We didn't have time to discuss networking in docker, but it is more critical to understand how networking works on K8S.  These are defined as `services`.

- remember each pod has a unique ip address
- pods can be created and destroyed by a deployment
- must have a way of tracking how to route requests to the backend pods

------------------------------------------------------------------

#### Kubernetes services confusion?

- a node has an ip address:port
- a pod has an ip address:port
- containers within a pod can access each other's ports on `localhost`.
- so containers in a pod must coordinate port usage

------------------------------------------------------------------

#### Kubernetes services howto

- `kubectl get services`
- `kubectl apply -f https://raw.githubusercontent.com/kubernetes/website/master/content/en/examples/service/networking/run-my-nginx.yaml`
- `kubectl apply -f http://it3300.cs.utahtech.edu/notes/my-nginx.yaml`
- `kubectl describe svc my-nginx-np`
- `curl localhost:31894` (or whatever port it is)

------------------------------------------------------------------

#### Scaling

This is where we change the number of replicas of a deployment.

------------------------------------------------------------------

#### Scaling image 1

![](https://d33wubrfki0l68.cloudfront.net/043eb67914e9474e30a303553d5a4c6c7301f378/0d8f6/docs/tutorials/kubernetes-basics/public/images/module_05_scaling1.svg)

------------------------------------------------------------------

#### Scaling image 2

![](https://d33wubrfki0l68.cloudfront.net/30f75140a581110443397192d70a4cdb37df7bfc/b5f56/docs/tutorials/kubernetes-basics/public/images/module_05_scaling2.svg)

------------------------------------------------------------------

#### Scaling 

- Scaling out a Deployment will ensure new Pods are created and scheduled to Nodes with available resources. Scaling in will reduce the number of Pods to the new desired state.
- If we run multiple instances of an APP, we then have to load-balance between them (services will inherently do this)
- Services will also make sure that traffic is only sent to pods that are available.

------------------------------------------------------------------

#### Scaling 

- Scale to 4
  * `kubectl scale deployments/my-nginx --replicas=4`
  * Check deployments again.
- Pods should have increased
  * `kubectl get pods` or
  * `kubectl get pods -o wide`
- You can describe the deployments again to view event logs.
- Make sure you can `curl` again.
  * As you run it, you should see that it pulls from different pod
- Can you scale to 2?

------------------------------------------------------------------

#### Clean up

Delete everything:

- `kubectl delete pod kubernetes-bootcamp`
- `kubectl delete deployment my-nginx`
- `kubectl delete svc my-nginx-np`

------------------------------------------------------------------

#### Example

See friendly-hello example in git repo.

------------------------------------------------------------------

#### Quiz

- `kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1`
- What ip addresses are the pods listening on? 
- `kubectl expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080`
- curl the localhost:<port> to see the page.
- Scale it to 5.
- curl the localhost:<port> multiple times.
- What are the endpoints identified by the service?
- Scale back to 2, did things change?

------------------------------------------------------------------

#### Example

See api-test-solved kubernetes example.

------------------------------------------------------------------

#### YAML

Can provide an easier way define our k8s objects.

- Convenience: You’ll no longer have to add all of your parameters to the command line
- Maintenance: YAML files can be added to source control, so you can track changes
- Flexibility: You’ll be able to create much more complex structures using YAML than you can on the command line

------------------------------------------------------------------

#### YAML

- YAML is a superset of JSON
- A MAP is a key:value pair
- A LIST is a sequence of objects
- Don't use tabs 

------------------------------------------------------------------

#### Pod Example

        ---
        apiVersion: v1
        kind: Pod
        metadata:
         name: rss-site
         labels:
           app: web
        spec:
         containers:
           – name: front-end
             image: nginx
             ports:
               – containerPort: 80
           – name: rss-reader
             image: nickchase/rss-php-nginx:v1
             ports:
               – containerPort: 88

------------------------------------------------------------------


#### Action

- Apply the changes like:

        kubectl create -f pod.yaml

or 

        kubectl delete -f pod.yaml

------------------------------------------------------------------

#### YAML Deployment

        ---
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          creationTimestamp: null
          labels:
            app: nchase
          name: nchase
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: nchase
          strategy: {}
          template:
            metadata:
              creationTimestamp: null
              labels:
                app: nchase
            spec:
              containers:
              - image: nickchase/rss-php-nginx:v1
                name: rss-php-nginx
                resources: {}
        status: {}


------------------------------------------------------------------

#### YAML Service 

        ---
        apiVersion: v1
        kind: Service
        metadata:
          creationTimestamp: null
          labels:
            app: nginx
          name: nginx
        spec:
          ports:
          - name: 80-80
            port: 80
            protocol: TCP
            targetPort: 80
          selector:
            app: nginx
          type: LoadBalancer
        status:
          loadBalancer: {}

------------------------------------------------------------------

#### Easy yaml creation 

Create a deployment named mydeployment with image Nginx

        kubectl create deployment mydeployment \
            --image=nginx:latest \
            --dry-run=client -o yaml > mydeployment.yaml        

------------------------------------------------------------------

#### Easy yaml creation 

Create a NodePort service YAML for deployment mydeployment with service port 8080

        kubectl expose deployment mydeployment \
            --type=NodePort \
            --port=8080 \
            --name=mydeployment-service \
            --dry-run=client -o yaml > mydeployment-service.yaml

------------------------------------------------------------------

#### Yaml example

See api-test-solved/k8s

------------------------------------------------------------------

#### Android and docker

- This will NOT work on a virtual machine.
- Containers do NOT work well for Android development since you must have a physical machine
- If you must use a physical machine, you may as well just install the ADB and related things on your machine.
- Containers are very useful for microservices, not as useful for mobile development (unless you are creating a backend API)

------------------------------------------------------------------

#### Can it be done?

Instructions are [here](https://github.com/amrsa1/Android-Emulator-image). Since I didn't give you a physical machine, you will just have to watch me do it.

- my machine name is `othello`. Directory is `/home/joe/Android-Emulator-image`
- `docker build -t android-emulator .`
- `docker run -it --privileged -d -p 5900:5900 --name androidContainer --privileged android-emulator`
- `docker exec --privileged  -it androidContainer bash -c "./start_appium.sh"`
- `docker exec --privileged -it -e EMULATOR_TIMEOUT=300 androidContainer bash -c "./start_emu_headless.sh"`
- `docker exec --privileged -it androidContainer bash -c "./start_vnc.sh"`
- Now create ssh tunnel to view: `ssh joe@ssh.cs.utahtech.edu -L 5900:othello:5900`
- Connect to `localhost:5900`, start a dash shell and `./start_emu.sh`.
- The emulator shoudl start.

------------------------------------------------------------------

#### Another way

Instructions are [here](https://github.com/budtmo/docker-android)

- `docker run -d -p 6080:6080 -p 4723:4723 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true -e APPIUM=true --device /dev/kvm --name android-container budtmo/docker-android:emulator_11.0`
- Then make a tunnel and connect to port 6080 in a browser.


