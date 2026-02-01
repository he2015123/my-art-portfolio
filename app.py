from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "我的第一个网站运行成功！"

if __name__ == '__main__':
    app.run()