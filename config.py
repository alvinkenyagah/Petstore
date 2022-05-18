
import os 

class Config:
    SECRET_KEY = 'voke'
    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1421@localhost/petstore'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
     # api config
 



class ProdConfig(Config):
    pass
 
class DevConfig(Config):
    DEBUG = True



config_options = {
'development':DevConfig,
'production':ProdConfig
}