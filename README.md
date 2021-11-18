# reports

A simple automation framework.

Developed with React, Flask and MongoDB.

Check a demonstration [here](https://henriquencmt-reports-ui.herokuapp.com).

Running locally
---------------

Ensure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

Clone the repository to your local environment.

```shell
git clone https://github.com/henriquencmt/reports.git
```

Navigate to the project directory and copy the files ".example.env" to files called ".env".

```shell
cd reports
cp reports_api/.example.env reports_api/.env
cp reports_service/.example.env reports_service/.env
```

:warning:
If you want to be able to send reports by email each time a report runs, change the keys `EMAIL_USER` and `EMAIL_PASSWORD` values.
You have to setup your MongoDB instance with a database called "users" with a collection called "users", and insert users containing these two fields: { "mailing_list": true, "email": "example@email.com" }.

Start the application containers.

```shell
docker-compose up
```