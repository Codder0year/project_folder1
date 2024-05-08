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

    def __str__(self):
        return (f'\nНазвание: {self.name}'
                f'\nКомпания: {self.company_name}'
                f'\nРегион: {self.area}'
                f'\nСсылка: {self.url}'
                f'\nЗарплата: {self.salary_from}-{self.salary_to} {self.currency}'
                f'\nОписание: {self.snippet_req}')

    @staticmethod
    def cast_to_object_list(hh_vacancies):
        """
        собираем по ключам ссылки
        сортируем что бы были только с указанными зп
        :param hh_vacancies:
        :return:
        """
        vacancies = []
        for vacancy_data in hh_vacancies:
            name = vacancy_data.get('name', 'Не указано')
            area = vacancy_data.get('area', {}).get('name', 'Не указано')
            company = vacancy_data.get('employer', {}).get('name', 'Не указано')
            url = vacancy_data.get('url', 'Ссылка не доступна')
            snippet_req = vacancy_data.get('snippet', {}).get('requirement', 'Описание не доступно')
            salary_data = vacancy_data.get('salary')

            # Проверяем наличие данных о зарплате
            if salary_data:
                salary_from = salary_data.get('from', '')
                salary_to = salary_data.get('to', '')
                currency = salary_data.get('currency', '')

                # Пропускаем вакансию, если хотя бы одно из значений зарплаты отсутствует
                if salary_from is None or salary_to is None or currency is None:
                    continue
            else:
                # Пропускаем вакансию, если данные о зарплате отсутствуют
                continue

            vacancy = Vacancy(name, company, area, url, snippet_req, salary_from, salary_to, currency)
            vacancies.append(vacancy)

        return vacancies
