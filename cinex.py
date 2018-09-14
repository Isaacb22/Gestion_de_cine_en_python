import getpass
porcentaje_de_clientes_vip = 20
lista_salas = []

salas = {}


def eleccion_cliente(config):
	while True:
		try:
			elegir_cliente = int(input('\nQue tipo de cliente quiere ser? \n\n\t\t\t1)VIP  \t\t\t\t\t\t2)NORMAL : '))
			if elegir_cliente == 1:
				config['cont_vip']+=1
			else:
				if elegir_cliente == 2:
					config['cont_normal'] += 1
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
		
	
	while validacion_de_porcentaje(config["limite_sala"],config["cont_vip"]) == False:
			print ("Limite de asientos VIP excedido")
			config["cont_vip"] = input("Ingrese la cantidad de clientes VIP de la sala {}: ".format(i))


def validacion_de_porcentaje(limite_sala,clientes_vip):
	porcentaje_total = int(limite_sala) * int(porcentaje_de_clientes_vip) / 100
	if int(clientes_vip) < int(porcentaje_total):
		return 	True
	else:
		return False


def menu():
	
	print ("\n\n\t\t\t\t\t\t\t  Bienvenido al cine VERGATARIO")
	print (" =============================================================================================================================================")
	print (" |||  1)Control de salas   |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    2)Control de clientes  |||")
	print (" |||=======================|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||===========================|||")
	print (" |||	  3)Resultados     |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    4)Salir del programa   |||")
	print (" =============================================================================================================================================")
	selecciona_una_opcion = input("\nSeleccione una opcion: ")
	
	if selecciona_una_opcion == '1':
		print ("\nTu has elegido la opcion Control de salas")
		
		nombre_de_usuario = input("\nIngrese su nombre de usuario: ")
		contrasena = getpass.getpass('\nIngrese su contrasena: ')
		while True:
			if nombre_de_usuario != 'isaacb22' or contrasena != '1234':
				print ('\nInicio de sesion fallido. Intente otra vez')
				nombre_de_usuario = input("\nIngrese su nombre de usuario: ")
				contrasena = getpass.getpass('\nIngrese su contrasena: ')
			else:
				print ("\nInicio de sesion exitoso")
				control_de_salas(config)
				break
			
	else:
		if selecciona_una_opcion == '2':
			print ("\nTu has elegido la opcion Contro de clientes")
			eleccion_cliente(config)
	
	
	
def control_de_salas(config):
	while True:
		try:
			nro_sala = int(input("\n\nIngrese el numero de salas: "))
			break	
	
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
	
	
	for i in range(1,int(nro_sala)+1):
		

		while True:
			try:
				limite_sala = int(input("\nIngrese el limite para la sala {}: ".format(i)))
				config['limite_sala'] = limite_sala
				nombre_de_salas = "sala{}".format(i)
				salas[nombre_de_salas] = {"limite" : limite_sala}
				break
			

			except ValueError:
				print ('\nCaracter invalido, solo se permiten numeros')

		
	print ("\n\t\t\t\t\t     Has validado la opcion Control de salas exitosamente")
	
		
	config['num_sala'] = i
		
		

		
	lista_salas.append(config)
	config = {}  

while True:
	menu()