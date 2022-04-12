from sqlalchemy.orm import Session

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

from Database import engine
from Tables import User

class UserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        chat_id = message.from_user['id']
        username = message.from_user['username']

        with Session(engine) as session:
            user: User = session.query(User).where(
                User.chat_id == chat_id
            ).first()

            if not user:
                user = User(
                    chat_id=chat_id,
                    username=username
                )
                session.add(user)
            session.commit()
            data['user'] = user
            data['user_role'] = user.role


        