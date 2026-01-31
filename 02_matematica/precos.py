item_prices = {  
    'apple': 0.5,  
    'banana': 0.75,  
    'orange': 0.6  
}  

def calculate_total_price(item, quantity):  
    price = item_prices.get(item, 0)  
    return quantity * price