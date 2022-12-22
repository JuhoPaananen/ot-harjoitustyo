import os
import unittest
from repositories.high_scores_repository import HighScoresRepository

dirname = os.path.dirname(__file__)

class TestHighScoresRepository(unittest.TestCase):
    def setUp(self):
        self.repository = HighScoresRepository("testi.csv")

    def test_high_scores_are_sorted_correctly(self):
        hs = self.repository.get_high_scores()

        self.assertEqual(hs[0], ["Paraspelaaja", "2000"])
        
    def test_eleventh_element_not_included_in_high_scores(self):
        hs = self.repository.get_high_scores()
        self.assertNotIn(["Ei_mukana_top10"," 0"], hs)

    def test_high_score_input_is_saved_to_file(self):
        temp_file_path = f"{dirname}/../data/newfile.csv"
        repository = HighScoresRepository("newfile.csv")
        repository.add_new_high_score("Huipputulos", 2135)
        hs = repository.get_high_scores()
        
        self.assertEqual(hs[0], ["Huipputulos", "2135"])
        os.remove(temp_file_path)