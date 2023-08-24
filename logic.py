# import string

# def remove_punctuation(s):
#     return s.translate(str.maketrans('', '', string.punctuation))



import unicodedata
import re

def remove_punctuation(s):
    # Удаление пунктуации
    no_punctuation = ''.join([char for char in s if not unicodedata.category(char).startswith('P')])
    # Удаление двойных пробелов
    no_double_spaces = re.sub(r'\s+', ' ', no_punctuation)
    print(no_double_spaces.strip())
    return no_double_spaces.strip()  # Убираем лишние пробелы только по краям
# import redis
# import re

# def increase_counter(redis_host='localhost', redis_port=6379, redis_password=None, counter_key='counter', increment_by=1):
#     try:
#         redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
#         current_value = redis_client.get(counter_key)
#         if current_value is None:
#             current_value = 0
#         else:
#             current_value = int(current_value)
#         new_value = current_value + increment_by
#         redis_client.set(counter_key, new_value)
#         return new_value

#     except Exception as e:
#         print("Произошла ошибка:", e)
#         return None
    
# def is_valid_email(email):
    
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
#     if re.match(pattern, email):
#         return True
#     else:
#         return False