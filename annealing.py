import random
import math

def score(a, b, c, d):
    total = 0
    if not a or d:
        total += 1
    if c or b:
        total += 1
    if not c or not d:
        total += 1
    if not d or not b:
        total += 1
    if not a or not d:
        total += 1
    return total

def annealing(init: list[int], temperature: int, dt: int):
    cutoffs = [0.655, 0.254, 0.432]
    
    for i in range(3):
        ind = random.randint(0, 3)
        temp = init.copy()

        temp[ind] = not temp[ind]
        if score(temp[0], temp[1], temp[2], temp[3]) > score(init[0], init[1], init[2], init[3]):
            print(f"Score changed from {score(init[0], init[1], init[2], init[3])} to {score(temp[0], temp[1], temp[2], temp[3])}")
            print(f"New state: {temp}")
            init = temp
        else:
            dE = score(temp[0], temp[1], temp[2], temp[3]) - score(init[0], init[1], init[2], init[3])
            p = 1 / (1 + math.e**(-dE/temperature))

            print(f"Bad move with probability {p}")
            if p >= 0.5:
                print(f"Score changed from {score(init[0], init[1], init[2], init[3])} to {score(temp[0], temp[1], temp[2], temp[3])}")
                print(f"New state: {temp}")
                init = temp

        temperature -= dt
        print(" ")
    return init

if __name__ == "__main__":
    print(annealing([True, True, True, True], 500, 50))