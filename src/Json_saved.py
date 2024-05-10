import json
from src.vacancy import Vacancy
from abc import ABC, abstractmethod


class AbstractJsonSave(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def load_from_file(self):
        pass


class JSONSaver(AbstractJsonSave):
    def __init__(self, file_path):
        super().__init__()
        self.filename = file_path

    def save_to_file(self, vacancies):
        # Преобразуем каждый объект Vacancy в словарь
        vacancy_dicts = [vars(vacancy) for vacancy in vacancies]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(vacancy_dicts, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            vacancy_dicts = json.load(f)

        # Преобразуем словари обратно в объекты Vacancy
        vacancies = [Vacancy(**vacancy_dict) for vacancy_dict in vacancy_dicts]
        return vacancies
