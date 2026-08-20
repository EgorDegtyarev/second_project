import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env в окружение
load_dotenv()

def print_author():
    # Читаем значение из AUTHOR и присваиваем переменной author
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

# Вызываем функцию для проверки работы
if __name__ == "__main__":
    print_author()
