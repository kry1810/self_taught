
x = 0
for i in range(100):
    x += 1
    if x % (3 * 5) == 0:
        print("FizzBuzz")
        continue
    if x % 3 == 0:
        print("Fizz")
        continue
    if x % 5 == 0:
        print("Buzz")
        continue
    print(x)

