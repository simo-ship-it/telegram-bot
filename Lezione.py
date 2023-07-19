class Lezione:
   
    def __init__(self, materia, professore, data, oraInizio, oraFine, idLezione):
        self.materia= materia 
        self.professore= professore 
        self.data= data 
        self.oraInizio= oraInizio
        self.oraFine= oraFine 
        self.idLezione =idLezione

    def getId(self): 
        return self.idUtente

    def autenticazione(self, input):
        if input==self.token:
            return True 
        else: 
            return False 