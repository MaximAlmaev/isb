import math

def freq_binary_test(arr: list) -> float:
    """
    Частотный тест для проверки случайности бинарных последовательностей.
    
    Args:
        arr (list): Массив бинарных значений (0 и 1) для тестирования
    
    Raises:
    ValueError: Генерирует исключение если последовательность пустая
    ValueError: Генерирует исключение если последовательность содержит какие-либо символы кроме "0" и "1"
    
    Returns:
    float: p-значение теста
    """

    try:
        if not arr:
            raise ValueError("Пустая последовательность")
        if not all(bit in {0, 1} for bit in arr):
            raise ValueError("Последовательность должна содержать только '0' и '1'")

        new_arr = [(2*x) - 1 for x in arr]
        norm_abs_sum = (abs(sum(new_arr)))/(math.sqrt(len(new_arr)))
        p_value = math.erfc(norm_abs_sum/(math.sqrt(2)))
        print(p_value)

    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    return p_value