import numpy as np
from scipy.stats import norm

def con_ide_bits_test(arr) -> float:
    """
    Тест на одинаковые подряд идущие биты
    
    Args:
        arr (list): Массив бинарных значений
    
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
        n = len(arr)
        ones_count = sum(arr)
        pi = ones_count / n
        threshold = 2 / np.sqrt(n)
        condition = abs(pi - 0.5)
        if (condition > threshold):
            return -1
        
        if n == 0:
            return 0
        runs += 1 
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                runs += 1  

        expected_runs = 2 * n * pi * (1 - pi)
        variance = 2 * n * pi * (1 - pi) * (1 - 3*pi + 3*pi*pi)
        std_dev = np.sqrt(variance)
        z_statistic = (runs - expected_runs) / std_dev
        p_value = 2 * (1 - norm.cdf(abs(z_statistic)))
        print(p_value)
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    return p_value
    
