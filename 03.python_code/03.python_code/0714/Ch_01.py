#sepearator 옵션

print('P','Y', 'T', 'H','O','N', sep='  ')
print('010','7777','1234', sep='-')
print('pyton', 'gmail.com', sep='@')


# end 옵션 

print('Welcome to', end=' | ')
print('IT News', end=' | ')
print('Web Site')

#format  사용 (d: 3, s: 'python, f : 3.3133434)

print('%s, %s' %('one','two'))
print('{}{}'.format('one', 'two'))
print('{1}{0}'.format('one','two'))
print('%10s' % ('nice111'))
print('{:>10}'.format('nice111'))
print('{:@>10}'.format('nice111'))
print('{:10}'.format('nice111'))
print('{:<10}'.format('nice111'))
print('{:^10}'.format('nice111'))
print('%10.5s'.format('nice111'))
print('%.7s' % ('pythonstudy'))
print('{:10.7}'.format('pythonstudy'))


#%d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%d' %(42))
print('{:<4d}'.format(42))

#%f 
print('%f' % (3.143434343434))
print('{:f}'.format(3.144565656))
print('%1.10f' % (111113.14434343434))
print('%1.2f' % (11113.14144434343443))
print('%06.2f' % (3.1434343434))
print('{:06.2f}'.format(3.14143434343434))
      