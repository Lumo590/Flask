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
    professor=request.form["professor"]
    
    query="INSERT INTO courses (title,description,price,professor) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(title,description ,price,professor))
    conn.commit()
    return redirect("/courses")

@app.route("/delete/<int:id>",methods=["POST"])
def delete(id):
    conn=courses_db()
    cursor=conn.cursor()
    
    query="DELETE FROM courses WHERE id=%s"
    cursor.execute(query,(id,))
    conn.commit()
    return redirect("/courses")

@app.route('/edit/<int:id>')
def edit(id):
    conn = courses_db()
    cursor = conn.cursor()
    query = "SELECT * FROM courses WHERE id =%s"
    cursor.execute(query,(id,))
    courses = cursor.fetchone()
    return render_template("edit.html", courses = courses)

@app.route('/update/<int:id>', methods=["POST"])
def update(id):
    conn = courses_db()
    cursor = conn.cursor()
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    professor = request.form['professor']
    query = """
        UPDATE courses SET 
        title=%s ,
        description=%s,  
        price = %s,
        professor=%s
        WHERE id = %s
        """
    cursor.execute(query,(title,description, price,professor, id))
    conn.commit()
    return redirect('/courses') 
     

if __name__ == "__main__":
    app.run(debug=True)
