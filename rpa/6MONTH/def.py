import random, os, time

alphabet = "abcdefghijklmnopqrstuvwxyz"
def random_choice():
    text = ""
    text += random.choice(alphabet)
    text += random.choice(alphabet)
    text += random.choice(alphabet)
    text += random.choice(alphabet)
    return text


print(random_choice())

first = "김이박최정"
middle = "용지성태은우"
last = "범정성양재성"
def random_name():
    result = ""
    result += random.choice(first)
    result += random.choice(middle)
    result += random.choice(last)
    return result

print(random_name())

print(random.randint(1, 7))

def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet)
    return result

print(random_string(10))
