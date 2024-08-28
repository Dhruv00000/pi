from decimal import Decimal
from time import perf_counter

def double_factorial(n: int):
    return double_factorial(n - 2) * n if n not in [0, 1] else 1
def factorial(n: int):
    return factorial(n - 1) * n if n != 0 else 1

pi: Decimal = Decimal(3.141592653589793238462643383279502884197169399375) # math.pi has less decimal places, and this is the highest number of decimal places I could get python to print.

k: int = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0

while True:

    iterationStartTime: float = perf_counter()
    approximation += 2 * Decimal(factorial(k) / double_factorial(2*k + 1))
    # approximation += Decimal(pow(2, k + 1) * pow(factorial(k), 2) / factorial(2*k + 1))
    # This is another form of the algorithm, but it is slower and does not yeild any better approximations.
    iterationEndTime: float = perf_counter()

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        if char != str(approximation)[i]:
            if i < 2: print("No accurate decimal places")
            else:
                print(f"{i - 2} correct decimal place(s)")
                finalAccuracy = i - 2
            break

    print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
    totalComputationTime += iterationEndTime - iterationStartTime

    deviation: Decimal = approximation - previous
    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k + 1} iterations.\n")