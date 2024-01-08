# Employee Management System

Employee Management System is a web application built with Django and Bootstrap for managing employee hierarchies, displaying employee information, and providing sorting and searching functionalities.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
  - [Employee Hierarchy](#employee-hierarchy)
  - [Employee List](#employee-list)

## Features

- Display employee hierarchy in a tree-like structure.
- Lazy loading for employee hierarchy.
- Sort and search employees without page reloads using AJAX.
- Bootstrap styling for a responsive and modern UI.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (3.x)
- Django
- venv (optional but recommended for virtual environment management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/employee-management.git
   ```
2. Navigate to the project directory:

    ``` bash
    cd employee-management
    ```
3. Create and activate a virtual environment:
    ``` bash
    python -m venv venv
    source venv/bin/activate    # On Linux/Mac
    .\venv\Scripts\activate     # On Windows

   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Apply migrations:
    ```bash
    python manage.py seed_data
    ```
7. Run the development server:
    ```bash
    python manage.py runserver

    ```

## Usage
### Employee Hierarchy
1. Navigate to the Employee Hierarchy page to view the hierarchical structure of employees. 
2. Lazy loading is implemented, so you can expand/collapse branches of the tree. 
3. Clicking on an employee can load additional levels of the hierarchy.
### Employee List
1. Go to the Employee List page to view a table of all employees. 
2. Sort the table by clicking on column headers. 
3. Use the search bar to filter employees based on various fields.