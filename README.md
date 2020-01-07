# encrypt your string!
this lib is for encrypt
for example:
```
import encrypt
import time
enc = lambda x:encrypt.encrypt(x).__str__()
string = input('string here!')
print('-' * 100)
V = enc(string)
print('94chars encrypt')
print('-' * 100)
print('encrypted string:%s'%V)
print('-' * 100)
print('done.')
print('-' * 100)
```
