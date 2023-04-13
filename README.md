# Languages.ai

This is an web app that runs in a microservices architecture using Kubernetes and Docker Containers. I created this project in order to start the architecture of an open-source project for the language learning community to have a fun tool that's integrated with AI models created also by me in another projects :)

# Installation

In order to run this app you must have Docker, Kind and KubeCTL installed in your environment.

If you're sure you already got that than you can run:

```
$ sh ./start.sh
```

This script contain most of configuration needed in order to create a k8s cluster for our app ready to be accessed at `http://localhost:3000`