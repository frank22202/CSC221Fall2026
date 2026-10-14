number = int(input('Enter a number: '))
print(bin(number))
print(f'{number:b}')

dec_num = ""
while number > 0:
    dec_num += str(number % 2)
    number //= 2

print(dec_num[::-1])