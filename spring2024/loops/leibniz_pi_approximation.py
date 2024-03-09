"""
    Write a loop to compute the Leibniz approximation for pi/4,
    which is 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11
"""


terms: int = 0
approximation: float = 0.0
i: int = 1
accumulate: float = 0.0
denom: int = 0
sign: int = 1

terms = int(input("How many terms do you want in your approximation series for pi/4? "))
for i in range(terms):
    approximation = sign * (1/(1 + 2*i))
    accumulate += approximation
    sign *= -1 

print("Your approximate value of pi with {:d} terms is {:.5f}"
      .format(terms,accumulate))
