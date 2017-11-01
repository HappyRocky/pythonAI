import math
print("solving ax^2 + bx + c = 0")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
try:
    d = math.sqrt(b * b - 4 * a * c)
    fenmu = 2 * a
    answer1 = (-b + d) / fenmu
    answer2 = (-b - d) / fenmu
    print("Two answers:{} {}".format(answer1, answer2))
except ZeroDivisionError:
    print("a should not be 0")
except:
    print("Answers are imaginary")
finally:
    print("Over")