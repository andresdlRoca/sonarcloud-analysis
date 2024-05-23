import os
import sqlite3
import requests

# Hardcoded API key - This is a serious security risk
API_KEY = "12345-ABCDE"

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def get_user_input():
    user_input = input("Enter some text: ")
    return user_input

def process_data(data):
    if data is None:
        print("No data to process")
        return ""
    processed_data = data.lower()
    return processed_data

def connect_to_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def execute_query(conn, query, params):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()

def call_external_api(api_key, data):
    # This simulates an API call using the hardcoded API key
    response = requests.post("https://example.com/api", headers={"Authorization": f"Bearer {api_key}"}, json={"data": data})
    return response.json()

def main():
    file_path = "example.txt"
    db_name = "example.db"

    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return
    
    # Processing data
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")

    # Getting user input and writing to a file
    user_input = get_user_input()
    if user_input:
        write_file(file_path, user_input)
    else:
        write_file(file_path, processed_data)

    # Connect to a database
    conn = connect_to_db(db_name)
    try:
        user_id = input("Enter user ID: ")
        
        # Secure parameterized query to prevent SQL Injection
        query = "SELECT * FROM users WHERE id = ?"
        execute_query(conn, query, (user_id,))
    
        print("Query executed successfully.")
        
        # Call external API with hardcoded API key
        api_response = call_external_api(API_KEY, processed_data)
        print(f"API Response: {api_response}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
