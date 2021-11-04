#chalE.py

from Crypto.Util.number import *
f = open("m_list.txt")
a = f.readlines()
m_list = eval(a[0])
tmp = []
n_list = []
for m in m_list:
	if m in tmp: continue
	tmp.append(m)
	p = getPrime(256)
	q = getPrime(256)
	n = p*q
	n_list.append(n)

e = len(tmp)

c_list = []

for mes in m_list:
	for n in n_list:
		m = int(mes,2)
		c = pow(m,e,n)
		c_list.append(c)

print("c_list : ",c_list)
print("n_list : ",n_list)


