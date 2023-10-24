v = int(input('digite quanto voce ganha por hora: '))
h = int(input('digite o numero de horas trabalhadas no mes: '))
s = v * h
ir = (11/100.0 * s)
print ('imposto de renda: ',ir)
inss = (8/100.0 * s)
print ('INSS: ',inss)
si = (5/100.0 * s)
print ('Sindicato: ',si)
desc = ir + inss + si
sa = s - desc
print ('O desconto total do salario bruto(',s,'R$)',
       'foi',desc,'\nO salario liquido ficou,',sa)