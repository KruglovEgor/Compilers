def ll1_parser(input_string):
    parse_table = {
        'S': {'a': ['a', 'S_1']},
        'S_1': {'a': ['a'], 'b': ['b', 'A', 'C'], 'c': ['c', 'A', 'B']},
        'B': {'b': ['b', 'B_1']},
        'B_1': {'a': ['a', 'b', 'B_1'], 'b': ['B', 'b', 'B_1'], 'c': ['c']},
        'A': {'a': ['a', 'A_1'], 'b': ['b', 'B']},
        'A_1': {'a': ['A', 'A'], 'b': ['A', 'A'], 'c': ['C', 'C']},
        'C': {'c': ['c', 'C_1']},
        'C_1': {'a': ['a'], 'c': ['C']}
    }

    stack = ['$', 'S']
    input_string = list(input_string) + ['$']
    pointer = 0

    print(f"Parsing '{''.join(input_string[:-1])}':")

    while stack:
        top = stack[-1]
        current_input = input_string[pointer]

        print(f"Stack: {stack}, Input: {input_string[pointer:]}")

        # Если верхний символ — терминал или конец строки
        if top in {'a', 'b', 'c', '$'}:
            if top == current_input:
                if top == '$':
                    print("Success! Input accepted.")
                    return True
                stack.pop()
                pointer += 1
            else:
                # Ошибка: промах по терминалу
                print(f"Error: Expected '{top}', but found '{current_input}' at position {pointer}")
                return False

        # Если верхний символ — нетерминал
        elif top in parse_table:
            if current_input in parse_table[top]:
                stack.pop()
                production = parse_table[top][current_input]
                # Добавляем правило в стек в обратном порядке
                for symbol in reversed(production):
                    stack.append(symbol)
            else:
                # Ошибка: промах по нетерминалу
                expected = list(parse_table[top].keys())
                print(
                    f"Error: No rule for '{top}' with input '{current_input}' at position {pointer}. Expected one of {expected}")
                return False
        else:
            print(f"Error: Unknown symbol '{top}' in stack")
            return False

    print("Error: Stack not empty after input exhaustion")
    return False


# Тестирование
positive_cases = [
    "aa",
    "abacaccaca",
    "acbbcbabc"
]

negative_cases = [
    "abcc",
    "acaab",
    "abc"
]

print("Testing positive cases:")
for test in positive_cases:
    ll1_parser(test)
    print("---------------------------------")

print("\nTesting negative cases:")
for test in negative_cases:
    ll1_parser(test)
    print("---------------------------------")