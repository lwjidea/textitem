
class Text(object):
    sqlli = "mysql"
    driver = "mysqldb"
    host = "127.0.0.1"
    port = "3306"
    user = "lwj"
    password = "123456"
    database = "textdb"
    charset = "utf8"

    def to_set(self,app):
        app.config["SQLALCHEMY_DATABASE_URI"]="{}+{}://{}:{}@{}:{}/{}?charset={}".format(
            self.sqlli,self.driver,self.user,self.password,self.host,self.port,self.database,self.charset
        )
        app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True
        app.config["SESSION_KEY"]= "ad.w;/dad[d}da1.d\8a"