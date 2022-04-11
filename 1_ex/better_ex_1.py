def sum_divisible_by(n, target):
    p = target//n 
    return n*p*(p+1)//2

def main():

    target = int(input("Límite superior: "))-1
    
    if type(target) is int:
        total_sum = sum_divisible_by(3, target) + sum_divisible_by(5, target) - sum_divisible_by(15, target)
        print(total_sum)
    else:
        print("No ingresó un entero.")

if __name__ == "__main__":
    main()