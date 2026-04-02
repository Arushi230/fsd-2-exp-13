from flask import Flask, request, jsonify
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="college"
    )
    cursor = db.cursor()
    print("Database connected")

except:
    print("Database not connected")
    
# CREATE Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    # Validation
    if not name or not email or not course:
        return jsonify({"message":"All fields required"}),400

    query = "INSERT INTO student(name,email,course) VALUES(%s,%s,%s)"
    values = (name,email,course)

    cursor.execute(query,values)
    db.commit()

    return jsonify({"message":"Student added successfully"})


# READ Students
@app.route('/students', methods=['GET'])
def get_students():

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append({
            "id":row[0],
            "name":row[1],
            "email":row[2],
            "course":row[3]
        })

    return jsonify(students)


# UPDATE Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    course = data.get("course")

    if not name or not email or not course:
        return jsonify({"message":"All fields required"}),400

    query = "UPDATE student SET name=%s,email=%s,course=%s WHERE id=%s"
    values = (name,email,course,id)

    cursor.execute(query,values)
    db.commit()

    return jsonify({"message":"Student updated"})


# DELETE Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    query = "DELETE FROM student WHERE id=%s"
    values = (id,)

    cursor.execute(query,values)
    db.commit()

    return jsonify({"message":"Student deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    