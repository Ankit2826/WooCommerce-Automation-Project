import random
import string


def email_id(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'example.com', 'supersqa.com']
    random_email = rand_string + '@' + random.choice(domains)
    return random_email  # Return the generated email


def rand_password(length):
    # Generate Random Strong Password (Generate a strong password with upper and lower case letters, numbers,
    # and symbols.)
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    lower_letters = ''.join(random.choice(lower) for j in range(length))
    symbols = '@!\"?$%^&*()'
    digits = string.digits  # '0123456789'
    random_password = (
            random.choice(upper) +
            lower_letters +
            random.choice(symbols) +
            random.choice(digits)
    )

    # Shuffle the result to make the password random
    random_password = ''.join(random.sample(random_password, len(random_password)))
    return random_password


# print(f'Email:- {email_id(10)}')
# print(f'Password:-{password(13)}')
