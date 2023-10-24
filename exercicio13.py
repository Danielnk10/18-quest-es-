s= int(input('escolha: 1 masculino / 2 feminino'))
h= float(input('digite sua altura'))
p= float(input('digite seu peso'))
p1= (72.7*h)-58 if s==1 else (62.1*h) - 44.7 
if p < p1:
    print('seu peso esta abaixo do ideal')
elif p == p1:
    print('seu peso esta ideal')
else:
    print('seu peso esta acima do ideal')
    print('peso: %.2f / peso ideal: %.2f' %(p,p1))
    if s ==1:
        p1 = (72.7*h) - 58
    else:
        p1 = (62.1*h) - 44.7
