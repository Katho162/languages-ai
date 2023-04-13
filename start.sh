# Create kind cluster
kind create cluster --config=./kind-config.yaml --name languages-ai

helm uninstall languages-ai

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/kind/deploy.yaml

cd web

# Build images and load to the cluster
docker build -t web:1.0 . && kind load docker-image web:1.0 --name languages-ai

cd .. && cd user-auth-api

docker build -t user-auth:1.0 . && kind load docker-image user-auth:1.0 --name languages-ai

cd ..

# Apply the deployment and services config
helm install languages-ai ./languages-ai
