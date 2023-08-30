class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///cupcakes_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
