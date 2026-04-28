import sqlite3

def get_user_balance(username):
    # Error 1: Credencial expuesta
    api_key = "AKIA-SECRET-12345" 
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    # Error 2: Inyección SQL
    query = "SELECT balance FROM accounts WHERE username = '" + username + "'"
    cursor.execute(query)
    
    return cursor.fetchone()
