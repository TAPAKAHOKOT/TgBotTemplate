from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:postgres@localhost/tg_bot_template', echo=True
)