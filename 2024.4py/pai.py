
import math

def calculate_pi(iterations):
    pi = 0
    for k in range(iterations):
        pi += ((-1)**k * math.factorial(6*k)) / ((545140134*k + 13591409) * math.factorial(3*k) * math.factorial(k)**3)
    pi = pi * (12 / (640320**1.5))
    pi = 1 / pi
    return pi

# 调用函数进行计算
calculated_pi = calculate_pi(10000)
print("Calculated value of pi:", calculated_pi)
