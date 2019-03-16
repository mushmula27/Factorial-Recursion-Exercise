def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)


def main():
    print("Welcome to your factorial calculator!")

    while True:
        try:
            num = int(input("Enter a positive number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if num < 0:
            print("Factorial does not exist for negative numbers, try again.")
            continue
        else:
            ans = factorial(num)
            print(str(num) + "! = " + str(ans))
            again = input("Go again? (y/n) ")
            if again.lower() in ["y", "yes", "ye"]:
                continue
            else:
                break


main()
