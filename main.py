import random
from time import sleep


# Written by Jonathan Latkowcer
# latk0004

# Github : https://github.com/JLatkowcer/NET2008_Assignment04
# DockerHub : https://hub.docker.com/repository/docker/latk0004/latk0004-net2008-a04


def random_num():
    random_number = random.randrange(0, 99, 1)
    return random_number


# Use a breakpoint in the code line below to debug your script.

random.seed()

print("Welcome to the math problem generator!\n\n")
print("Type Q to quit any time.")

while True:
    num1 = random_num()
    num2 = random_num()

    sum_guess = input(f"What is the sum of {num1} plus {num2}? >>> ")

    if sum_guess == "q" or sum_guess == "Q":
        print("\n\n\nThanks for using the math problem generator. Quitting...\n\n\n")
        sleep(2)
        break

    try:
        sum_guess = int(sum_guess)
    except:
        sum_guess = -1

    if sum_guess == (num1 + num2):
        print("\nWell done!\n\n")
    else:
        print("\nHmm, I don't think that was correct...\n\n")
