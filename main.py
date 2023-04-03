import random

def password():
k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rez = ''
for i in range(11):
rez += random.choice(k)
return rez

d = password()
print('Пароль:',d)
