import subprocess, re
from prettytable import PrettyTable
users=[]; n=1
command='netsh wlan show profiles'
proceso = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
ox=proceso.stdout.splitlines()
for i in ox:
	if re.search(':', i):
		b=re.search('WIFI', i, re.IGNORECASE)
		if b == None:
			users.append(i.split(':')[1].lstrip())
uspass=[]
for i in users:
	c=f'netsh wlan show profiles name={i} key=clear'
	salida=subprocess.run(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	vz=salida.stdout.splitlines()
	for e in vz:
		b=e.find('clave')
		if b != -1:
			usk=f"{i} -> {e.split(':')[1].lstrip()}"
			uspass.append(usk)
tabla = PrettyTable()
tabla.field_names = ['NRO', "USUARIO", "CLAVE"]
for i in uspass:
	user=i.split('->')[0]
	pass1=i.split('->')[1].lstrip()
	tabla.add_row([n, user, pass1])
	print(tabla)
	n=n+1
input('\nPresione [ENTER] para SALIR ')
