import random

def password():
k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rez = ''
for i in range(11):
rez += random.choice(k+a)
return rez

d = password()
print('Пароль:',d)
