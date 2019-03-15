def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)

def main():
    print("Welcome to your factorial calculator!")

    while True:

        num = int(input("Enter a positive number: "))

        if num < 0:
            print("Factorial does not exist for negative numbers, try again.")
            main()
        else:
            ans = factorial(num)
            print(str(num) + "! = " + str(ans))
            again = input("Go again? (y/n) ")
            if again == "y":
                True
            else:
                break

main()