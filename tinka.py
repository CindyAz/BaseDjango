from Seguridad import Usuario as us
from ruta import Ruta as ru
from ruta import Bus as bu
from ruta import ListaBus
from ruta import VentaPasaje as vp

#-- Inicializando variables fijas
v_ruta = []
v_usuario = []
v_bus = []
v_pasajes = []
v_pasajesvendido = []
usuario = us('CAZANA','CAZANA',1,'')
v_usuario.append(usuario)
usuario = us('LMANUEL','LMANUEL',2,'')
v_usuario.append(usuario)
lista_bus = ListaBus()



def clearScreen(): 
	import os 
	if os.name == "nt": 
		os.system("cls") 
	elif os.name == "posix": 
		os.system("clear")
	else: 
		raise("No se puede limpiar la pantalla")
		print("<-No se pudo borrar la pantalla->") 

def eliminarElemento(lista,value):
	lista.remove(value)

def imprimirListaUsuario(lista):
	for item in lista:
		usuario = us(item.usuario,item.clave, item.nivel, item.email)
		usuario.imprime()        
		#print(str(item.usuario)+'- '+ str(item.nivel))

def fu_menu(proceso):
	print('		'+proceso+'		')
	print('---------------')
	print(' 1.- Reporte ')
	print(' 2.- Registro')
	op1 = int(input('Ingrese Opcion: '))
	while op1 not in (1,2):
		op1 = input('Ingrese Opcion Valida: ')
	return op1


def fu_main(s_usuario,s_clave,v_cont_bus):
	clearScreen()
	cont = 0
	for i in range(0,len(v_usuario)):
		if s_usuario in v_usuario[i].usuario and s_clave in v_usuario[i].clave:
			print("------------------------------------------------------")
			print('			Bienvenido a TITANIC')
			usuario.imprime_nivel(v_usuario[i].usuario,v_usuario[i].nivel)
			print("------------------------------------------------------")

			usuario.define_rol(v_usuario[i].nivel)
			op = int(input('Ingrese Opciòn: '))
			while op not in(usuario.imprime_rolusuario(v_usuario[i].nivel)):
				op = int(input('Ingrese Opciòn valida: '))
			if op == 1:
				clearScreen()
				op1 = fu_menu('USUARIO')
				if op1==1:
					print('---------------------------------')
					for j in range(0,len(v_usuario)):
						usuario.imprime_nivel(v_usuario[j].usuario,v_usuario[j].nivel)
				elif op1 == 2:
					print('---------------------------------')
					l_usuario = input('Ingrese Usuario: ')
					l_clave = input('Ingrese Clave: ')
					l_nivel = int(input('Ingrese Nivel[1 = Administrador, 2 = Vendedor]: '))
					while l_nivel not in(1,2):
						l_nivel = int(input('Ingrese Nivel[1 = Administrador, 2 = Vendedor]: '))
					l_email = input('Ingrese email:')
					v_usuario.append(us(l_usuario,l_clave,l_nivel,l_email))
				op=-1
			elif op == 2:
				clearScreen()
				op1 = fu_menu('Bus')
				if op1 == 1:
					print('------------------------------------')
					#lista_bus.consultar()
					bus = bu()
					if len(v_bus) == 0:
						print('No existen Buses')
					else:
						print('BUSES: '+ v_bus[0].descripcion +' -- '+v_bus[1].descripcion)
						print('| Nro |  Bus |  Nro. Asientos')
						for j in range(0,len(v_bus)):
							bus.codigo = v_bus[j].codigo
							bus.descripcion = v_bus[j].descripcion
							bus.cant_asientos = v_bus[j].cant_asientos
							bus.imprime_bus()
				elif op1 == 2:
					print('------------------------------------')
					bus = bu()
					v_cont_bus = v_cont_bus + 1
					bus.codigo = int(v_cont_bus)
					bus.descripcion = input('Ingrese Descripción: ')
					bus.cant_asientos = int(input('Ingrese Nro Asientos: '))
					v_bus.append(bus)
					#lista_bus.insertar(bus)
				op=-1
			elif op == 3:
				clearScreen()
				op1 = fu_menu('RUTA')
				if op1 == 1:
					print('------------------------------------')
					if len(v_ruta) == 0:
						print('No existen Rutas')
					else:
						for j in range(0,len(v_ruta)):
							ruta = ru()
							ruta.codigo = v_ruta[j].codigo
							ruta.lugar_ori = v_ruta[j].lugar_ori
							ruta.lugar_dest = v_ruta[j].lugar_dest
							ruta.tiempo_apro = v_ruta[j].tiempo_apro
							ruta.hora_salida = v_ruta[j].hora_salida
							ruta.turno = v_ruta[j].turno
							ruta.bus = v_ruta[j].bus
							ruta.servicio = v_ruta[j].servicio
							ruta.imprime_ruta()
				elif op1 == 2:
					print('------------------------------------')
					ruta = ru()
					v_max = len(v_ruta)+1
					ruta.codigo = v_max
					ruta.lugar_ori = input('Ingrese Lugar de Origen: ')
					ruta.lugar_dest = input('Ingrese Lugar de Destino: ')
					ruta.tiempo_apro = input('Ingrese Tiempo Aproximado: ')
					ruta.hora_salida = input('Ingrese Hora de Salida: ')
					aux_turno = input('Ingrese Turno[PM/AM]: ').upper()
					while aux_turno not in('PM','AM'):
						aux_turno = input('Ingrese Turno Correcto[PM/AM]: ')
					ruta.turno = aux_turno
					aux_bus = input('Ingrese Bus: ')
					flag = False
					while flag == False:
						for z in range(0,len(v_bus)):
							bus = bu()
							if aux_bus in str(v_bus[z].codigo):
								bus.codigo = v_bus[z].codigo
								bus.descripcion = v_bus[z].descripcion
								ruta.bus = bus
								flag = True
							else:
								flag == False
						if flag == False:
							aux_bus = input('Ingrese Bus Valido: ')
					#ruta.bus = aux_bus
					ruta.servicio = int(input('Ingrese Ruta[1=Especial/2=Econocimica]:'))
					v_ruta.append(ruta)
				op=-1
			elif op == 4:
				clearScreen()
				op1 = fu_menu('VENTA DE PASAJES')
				if op1 == 1:
					for m in range(0,len(v_pasajes)):
						ruta = ru()
						venta = vp()
						venta.codigo = v_pasajes[i].codigo
						venta.cliente = v_pasajes[i].cliente
						ruta.lugar_ori = v_pasajes[i].ruta.lugar_ori
						ruta.lugar_dest = v_pasajes[i].ruta.lugar_dest
						ruta.hora_salida = v_pasajes[i].ruta.hora_salida
						ruta.turno = v_pasajes[i].ruta.turno
						venta.ruta = ruta
						venta.asiento = v_pasajes[i].asiento
						venta.imprime_venta()
				elif op1 == 2:
					venta = vp()
					aux_max = len(v_pasajes) + 1 
					venta.codigo = aux_max
					venta.cliente = input('Ingrese Datos del Pasajero: ')
					ruta.codigo = int(input('Ingrese Codigo de Ruta: '))
					flag = False
					for m in range(0,len(v_ruta)):
						if str(ruta.codigo) in str(v_ruta[m].codigo):
							ruta.lugar_ori = v_ruta[m].lugar_ori
							ruta.lugar_dest = v_ruta[m].lugar_dest
							ruta.hora_salida = v_ruta[m].hora_salida
							flag = True
					while flag == False:
						ruta.codigo = int(input('Ingrese Codigo de Ruta Correcto: '))
					venta.asiento = input('Ingrese Nro Asiento: ') 
					while venta.genera_venta(v_pasajesvendido)  in (-1,-2):
						if venta.genera_venta(v_pasajesvendido) == -1:
							print('Nro de Asiento No valido')
						else:
							print('Nro de Asiento Ya Esta Vendido')
						venta.asiento = input('Ingrese Nro Asiento valido: ')
					venta.ruta = ruta
					v_pasajes.append(venta)
					v_pasajesvendido.append(aux_max)
				op=-1
			cont = cont + 1
			if op == -1:
				ops = input('Desea Continuar[S/N]: ')
				if ops == 'S':
					fu_main(v_usuario[i].usuario,v_usuario[i].clave,v_cont_bus)
	if cont == 0:
			print('Ud. No Esta Registrado en TITANIC...!')

	#print(dir(usuario))
	#imprimirListaUsuario(v_usuario)

s_usuario = input('Ingrese Usuario: ')
s_clave = input('Ingrese Clave:')
v_cont_bus = 0
fu_main(s_usuario,s_clave,v_cont_bus)
