import os
from pathlib import Path
import csv

dirname = os.path.dirname(__file__)

class HighScoresRepository:
    """Huippupisteistä vastaava luokka
    """
    def __init__(self, filename):
        """Luokan konstruktori
        """
        data_file_path = f"{dirname}/../data/{filename}"
        self._file_path = data_file_path

    def get_high_scores(self) -> list:
        """Palauttaa listan tiedostosta luetuista huippupisteistä

        Returns:
            list: Huippupisteet
        """
        return self._read_scores()

    def add_new_high_score(self, name: str, score: int):
        """Lisää uuden pistetiedon tiedostoon

        Args:
            name (str): Pelaajan nimi
            score (int): Pelaajan pisteet
        """
        self._write_scores(name, score)

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read_scores(self) -> list:
        scores = []

        self._ensure_file_exists()

        with open(self._file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(row)

        file.close()

        scores.sort(key=lambda a: int(a[1]), reverse=True)

        return scores

    def _write_scores(self, name, score):
        new_score = name, score

        self._ensure_file_exists()

        with open(self._file_path, 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_score)

        file.close()
