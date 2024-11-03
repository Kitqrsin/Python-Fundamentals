def factorial(number, times_to_repeat):
    result = 1
    for current_number in range(times_to_repeat):
        result = result * (number - current_number)
    return int(result)


number_of_tests = int(input())

for current_test in range(number_of_tests):
    # P, B, X, Y
    number_purchases, number_gift_papers, type_of_purchases, type_of_gift_papers = input().split()
    number_purchases = int(number_purchases)
    number_gift_papers = int(number_gift_papers)
    type_of_purchases = int(type_of_purchases)
    type_of_gift_papers = int(type_of_gift_papers)
    every_possible_outcome = factorial(type_of_purchases, number_purchases)
    outcomes = factorial(type_of_gift_papers, number_gift_papers)
    first_divider = factorial(number_purchases, number_purchases)
    second_divider = factorial(number_gift_papers, number_gift_papers)
    divider = first_divider * second_divider
    result = (every_possible_outcome * outcomes) // divider
    print(result)
