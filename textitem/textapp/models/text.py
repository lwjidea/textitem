from . import db
# 这是测试模型
class Text(db.Model):
    # 表的名字（如果放在定义表之后就是创建一个和此表字段相同的表）
    __tablename__ = 'text'
    # 定义id主键，自增字段
    tid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 定义不能为空，且唯一的姓名字段
    name = db.Column(db.String(10), unique=True, nullable=False)
    # 定义整型，默认为20的年龄字段
    age = db.Column(db.Integer, default=20)