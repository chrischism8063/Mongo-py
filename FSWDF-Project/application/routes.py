# main entry to the system
from application import app, db
from flask import render_template, request, json, Response

courseData = [
    { "courseID": "1111", "title": "PHP 111", "description": "intro to PHP", "credits": "3", "term": "Fall, Spring" },
    { "courseID": "1411", "title": "C++", "description": "intro to C++", "credits": "3", "term": "Summer" },
    { "courseID": "1151", "title": "FLASK 110", "description": "intro to FLASK", "credits": "3", "term": "Spring" },
    { "courseID": "121", "title": "C# 110", "description": "intro to C#","credits": "3", "term": "Fall, Spring" },
    { "courseID": "1126", "title": "HTML 101","description": "intro to HTML", "credits": "3", "term": "Spring" },
    { "courseID": "1123", "title": "NET 100", "description": "intro to NET", "credits": "3", "term": "Summer" }
]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/login")
def login():
    return render_template("login.html", login=True)



@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):   #When parameters exsist, must also add them to the render_template function call
   
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/register")
def register():
    return render_template("register.html", register=True)


#add form to get items from form
#request.args.get is to pull data from the GET method / options in the get method
@app.route("/enrollment", methods=["GET", "POST"])      #State methods of acceptability
def enrollment():
    id = request.form.get['courseID']     
    title = request.form.get['title']
    term = request.form.get['term']
    return render_template("enrollment.html", enrollment=True, data={"id":id, "title":title, "term":term })


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
        if(idx == None):
            jdata = courseData
        else:
            jdata = courseData[int(idx)]
        
        return Response(json.dumps(jdata), mimetype="application/json")

#create user class
class User(db.Document):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )   
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30 )
    password    =   db.StringField( max_length=30 )

@app.route("/user")
def user():
    # User(user_id=1, first_name="Christopher", last_name="Chism", email="chrischism@aol.com", password="1234ab" ).save()
    # User(user_id=2, first_name="Bob", last_name="Stephens", email="BobStephens@aol.com", password="1256de").save()
    users = User.objects.all()
    return render_template("user.html", users=users)

