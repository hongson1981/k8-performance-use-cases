# Docker image and k8s manifest for mvp-icap-service

## Prerequisites
	Install minikube
	Point your terminal to use the docker daemon inside minikube by command below :
	- eval $(minikube docker-env)  (For Linux)
	- & minikube -p minikube docker-env | Invoke-Expression  (For windows)
## Usage

### Build Docker imager for icap-service

	Refer https://github.com/filetrust/mvp-icap-service

### Build ConfigMap to set environment variables to ICAP server on Kubernetes
	
	> kubectl apply ./icapConfigMap.yml
	
### Build and run Kubernetes pod for ICAP server pointing to local docker image

   > kubectl apply ./icapPod.yml
   
### Check ICAP server env
	
	> kubectl exec icapserver -it -- env


## License
MIT License
See: LICENSE
