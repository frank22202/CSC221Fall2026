# Raw, messy user input
raw_input = '   !!!  JoHn_DoE@GM aIl.COM   !!!   '

# Method Chaining
clean_email = (
    raw_input
    .strip('   !')
    .lower()
    .replace(' ', '')
    .replace('_', '.')
)

# Output
print(clean_email)