from modules.get_menu import *

day_input = input("급식정보 크롤링\n원하는 요일을 입력하세요 (예: 월): ").strip()
result = get_menu(day_input)
print(result)

