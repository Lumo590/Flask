import pymysql

def courses_db():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mysql_curses",
        cursorclass=pymysql.cursors.DictCursor
    )

    print("Database connected successfully")
    return conn

if __name__ == "__main__":
    courses_db()