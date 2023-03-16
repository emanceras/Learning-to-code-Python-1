# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado
pago_sin_impuesto = float(input("Proporcione el pagon sin impuesto:"))
iva = float(input("Proporcione el total del IVA:"))


def pago_con_iva():
    total = pago_sin_impuesto + pago_sin_impuesto * (iva / 100)
    return total


resultado = pago_con_iva()
print(resultado)
