# Django REST Framework (DRF) Learning Guide

This repository documents my learning journey of Django REST Framework (DRF) based on a detailed video tutorial. Below is a structured breakdown of key concepts covered.

---

## Introduction
- Overview of Django REST Framework (DRF)
- Importance of REST APIs

## Software Installation
- Setting up Python
- Installing Django
- Installing Django REST Framework

## APIs and REST APIs
- What is an API?
- Understanding REST principles
- How APIs communicate using HTTP

## Django & DRF Installation
- Setting up a Django project
- Installing Django REST Framework
- Creating a Django app

## Building APIs
- Creating a simple API endpoint
- Understanding web application endpoints
- Writing basic views in Django
- Introduction to models in Django

## Serializers
- What is serialization?
- Manual serialization
- Using Django REST Framework Serializers

## Function-Based Views
- Writing GET methods
- Storing data using serializers
- Retrieving, updating, and deleting data

## Class-Based Views
- Introduction to Class-Based Views (CBVs)
- Creating Employee model
- Writing GET, POST, PUT, DELETE methods in CBVs

## Mixins
- Understanding mixins in Django
- List and Create Model Mixins
- Retrieve, Update, Destroy Mixins

## Generics
- Introduction to generics
- Using ListCreateAPIView
- RetrieveUpdateDestroyAPIView for CRUD operations

## ViewSets
- Introduction to ViewSets
- Creating and retrieving data using ViewSets
- Understanding ModelViewSets

## Nested Serializers
- Introduction to nested serializers
- Creating Blog and Comment models
- Implementing nested serialization
- Primary key-based operations on nested models

## Pagination
- Overview of pagination in DRF
- Global pagination settings
- Custom pagination techniques

## Filtering & Search
- Custom filtering by designation, name, and ID
- Advanced filtering techniques
- Search filters and ordering

## Final Thoughts
- Summary of Django REST Framework features
- Best practices for building REST APIs
- Future learning paths

---

##  Running the Project
To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/oshowritescode/django-api.git
cd django-api

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
```

---

## Contributions
Feel free to fork this repository and contribute to improve the documentation or add more learning resources!




### 🚀 Happy Coding with Django REST Framework! 🎉

