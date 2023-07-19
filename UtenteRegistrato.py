class UtenteRegistrato:
   
    def __init__(self, nome, cognome, matricola, idUtente, token):
        self.nome = nome 
        self.cognome = cognome 
        self.matricola = matricola
        self.idUtente = idUtente
        self.token = token 
        print("")

    def getId(self): 
        return self.idUtente

    def autenticazione(self, input):
        if input==self.token:
            return True 
        else: 
            return False 
        

        
        
    

        