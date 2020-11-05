# DJANGO API
## Author  
  
[Victor Nduati](https://github.com/Vector254)  
  
# Description  
This is a Django application for an api that allows CRUD(create, read, update and delete operations on a database)

# User stories
1. CREATE
2. READ
3. UPDATE
4. DELETE 

  
   
  
## Setup and Installation  
   
##### Cloning the repository:  
 ```bash
 https://github.com/Vector254/v-rate.git
```
##### Navigate into the project folder and install dependencies  
 ```bash 
 pip install -r requirements.txt 
```
##### Install and activate Virtual environment
 ```bash 
 virtualenv virtual && source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User and Password, then makemigrations 
 ```bash 
 python manage.py makemigrations 
 ``` 
 Then Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Testing the application  
 ```bash 
 python manage.py test 
```

### API endpoints
#### To generate authentication tokens, provide username and password in request body then post to the link below
```bash
 http://localhost:8000/api-token-auth/
```
#### JSON web tokens
```bash
 http://localhost:8000/api/jwt-token/
```

#### GET requests(for POST requests add a trailing slash)
```bash
 http://localhost:8000/api/projects
```
#### single item operations(UPDATE & DELETE)
#### replace id with project id to get
```bash
http://localhost:8000/api/projects/project-id/id
```

## Technologies used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.1.2](https://www.djangoproject.com/download/)  
* [Django REST framework](https://www.django-rest-framework.org/)  
  
  
## Known Bugs  
* None, reach out below incase of any.
  
## Contact Information   
In case of any question or complaints, please [email](ochrist7@gmail.com) me
  
## License 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
 Copyright (c) 2019 **Vector**