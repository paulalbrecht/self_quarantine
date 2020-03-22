import string


dec_number = 0
hex_number = input("Enter a hex number to convert: ")

for power, digit in enumerate(reversed(hex_number)):
    dec_number += int(digit, 16) * (16 ** power)

print(dec_number)


dec_number = 0
hex_number = input("Enter a hex number to convert: ")

for power, digit in enumerate(reversed(hex_number)):
    dec_number += int(digit, 16) * (16 ** power)

print(dec_number)

