from flask import Flask, render_template, redirect, url_for, request
import pymysql
from flask import request

app = Flask(__name__, template_folder='html')

@app.route("/first/step")
def login():
    if request.method == 'GET':
        return render_template("login.html")
    return redirect(url_for('Home_page'))

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

    return redirect(url_for('Home_page'))

@app.route("/post/step", methods=['POST'])
def post_register():
    # receive the data from the former website with the form of 'POST'
    # give the result back to user
    print(request.form)
    return render_template('Back_page.html')

@app.route('/Home/Page', methods=["POST","GET"])
def Home_page():
    message = ''
    if request.method == 'GET':
        return render_template('home.html', message='Please choose a button')

    if request.method == 'POST':
        bt_a = request.values.get("button1")
        bt_b = request.values.get("button2")
        bt_c = request.values.get("button3")
        if (bt_a == 'Create a New Plan'):
            return render_template('CreatNewPlan.html')
        if (bt_b == 'View Plans'):
            return render_template('ViewPlans.html')
        if (bt_c == 'Search for Recommendations'):
            return render_template('SearchRecommendation.html')

@app.route('/Plan/Page', methods=['GET','POST'])
def CreateNewPlan():
    if request.method == 'GET':
        return render_template("CreatNewPlan.html")
    elif request.method == 'POST':
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        startdate = request.form.get("startdate")
        returndate = request.form.get("returndate")
        plan = request.form.get("plan")

        # connect to MYSQL
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="AWNYGELL030910", charset="utf8", db="db2")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        # send command
        sql2 = 'insert into plan(origin,destination,startdate,returndate,plan) values(%s,%s,%s,%s,%s)'
        cursor.execute(sql2, [origin,destination,startdate,returndate,plan])
        conn.commit()

        # close mysql
        cursor.close()
        conn.close()

        return redirect(url_for('Home_page'))


# @app.route("SearchRecommendation", methods=['POST'])
# # 这个页面会出现一个search box，让用户输入一个travel destination
# # 这里用户输入的内容不录入database，但要根据用户输入的destination在下面ViewRecommendation的界面显示database中和这个destination有关的所有plan
# def SearchRecommendation():
#     return render_template("SearchRecommendation.html")
#
# @app.route("ViewRecommendation", methods=['POST'])
# # 这里不包含信息录入
# # 这个界面是根据用户在上一个SearchRecommendation界面中输入的destination，显示database中和这个destination有关的所有plan
# def ViewRecommendation():
#     return render_template("ViewRecommendation.html")

if __name__ == '__main__':
    app.run()
