from manager import QueueClient 
import time
from task import Task 

# Définit une classe Minion qui hérite de QueueClient.
class Minion(QueueClient):  
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            # Pause d'une seconde pour simuler l'attente d'une tache
            time.sleep(1)
            # Récupère une tache de la file d'attente des taches
            task = self.tasks.get()  
            # Exécute le travail associé à la tache et récupère le résultat
            result = task.work()  
            # Ajoute le résultat à la file d'attente des résultats
            self.results.put((task.x, task.time))  

if __name__ == "__main__":
    m = Minion()
    m.run()
