
import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bd import Database
import datetime

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

bot = Bot(token = "5563579070:AAFVJB_pE2K2PklXU8n4yzW980WiOVOSWkg")
dp = Dispatcher(bot, storage=storage)

db = Database("database.db")


class Register (StatesGroup):  #создаю класс где буду хранить данные 
    messag = State()

ref = []

chas = datetime.datetime.now()

mainMenu = ReplyKeyboardMarkup(resize_keyboard= True)
brnProfile = KeyboardButton("/link")
mainMenu.add(brnProfile)

@dp.message_handler(commands=['start'])
async def starss(message: types.Message):
    if message.chat.type == "private":
        # if not db.user_exists(message.from_user.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        

        if str(referrer_id) != "":
            if str(referrer_id) != str(message.from_user.id):
                # db.add_user(message.from_user.id, referrer_id)
                try:
                    #await bot.send_message(referrer_id, "По вашій силці хтось зарегався")
                    await bot.send_message(message.from_user.id , "Можливо ви щось хочете написати йому, якщо так то введіть повідомлення")
                    
                    
                    
                    await Register.messag.set()
                    ref.insert(0, referrer_id)
                except:
                    pass
            else:
                await bot.send_message(message.from_user.id, "Не можна взаємодіяти з собою")
                    
            #else:
                # db.add_user(message.from_user.id)
        
        await bot.send_message(message.from_user.id, "Вітаю вас!" ,reply_markup=mainMenu)
        #await bot.send_message(message.from_user.id, f"Ку вот твоя ссилка \nhttps://t.me/Infoappbotebot?start={message.from_user.id}")
        
        
# @dp.message_handler()
# async def send(message: types.Message):
#     start_command = message.text
#     referrer_id = str(start_command[7:])
    
#     await bot.send_message(referrer_id, "Можливо ви щось хочете написати йому, якщо так то введіть повідомлення")
#     await Register.messag.set()
@dp.message_handler(commands=["link"])
async def links(message: types.Message):
    await message.answer(f"вот твоя ссилка \nhttps://t.me/Infoappbotebot?start={message.from_user.id}")
        
@dp.message_handler(state=Register.messag)
async def get_username(message: types.Message, state: FSMContext):
    await state.update_data(messaggge = message.text)
    
    data = await state.get_data()
    await bot.send_message( message.from_user.id, "Незабаром реферал отримає ваше звернення")
    await bot.send_message( message.from_user.id, "Щоб розпочати роботу заново введіть /start")
    await bot.send_message(ref[0], f"{data['messaggge']}")

    db.save_msg(ref[0], message.from_user.id, message.from_user.first_name, chas, data["messaggge"])
    
    
    # db.dell_user(message.from_user.id)
    # db.dell_user(ref[0])
    await state.finish()
    

    
    
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
    

#types.Message.from_user.id
