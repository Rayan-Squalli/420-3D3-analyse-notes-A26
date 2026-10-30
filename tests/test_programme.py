import unittest

from donnees import construire_programme


class TestProgramme(unittest.TestCase):
    def test_iter_etudiants_compte_les_etudiants(self):
        programme = construire_programme()

        etudiants = list(programme.iter_etudiants())

        self.assertEqual(len(etudiants), 9)
        self.assertEqual(programme.nb_etudiants(), 9)

    def test_to_dict_conserve_la_structure_de_l_arbre(self):
        programme = construire_programme()

        arbre = programme.to_dict()

        self.assertEqual(arbre["type"], "programme")
        self.assertEqual(arbre["nom"], "Techniques de l'informatique")
        self.assertEqual(len(arbre["enfants"]), 2)
        self.assertEqual(arbre["moyenne"], programme.moyenne())
        self.assertEqual(arbre["nb_etudiants"], programme.nb_etudiants())


if __name__ == "__main__":
    unittest.main()
