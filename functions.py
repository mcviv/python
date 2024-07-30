def my_func():
    print("hello welcome to my funtion")
my_func()

def mfunc():
    print("are you sure you want to join")
    print("are you sure you want to join")
    print("are you sure you want to join")
mfunc()
mfunc()

def my_string():
    hello = "Good morning sir, welcome to my application"
    print(hello)
my_string()

def my_string1(name):
    print('hello,' + name + 'welcome to my application')
my_string1('john')
my_string1('esther')

def my_string2(name, age):
    print('hello,' + name + 'your age is ' + str(age) + 'years')
my_string2('paul', 21)
my_string2('njoki',34)
def person(firstname, lastname, age):
    print('hello,' + firstname + ' ' + lastname + 'your age is ' + str(age) + 'years')
person('john,' ' ', 'wathiongo', 45)
# ass
def perform_sum(num1, num2):
    """ Function to perform summation of two numbers and display the result """
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")

# Example usage:
perform_sum(5, 3)

def calc_multiple(x,y):
    return x*y
print(calc_multiple(10, 20))

def calc_age(a,b):
    c= a+b
    return c
print(calc_age(10, 27))

def add_five(age):
    next_five_years = age+5
    return next_five_years
specific_age = add_five(23)
print(specific_age)

def calc_your_age(name, age):
    if age >5:
        print('you can move to grade 1')
    elif age == 5:
        print('you can join kindergarten')
    elif age<=4 and age>0:
        print(f'{name} can stay at home')

    print(calc_your_age('judah', 8))