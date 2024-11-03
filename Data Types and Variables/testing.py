user_input = input()
discount = 1
taxes_sum = 0
total_price_no_tax = 0
while user_input != 'special' and user_input != 'regular':
    user_input = eval(user_input)
    if user_input < 0:
        print('Invalid price!')
        user_input = input()
        continue
    total_price_no_tax += user_input
    taxes_sum += user_input * 0.2
    user_input = input()

if user_input == 'special':
    discount = 0.90


total_price = (total_price_no_tax + taxes_sum) * discount

if total_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price_no_tax:.2f}$\n"
          f"Taxes: {taxes_sum:.2f}$\n"
          f"-----------\n"
          f"Total price: {total_price:.2f}$\n")