import unittest
from src.HH_api import HeadHunterAPI

class TestHeadHunterAPI(unittest.TestCase):
    def test_initialization(self):
        """Тестирование инициализации параметров API."""
        api = HeadHunterAPI()
        self.assertEqual(api.url, 'https://api.hh.ru/vacancies')
        self.assertEqual(api.headers, {'User-Agent': 'HH-User-Agent'})
        self.assertEqual(api.params, {'text': '', 'page': 0, 'per_page': 100})

    def test_get_vacancies(self):
        """Тестирование получения вакансий. Проверка на непустой результат."""
        api = HeadHunterAPI()
        results = api.get_vacancies('Python')
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)  # Проверяем, что список не пустой


if __name__ == '__main__':
    unittest.main()