# Employee Search API

This project is a Django-based API for searching and filtering employees within a company. It leverages Django REST Framework (DRF) to provide a customizable and dynamic way to retrieve employee data based on various filters.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Pagination](#pagination)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Dynamic Field Selection**: Fields included in the response are dynamically determined based on the company's column configuration.
- **Advanced Filtering**: Filter employees by status, location, department, and position.
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

**Create a .env file in the root directory to manage your environment-specific settings**:

```bash
    DEBUG=True
    SECRET_KEY=your_secret_key_here
