from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    entering_name = State()
    confirmation_name = State()
    menu = State()
    start_confirmation = State()
    task_1 = State()
    task_1_exit = State()
    task_2 = State()
    task_2_exit = State()
