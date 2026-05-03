# Hotel Management System

## Project Description
  This is a Flask-based Hotel Management System that uses MySQL to manage hotel operations such as guests, rooms, reservations, and payments.
  
  This application is designed for hotel staff or administrators to efficiently manage hotel data through a web interface.

## Installation Instructions

  1.Clone the repository:
  
      git clone <your-repo-url>
      cd <your-repo-folder>
  
  2.Create and activate a virtual environment:
  
      python3 -m venv venv
      source venv/bin/activate
  
  3.Install dependencies:
        
        pip install flask mysql-connector-python

## Database Setup

    The database schema is provided in the Database_Tables folder.
    
    Step 1: Create database and tables
    
    Run the following command from the project root:
    
    mysql -u root -p < Database_Tables/schema.sql
    
    This will create the HotelDB database and all required tables.
    
    Step 2: Import data (CSV files)
    
    The dataset is provided in CSV format:
    
    Database_Tables/
    ├── Guests.csv
    ├── Rooms.csv
    ├── Reservations.csv
    ├── Payments.csv

  # To import data:

    Open MySQL Workbench
    Right-click a table → Table Data Import Wizard
    Select corresponding CSV file
    Repeat for all tables
## Usage:

  Start the Flask application:
  
      python app.py
  
  Open in browser:

    http://127.0.0.1:5000
    
  # Features :
  Manage Guests
  Manage Rooms
  Handle Reservations
  Track Payments
