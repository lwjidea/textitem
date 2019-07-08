from flask import Blueprint, render_template, request, session
from ..models import db
from ..models.text import Text
# 这是一个测试蓝图
tblue = Blueprint("tblue",__name__)


@tblue.route("/")
def hello():
    try:
        db.drop_all()
        msg = "数据库连接成功"
        print(msg)
    except Exception as e:
        msg = "数据库连接失败:%s"%e
        print(msg)
    data = {}
    a = "hello"
    data["a"]=a
    data["msg"]=msg
    return render_template('hello.html', **data)

@tblue.route("/lod")
def addse():

    return "session设置"

@tblue.route("/ppp")
def redse():
    sess = request.session.get("aaa")
    return