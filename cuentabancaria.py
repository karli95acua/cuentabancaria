# EJERCICIO CUENTA BANCARIA
class CuentaBancaria: #Este es la clase de mi objeto
    cuentas = [] #aqui voy a almacenar todas las cuentas creadas
    def __init__(self, banco, tasa_interes = 0.01, balance = 0): #Mi constructor
        self.banco = banco
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    #Aqui van los métodos solicitados:
    #Método de depósito:
    def deposito(self, amount):
        print(f"Ha realizado un depósito de ${amount} en su cuenta bancaria,")
        self.balance += amount
        print(f"ahora su cuenta tiene un saldo de: ${self.balance},")
        print(f"en la institución: {self.banco}.")
        return self

    #Método de retiro:
    def retiro(self, amount):
        if self.balance - amount < 0:
            self.balance -= 5
            print(f"Usted ha intentado realizar un retiro por ${amount}, el cual no se ha concretado,")
            print("por fondos insuficientes, se ha cobrando una tarifa de $5,")
            print(f"ahora su cuenta tiene un saldo de: ${self.balance},")
            print(f"en la institución: {self.banco}.")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"Ha realizado un retiro de ${amount} en su cuenta bancaria,")
            print(f"ahora su cuenta tiene un saldo de: ${self.balance},")
            print(f"en la institución: {self.banco}.")
        return self

    #Método de mostrar información del balance de la cuenta:
    def mostrar_info_cuenta(self):
        print(f"Balance de cuenta: ${self.balance},")
        print(f"en la institución: {self.banco}.")
        return self

    #Método de generar intereses:
    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
            print(f"Su actual tasa de interés es de {self.tasa_interes}, por lo que")
            print(f"ha generado un interés de: ${'{:.1f}'.format(interes_generado)} en su cuenta bancaria.")
        else:
            print("Debido a que su balance no ha sido positivo, usted no ha acumulado intereses,")
            print(f"en su cuenta en la institución {self.banco}.")
        return self
    
    #Aqui va mi método de clase:
    @classmethod
    def mostrar_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

#Aquí creo las instancias    
cuenta_uno = CuentaBancaria("Banco Internacional POO", 0.01, 2000)
cuenta_dos = CuentaBancaria("Banco Nacional Python", 0.01, 500)

#Acciones de la primera cuenta:
#Hacer 3 depósitos y 1 retiro, luego generar intereses y luego mostrar la información de la cuenta:
cuenta_uno.deposito(25).deposito(75).deposito(120).retiro(1000).generar_interes().mostrar_info_cuenta()
print("----------------SIG CUENTA----------------")
#Acciones de la segunda cuenta:
#Hacer 2 depósitos y 4 retiros, luego generar intereses y luego mostrar la información de la cuenta:
cuenta_dos.deposito(50).deposito(100).retiro(300).retiro(150).retiro(120).retiro(80).generar_interes().mostrar_info_cuenta()
print("----------------BONUSNINJA----------------")
#Aqui voy a llamar a mi método de clase para el BONUS NINJA:
CuentaBancaria.mostrar_las_cuentas()