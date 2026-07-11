from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery #KeyboardButton, ReplyKeyboardMarkup
from aiogram import F, Router
import app.keyboard as kb
import app.database.requests as rq
from app.database.requests import add_or_get_user
#from aiogram.fsm.context import FSMContext
#from aiogram.fsm.state import State, StatesGroup

router = Router()




@router.message(CommandStart())
async def cmd_srt(message: Message):
    tg_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    # Добавляем или получаем пользователя
    user = await add_or_get_user(tg_id, first_name, username)
    # Приветствие
    await message.answer(
        f"Привет, {first_name}! Ты добавлен в базу данных с ID: {user.id}",
        reply_markup= kb.first
    )
    
 
@router.message(F.text == 'Каталог')
async def catalog(message: Message):
   pass

  









  


