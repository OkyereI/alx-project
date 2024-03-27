from flask import Flask, render_template, request, Response, send_file,redirect, url_for
app = Flask(__name__)

# items to display as company projects
companys=[
    {
        'id':1,'project':'web development','status':'available', "location":'Ghana'
    },
     {
        'id':2,'project':' Registration form development','status':'available',"location":'Ghana'
    },
     {
        'id':3,'project':'Database Management','status':'available',"location":'Ghana'
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', companys = companys)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7002, debug=True)