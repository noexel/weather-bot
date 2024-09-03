import logging, random, time
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.markdown import hlink

logging.basicConfig(level=logging.INFO)
bot = Bot(token='7509353699:AAFs3ZJ2QZhQYXLT6DrIx1NUpUnu3I8a1Fk')
dp = Dispatcher(bot)

gift = InlineKeyboardMarkup()
gift.add(types.InlineKeyboardButton(text="Участвовать", callback_data="gift"))

crypto_notes = hlink('Crypto Notes', 'https://t.me/+YdWFDkUtIv03Y2Iy')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    error_photo = open('error_photo.png', 'rb')
    print(message)
    await bot.send_photo(chat_id=message.from_user.id, photo=error_photo, caption=f'<b>Такой команды не существует!</b>\n\nВозможно вы имели ввиду /gift', parse_mode='HTML')


@dp.message_handler(commands=['gift'])
async def send_welcome(message: types.Message):

    gift_photo = open('gift-50-usdt-test.png', 'rb')
    done_photo = open('done_photo.png', 'rb')

    if message.from_user.id == 1226892780:
        await bot.send_photo(chat_id=message.from_user.id, photo=done_photo, caption=f'<b>Розыгрыш выставлен в канале {crypto_notes}</b>', parse_mode='HTML')
        await bot.send_photo(chat_id='-1002189817195', photo=gift_photo, caption=f"<b>Розыгрыш 50 $USDT</b>\n\n1. Будь подписан на канал {crypto_notes}\n2. Нажми кнопку участовать\n\n<b>Итоги розыгрыша: 08.09.24 в 20:00</b>", reply_markup=gift, parse_mode='HTML')
    else:
        await bot.send_message(chat_id=message.from_user.id, text="You are not admin.") 


@dp.message_handler(commands=['preview'])
async def send_welcome(message: types.Message):

    gift_photo = open('gift-50-usdt-test.png', 'rb')

    if message.from_user.id == 1226892780:
        await bot.send_photo(chat_id=message.from_user.id, photo=gift_photo, caption=f"<b>Розыгрыш 50 $USDT</b>\n\n1. Будь подписан на канал {crypto_notes}\n2. Нажми кнопку участовать\n\n<b>Итоги розыгрыша: 08.09.24 в 20:00</b>", reply_markup=gift, parse_mode='HTML')
    else:
        await bot.send_message(chat_id=message.from_user.id, text="You are not admin.") 


@dp.callback_query_handler(text='gift')
async def first(callback_query: types.CallbackQuery):

    user_channel_status = await bot.get_chat_member(chat_id='-1002189817195', user_id=callback_query.from_user.id)

    if user_channel_status.status != 'left':
        time.sleep(.5)
        await callback_query.answer("Вы участвуете в розыгрыше!", show_alert=True)
    else:
        await callback_query.answer("Вы не подписались на канал!", show_alert=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)