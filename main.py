import os
import sqlite3
import hashlib
import traceback


secret_key = "password1234"  


def read_file(file_path):
    try:
        # Vulnerabilidad: No manejo de paths absolutos
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        # Error: Capturar excepciones genéricas
        print(f"An error occurred: {e}")
        return None

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
    print("Data written to file successfully")

def login(password):
    if password == password:
        print("Login successful")
    else:
        print("Login failed")
        print(password)

def handle_error():
    try:
        pass
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()  # Exposición de detalles internos del sistema

def weak_password_hashing(password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def store_user_credentials(username, password):
    # Hardcoded database credentials
    db_path = "user_credentials.db"
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Vulnerabilidad: Uso de un hash débil
    hashed_password = weak_password_hashing(password)
    
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    connection.commit()
    connection.close()

def main():
    file_path = "/tmp/example.txt"
    user_password = "P@ssw0rd122134"  

    # Lectura de un archivo
    data = read_file(file_path)
    if data is None:
        return

    eval(user_password)

    # Writing to a potentially insecure temporary file
    temp_file_path = "/tmp/tempfile.txt"
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write("This is a temporary file.")
        # Security risk demonstration
    


    # Almacenar credenciales de usuario con hash débil
    username = "user1"
    store_user_credentials(username, user_password)

    # Vulnerabilidad: posible inyección de comandos
    os.system(f"echo {user_password}")

    write_file(file_path, username)

    # Command injection
    os.system(user_password)  # Using user input in system command
    
    try:
        write_file(file_path, user_input)
    except Exception as e:
        # Exposing internal errors to the user
        print(f"An error occurred: {e}")  # Improper error handling

if __name__ == "__main__":
    main()