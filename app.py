from flask import Flask ,render_template,request,redirect
from config import courses_db

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("homepage.html")
@app.route("/courses")
def courses():
    conn=courses_db()
    cursor=conn.cursor()
    
    query = "SELECT * FROM courses"
    cursor.execute(query)
    courses=cursor.fetchall()
    return render_template("courses.html",courses=courses)
@app.route("/show")
def show():
    return render_template("add_courses.html")
    
@app.route("/create",methods=["POST"])
def create():
    conn=courses_db()
    cursor=conn.cursor()
    
    title=request.form["title"]
    description=request.form["description"]
    price=request.form["price"]
    proccessor=request.form["proccessor"]
    
    query="INSERT into 'courses' (title,description ,price,proccessor) VALUE (%s,%s,%s)"
    cursor.execute(query,(title,description ,price,proccessor))
    conn.commit()
    return redirect("courses")
     
     

if __name__ == "__main__":
    app.run(debug=True)
