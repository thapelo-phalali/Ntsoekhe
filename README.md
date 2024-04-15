Ntsoekhe Distributed Database Management System (DDBMS)
Welcome to the Ntsoekhe Distributed Database Management System (DDBMS) project. This system is designed to manage patients' medical information in a distributed manner using Django and SQLite. It provides functionalities for creating, retrieving, updating, and deleting patient records across multiple nodes.

Project Overview
The Ntsoekhe DDBMS is built with the following components and features:

Django Backend: Utilizes Django for backend development, providing a robust framework for web applications.
SQLite Database: Uses SQLite as the database engine for storing patient and medical data locally on each node.
Peer-to-Peer (P2P) Architecture: Implements a decentralized network of nodes using Django with P2P frameworks like IPFS or Dat for data synchronization.
CRUD Operations: Supports CRUD (Create, Read, Update, Delete) operations for managing patient records across distributed nodes.
Security and Access Control: Implements SSL/TLS encryption, user authentication, and role-based access control (RBAC) to secure sensitive health data.
User Interface: Provides user-friendly interfaces for interacting with the database, including patient listing, detail view, creation, updating, and deletion.

System Requirements
Functional Requirements:
Support CRUD operations across a minimum of three distributed nodes.
Ensure data consistency and replication strategies for fault tolerance.
Implement secure access controls with robust authentication and RBAC.

Non-Functional Requirements:
User-friendly interface for database interactions.
Data encryption and anonymization to protect patient privacy.
Audit trails and logging for security monitoring and compliance.

Installation and Setup
Prerequisites:
Python (version 3.6 or higher)
Django (version 3.x or 4.x)
Docker (optional, for containerization)

Steps to Run the Project Locally:
1. Clone the Repository:
git clone https://github.com/thapelo-phalali/Ntsoekhe
cd ddbms_project

2. Install Dependencies:
pip install -r requirements.txt

3. Initialize the Database:
python manage.py migrate
python manage.py createsuperuser

4. Run the Development Server:
python manage.py runserver

5. Access the Application:
Open a web browser and go to http://127.0.0.1:8000/ to access the application.

Usage
Once the application is running, you can perform the following actions:

View Patients: Navigate to http://127.0.0.1:8000/patients/ to see a list of all patients.
Add New Patient: Click on "Add Patient" to create a new patient record.
Update Patient: Click on a patient's name to edit their information.
Delete Patient: Click on "Delete" next to a patient's name to remove their record (confirmation required).

Contributing
Contributions to this project are welcome! If you have suggestions, feature requests, or bug reports, please feel free to submit a pull request or open an issue on GitHub.

License
This project is licensed under the MIT License.
