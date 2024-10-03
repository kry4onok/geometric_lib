import circle
import square

# Список доступных фигур
figs = ['circle', 'square']

# Список доступных функций (площадь и периметр)
funcs = ['perimeter', 'area']

# Словарь, который хранит количество параметров, необходимых для каждой комбинации функции и фигуры
sizes = {
    'perimeter-circle': 1,
    'area-circle': 1,
    'perimeter-square': 1,
    'area-square': 1
}


def calc(fig, func, size):
    """Вычисляет и выводит результат заданной функции для заданной фигуры.

    Args:
        fig (str): Название фигуры (доступные варианты: 'circle', 'square').
        func (str): Название функции (доступные варианты: 'perimeter', 'area').
        size (list): Список размеров фигуры, которые будут переданы в функцию.

    Returns:
        None: Ничего не возвращает, но выводит результат вычислений функции для фигуры.

    Example:
        >>> calc('circle', 'area', [10])
        area of circle is 314.1592653589793
    """
    assert fig in FIGS, f"Фигура {fig} недоступна. Доступные фигуры: {FIGS}"
    assert func in FUNCS, f"Функция {func} недоступна. Доступные функции: {FUNCS}"

    # В зависимости от фигуры, выбираем правильный модуль
    module = globals()[fig]
    
    # Получаем нужную функцию из модуля и вызываем её с параметрами
    result = getattr(module, func)(*size)

    print(f'{func} of {fig} is {result}')


def main():
    """Основная программа, которая взаимодействует с пользователем для ввода фигуры, функции и её размеров.

    Пользователю предлагается ввести фигуру, функцию и размеры, после чего программа вызовет соответствующую функцию
    и выведет результат.
    """
    func = ''
    fig = ''
    size = []

    # Запрашивает у пользователя фигуру до тех пор, пока не введена допустимая фигура
    while fig not in FIGS:
        fig = input(f"Enter figure name, available are {FIGS}:\n").strip()

    # Запрашивает у пользователя функцию до тех пор, пока не введена допустимая функция
    while func not in FUNCS:
        func = input(f"Enter function name, available are {FUNCS}:\n").strip()

    # Запрашивает у пользователя размеры фигуры до тех пор, пока не будет введено правильное количество аргументов
    expected_size = SIZES.get(f"{func}-{fig}", 1)
    while len(size) != expected_size:
        size_input = input(f"Input {expected_size} size(s) for {fig}, separated by space:\n")
        try:
            size = list(map(float, size_input.split()))
        except ValueError:
            print("Please enter valid numbers.")

    # Вызывает функцию calc для вычисления и вывода результата
    calc(fig, func, size)


if __name__ == "__main__":
    main()
