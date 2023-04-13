# Create kind cluster
kind create cluster --config=./kind-config.yaml --name languages-ai

helm uninstall languages-ai

kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission

kubectl apply -f https://projectcontour.io/quickstart/contour.yaml
kubectl patch daemonsets -n projectcontour envoy -p '{"spec":{"template":{"spec":{"nodeSelector":{"ingress-ready":"true"},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Equal","effect":"NoSchedule"},{"key":"node-role.kubernetes.io/master","operator":"Equal","effect":"NoSchedule"}]}}}}'

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/cloud/deploy.yaml

cd web

# Build images and load to the cluster
docker build -t web:1.0 . && kind load docker-image web:1.0 --name languages-ai

# cd .. && cd user-auth-api

# docker build -t user-auth:1.0 . && kind load docker-image user-auth:1.0 --name languages-ai

cd ..

# Apply the deployment and services config
helm install languages-ai ./languages-ai
