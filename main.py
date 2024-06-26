from src.HH_api import HeadHunterAPI
from src.Json_saved import JSONSaver
from src.utils import get_filtered_list, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_top_vacancies
from src.vacancy import Vacancy
import os
from config import ROOT_DIR
file_path = os.path.join(ROOT_DIR, "data", "vacancies.json")


def main():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    min_salary = int(input("Введите минимальную зарплату: "))   #yes


    filtered_vacancies = get_filtered_list(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, min_salary)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_top_vacancies(top_vacancies, top_n)
    json_saver = JSONSaver(file_path)
    json_saver.save_to_file(top_vacancies)

if __name__ == "__main__":
    main()
