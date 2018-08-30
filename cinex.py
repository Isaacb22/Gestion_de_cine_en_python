print ("\n\n\t  Bienvenido al control administrativo del cine VERGATARIO")


def menu():
	pass
	

def control_de_salas():
	numero_de_salas = input("\nIngrese el numero de salas: ")
	lista_salas = []
	for i in range(1,int(numero_de_salas)+1):
		obj_sala = {}
		limite_sala = input("Ingrese el limite para la sala {}:".format(i))

		obj_sala['nro_sala'] = i
		obj_sala[limite_sala] = limite_sala

		lista_salas.append(obj_sala)
		obj_sala = {}	
	return lista_salas

control_de_salas()