import circle
import square
import triangle

# Определение доступных фигур и функций
figs = {
    "circle": {"module": circle, "params": 1},
    "square": {"module": square, "params": 1},
    "triangle": {"module": triangle, "params": 3},
}

funcs = ["perimeter", "area"]


def calc(fig, func, size):
    # Проверка наличия фигуры и функции
    if fig not in figs:
        raise ValueError(
            f"Фигура {fig} недоступна. Доступные фигуры: {list(figs.keys())}"
        )
    if func not in funcs:
        raise ValueError(f"Функция {func} недоступна. Доступные функции: {funcs}")

    # Проверка количества параметров
    num_params = figs[fig]["params"]
    if len(size) != num_params:
        raise ValueError(
            f"Ожидается {num_params} параметров для фигуры {fig}, получено {len(size)}"
        )

    # Проверка, что все размеры положительные
    if any(s <= 0 for s in size):
        raise ValueError("Все размеры должны быть положительными целыми числами")

    # Получение нужного модуля и функции
    module = figs[fig]["module"]
    func_to_call = getattr(module, func)

    # Вычисление результата
    result = func_to_call(*size)
    return f"{func.capitalize()} of {fig} with size(s) {size} is {result}"
