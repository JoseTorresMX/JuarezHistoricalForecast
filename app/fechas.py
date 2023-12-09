from datetime import datetime, timedelta

# Obtener la fecha actual
fecha_actual = datetime.now()

# Formatear la fecha en formato americano (MM/DD/YYYY)
fecha_americana = fecha_actual.strftime("%m/%d/%Y")

# Definir la cantidad de días a sumar
dias_a_sumar = 36  # Puedes cambiar este valor según tus necesidades

# Sumar la cantidad de días
fecha_futura = fecha_actual + timedelta(days=dias_a_sumar)

# Formatear la fecha en formato numérico (MMDDYYYY)
fecha_numerica_futura = fecha_futura.strftime("%m%d%Y")

# Imprimir la fecha futura en formato numérico
print(f"Fecha actual + {dias_a_sumar} días en formato numérico:", fecha_numerica_futura)