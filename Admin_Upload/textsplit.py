email = 'admin.test@domain.com'

str = email.split('.')

print str

first = str[0]
last = str[1]

lastname = last.split('@')

print lastname 

print first
print lastname[0]

name = 'balaji'

L = name.split()

print L