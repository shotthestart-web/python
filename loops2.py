def is_armstrong_number(number):
    num_str = str(number)
    n = len(num_str)

    total_sum = sum(int(digit) ** n for digit in num_str)
    return total_sum == number

try:
    user_num = int(input("Enter a positive integer: "))
    
    if user_num < 0:
        print("Please enter a positive integer.")
    elif is_armstrong_number(user_num):
        print(f"{user_num} is an Armstrong number.")
    else:
        print(f"{user_num} is NOT an Armstrong number.")
        
except ValueError:
    print("Invalid input! Please enter a valid integer.")