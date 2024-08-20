from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords
    # Calculate distance using the spread operator
    distance = get_distance(*from_coords, *to_coords)
    # Retrieve the shipping rate for the given shipping_type
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)

# test_function(calculate_shipping_cost)  # Uncomment to test

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = distance / driver.speed
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver <= cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver

# test_function(calculate_driver_cost)  # Uncomment to test

# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0
    for trip_id, trip in trips.items():
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue
    return total_money_made

# Test the function by calling 
test_function(calculate_money_made)
