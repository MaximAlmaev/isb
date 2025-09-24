from scipy import special

def longest_seq_test(arr: list, p_i: list, N: int, M: int) -> float:
    """Функция реализует тест NIST на самую длинную последовательность единиц в блоке
    Args:
        arr (list): Бинарная последовательность длиной 128

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
    
        num_of_blocks = N // M
        blocks = (arr[i * M:(i + 1) * M] for i in range(num_of_blocks))
        
        statistics = [0] * 4
        
        for block in blocks:  
            cur_n = 0          
            max_n = 0
            
            for num in block:
                if num == 1:
                    cur_n += 1
                    max_n = max(max_n, cur_n)
                else:
                    cur_n = 0
                    
            match max_n:
                case n if n <= 1:
                    statistics[0] += 1
                case 2:
                    statistics[1] += 1
                case 3:
                    statistics[2] += 1
                case _:
                    statistics[3] += 1 
        
        xi_square = 0
                
        for v, p in zip(statistics, p_i):
            xi_square += (v - 16 * p) ** 2 / (16 * p)
        
        p_value = (special.gammaincc(3/2, xi_square/2))
        print(p_value)
    
    except ValueError as e:
        print(f"Ошибка в данных: {e}")
        return -1
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return -1
    
    return p_value