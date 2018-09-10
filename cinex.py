porcentaje_de_clientes_vip = 20
lista_salas = []
config = {}



def eleccion_cliente():
	while True:
		try:
			elegir_cliente = int(input('Que tipo de cliente quiere ser? \n\n\t\t\t1)VIP o 2)NORMAL:'))
			if elegir_cliente == 1:
				config["cont_vip"]+=1
			else:
				if elegir_cliente == 2:
					config["cont_normal"] +=1
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
		



def validacion_de_porcentaje(limite_sala,clientes_vip):
	porcentaje_total = int(limite_sala) * int(porcentaje_de_clientes_vip) / 100
	if int(clientes_vip) < int(porcentaje_total):
		return 	True
	else:
		return False



def menu():
	print ("\n\n\t\t\t\t\t\t\t  Bienvenido al cine VERGATARIO")
	print (" ============================================================================================================================================")
	print (" ||| 1)control de salas ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 2)control de clientes VIP |||")
	print (" |||====================||||||||||||||||||||||||||||||===============================||||||||||||||||||||||||||===========================|||")
	print (" ||||||||||||||||||||||||||||||||||||||||||||||||||||| 3)control de clientes normal  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	print (" ============================================================================================================================================")
	selecciona_una_opcion = input("\nSeleccione una opcion: ")
	
	if selecciona_una_opcion == '1':
		print ("\nTu has elegido la opcion Control de salas")
		control_de_salas(config)



	
def control_de_salas(config):
	while True:
		try:
			nro_sala = int(input("\nIngrese el numero de salas: "))
			break	
	
		except ValueError:
			print ('\nCaracter invalido, solo se permiten numeros')
	
	
	
	for i in range(1,int(nro_sala)+1):
		
		
		while True:
			try:
				config['limite_sala'] = int(input("\nIngrese el limite para la sala {}: ".format(i)))
				
				break
			
			except ValueError:
				print ('\nCaracter invalido, solo se permiten numeros')	
		
		eleccion_cliente()
		
		config['num_sala'] = i
		
		
		while validacion_de_porcentaje(config["limite_sala"],config["cont_vip"]) == False:
			print ("Limite de asientos VIP excedido")
			config["cont_vip"] = input("Ingrese la cantidad de clientes VIP de la sala {}: ".format(i))

		
		lista_salas.append(config)
		config = {}  
	
menu()