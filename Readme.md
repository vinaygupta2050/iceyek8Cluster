# Iceye K8 cluster

The project includes config files which will help you setup k8 cluster for greet service

## Getting Started

To get started clone project from github. 

Below are the software used for setup
* Minikube
* Kubernetes
* Docker

Prerequisites

* Make sure minikube, kubernetes is installed and running. 
* Pull hello world container using below command
```
docker pull vinaygupta2050/hello-world
```
* You can also build the container with docker file locally with below command. Navigate to hello-world folder and execute below command 
```
docker build -t vinaygupta2050/hello-world .
```

## Verify Container is working by running below command

```
docker run --rm -it -p 8000:8000 datawire/hello-world
``` 
You can either use curl command to send a request.

```
curl http://localhost:8000/vinaykumar/
```

###Setup K8 cluster

1- Create the namespace from the ns-hello-world.yaml manifest

```
kubectl create -f ns-hello-world.yaml
```
2- View all available namespaces in your cluster 

```
kubectl get namespaces
```
3- Create the Service for your hello-world api

```
kubectl create -f Service.yaml
```
4- View the service and its corresponding information:

```
kubectl get services -n hello-world
```

5- Create deployment for hello-world api:

```
kubectl create -f Deployment.yaml
```
6- Get your worker node’s external IP address. Copy down the EXTERNAL-IP value for any worker node in the cluster:

```
kubectl get nodes -o wide
```
7- Access the hello-world services to view its exposed port.

```
kubectl get svc -n hello-world
```
8- Open a browser window and enter in a worker node’s IP address and exposed port. An example url to your hello-world would be, http://192.0.2.1:30304/vinaykumar.

## Author

* **Vinaykumar Gupta** - [LinkedIn](https://in.linkedin.com/in/vinaygupta2050)
