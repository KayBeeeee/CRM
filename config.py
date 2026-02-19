import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('MYSQLUSER')}:{os.getenv('MYSQLPASSWORD')}"
        f"@{os.getenv('MYSQLHOST')}:{os.getenv('MYSQLPORT')}/"
        f"{os.getenv('MYSQLDATABASE')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
