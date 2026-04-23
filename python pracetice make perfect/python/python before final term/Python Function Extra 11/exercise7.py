import random

def flip_coin():
    result = random.choice(["Head","Tail"])
    return result
print(f"Random : {flip_coin()}")