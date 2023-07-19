import sqlite3

# 1. Creare una connessione al database (crea un nuovo database chiamato 'esempio.db' se non esiste)
conn = sqlite3.connect('utenti.db')

# 2. Creare una tabella (se non esiste già)
with conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persone (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            cognome TEXT,
            matricola INTEGER,
            numeroTelefono INTEGER, 
            token DOUBLE
        )
    ''')

# 3. Inserire dati nella tabella
with conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Alice', 'Fornero', 342969, 3491234123, 8473098562254837 ))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Franco', 'Forse', 358756, 3887868580, 5945362547632158))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Mario', 'Biondi', 389654, 3348798728, 1679325483018034))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Alfredo', 'Verdi', 310988, 3499871636, 9325498555366696))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Quinto', 'Monacelli', 365678, 3350273893, 2597403164985214))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Simone', 'Billeri', 343523, 3883279408, 2496573100056488))
    cursor.execute('INSERT INTO persone (nome, cognome, matricola, numeroTelefono) VALUES (?, ?, ?, ?, ?)', ('Alessio', 'Bistoni', 342966, 3895786999, 2455556872130049))




# 4. Esempio di query per leggere dati dalla tabella
with conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM persone')
    persone = cursor.fetchall()
    for persona in persone:
        print(persona)

# Chiudi la connessione al termine
conn.close()
