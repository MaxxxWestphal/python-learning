message = "Hello, Python!"
print(message)
Hello, Python!
print(type(message))
<class 'str'>
number = 42
print(type(number))
<class 'int'>




first_name = "Taylor"
user_age = 21
course_name = "Computer Science"  # 'class' is a keyword
my_score = 100

print(first_name, user_age, course_name, my_score)





a = 256
b = 256
print("a =", a, "id(a) =", id(a))
a = 256 id(a) = 140710890411096
print("b =", b, "id(b) =", id(b))
b = 256 id(b) = 140710890411096
print("Same object?", id(a) == id(b))
Same object? True
print()

c = 257
d = 257
print("c = {c}, id(c) = {id(c)}")
c ={c}, id(c) = {id(c)}
print("d = {d}, id(d) = {id(d)}")
d = {d}, id(d) = {id(d)}
print("Same object? {id(c) == id(d)}")
Same object? {id(c) == id(d)}




x="johnsmith@email.com"
Y=2026-2004
z=Y>=18
a="Welcome" if z else "Sorry, too young"
print(a)



user_email = "johnsmith@email.com"
user_age = 2026 - 2004
is_adult = user_age >= 18
welcome_message = "Welcome" if is_adult else "Sorry, too young"
print(welcome_message)

