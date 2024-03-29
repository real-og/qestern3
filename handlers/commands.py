from loader import dp, CODES
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if len(message.text.split()) == 2:
        code = message.text.split()[1]
        if code in CODES:
            await message.answer(texts.welcome)
            await message.answer(texts.enter_team_name)
            await State.entering_name.set()
            await state.update_data(team_number=CODES.index(code) + 1)
            if data.get('score') is None:
                await state.update_data(score=0)
                await state.update_data(team_name='_')
                await state.update_data(completed_tasks=[])
 
            await aiotable.append_user(message.from_user.id, message.from_user.username, code)
            
        else:
            await message.answer(texts.wrong_code)
    else:
        await message.answer(texts.no_code_enter)

@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
