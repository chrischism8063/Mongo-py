# main entry to the system
from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)


@app.route("/courses")
def courses():
    courseData = [{"courseID": "1111", "title": "PHP 111", "description": "intro to PHP", "credits": "3", "term": "Fall, Spring"},
    {"courseID": "1411", "title": "C++","description": "intro to C++", "credits": "3", "term": "Summer"},
    {"courseID": "1151", "title": "FLASK 110","description": "intro to FLASK", "credits": "3", "term": "Spring"},
    {"courseID": "121", "title": "C# 110", "description": "intro to C#","credits": "3", "term": "Fall, Spring"},
    {"courseID": "1126", "title": "HTML 101","description": "intro to HTML", "credits": "3", "term": "Spring"},
    {"courseID": "1123", "title": "NET 100","description": "intro to NET", "credits": "3", "term": "Summer"}]
    return render_template("courses.html", courseData=courseData, courses=True)


@app.route("/register")
def register():
    return render_template("register.html", register=True)
