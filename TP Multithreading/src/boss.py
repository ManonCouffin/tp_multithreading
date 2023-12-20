import time
import queue
from manager import QueueClient
from task import Task

class Boss(QueueClient):  
    def __init__(self):
        super().__init__() 

    def submit_task(self, task_id, task_size):
        # Crée une nouvelle tâche avec l'ID et la taille spécifiés
        task = Task(task_id, task_size)  
        # Ajoute la tâche à la file de tâches du client
        self.tasks.put(task)  
        print(f"Le Boss a ajouté la tache {task_id} à la file.")  

    def run(self):
        while True:
            try:
                # Récupère un résultat de la file de résultats
                result_id, result_time = self.results.get_nowait()  
                print(f"Le Boss a récupéré le résultat {result_id} en {result_time} secondes.")
            except queue.Empty:
                print("La file est vide.")  
                # Pause de 5 secondes avant de vérifier à nouveau
                time.sleep(5)  
                continue

if __name__ == "__main__":
    boss = Boss() 
    id = 0
    while id != 31 :
        boss.submit_task(id, 3000)  # Soumet une tâche avec l'ID 0 et une taille de 3000
        id += 1
    boss.run()
