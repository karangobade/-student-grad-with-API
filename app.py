from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to student grad system enter name and mark in api link /name/mark"

@app.route('/<name>/<int:mark>')
def grad(name,mark):
    if mark >=35:
        return f"{name} you are pass"
    else:
        return f"{name} you are fail"
    
if __name__=="__main__":
    app.run(debug=True)