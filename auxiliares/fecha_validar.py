import datetime

def pedir_fecha_valida(mensaje):
    """
    Pide al usuario una fecha en formato AÑO/MES/DIA y la valida
    """
    while True:
        fecha_str = input(mensaje)
        try:
            fecha_obj = datetime.datetime.strptime(fecha_str,'%Y/%m/%d')
            return fecha_obj
        except ValueError:
            print('Formato de fecha incorrecto. Por favor, use el formato AAAA/MM/DD')