import schedule
import time

# Функция для сбора данных и проверки цены по квери
def collect_data(query):
    # Код для сбора данных и проверки цены по квери
    print(f"Сбор данных и проверка цены для квери: {query}")

# Функция для выполнения задачи по расписанию
def run_task():
    # Список квери
    queries = ["квери1", "квери2", "квери3"]  # Заменить на свои квери

    for query in queries:
        collect_data(query)

# Запуск задачи по расписанию
schedule.every(1).hour.do(run_task)  # Можно изменить интервал выполнения задачи

# Бесконечный цикл для выполнения задачи
while True:
    schedule.run_pending()
    time.sleep(1)
