from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('register.html')
@app.route('/register',methods=['GET'])
def register():
    username=request.form.get('username')
    branch=request.form.get('branch') 
    year=request.form.get('year')
    return render_template('success.html')
if __name__=='__main__':
    app.run(debug=True,port=5001,host='0.0.0.0')
