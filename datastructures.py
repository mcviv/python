# # lists
# names = ['john', 'smith', 'andrew']
# # tuples
# names = ('john', 'smith', 'andrew')
# # sets
# names = ('john', 'smith', 'andrew')
# # dictionary
# students = {'john':100, 'smith':300, 'andrew':200}

# lists

employees = ['peter', 'john', 'smith', 'ruth', 'ester', 'annastacia']
print(employees)
print(employees[2])
print(employees[0])
print(employees[4])
print(employees[5])
print(employees[1:5])
print(employees[4:5])
employees[1] = 'alex'
print(employees)
employees[2] = 'moses'
print(employees)
employees.append('zack')
print(employees)
employees.append('pauline')
print(employees)
employees.insert(0,'jack')
print(employees)
employees.insert(3,'william')
print(employees)
employees.extend(['kamau', 'wafula', 'wafula'])
print(employees)
marks = [200, 321, 324, 455]
print(max(marks))
print(min(marks))
print(sum(marks))

# tuple
languages = ('python', 'java', 'php', 'kotlin')
print(languages)
print(languages[1])
print(languages[1:4])
numtuple  = (1,2,3,4,5,6,7,8,9,10)
print(max(numtuple))
print(min(numtuple))
print(sum(numtuple))

# set
mysets = {1,2,3,4,5,6,7,8,9,10}
print(mysets)
number = 2
if number in mysets:
    output = number
    print(output)
majina = {'john', 'smith', 'ruth', 'esther'}
name = 'esther'
if name in majina:
    jina = name
    print(jina)
name = 'smith'
if name in majina:
    jina = name
    print(jina)
majina.add('charles')
print(majina)
majina.update(['njoroge', 'collins', 'musa'])
print(majina)

# dictionary
books = {
    'title': 'the code',
    'Author': 'john doe',
    'year published': 2000
}
print(books['year published'])
books['year published'] = 2003
print(books)
books['version'] = 'version one'
print(books)
if 'title' in books:
    print('yes it is in the dictionary')
else:
    print('no it is not in the dictionary')
# ass
# Create an empty dictionary for students
students = {}

# Add student details (for example)
students['John'] = {'age': 20, 'major': 'Computer Science'}
students['Alice'] = {'age': 21, 'major': 'Mathematics'}
students['Bob'] = {'age': 19, 'major': 'Engineering'}

# Display the current dictionary
print("Current students dictionary:")
print(students)

# Check if a student exists and add a new key-value pair
name = 'Alice'
if name in students:
    students[name]['gpa'] = 3.8  # Adding GPA as an example
    print(f"Added GPA for {name}")

# Display the updated dictionary
print("\nUpdated students dictionary:")
print(students)


