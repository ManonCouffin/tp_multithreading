import json
import time
import numpy as np

# Définition de la classe Task
class Task:
    # Constructeur de la classe, initialisation des attributs
    def __init__(self, identifier, size = None, a = None, b=None):
        self.identifier = identifier  # Identifiant de la tâche
        self.size = size or np.random.randint(300, 3_000)  # Taille aléatoire de la tâche
        
        self.a = a or np.random.rand(self.size, self.size)  # Matrice aléatoire de taille (size x size)
        self.b = b or np.random.rand(self.size)  # Vecteur aléatoire de taille size
        self.x = np.zeros((self.size))  # Vecteur résultant initialisé à zéros
        self.time = 0  # Temps de calcul initialisé à zéro

    # Méthode pour effectuer le travail de la tâche
    def work(self):
        start = time.perf_counter()  # Enregistre le temps de début
        self.x = np.linalg.solve(self.a, self.b)  # Résout le système linéaire Ax = B
        self.time = time.perf_counter() - start  # Calcule le temps écoulé pour la résolution

    # Méthode pour convertir l'objet en format JSON
    def to_json(self) -> str:
        data = {
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),  # Ajoutez cette ligne pour inclure le vecteur x
            "time": self.time  # Ajoutez cette ligne pour inclure le temps
        }
        return json.dumps(data)

    # Méthode de classe pour créer une instance de Task à partir d'une chaîne JSON
    @classmethod
    def from_json(cls, text: str) -> "Task":
        data = json.loads(text)
        task = cls(identifier=data["identifier"], size=data["size"], a=data["a"], b=data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]
        return task

    def eq(self, t):
        if isinstance(t, Task):
            if np.array_equal(self.a, t.a) and np.array_equal(self.b, t.b):
                return True
        return False
    
if __name__ == "__main__":
    print("test unitaire a==b (True)")
    a = Task("000")
    txt = a.to_json()
    b = Task.from_json(txt)
    print(a == b)
    print("test unitaire a==c (False)")
    c = Task("001")
    print(a == c)
