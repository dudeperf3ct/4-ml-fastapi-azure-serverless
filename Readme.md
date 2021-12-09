### Deploy ML model to Azure using FastAPI

Azure app: https://wine-ratings.azurewebsites.net/

In this exercise, we will build a fastapi ML application and deploy it with continuous delivery on Azure using Azure App Services and Azure DevOps Pipelines.

### ML

To build a ML model, refer the colab notebook under `notebooks` folder.

### FastAPI

To validate the fastapi application locally,

```bash
docker build -t wine .
docker run --rm -it -v $(pwd):/app -p 8000:8000 wine
```

### Azure

To deploy the fastapi application on Azure following steps were taken.

1. Add Azure Pipelines from Github Marketplace while creating the github repo.
2. Create a Azure DevOps account and create a build pipeline for this repo. Check if the build was successful.
3. Create a Azure account and from `Container registries` -> `Repositories`, using the proper docker image created from previous step and tag, click `Deploy to web app` option.