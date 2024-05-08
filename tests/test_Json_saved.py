# Для тестирования напишем код на Python, создав фиктивные объекты Vacancy и используя класс JSONSaver для сохранения и загрузки
test_code = """
import json

# Используем классы из предоставленных файлов
class Vacancy:
    def __init__(self, name, company_name, area, url, snippet_req, salary_from, salary_to, currency):
        self.name = name
        self.company_name = company_name
        self.area = area
        self.url = url
        self.snippet_req = snippet_req
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

class JSONSaver:
    def __init__(self, file_path):
        self.filename = file_path

    def save_to_file(self, vacancies):
        vacancy_dicts = [vars(vacancy) for vacancy in vacancies]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(vacancy_dicts, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            vacancy_dicts = json.load(f)
        return [Vacancy(**vacancy_dict) for vacancy_dict in vacancy_dicts]

# Создаем тестовые объекты Vacancy
vacancies = [
    Vacancy("Software Engineer", "Google", "Mountain View", "http://google.com", "Experience with Python", 100000, 150000, "USD"),
    Vacancy("Product Manager", "Apple", "Cupertino", "http://apple.com", "Experience with product development", 120000, 180000, "USD")
]

# Сохраняем в файл
saver = JSONSaver('test_vacancies.json')
saver.save_to_file(vacancies)

# Загружаем из файла
loaded_vacancies = saver.load_from_file()

# Проверяем, что загруженные данные соответствуют исходным
assert len(loaded_vacancies) == len(vacancies)
for original, loaded in zip(vacancies, loaded_vacancies):
    assert original.name == loaded.name
    assert original.company_name == loaded.company_name
    assert original.area == loaded.area
    assert original.url == loaded.url
    assert original.snippet_req == loaded.snippet_req
    assert original.salary_from == loaded.salary_from
    assert original.salary_to == loaded.salary_to
    assert original.currency == loaded.currency


# Записываем и выполняем тестовый код
exec(test_code)
