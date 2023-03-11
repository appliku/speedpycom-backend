# SpeedPyCom Starter Template

## Quickstart

This is the starter backend boilerplate SpeedPyCom.

Edit any files you want to change and start building your project.

It is recommended to avoid editing project/settings_base.py for ease of future updates.

## Update SpeedPyCom
To update speedpycom-backend update the requirements.txt and settings_base.py files.

### Get the template and start work

For local development you should have Docker instance running locally.

Read more about docker-compose.yml down the document.

```bash
curl -sSL https://gitlab.com/speedpycom/speedpycom-backend/-/archive/main/speedpycom-backend-main.zip > speedpycom-backend-main.zip
unzip speedpycom-backend-main.zip

mv speedpycom-backend-main myproject
cd myproject
cp start.env .env
```


Apply migrations with:

```bash
docker compose run web python manage.py migrate
```

Create a superuser account:

```bash
docker compose run web python manage.py makesuperuser
```

The output of the last command will display the login and password for the admin user that was created, like this:

```
admin user not found, creating one
===================================
A superuser was created with email admin@example.com and password xLV9i9D7p8bm
===================================
```

Run the project with:

```bash
docker compose up
```


Open [http://127.0.0.1:8060/admin/](http://127.0.0.1:8060/admin/) and login with these credentials.

## Docker-Compose.yml for local development

This template implies using Docker for local development.

If you don't have Docker installed go
to [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) and follow
installation instructions for your OS.

`docker-compose.yml` file has a number of services defined to run the project.

To reduce the initial resource usage on your machine only few of them are uncommented and will be used:

- `redis`
- `db`
- `web`

If you need Celery - uncomment all lines for the `celery` service.

Same way, if you need Celery Scheduler – uncomment `celery-beat` service.

Flower (celery monitoring) is also included, uncomment `flower` service in order to have it running.

For the purpose of using less resource of your machine Redis is used for Celery broker by default.

You can easily switch to using RabbitMQ by uncommenting `rabbitmq` service and `rabbitmq` in all services' `links`
and `depends_on` sections.

Then in `.env` change the broker setting to this: `CELERY_BROKER_URL=amqp://speedpycom:speedpycom@rabbitmq/speedpycom` and `docker-compose restart` so the new settings are
applied.

## Dockerfile

Dockerfile contains instructions for convenient development. Uncomment the `useradd` and `USER` lines to develop within GitPod environment.

## Deployment

In order to deploy the project on [https://Appliku.com](https://Appliku.com) we have included the `Procfile` with commands needed to run your project.


## User model

Project template comes with a custom user model in the app `usermodel`.
