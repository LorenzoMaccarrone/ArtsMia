import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumNodi()} nodi e {self._model.getNumArchi()}"))
        self._view.update_page()


    def handleCompConnessa(self,e):
        nMinStr = self._view._txtIdOggetto.value
        try:
            nMin = int(nMinStr)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Il valore inserito nel campo non è un intero."))
            self._view.update_page()
            return
        if self._model.checkExistance(nMin):
            connessa = self._model.handleConnessa(nMin)
            self._view.txt_result.controls.append(ft.Text(f"la componente connessa ha {len(connessa)} nodi"))
            for c in connessa:
                self._view.txt_result.controls.append(ft.Text(f"{c}"))
            self._view.update_page()


        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Valore non trovato"))
            self._view.update_page()
            return



