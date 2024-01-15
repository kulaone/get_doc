# Cloud Run with Langchain and unstructured

My try to deploy a cloud run service with langchain and unstructured.

## Build

- Set an environment variable with your GCP Project ID:

```
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
```

- Use a [Buildpack](https://github.com/GoogleCloudPlatform/buildpacks) to build the container:

```sh
gcloud builds submit --pack image=gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```

## Run Locally

```sh
docker run --rm gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```

## Test

```
pytest
```

_Note: you may need to install `pytest` using `pip install pytest`._

## Deploy

```sh
# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Deploy to Cloud Run
gcloud run deploy helloworld --source .
```

For more details on how to work with this sample read the [Python Cloud Run Samples README](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/run)
