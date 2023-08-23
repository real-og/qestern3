from loader import dp, CODES
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.start_confirmation)
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/map.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.map_instruction)
    await message.answer(texts.route_instruction)
    data = await state.get_data()
    team_number = data.get('team_number')
    await message.answer(texts.route_header, reply_markup=kb.generate_locations_kb(team_number))
    await State.menu.set()


