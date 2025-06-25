from modules.get_menu import *


if __name__ == "__main__":
    day_input = input("급식정보 크롤링\n원하는 요일을 입력하세요 (예: 월): ").strip()
    result = get_menu(day_input)
    
    print(f"\n📅 {result['day']}요일 ({result['date']}) 중식 메뉴")
    print("=" * 40)
    
    if result['menu']:
        print("🍽️ 메뉴:")
        for i, menu in enumerate(result['menu']):
            print(f"  {i+1}. {menu}")
        
        print(f"\n⚠️ 알러지 정보:")
        if result['allergy_names']:
            print(f"  포함 알러지: {', '.join(result['allergy_names'])}")
            print(f"  알러지 번호: {', '.join(result['allergy'])}")
        else:
            print("  알러지 정보 없음")
    else:
        print("급식 정보가 없습니다.")
    
    print(f"\n📊 전체 결과: {result}")
