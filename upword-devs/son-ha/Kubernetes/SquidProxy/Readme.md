# Install squid proxy on Pod

## Create a ConfigMap to store configuration file for the Squid proxy
	kubectl apply proxy-configmap.yml

## Deploy a container with Squid:

	kubectl apply -f .\squidProxy.yml

## Usage (Proxy)

	Get IP address of Squid pod:
	> kubectl get pod -l app=squid -o wide
	Set IP:port (3128) to any pod or app which target traffic over Squid proxy
