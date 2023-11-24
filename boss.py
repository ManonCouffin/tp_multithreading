import time
from task import Task

class Boss:
    def run(self):
        i = 1
        while True:
            # Création d'une nouvelle tâche avec l'itération actuelle comme argument
            t = Task(i)  
            # Ajout de la tâche à la file d'attente des tâches
            self.tasks.put(t)  
            # Pause de 4 secondes pour simuler le traitement d'une tâche
            time.sleep(4)  

            # Récupération du résultat de la tâche traitée
            result = self.results.get()  

            print("Le Boss a récupéré le résultat " + str(result[0]) + " en " + str(result[1]) + " secondes.")
            i += 1

if __name__ == "__main__":
    b = Boss()
    b.run()

    