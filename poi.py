import time
import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = input("set password")

print("\naccessing database...........\n")

guess = " "

while guess != password:
    guess = ""
    for i in range(len(password)):
        guess += random.choice(chars)



print("\ntyping......!",guess)
time.sleep(0.1)

print("\nPASSWORD CRACKED:",password)