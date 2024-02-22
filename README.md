________________Content Management System API________________

This is a Django REST Framework-based API for a Content Management System (CMS) that allows users to manage and interact with content items. The system supports two types of user roles: admin and author.

__Features__
* User Authentication: Supports registration and login for authors using email.
* Role-based Access Control: Admin users can view, edit, and delete all content items, while authors can only manage their own content.
* Search Functionality: Users can search for content items by title, body, summary, and categories.
* Field Level Validations: Implements validations for user and content item fields to ensure data integrity.
* Test-Driven Development (TDD): Test cases are written before implementing features to ensure robustness and reliability.
* Token-Based Authentication: Uses token-based authentication for secure access to the API endpoints.

__Technologies Used__
* Python
* Django
* Django Rest Framework

__Setup Instructions__
1. git clone https://github.com/shammas01/Arcitech_Content.git
2. cd Arcitech
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

__Testing__
* python manage.py test




