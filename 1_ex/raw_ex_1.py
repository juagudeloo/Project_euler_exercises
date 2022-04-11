from operator import truediv


def multiple_3_5(n: int):
    if n%3 == 0 or n%5 == 0:
        return True
    else:
        return False


def main():
    MAX = int(input("Límite: "))
    sum = 0
    for i in range(MAX):
        if multiple_3_5(i):
            sum += i

    print(sum)



if __name__ == "__main__":
    main()