import os
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if os.environ.get("dev") == "true":
    # Muss durch env variablen ersetzt bzw durch txt file ersetzt werden
    UPLOAD_FOLDER = r"C:\Users\Public\Downloads"

    DB = "aq"
    USER = "flask_user"
    PW = "Aperion2023"
    PORT = 5432
    HOST = "localhost"
    connection_string = f"postgresql+psycopg2://{USER}:{PW}@{HOST}:{PORT}/{DB}"

    connection_string = connection_string

    # HOST = 'localhost\\SQLEXPRESS'
    # DB = 'Heat_local'
    # USER='flask_user'
    # PW = 'Aperion2023'
    # PORT = 1433
    # connection_string = f"mssql+pyodbc://{USER}:{PW}@{HOST}:{PORT}/{DB}?driver=ODBC+Driver+18+for+SQL+Server" #?options=-csearch_path%3D{SCHEMA}

else:
    UPLOAD_FOLDER = r"C:\Users\Public\Downloads"
    HOST = "10.31.153.28"
    DB = "CA_R_MS_PORTFOLIO_DB"
    USER = "CARMSDB"
    PW = "Pe2lNK+Lajf5XSe4*SFf91e36"
    PORT = 60011
    connection_string = f"mssql+pyodbc://{USER}:{PW}@{HOST}:{PORT}/{DB}?driver=ODBC+Driver+17+for+SQL+Server"  # ?options=-csearch_path%3D{SCHEMA}


SQLALCHEMY_DATABASE_URI = connection_string
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_pre_ping": True,
}

ALLOWED_EXTENSIONS = {".xlsx", ".xlsm"}
DEBUG = True
SECRET_KEY = "DiesesJahrBaueIchCooleSoftwareBeiAperion"

SECURITY_PASSWORD_SALT = "251792882350722049398923633490206800359"
REMEMBER_COOKIE_SAMESITE = "strict"
JWT_SECRET_KEY = SECRET_KEY

JWT_COOKIE_SECURE = False
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=60 * 8)
