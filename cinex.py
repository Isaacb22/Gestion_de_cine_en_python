def control_de_salas():
		numero_de_salas = input("\nIngrese el numero de salas: ")
		lista_salas = []
	
		for i in range(1,int(numero_de_salas)+1):
			obj_sala = {}
			limite_sala = input("Ingrese el limite para la sala {}:".format(i))

			obj_sala['nro_sala'] = i
			obj_sala['limite_sala'] = limite_sala

			lista_salas.append(obj_sala)
			obj_sala = {}   
		return lista_salas



def menu():
	print ("\n\n\t\t\t  Bienvenido al cine VERGATARIO")
	print ("\n ||| 1)control de salas ||| \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ||| 2)control de clientes VIP |||")
	print ("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
	print ("\n 	\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ||| 3)control de clientes normal  ||| \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
	selecciona_una_opcion = input("\nSeleccione una opcion:")
	
	if selecciona_una_opcion == '1':
		print ("\nTu has elegido la opcion Control de salas")
		control_de_salas()


	
menu()