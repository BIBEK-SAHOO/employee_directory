# Employee Search API

This project is a Django-based API for searching and filtering employees within a company. It leverages Django REST Framework (DRF) to provide a customizable and dynamic way to retrieve employee data based on various filters.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Unit Test](#unit-test)
- [Rate Limiting](#rate-limiting)
- [API Documentation](#api-documentation)

## Features

- **Dynamic Field Selection**: Fields included in the response are dynamically determined based on the company's column configuration.
- **Advanced Filtering**: Filter employees by status, location, company, department, and position.
- **Pagination Support**: Efficiently handle large datasets with built-in pagination.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/employee-search-api.git
   cd employee-search-api
   
2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
   
3. **Install the required packages**:
    ```bash
   pip install -r requirements.txt

4. **Apply migrations**:
    ```bash
   python manage.py migrate

5. **Run the development server**:
    ```bash
   python manage.py runserver

## Configuration
### Environment Variables

1. **Create a .env file in the root directory to manage your environment-specific settings**:
   ```bash
   DEBUG=True
   SECRET_KEY=your_secret_key_here

## Unit Test
1. **To run the tests, you can use pytest**: 
   ```bash
   pytest
   
## Rate Limiting
1. **The project uses Django REST Framework throttling to implement rate limiting.**
   
## API Documentation
1. **API endpoints can be viewed and interacted with using Swagger**:
   ```bash
   http://localhost:8000/swagger/
   http://localhost:8000/redoc/
   
2. **Sample URL**:
   ```bash
   http://localhost:8000/api/search/?company_name=edusoft&department=sales&location=new_york&position=engineer&status=active
   
3. **Admin URL/Credentials**:
   ```bash
   http://localhost:8000/admin
   username: admin
   password: admin
