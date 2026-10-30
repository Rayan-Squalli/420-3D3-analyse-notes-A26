from models.cours import Cours

class Programme:
    def __init__(self, nom: str):
        self.nom = nom
        self.cours: list[Cours] = []

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

    def iter_etudiants(self):
        for cours in self.cours:
            yield from cours.iter_etudiants()

    def moyenne(self) -> float:
        etudiants = list(self.iter_etudiants())
        if not etudiants:
            return 0.0
        return round(sum(etudiant.moyenne() for etudiant in etudiants) / len(etudiants), 1)

    def nb_etudiants(self) -> int:
        return len(list(self.iter_etudiants()))

    def to_dict(self) -> dict:
        return {
            "type": "programme",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [cours.to_dict() for cours in self.cours]
        }
