from datetime import datetime

actual = datetime.now()

hora = actual.hour
minutos = actual.minute
segundos = actual.second

print(f'{hora+2}:{minutos}:{segundos}')