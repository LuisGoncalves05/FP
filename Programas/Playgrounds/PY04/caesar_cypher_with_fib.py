def fibonacci(n):
    return int(((1+5**0.5)**n - (1-5**0.5)**n)/((2**n)*(5**0.5)))

def caesar (message):
    new_message = ""
    index = -1
    for letter in message:
        index += 1
        old_order = ord(letter)
        if 65 <= old_order <= 90:
            new_order = int(old_order - (fibonacci(index) % 26))
            if new_order > 90:
                new_order = 65 + (new_order - 90 - 1)
            elif new_order < 65:
                new_order = 90 - (65 - new_order - 1) 
            new_message += chr(new_order)
        else:
            new_message += letter
    return(new_message)