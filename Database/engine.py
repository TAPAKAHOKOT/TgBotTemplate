from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    '{DB}://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'.format(
        DB=getenv("DB"),
        DB_USER=getenv("DB_USER"),
        DB_PASS=getenv("DB_PASS"),
        DB_HOST=getenv("DB_HOST"),
        DB_NAME=getenv("DB_NAME")
    ), echo=True
)