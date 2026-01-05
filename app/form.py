from flask import Flask, request, render_template, session
from .db import create_record_table, get_conn

create_record_table()
app = Flask(__name__)


@app.route("/")
def form():
    name = name = request.args.get("name", "")
    weight = request.args.get("weight", type=int)
    sets = request.args.get("sets", type=int)
    reps = request.args.get("reps", type=int)
    days = request.args.get("days", type=int)

    records = record()

    return render_template("index.html", name=name, weight=weight, sets=sets, reps=reps, days=days, datas=records)

@app.route("/submit", methods=["POST"])
def submit():
    name= request.form.get('name')
    weight=request.form.get('weight', type=int)
    sets=request.form.get('sets', type=int)
    reps=request.form.get('reps',type=int)
    days=request.form.get('days', type=int)

    temp=sets*reps*days
    num=0
    if sets==1 and reps<=15:
        message="セット数を増やそう！"
        num=2
    elif reps<3:
        message="回数を増やそう!"
        num=2
    
    elif days<3:
        message="現状維持"
        num=4
    
    elif 3<=days<5 and temp<=90:
        message="重量を上げても良いかもしれない"
        num=3
    
    elif 8<=days and 210<=temp:
        message="今すぐ重量を上げよう!"
        num=1
    
    else:
        message="重量を上げよう!"
        num=2
    
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO users (name, weight, sets, reps, days) VALUES (%s, %s, %s, %s, %s)",
    (name, weight, sets, reps, days)
    )
    conn.commit()

    deleteOldHistory()  
    records = record()

    cur.close()
    conn.close()


    return render_template("index.html", name=name, weight=weight, sets=sets,reps=reps, days=days, message=message,num=num,datas=records)




def record():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT name, weight, sets, reps, days, created_at
        FROM users
        ORDER BY created_at DESC
        LIMIT 5;
    """)

    records = cur.fetchall()
    cur.close()
    conn.close()
    return records


def deleteOldHistory():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM users
        WHERE id NOT IN (
            SELECT id
            FROM users
            ORDER BY created_at DESC
            LIMIT 5
        );
    """)
    conn.commit()

    cur.close()
    conn.close()
