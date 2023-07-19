import sqlite3

class Utente:
    def __init__(self, numeroTelefono):
        self.numeroTelefono = numeroTelefono

    def verificaRegistrazione(self):
       
        conn = sqlite3.connect('utenti.db')
        
        # 4. Esempio di query per leggere dati dalla tabella
        with conn:
            cursor = conn.cursor()
            dato_da_cercare = self.numeroTelefono
            query = "SELECT * FROM persone WHERE numeroTelefono = ?"  # Sostituisci "nome_tabella" e "nome_colonna" con i nomi corrispondenti.
            cursor.execute(query, (dato_da_cercare,))
            risultati = cursor.fetchall()

            if risultati:
            print("Il dato è presente nel database.")
            else:
                print("Il dato non è presente nel database.")


            conn.close()


        
    
















































    