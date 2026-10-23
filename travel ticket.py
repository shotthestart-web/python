
destination = "Paris"          
ticket_count = 2                               
base_price = 250.50                           
is_premium_member = True       

print("--- Step 1: Data Types ---")
print("Destination Type:", type(destination))
print("Ticket Count Type:", type(ticket_count))
print("Base Price Type:", type(base_price))
print("Premium Member Type:", type(is_premium_member))
print()



subtotal = base_price * ticket_count
discount_rate = 0.10             
discount_amount = subtotal * discount_rate
final_price = subtotal - discount_amount

print("--- Step 2: Arithmetic Calculations ---")
print(f"Subtotal: {base_price} * {ticket_count} = ${subtotal}")
print(f"Discount: ${discount_amount}")
print(f"Final Price: ${final_price}")
print()

is_expensive = final_price > 400
is_paris = destination == "Paris"
has_discount = discount_amount >= 10.0

print("--- Step 3: Comparison Results ---")
print("Is final price greater than $400?:", is_expensive)
print("Is the destination Paris?:", is_paris)
print("Did customer save $10 or more?:", has_discount)
print()

first_name = "John"
last_name = "Doe"


full_name = first_name + " " + last_name  

upper_name = full_name.upper()
lower_destination = destination.lower()
destination_initial = destination[0]
name_length = len(full_name)

print("--- Step 4: String Operations ---")
print("Full Name:", full_name)
print("Uppercase Name:", upper_name)
print("Lowercase Destination:", lower_destination)
print("First Letter of Destination:", destination_initial)
print("Length of Full Name:", name_length)
print()

departure_airport = "LAX"
arrival_airport = "CDG"

print("--- Step 5: Variable Swapping ---")
print(f"Before Swap -> Departure: {departure_airport}, Arrival: {arrival_airport}")

departure_airport, arrival_airport = arrival_airport, departure_airport

print(f"After Swap  -> Departure: {departure_airport}, Arrival: {arrival_airport}")
print()


print("========================================")
print("         BOARDING PASS SUMMARY          ")
print("========================================")
print(f"Passenger Name : {upper_name}")
print(f"Route          : {departure_airport} -> {arrival_airport} ({destination})")
print(f"Tickets Booked : {ticket_count}")
print(f"Base Ticket Fare: ${base_price:.2f}")
print(f"Total Discount : -${discount_amount:.2f}")
print(f"----------------------------------------")
print(f"FINAL AMOUNT   : ${final_price:.2f}")
print(f"Premium Status : {'ACTIVE' if is_premium_member else 'INACTIVE'}")
print("========================================")
print("       Thank you for flying with us!    ")
print("========================================")