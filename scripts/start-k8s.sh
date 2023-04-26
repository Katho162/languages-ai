# Create kind cluster
kind create cluster --config=./kind-config.yaml --name languages-ai
kubectl create namespace languages-ai

helm uninstall languages-ai

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

helm install ingress-nginx ingress-nginx/ingress-nginx \
  --create-namespace \
  --namespace ingress-nginx \


cd web

# Build images and load to the cluster
docker build -t web:1.0 . && docker run --name languages-ai-web -p 80:3000 --env MODE=local-k8s web:1.0

# cd .. && cd user-auth-api

docker build -t user-auth:1.0 . && kind load docker-image user-auth:1.0 --name languages-ai

cd ..

# Apply the deployment and services config
helm install languages-ai ./languages-ai -n languages-ai
