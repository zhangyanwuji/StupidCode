
# name = ["alvin", "zhang"]
# for index in name:
# print(index, len(index))

# x = int(input("Please input a integer:"))
# if x < 0:
# print("This is a negtive number")
# elif x > 0:
# print("This is a positive number")
# else:
# print("You inputted zero")

def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
        return result


def fib2(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


if __name__ == "__main__":
    import sys
    fib2(int(sys.argv[1]))
