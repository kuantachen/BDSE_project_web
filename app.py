from flask import Flask, render_template, request, url_for
from flask_moment import Moment
from datetime import datetime
from pathlib import Path
import uuid

# practice start
import recognition.load_model as model
# practice end

app = Flask(__name__)
moment = Moment(app)

# practice start
UPLOAD_FOLDER = Path(__file__).resolve().parent/'static/uploaded'
# practice end

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


#----------practice start------------

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/predict/insult', methods=['GET', 'POST'])
def get_para1():
    if request.method == "GET":
        return render_template('insult.html')
    elif request.method == "POST":
        # file = request.values # key is the value of name(html attribute) in <input type="file">
        # if file:
        #     filename = str(uuid.uuid4())+"_"+file.filename
        #     file.save(UPLOAD_FOLDER/filename)
        f0 = request.form.get('court')
        f1 = request.form.get('simplejudge')
        f2 = request.form.get('record')
        f3 = request.form.get('place')
        f4 = request.form.get('compromise')
        f5 = request.form.get('xword')
        f6 = request.form.get('education') 
        f7= request.form.get('financial')
        f8 = request.form.get('attitude')
        f9 = request.form.get('confess')
        f10 = request.form.get('sequel')
       
        
        insult = model.recog_digit_insult(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
        if insult == 1:
            result = "3,000元"
        elif insult == 2:
            result = "5,000元"
        elif insult == 3:
            result = "10,000元"
        elif insult == 4:
            result = "20,000元"
        else:
            result = "30,000元"
        return render_template('insult.html', predict = result)

@app.route('/predict/defamation', methods=['GET', 'POST'])
def get_para2():
    if request.method == "GET":
        return render_template('defamation.html')
    elif request.method == "POST":
        # file = request.values # key is the value of name(html attribute) in <input type="file">
        # if file:
        #     filename = str(uuid.uuid4())+"_"+file.filename
        #     file.save(UPLOAD_FOLDER/filename)
        f0 = request.form.get('court')
        f1 = request.form.get('simplejudge')
        f2 = request.form.get('record')
        f3 = request.form.get('place')
        f4 = request.form.get('compromise')
        f5 = request.form.get('xword')
        f6 = request.form.get('education') 
        f7= request.form.get('financial')
        f8 = request.form.get('attitude')
        f9 = request.form.get('confess')
        f10 = request.form.get('sequel')

        defamation = model.recog_digit_defamation(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
        if defamation == 0:
            result = "5,000元"
        elif defamation == 1:
            result = "10,000元"
        elif defamation == 2:
            result = "30,000元"
        elif defamation == 3:
            result = "50,000元"
        else:
            result = "100,000元"
        return render_template('defamation.html', predict = result)



@app.route('/member')
def member():
    return render_template("member.html")


#----------practice end-------------- 


if __name__=="__main__":
    app.run(debug=True)
