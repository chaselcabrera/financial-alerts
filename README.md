# Django Financial Alerts System

This project utilizes is built onto of the Financial Alert System Django [REST] framework provided by Piere found at 
https://github.com/Univers-Technology/financial-alerts. 

What has been added is a budget app which contains logic for three end-points listed below,

http://127.0.0.1:8000/api/alert

Supports GET & POST:
{
    user: id, 
    threshold: id, 
    message: 'text'
}

http://127.0.0.1:8000/api/transaction

Supports GET & POST:
{
    user: id, 
    date: "date", 
    category: "text", 
    description: "text", 
    amount: "decimal", 
    type: 'text'
}

http://127.0.0.1:8000/api/threshold

Supports GET & POST:
{
    user: id, 
    name: "text", 
    slug: "slug",
    threshold_amount: "decimal", 
    type: 'text'
}

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Build Migrations using `python manage.py makemigration`.
4. Apply migrations using `python manage.py migrate`.
5. Run the development server using `python manage.py runserver`.

## Testing
1. Test file can be found in budget app called "tests.py"
2. To run "python manage.py test"

## Given Additional Time

- Create the following models TransactionType, ThresholdType, TransactionCategory this would help in production env in searching for specific filtering
- Build in pagination, searching, ordering
- Add operator to ThresholdType allowing for greater than, equal to or less than logic to be applied to thresholds
- More Robust Testing of alerts and error 
- Build in error handling


## Steps to Deploy on Production


1. Stand Up Postgres DB RDS in AWS
2. Setup pgadmin
3. Adjust DJANGO settings to utilizing a production settings.py instead of the dev and ensure the production settings are routed to the Postres DB on AWS, adjust security settings
4. Dockerize the django app, including necessary dependencies and configuration in the Dockerfile and building the Docker image

    - Install Docker Desktop
    - Setup Dockerfile within project folder
    Dockerfile Content: 
    FROM python:3.13-alpine
    RUN apk update &&  \ 
        ask add nano

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1

    WORKDIR /app

    COPY ./requirements.txt /app
    RUN pip install —no-cache-dir -r requirements.txt
    ...

5. Secure application: Configure IAM roles, security groups and VPC and leverage AWS Secrets to manage credentials

6. Container orchestration with ECS
    Setup ECS cluster
    Create an ECS task definition for Django application

7. Push Docker Image to ECR
    Create a repositry in ECR to store the Docker Image and Push Docker Image

8. Deploy to AWS
    Use ECS to deploy Dockerized Django application
    Configure auto-scaling policies and health checks

9. Load Balancer, DNS & SSL
    Setup DNS records to point domain to AWS resources, load balancer

10. Site should be functional at this point but as an added step Redis cache could be used as a state cache

11.) Bonus, setup CDN on S3 and leverage CloudFrount for any images/videos 
