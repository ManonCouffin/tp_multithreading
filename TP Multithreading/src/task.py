import json
import time
import numpy as np

# Définition de la classe Task
class Task:
    # Constructeur de la classe, initialisation des attributs
    def __init__(self, identifier, size = None):
        self.identifier = identifier  # Identifiant de la tâche
        self.size = np.random.randint(300, 3_000)  # Taille aléatoire de la tâche
        self.a = np.random.rand(self.size, self.size)  # Matrice aléatoire de taille (size x size)
        self.b = np.random.rand(self.size)  # Vecteur aléatoire de taille size
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
            "x": self.x.tolist(),
            "time": self.time,
        }
        return json.dumps(data)

    # Méthode de classe pour créer une instance de Task à partir d'une chaîne JSON
    @classmethod
    def from_json(cls, text: str) -> "Task":
        data = json.loads(text)
        task = cls(identifier=data["identifier"], size=data["size"])

        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]
        return task

    # Méthode spéciale pour comparer deux instances de Task
    def __eq__(self, other: "Task") -> bool:
        if not isinstance(other, Task):
            return False
        # Vérifie l'égalité des attributs de base (identifier, size, time)
        are_basic_attrs_equal = (
            self.identifier == other.identifier and
            self.size == other.size and
            self.time == other.time
        )

        if not are_basic_attrs_equal:
            return False

        # Vérifie l'égalité des matrices et vecteurs avec np.array_equal
        are_arrays_equal = (
            np.array_equal(self.a, other.a) and
            np.array_equal(self.b, other.b) and
            np.array_equal(self.x, other.x)
        )
        return are_arrays_equal
