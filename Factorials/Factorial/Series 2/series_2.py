from decimal import Decimal
from time import perf_counter

k: int = 0
approximationInverted: float = 0
approximation: Decimal = 0
previous: Decimal = 0
finalAccuracy: int = 0
totalComputationTime: float = 0
iterationStartTime: float = 0
iterationEndTime: float = 0

def factorial(n: int) -> int:
    return factorial(n - 1) * n if n != 0 else 1

while True:

    iterationStartTime = perf_counter()
    approximationInverted += Decimal((pow(factorial(2*k), 3) * (42*k + 5)) / (pow(factorial(k), 6) * pow(16, 3*k + 1)))
    approximation = 1 / approximationInverted
    iterationEndTime = perf_counter()

    print(f"\nIteration {k + 1}")
    print(f"Approximation = {approximation}")

    for i, char in enumerate("3.141592653589793238462643383279502884197169399375"): # using str(pi) instead of writing the whole string like I have done here somehow displays a different number??? idk
        try:
            if char != str(approximation)[i]:
                if i < 2: print("No accurate decimal places")
                else:
                    print(f"{i - 2} correct decimal place(s)")
                    finalAccuracy = i - 2
                break
        except IndexError: print("No incorrect decimal places.")

    print(f"Iteration duration: {iterationEndTime - iterationStartTime}  seconds")
    totalComputationTime += iterationEndTime - iterationStartTime

    deviation: Decimal = Decimal(approximation - previous)
    if deviation == 0: 
        print("Negligible deviation (terminating the program)\n")
        break
    elif deviation != approximation: print(f"Deviation from previous iteration: {deviation}") # this if-statement prevents a deviation from being shown during the first iteration.

    previous = approximation
    k += 1

print(f"\n\nComputed {finalAccuracy} correct decimal places in {totalComputationTime} seconds and {k + 1} iterations.\n")