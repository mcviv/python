# def main():
#     num = int(input("Enter a number: "))
#
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")
#
#
# if __name__ == "__main__":
#     main()

# 2nd
def main():
    age = int(input("Enter your age: "))
    if age < 0:
        print("Please enter a valid age (a positive number).")
    else:
        if age <= 13:
            print("You are a child.")
        elif age < 20:
            print("You are a teenager.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
if __name__ == "__main__":
    main()
