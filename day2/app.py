# import converters
from converters import kg_to_lbs, constant

print(kg_to_lbs(43))
print(constant)



# import ecommerce.shipping
from ecommerce.shipping import calculate_shipping


# ecommerce.shipping.calculate_shipping()
calculate_shipping()


import random

print(random.random())
print(random.randint(20,30))

team = ['a', "b", "c", "d"]

rand = random.choice(team)
print(rand)