

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345@localhost:5432/flasktask"


projectConfig = {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}

#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'flasktask',
#     'USER': 'postgres',
#     'PASSWORD': '12345',
#     'HOST': '127.0.0.1',
#     'PORT': '5432',
# }
