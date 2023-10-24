n1=float(input('digite o preso dos peixes'))
e= 0
m= 0
if n1 <=50:
    print('excesso: %.2f' %e)
    print('multa: %.2f' %m)
else:
    e = n1 - 50
    m = e * 4
    print('escesso: %.2f' %e)
    print('multa: %.2f' %m)