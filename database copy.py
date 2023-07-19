import sqlite3

# 1. Creare una connessione al database (crea un nuovo database chiamato 'esempio.db' se non esiste)
conn = sqlite3.connect('utenti.db')

# 2. Creare una tabella (se non esiste già)
with conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persone (
            id INTEGER PRIMARY KEY,
            materia TEXT,
            professore TEXT,
            data INTEGER,
            orainizio INTEGER, 
            orafine DOUBLE
        )
    ''')

# 3. Inserire dati nella tabella
with conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Algoritmi e strutture dati', 'Pinotti', 19-7-23, 9:00, 11:00 ))
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Diritto dell''informatica', 'Florindi', 20-7-23, 9:00, 11:00))
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Fisica generale', 'Tosti', 5-7-23, 16:00, 18:00))
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Ingegneria del software', 'Milani', 3-7-23, 11:00, 13:00))
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Linguaggi formali e compilatori', 'Carpi', 27-7-23, 9:00, 11:00))
    cursor.execute('INSERT INTO persone (materia, professore, data, orainizio, orafine) VALUES (?, ?, ?, ?, ?)', ('Sistemi operativi', 'Carpi', 13-7-23, 14:00, 16:00))


# 4. Esempio di query per leggere dati dalla tabella
with conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM persone')
    persone = cursor.fetchall()
    for persona in persone:
        print(persona)

# Chiudi la connessione al termine
conn.close()
