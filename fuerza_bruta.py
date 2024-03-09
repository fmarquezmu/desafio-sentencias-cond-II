from string import ascii_lowercase
import getpass #Para ingresar el input de manera oculta

attempts = 0
hidden_pass = getpass.getpass("Ingrese la contraseña: ").lower()

for letter in hidden_pass:
    for character in ascii_lowercase:
        if letter == character:
            attempts += 1
            break
        else:
            attempts += 1

print(f"La contraseña fue forzada en {attempts} intentos")