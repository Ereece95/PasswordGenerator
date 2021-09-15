# Eric Reece - 9/15/2021
# This is a simple program used to generate a random password for a user.
# To accomplish this, we must use the random library to select upper case and lower case numbers
# as well as some digits and punctuation signs, using the ASCII chart to determine value locations.


import random


# Function to shuffle string values
def shuffle(string):
    temp_pass = list(string)
    random.shuffle(temp_pass)
    return ''.join(temp_pass)


# Function to generate random values for string
def values():
    uppercase_letter1 = chr(random.randint(65, 90))
    uppercase_letter2 = chr(random.randint(65, 90))

    lowercase_letter1 = chr(random.randint(97, 122))
    lowercase_letter2 = chr(random.randint(97, 122))

    random_digit1 = chr(random.randint(48, 57))
    random_digit2 = chr(random.randint(48, 57))

    random_punc1 = chr(random.randint(33, 152))
    random_punc2 = chr(random.randint(33, 162))

    random_password = uppercase_letter1 + uppercase_letter2 + lowercase_letter1 + lowercase_letter2 \
                     + random_digit1 + random_digit2 + random_punc1 + random_punc2

    return random_password


# ====== Main ======= #
randPass = values()
finalPass = shuffle(randPass)

print("Random password generated: " + finalPass)
