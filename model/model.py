import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._allOpere = DAO.getAllOpere()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._allOpere)
        self._idMap = {}
        for a in self._allOpere:
            self._idMap[a.object_id] = a

    def buildGraph(self):
        self._aggiungiArchi()

    def _aggiungiArchi(self):
        self._grafo.clear_edges()
        archi=DAO.getAllConnessioni()
        for a in archi:
            self._grafo.add_edge(self._idMap[a.o1],self._idMap[a.o2], weight=a.peso)

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)
    def checkExistance(self, n):
        for a in self._grafo.nodes:
            if a.object_id==n:
                return True
        return False
    def handleConnessa(self,n):
        v0=self._idMap[n]
        return nx.node_connected_component(self._grafo, v0)
