from flask import Flask, render_template
import pymysql
from flask import request

app = Flask(__name__, template_folder='html')

@app.route("/first/step")
def index():
    return render_template("login.html")

@app.route("/register/step", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")

    name = request.form.get("name")
    password = request.form.get("password")
    gender = request.form.get("gender")

    # connect to MYSQL
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="AWNYGELL030910", charset="utf8", db="db1")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # send command
    sql = 'insert into register(name,password,gender) values(%s,%s,%s)'
    cursor.execute(sql, [name, password, gender])
    conn.commit()

    # close mysql
    cursor.close()
    conn.close()

    return "Successfully registered!!!"

@app.route("/post/step", methods=['POST'])
def post_register():
    # receive the data from the former website with the form of 'POST'
    # give the result back to user
    print(request.form)
    return render_template('Back_page.html')

@app.route('/Plan/Page', methods=["POST"])
def plan_page():
    return "Start planning a wonderful trip"
#
if __name__ == '__main__':
    app.run()
