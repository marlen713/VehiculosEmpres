
from app.models import Chofer, Vehiculo, RegistrarContabilidad


def crear_vehiculo(patente, marca, modelo, year): 
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save() 
    return vehiculo

def crear_chofer(rut, nombre, apellido, activo):
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo)
    chofer.save()
    return chofer


