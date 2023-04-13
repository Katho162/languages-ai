
kind create cluster --name languages-ai

cd web

docker build -t web:1.0 . && kind load docker-image web:1.0 --name languages-ai

cd ..

kubectl run languages-ai-deployment --image=web:1.0 --label web

kubectl expose web --port=3000 --type=NodePort

kubectl create -f ./manifest.yaml
