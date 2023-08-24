from loader import dp, CODES
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.start_confirmation)
async def get_to_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if len(data.get('completed_tasks')) == 7:
        await message.answer(texts.congrats)
        await State.finished.set()
        return
    with open('images/map.jpg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.map_instruction)
    await message.answer(texts.route_instruction)
    print(data.get('score'))
    team_number = data.get('team_number')
    await message.answer(texts.route_header, reply_markup=kb.generate_locations_kb(team_number))
    await State.menu.set()

@dp.message_handler(state=State.finished)
async def get_to_menu(message: types.Message, state: FSMContext):
    await message.answer(texts.quest_finished)

