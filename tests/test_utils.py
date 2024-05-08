import unittest

from src.utils import get_filtered_list, get_vacancies_by_salary, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy


class TestVacancyUtils(unittest.TestCase):
    def setUp(self):
        self.vacancies = [
            Vacancy(name='Python Developer', company_name='Company A', area='Area A', url='http://example.com', snippet_req='Python experience', salary_from=120000, salary_to=180000, currency='USD'),
            Vacancy(name='Data Scientist', company_name='Company B', area='Area B', url='http://example.com', snippet_req='Data analysis and Python', salary_from=None, salary_to=None, currency='USD'),
            Vacancy(name='Web Developer', company_name='Company C', area='Area C', url='http://example.com', snippet_req='JavaScript experience', salary_from=100000, salary_to=150000, currency='USD')
        ]

    def test_get_filtered_list(self):
        filtered = get_filtered_list(self.vacancies, ['Python'])
        self.assertEqual(len(filtered), 2)  # Проверяем фильтрацию по ключевому слову 'Python'

    def test_get_vacancies_by_salary(self):
        filtered = get_vacancies_by_salary(self.vacancies, 70000)
        self.assertEqual(len(filtered), 2)

    def test_sort_vacancies(self):
        sorted_vacancies = sort_vacancies(self.vacancies)
        self.assertTrue(all(sorted_vacancies[i].salary_from >= sorted_vacancies[i+1].salary_from for i in range(len(sorted_vacancies) - 1) if sorted_vacancies[i+1].salary_from is not None))

    def test_get_top_vacancies(self):
        top_vacancies = get_top_vacancies(self.vacancies, 2)
        self.assertEqual(len(top_vacancies), 2)  # Проверяем, что возвращаются только две топ вакансии

if __name__ == '__main__':
    unittest.main()
    unittest.main()