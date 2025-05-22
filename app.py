from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello_world():
    return '<h1>Welcome to Coding</h1>'
 
# main driver function
if _name_ == '_main_':
    app.run(debug=True,host='0.0.0.0')