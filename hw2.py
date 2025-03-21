def get_integer():
    return int(input("금액 입력: "))

def exchange(amount):
    for coin in [500, 100, 50, 10]:
        print(f"{coin}원: {amount // coin}개")
        amount %= coin

amount = get_integer()
exchange(amount)
