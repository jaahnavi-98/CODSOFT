import random
import string

def generate_password(length):
    char = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    pas = ''.join(random.choice(char) for _ in range(length))
    return pas

pass_len = int(input("Enter the length of the password: "))
print(generate_password(pass_len))