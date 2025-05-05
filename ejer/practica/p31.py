#7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria 
# ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita el turno de estudio
turno = input("¿En qué turno estudias? (mañana, tarde o noche): ").strip().lower()

# Verifica y muestra el saludo correspondiente
if turno == "mañana":
    print("¡Buenos Días!")
elif turno == "tarde":
    print("¡Buenas Tardes!")
elif turno == "noche":
    print("¡Buenas Noches!")
else:
    print("¡Valor Inválido!")
