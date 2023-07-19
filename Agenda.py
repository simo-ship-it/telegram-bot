from datetime import date


class Agenda:
    prossimeLezioni = []

    def __init__(self ):
        pass
    


    def aggiungiLeioni(lezioneDaAggiungere):

        Agenda.prossimeLezioni.append(lezioneDaAggiungere)
        Agenda.prossimeLezioni = sorted(Agenda.prossimeLezioni, key=getDate())

        
    
    def aggiungiLeioni(lezioneDaRimuovere):
        Agenda.prossimeLezioni.remove(lezioneDaRimuovere)
            

        
    def aggiornaAgenda():
        for lezione in Agenda.prossimeLezioni:
            if date.today() < lezione.date:
                Agenda.prossimeLezioni.remove(lezione) 



    def getAgenda(self): 
        return Agenda.prossimeLezioni
    
