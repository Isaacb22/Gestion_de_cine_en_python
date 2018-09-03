porcentaje_de_clientes_vip = 20

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
	selecciona_una_opcion = input("\nSeleccione una opcion:")
	
	if selecciona_una_opcion == '1':
		print ("\nTu has elegido la opcion Control de salas")
		control_de_salas()


	
def control_de_salas():
		numero_de_salas = input("\nIngrese el numero de salas: ")
		lista_salas = []
	
		for i in range(1,int(numero_de_salas)+1):
			obj_sala = {}
			limite_sala = input("Ingrese el limite para la sala {}:".format(i))
			clientes_vip = input("Ingrese la cantidad de clientes VIP de la sala {}".format(i))
			clientes_normales = input("Ingrese la cantidad de clientes normales de la sala :{}".format(i))
			obj_sala['nro_sala'] = i
			obj_sala['limite_sala'] = limite_sala
			obj_sala['clientes_vip'] = clientes_vip
			while validacion_de_porcentaje(limite_sala,clientes_vip) == False:
				print ("Limite de asientos VIP excedido")
				clientes_vip = input("Ingrese la cantidad de clientes VIP de la sala {}".format(i))
			obj_sala['clientes_normales'] = clientes_normales
			lista_salas.append(obj_sala)
			obj_sala = {}   
		return lista_salas

menu()