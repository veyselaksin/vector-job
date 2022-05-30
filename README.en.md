# Vector Job
Vector Job was created as an application study to Baykar Defense Industry. Multiple technologies and software tools are used in this project.

## İçindekiler
* [What is the Vector Job?](#vectorjob)
* [Used Technologies](#tech)
* [Setup](#setup)

<a name="vectorjob">
<h2>What is the Vector Job?</h2>
</a>

Vector Job is a job search platform where you can easily find a job and manage your applications, if you are a manager, you can open a job posting. You can filter job postings suitable for you, view them in your workflow and apply for one or more job postings you like.

**Note:** An activation link will be sent to your email address while registering. Your account will not be active until you click on the activation link. If you can't view the mail, please don't forget to check spam too!

<code>Vecor Job Web Site: http://ec2-52-12-227-159.us-west-2.compute.amazonaws.com</code>

<a name="tech">
<h2>Used Technologies</h2>
</a>

Vector Job was created using multiple technologies and tools. Vector Job project has been developed with the following technologies.

* AWS (Amazon Web Services)
* Docker
* Docker Compose
* NGINX
* Git / Github (for easy deployment integration)
* PostgreSQL
* Django
* Python
* HTML / CSS / Javascript
* Bash Scripts
* uWSGI

Developed using Docker, Vector Job offers an easy and convenient CI/CD operation process. Working in integration with Github, Docker can be integrated from the test environment to the production environment with a few commands.

On the AWS side, a cloud-based system was designed with EC2 (Elastic Compute Cloud) (Ubuntu 22.04 LTS Server was used). With the easy integration provided by Docker and Git / Github technologies, Vector Job project can run on local servers or any server of your choice. Detailed information about the installation will be shared under the [setup](#setup) heading.

<a name="setup">
<h2>Setup</h2>
</a>

First you need to download the project and go to the project directory.

```bash
git clone https://github.com/veyselaksin/vector-job.git
cd vector-job
```

**Note:** Docker is required to run the project. Otherwise the project will stop running and you will get an error.

**Note 2:** If you get docker-compose version error in the project, don't forget to update your <code>docker-compose</code> version!

**Note 3:** If you are working on a computer with a Linux operating system, please go to the main directory of the project and run the <code> sudo chmod -R a+rwx ./data </code> command on the terminal.

```bash
docker-compose build
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose up
```

* The <code>docker-compose build</code> command makes the docker file executable.
* <code>docker-compose run --rm app sh -c "python manage.py createsuperuser"</code> command is the command that helps us create username and password for our Django Application's admin panel login.
* The <code>docker-compose run --rm app sh -c "python manage.py makemigrations"</code> command is a command used when making changes, additions and removals on database models. If you are using more than one database, please specify the database specifically!
* <code>docker-compose up</code> is the command that makes the project stand up.

If you want to start and deploy the project on a local server, you need to run the following command lines.

```bash
docker-compose -f docker-compose-prod.yml build
docker-compose -f docker-compose-prod.yml run --rm app sh -c "python manage.py createsuperuser"
docker-compose -f docker-compose-prod.yml run --rm app sh -c "python manage.py makemigrations"
docker-compose -f docker-compose-prod.yml up -d
```

<code> -f docker-compose-prod.yml </code> parameters have been added while working on production mode. The "-f" statement specifically indicates that a file will be built. If you are not going to work in production mode, please do not use these command lines.