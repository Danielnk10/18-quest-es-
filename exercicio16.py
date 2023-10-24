m=float(input('digite o tamnho em metros da area a ser pintada'))
l = m/3
la= int(l/18)
if l% 18 != 0:
    la+= 1
    print('tera que compra', la, 'latas de tinta')
    print('o valor total é ', la+80)