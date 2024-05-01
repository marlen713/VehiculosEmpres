
from app.models import Chofer, Vehiculo, RegistrarContabilidad


def crear_vehiculo(patente, marca, modelo, year, activo): 
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year, activo=activo)
    vehiculo.save() 
    return vehiculo

def crear_chofer(rut, nombre, apellido, activo):
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo)
    chofer.save()
    return chofer

def crear_registro_contable(fecha_compra,valor,vehiculo):
    id_auto = Vehiculo.objects.get(patente=vehiculo)
    registro = RegistrarContabilidad(fecha_compra=fecha_compra,valor=valor,vehiculo=id_auto)
    registro.save()
    return registro

def deshabilitar_chofer(pk_id):
    try:
        chofer = Chofer.objects.get(rut=pk_id)
        chofer.activo = False
        chofer.save()
        return False
    except:
        print("error en deshabilitar chofer")


def deshabilitar_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(patente=pk_id)
        auto.activo= False
        auto.save()
        return False
    except:
        print("error en deshabilitar vehiculo")


def habilitar_chofer(pk_id):
    try:
        chofer = Chofer.objects.get(rut=pk_id)
        chofer.activo = True
        chofer.save()
        return True
    except:
        print("error en habilitar chofer")


def habilitar_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(patente=pk_id)
        auto.activo= True
        auto.save()
        return True
    except:
        print("error en habilitar vehiculo")


def obtener_vehiculo(pk_id):
    try:
        auto = Vehiculo.objects.get(patente=pk_id)
        return auto
    except:
        print("error en obtener vehiculo")


def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer

def  asignar_chofer_a_vehiculo(vehiculo,chofer):
    chofer.vehiculo = vehiculo 
    #vehiculo.save()
    chofer.save()

def imprimir_datos_vehiculos(): 
    vehiculos = Vehiculo.objects.all() 
    for v in vehiculos: 
        print(f"Vehiculo:{v.patente}/{v.marca}/{v.modelo}/" + 
              f"{v.year}/activo:{v.activo}") 
        if hasattr(v, "chofer"): 
            print(f"\tChofer[{v.chofer.rut}]:{v.chofer.nombre} " + 
                  f"{v.chofer.apellido}/activo:{v.chofer.activo}") 
        if hasattr(v, "contabilidad"): 
            print(f"\tContabilidad:[{v.contabilidad.id}]:fecha_compra:" + 
                  f"{v.contabilidad.fecha_compra}/valor:{v.contabilidad.valor}")
