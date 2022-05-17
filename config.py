
import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://joy:book@localhost/blogs"
   
    SECRET_KEY = "mysecretkey"
    SESSION_COOKIE_SECURE = False
  
    WTF_CSRF_ENABLED = False



class ProdConfig(Config):
    pass
 
class DevConfig(Config):
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig
}