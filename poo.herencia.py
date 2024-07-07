class Empleado:
    def __init__(self, nombre, salario, dni, direccion, tipo_contrato, estado_civil, sexo, agencia):
        self._nombre = nombre  # Atributo protegido
        self._salario = salario  # Atributo protegido
        self._dni = dni
        self._direccion = direccion
        self._tipo_contrato = tipo_contrato
        self._estado_civil = estado_civil
        self._sexo = sexo
        self._agencia = agencia

    def describir(self):
        return (f"{self._nombre}, DNI {self._dni}, del sexo {self._sexo} y estado civil {self._estado_civil}, "
                f"trabaja en {self._agencia} bajo un contrato {self._tipo_contrato}, vive en {self._direccion}, "
                f"tiene un salario de {self._salario}.")

# Clase derivada que extiende Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, dni, direccion, tipo_contrato, estado_civil, sexo, agencia, departamento):
        super().__init__(nombre, salario, dni, direccion, tipo_contrato, estado_civil, sexo, agencia)
        self._departamento = departamento  # Atributo protegido adicional

    # Sobrescribiendo el método describir para añadir información del departamento
    def describir(self):
        return (f"{super().describir()} Además, es el gerente del departamento de {self._departamento}.")

# Función para crear un empleado o gerente desde la entrada del usuario
def crear_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    dni = input("Ingrese el DNI del empleado: ")
    direccion = input("Ingrese la dirección del empleado: ")
    tipo_contrato = input("Ingrese el tipo de contrato: ")
    estado_civil = input("Ingrese el estado civil del empleado: ")
    sexo = input("Ingrese el sexo del empleado: ")
    agencia = input("Ingrese el nombre de la agencia o almacén: ")
    
    tipo = input("Es este empleado un gerente? (s/n): ")
    if tipo.lower() == 's':
        departamento = input("Ingrese el departamento del gerente: ")
        return Gerente(nombre, salario, dni, direccion, tipo_contrato, estado_civil, sexo, agencia, departamento)
    else:
        return Empleado(nombre, salario, dni, direccion, tipo_contrato, estado_civil, sexo, agencia)

def main():
    print("Bienvenido al sistema de gestión de empleados.")
    empleados = []
    
    while True:
        empleados.append(crear_empleado())
        continuar = input("¿Desea añadir otro empleado? (s/n): ")
        if continuar.lower() != 's':
            break

    for emp in empleados:
        print(emp.describir())

if __name__ == "__main__":
    main()
