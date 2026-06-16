# Inventory Management System (IMS)

A web-based Inventory Management System developed using Django and Bootstrap for managing organizational assets, inventory records, stock transactions, and asset assignments. The system provides real-time inventory tracking, reporting, and audit logging through an intuitive and responsive dashboard.

## Project Overview

The Inventory Management System (IMS) was developed as a final-year project to address the challenges associated with manual inventory management, such as poor record keeping, stock discrepancies, and inefficient asset tracking.

The system digitizes inventory operations by providing centralized management of inventory items, stock movements, asset assignments, and reports.

## Features

### Authentication and Authorization

* Secure user login and logout
* Administrator-controlled user accounts
* Role-based access control for administrators and staff

### Inventory Management

* Add new inventory items
* Update inventory records
* Delete inventory items
* Search and view inventory details
* Monitor stock quantities and statuses

### Stock Transactions

* Record stock-in operations
* Record stock-out operations
* Maintain transaction history
* Monitor stock movement analytics

### Asset Assignment

* Assign assets to users or departments
* Record assignment details
* Track assigned assets
* Monitor asset status and conditions

### Reports and Analytics

* Dashboard with inventory statistics
* Inventory by category chart
* Stock movement chart
* Low-stock alerts
* Recent transactions overview

### Audit Logging

* Record user activities
* Monitor system operations
* Maintain accountability and traceability

### Responsive Design

* Mobile-friendly user interface
* Responsive dashboard and tables
* Modern user experience using Bootstrap 5

## Technologies Used

### Backend

* Python
* Django Framework

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* jQuery
* Chart.js
* DataTables

### Database

* SQLite3

### Deployment

* Render

### Version Control

* Git
* GitHub

## System Modules

1. User Authentication Module
2. Inventory Management Module
3. Stock Transaction Module
4. Asset Assignment Module
5. Reporting Module
6. Audit Log Module

## Installation

### Clone the Repository

```bash
git clone https://github.com/NhartyInnovate/inventory-management-system.git
cd inventory-management-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

## Project Structure

```text
inventory-management-system/
│
├── ims_project/
├── inventory/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Screenshots

* Login Page
* Dashboard
* Inventory Management
* Asset Assignment
* Reports Dashboard
* Audit Logs

## Future Improvements

* Email notifications
* Barcode and QR code integration
* Export reports to PDF and Excel
* Cloud database integration
* Advanced role and permission management
* Inventory forecasting and predictive analytics

## Author

**Nathaniel Katugwa (NhartyInnovate)**

Matric Number: NOU223150149

Department of Computer Science

Faculty of Computing

National Open University of Nigeria (NOUN)

## License

This project was developed for academic purposes as a Final Year Undergraduate Project at the National Open University of Nigeria.
