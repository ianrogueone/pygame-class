print("hello")
a = 10
print (a)
a = 10.2
print (a)
name = 'Peter'
print (name)
a = 20
b = 5
c = a + b
print (c)
x = 3
y =(x * 2) + 1
print (y)
name = 'Peter'
greeting = 'hello'
phrase = greeting + name + '!!'
print (phrase)
for i in range(0, 5):
   print(i)
for i in range(0, 5):
       print('*')
for i in range(0, 5):
    stars = ''
    for j in range(0, i):
        stars = stars + '*'
    print(stars)
for i in range(0, 5):
    spaces = ''
    for j in range(0, 5 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 1):
        stars = stars + '*'
    print(spaces + stars)
for i in range(0, 5):
    spaces = ''
    for j in range(0, 5 - i - 1):
        spaces = spaces + ' '
    stars = ''
    for j in range(0, i + 1):
        stars = stars + '*'
    print(spaces + stars)