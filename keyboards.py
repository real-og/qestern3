from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts


def generate_locations_kb(team_number):
    team_number = str(team_number)
    if team_number == '1':
        places_order = [1, 2, 3, 4, 5, 6, 7]
    elif team_number == '2':
        places_order = [2, 3, 4, 5, 6, 7, 1]
    elif team_number == '3':
        places_order = [3, 4, 5, 6, 7, 1, 2]
    elif team_number == '4':
        places_order = [4, 5, 6, 7, 1, 2, 3]
    elif team_number == '5':
        places_order = [5, 6, 7, 1, 2, 3, 4]
    elif team_number == '6':
        places_order = [6, 7, 1, 2, 3, 4, 5]
    elif team_number == '7':
        places_order = [7, 1, 2, 3, 4, 5, 6]
    places_names = [texts.places_btns[index - 1] for index in places_order]
    kb = InlineKeyboardMarkup(row_width=1)
    for place_name in places_names:
        kb.add(InlineKeyboardButton(text=place_name, callback_data=place_name))
    return kb
        

begin_quest_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

yes_no_kb = ReplyKeyboardMarkup([[texts.yes_btn, texts.no_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

finish_task_kb = ReplyKeyboardMarkup([[texts.finish_task_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)



# hint_kb = ReplyKeyboardMarkup([[texts.get_hint]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)

# hint_double_kb = ReplyKeyboardMarkup([[texts.get_more_hint]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)



# continue_kb = ReplyKeyboardMarkup([[texts.continue_quest]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)


# hint_extended_kb = ReplyKeyboardMarkup([[texts.get_hint], [texts.hint_find_code_btn]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)

# hint_location_kb = ReplyKeyboardMarkup([[texts.hint_find_code_btn]],
#                                      resize_keyboard=True,
#                                      one_time_keyboard=True)
