# AI Usage Log

## Tool Used

* ChatGPT (OpenAI)


## 1. Flask Project Structure

### Prompt

How to structure a Flask project with routes, templates, and database connection?

### AI Output (Summary)

Suggested organizing the project using separate folders for routes, templates, and static files, along with a database connection file (`db.py`) and use of Flask Blueprints.

### My Modification

Implemented the structure using a `routes/` folder with separate files for dashboard, guests, and reservations. Adjusted imports and routing based on my application needs.

---

## 2. Database Connection in Flask

### Prompt

How to connect Flask to a MySQL database using Python?

### AI Output (Summary)

Provided example code using `mysql-connector-python` to establish a database connection and execute queries.

### My Modification

Created a `db.py` file and customized the connection settings (host, user, password, database). Integrated the connection into my Flask routes.

---

## 3. MySQL Workbench Issue

### Prompt

MySQL Workbench is showing a connection warning and not opening properly. What should I do?

### AI Output (Summary)

Explained that the warning was due to version incompatibility and suggested continuing anyway since it does not block functionality.

### My Modification

Proceeded with the connection and confirmed that queries and table operations worked correctly.

---

## 4. Table Export Issue

### Prompt

I am not able to see tables in the Data Export section of MySQL Workbench. How to fix it?

### AI Output (Summary)

Suggested checking schema selection, refreshing, and verifying table existence using SQL queries.

### My Modification

Verified tables using `SHOW TABLES` and used the `mysqldump` command as an alternative method to export the database schema.

---

## 5. GitHub & README Setup

### Prompt

How to add SQL and CSV files to a VS Code project and write a proper README for submission?

### AI Output (Summary)

Explained how to move files, commit them using Git, and generate a structured README with installation, database setup, and usage instructions.

### My Modification

Created a `Database_Tables` folder, added all required files, and customized the README to match assignment requirements and project structure.

---

## Notes

* AI was primarily used for debugging, setup guidance, and documentation support.
* All database design, schema creation, and application logic were implemented and verified independently.
* AI suggestions were reviewed and adapted before applying to the project.
