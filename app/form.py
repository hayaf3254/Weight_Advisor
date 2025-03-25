from flask import Flask, request, render_template,session

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("index.html")

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
    return render_template("index.html", name=name, weight=weight, sets=sets,reps=reps, days=days, message=message,num=num)


