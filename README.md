# lead_generator
<hr>

Lead generator is service for searching leads by location and keywords from Google Maps. 
It shows them to user and store to database. Access to 
search only for register user.

## Features:
<hr>

- User authenticate
- Admin panel: /admin/
- Search leads by location and keywords

## Installing using GitHub
<hr>

## Run with docker
<hr>

Docker should be installed

```python
git clone https://github.com/Terrrya/lead_generator.git
cd lead_generator
```

Create in root directory of project and fill .env file as shown in .env_sample file

```python
docker compose up
```
Open in browser 127.0.0.1:8000/api/ 

## Filling .env file
<hr>

To fill .env file you have to get Google API Key. 
<br> https://developers.google.com/maps/documentation/javascript/get-api-key can help you to get Google API token

## Getting access
<hr>

You can use following:
- superuser:
  - Username: admin
  - Password: 12345

Or create another superuser through admin panel or user by: /accounts/sign-up/
