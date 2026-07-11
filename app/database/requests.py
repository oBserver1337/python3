from app.database.madels import async_session
from app.database.madels import User,Category,Item
from sqlalchemy import select

async def add_or_get_user(tg_id : int, first_name: str, username : str =None):
  async with async_session() as session:
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    if not user:
      user = User(tg_id=tg_id,
                  first_name=first_name,
                  username=username,
                  tg_name = first_name)
      session.add(user)
      await session.commit()
      
      await session.refresh(user)
    return user

     

