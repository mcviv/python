# while loop
i = 0
while i <= 5:
    print(i)
    i = i + 1

a = 0
while a <= 10:
    print('*' * a)
    # a = a + 1
    a+=1

# for loop
for item in 'python':
    print(item)

for b in [1,2,3,4,5]:
    print(b)

for z in range(5,15):
    print(z)

products= [200,300,400,234,45]
total = 0
for product in products:
    total += product
    print(total)