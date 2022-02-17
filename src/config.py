class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'T3mp0r@l'
    MYSQL_DB = 'usuarios'


config = {
    'development': DevelopmentConfig
}
