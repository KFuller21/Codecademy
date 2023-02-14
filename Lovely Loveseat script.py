 lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend
on wood. 32 incudes high x 40 inches wide
x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch.
29.50 inches high x 54.75 inches wide
x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36
inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = """
Lovely Loveseat. Tufted polyester blend
on wood. 32 incudes high x 40 inches wide
x 30 inches deep. Red or white.
Luxurious Lamp. Glass and iron. 36
inches tall. Brown with cream shade.
"""

customer_one_total += luxurious_lamp_price + lovely_loveseat_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

itemization_heading = "Customer One Items:"
print(itemization_heading)
print(customer_one_itemization)

total_cost_heading = "Customer One Total:"
print(total_cost_heading)
print(customer_one_total)
