import pytest

# @pytest.mark.parametrize("name_of_parameter", ["value 1", "value 2", "value 3"])
# def test_numbers(name_of_parameter): # Имя параметра прокидывается в качестве аргумента тестового метода
#     print(name_of_parameter) # Все как в функциях, просто используем прокинутый аргумент

# @pytest.mark.parametrize(
#     "имя_параметра_1, имя_параметра_2", [ # Параметры
#         (значение_параметра_1, значение_параметра_2), # Первый тест
#         (значение_параметра_1, значение_параметра_2), # Второй тест
#         (значение_параметра_1, значение_параметра_2)  # Третий тест
#     ]
# )
# def test_print_people():
#     print()

@pytest.mark.parametrize(
    "number", [
        "One",
        "Two",
        "Three",
        "Four",
        "Five"
    ]
)
def test_numbers(number):
    print(number)
