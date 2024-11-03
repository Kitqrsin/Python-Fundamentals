import re

amount_of_barcodes = int(input())
pattern = r'(@+#{1,})[A-Z]+[a-zA-Z0-9]*[A-Z]+(@+#{1,})'
for _ in range(amount_of_barcodes):
    current_barcode = input()
    result = re.fullmatch(pattern, current_barcode)
    if result is None:
        print('Invalid barcode')
    else:
        final_result = re.split('@+#{1,}', result.group())[1]
        product_group = '00'
        times_a_digit_is_found = 0
        for current_letter in final_result:
            if times_a_digit_is_found == 0 and current_letter.isdigit():
                times_a_digit_is_found += 1
                if current_letter == 0:
                    product_group = '0'
                    break
                else:
                    product_group = f'{current_letter}'
            elif times_a_digit_is_found >= 1 and current_letter.isdigit():
                product_group += f'{current_letter}'

        print(f'Product group: {product_group}')
