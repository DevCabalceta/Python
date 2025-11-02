import xml.etree.ElementTree as ET

class Banco:
    def __init__(self, nombreBanco, cantidadEmpleados):
        self.nombreBanco = nombreBanco
        self.cantidadEmpleados = cantidadEmpleados

vectorBancos = []

banco1 = Banco("Banco de Costa Rica", 4000)
banco2 = Banco("BAC", 1900)
banco3 = Banco("Popular", 2500)
banco4 = Banco("Banco Nacional de Costa Rica", 3000)
banco5 = Banco("Prpmerica", 500)

vectorBancos.append(banco1)
vectorBancos.append(banco2)
vectorBancos.append(banco3)
vectorBancos.append(banco4)
vectorBancos.append(banco5)

root = ET.Element("listaBancos")

for banco in vectorBancos:
    bancoElemento = ET.SubElement(root, "banco")

    #Creando el atributo de banco y en el text le meto el valor del banco
    nombre_elemento = ET.SubElement(bancoElemento, "nombre")
    nombre_elemento.text = banco.nombreBanco

    cantidad_Elemento = ET.SubElement(bancoElemento, "cantidadEmpleados")
    cantidad_Elemento.text = str(banco.cantidadEmpleados)

arbol = ET.ElementTree(root)
arbol.write("informacionBanco.xml", encoding="UTF-8", xml_declaration=True)