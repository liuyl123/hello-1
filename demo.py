# coding=utf-8
from flask import Flask, render_template, request, json

app = Flask(__name__)
app.Debug = True


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        Date = request.form['Date']
        Consume = request.form['Consume']
        ret = dict()
        ret['Date'] = Date
        ret['Consume'] = Consume
        return json.dumps(ret, ensure_ascii=False)


if __name__ == '__main__':
    app.run("127.0.0.1", port=3000)
