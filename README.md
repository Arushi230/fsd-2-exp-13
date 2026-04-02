# Flask CRUD Student API

This project implements CRUD operations using Flask and MySQL.

Technologies Used:
- Python Flask
- MySQL
- Postman

Database Table:
student(id, name, email, course)

API Endpoints:
POST /students
GET /students
PUT /students/<id>
DELETE /students/<id>

Steps to Run:
1. Install dependencies
pip install flask
pip install mysql-connector-python

2. Create database and table in MySQL

3. Run server
python app.py

4. Test APIs using Postman 
# Screenshots
MySQL Database:- ![Database](<Screenshot (373).png>)
POST Request:- ![POST](<Screenshot (374).png>)
Outcome of POST Request:- ![Database returned after Post](<Screenshot (375).png>)
GET Request:- ![GET](<Screenshot (376).png>)
PUT Request:- ![PUT](<Screenshot (377).png>)
Outcome of PUT:- ![Updation of databse after PUT reques](<Screenshot (379).png>)
DELETE Request:- ![DELETE](<Screenshot (380).png>)
Outcome of DELETE:- ![Database deleted](<Screenshot (381).png>)
