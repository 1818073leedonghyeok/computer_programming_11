class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

user_choice = input("주문할 음료를 선택하세요 (커피, 녹차, 아이스티): ")

if user_choice not in ["커피", "녹차", "아이스티"]:
    print("잘못된 입력입니다.")
else:
    if user_choice == "커피":
        selected_beverage = Coffee
    elif user_choice == "녹차":
        selected_beverage = GreenTea
    else:
        selected_beverage = IceTea

    quantity = int(input("수량을 입력하세요: "))

    total_price = selected_beverage.calculate(quantity)
    print(f"{user_choice} {quantity}잔 주문이 완료되었습니다.")
    print(f"총 가격: {total_price}원")
