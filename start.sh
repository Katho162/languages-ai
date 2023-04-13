# Create kind cluster
kind create cluster --config=./kind-config.yaml --name languages-ai

cd web

# Build images and load to the cluster
docker build -t web:1.0 . && kind load docker-image web:1.0 --name languages-ai

cd ..

# Apply the deployment and services config
kubectl apply -f ./manifest.yaml
