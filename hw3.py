def get_fixed_price(rate, price):
    return int(price / (1 - rate / 100))

discount = int(input("할인율은? "))
a_sale = int(input("A 상품의 할인된 가격은? "))
b_sale = int(input("B 상품의 할인된 가격은? "))

a_price = get_fixed_price(discount, a_sale)
b_price = get_fixed_price(discount, b_sale)

print("A 상품의 정가는", a_price, "원")
print("B 상품의 정가는", b_price, "원")
