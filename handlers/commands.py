from loader import dp, CODES
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if len(message.text.split()) == 2:
        code = message.text.split()[1]
        if code in CODES:
            await message.answer(texts.welcome)
            await message.answer(texts.enter_team_name)
            await State.entering_name.set()
            print(CODES)
            print(CODES.index(code))
            await state.update_data(team_number=CODES.index(code) + 1)
        else:
            print('wrong code')
    else:
        await message.answer(texts.no_code_enter)

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
