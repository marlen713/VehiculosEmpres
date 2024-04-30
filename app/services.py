
from app.models import Chofer, Vehiculo, RegistrarContabilidad


def crear_vehiculo(patente, marca, modelo, year): 
    vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year)
    vehiculo.save() 
    return vehiculo




