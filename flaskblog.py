from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')
@app.route('/show_route',methods =['POST','GET'])
def showRoute():
    _start = request.form['startPoint']
    _end = request.form['EndPoint']
    print(_start)
if __name__ == '__main__':
    app.run()
