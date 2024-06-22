from dataclasses import dataclass
@dataclass
class Connessione:
    o1: int
    o2: int
    peso: int
    #visto che non vogliamo che questi elementi siano dei nodi la funzione di hash
    #possiamo non implementarla
    def __str__(self):
        return f"{self.o1} {self.o2} {self.peso}"
