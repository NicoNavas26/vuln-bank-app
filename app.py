import sqlite3

def get_user_balance(username):
    # CRÍTICO: Credencial expuesta directamente en el código
    aws_secret_key = "AKIAIOSFODNN7EXAMPLE" 
    
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    
    # CRÍTICO: Vulnerabilidad de Inyección SQL (concatenación de strings)
    query = "SELECT balance FROM accounts WHERE username = '" + username + "'"
    cursor.execute(query)
    
    return cursor.fetchall()
