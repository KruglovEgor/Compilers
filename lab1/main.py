def simulate_dfa(input_str):
    """
    Моделирует работу ДКА для языка с нечетным числом вхождений подстроки 'ab'
    Алфавит: {a, b, c}

    Состояния:
      S0: чётное число 'ab', нет подвешенного 'a'
      S1: чётное число 'ab', есть подвешенное 'a'
      S2: нечетное число 'ab', нет подвешенного 'a'
      S3: нечетное число 'ab', есть подвешенное 'a'

    Допускающие состояния: S2 и S3
    """
    # Начальное состояние: S0
    state = 'S0'

    # Переходы
    transitions_dic = {
        'S0': {
            'a': 'S1',
            'b': 'S0',
            'c': 'S0'
        },
        'S1': {
            'a': 'S1',
            'b': 'S2',
            'c': 'S0'
        },
        'S2': {
            'a': 'S3',
            'b': 'S2',
            'c': 'S2'
        },
        'S3': {
            'a': 'S3',
            'b': 'S0',
            'c': 'S2'
        }
    }

    # Допускающие состояния
    exit_states = ('S2', 'S3')

    for ch in input_str:
        possible_transitions = transitions_dic[state]
        if ch in possible_transitions:
            state = possible_transitions[ch]
        else:
            # Неизвестный символ (не из нашего алфавита)
            return False

    return state in exit_states


# Тестирование автомата
test_strings = {
    "valid": [
        "ab",
        "cab",
        "aab",
        "ababab"
    ],
    "invalid": [
        "",
        "abab",
        "acabcab",
        "acac"
    ]
}

print("Тестирование корректных цепочек:")
for s in test_strings["valid"]:
    result = simulate_dfa(s)
    print(f'"{s}" -> {result}')

print("\nТестирование некорректных цепочек:")
for s in test_strings["invalid"]:
    result = simulate_dfa(s)
    print(f'"{s}" -> {result}')
