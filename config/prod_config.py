class Config:
    SECRET_KEY = "secret"
    SQLALCHEMY_DATABASE_URI = "postgresql:///cupcakes"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
