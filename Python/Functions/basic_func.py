def sum_num(a, b):
     return a + b
# results = sum_num(3, 5)
# results2 = sum_num(17,12)
# print(results)
# print(results2)
# results = sum_num(2)
# print(results)
# results = sum_num(2,4,2)
# print(results)

# price of an item
# def calculate_price(quantity, price, tax_rate):
#     total_price = quantity * price
#     tax = total_price * (tax_rate / 100)
#     final_price = total_price + tax
#     return final_price
# results = calculate_price(2, 10, 5)
# print(results)

# def cart(qty,item, price):
#      print(f"{qty} {item} cost: Kshs.{price:.2f}")

# cart(2, "Mangoes", 100)
#will throw an error because 3rd argument is float

#*****************************KEYWORD ARGUMENT******************************************
# cart(4, item = "Bread", price = 200)

def cost(qty, price, cost, item):
    # print(f"{qty} {item} cost: Kshs.{price} and total cost is Kshs.{qty*price}")
    return cost

# results = cost(6, 100, 200, "Mangoes")