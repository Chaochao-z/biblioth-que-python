# Bibliothèque
## Presentation
This project aims to allow librarians to manage their books, create events and have a forum.
 All that compatible across multiple libraries.
## Install
### Starting the project
`$ docker-compose up -d`
### Creating an admin user
Attach to the web docker instance, then :  
`$ python manage.py createsuperuser`