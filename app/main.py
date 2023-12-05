from datetime import datetime

cadena='2000-01-01T19:00:00'
tiempo=946684800

fecha_hora2=datetime.utcfromtimestamp(tiempo)
fecha_hora=datetime.fromisoformat(cadena)

print(fecha_hora2)
print(fecha_hora)