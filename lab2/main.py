class DFA:
    def __init__(self):
        # Определяем таблицу переходов: {текущее состояние: {символ: следующее состояние}}
        self.transitions = {
            1: {'a': 2},
            2: {'b': 3},
            3: {'a': 4, 'c': 5},
            4: {'b': 3, 'c': 3},
            5: {}
        }
        self.start_state = 1  # Начальное состояние
        self.accept_states = {5}  # Множество терминальных состояний

    def recognize(self, input_string):
        state = self.start_state
        for char in input_string:
            if char in self.transitions[state]:
                state = self.transitions[state][char]
            else:
                return False  # Недопустимый символ или нет перехода
        return state in self.accept_states  # Проверяем, является ли состояние конечным


# Создаем экземпляр ДКА
dfa = DFA()

# Тестовые строки
test_strings = {
    "valid": [
        "abc",
        "ababacc",
        "abacc",
        "abababc"
    ],
    "invalid": [
        "",
        "abab",
        "cabac",
        "abacac"
    ]
}

print("Ожидаем, что принадлежит:")
for string in test_strings["valid"]:
    result = "принадлежит" if dfa.recognize(string) else "не принадлежит"
    print(f"Строка '{string}' {result} языку.")

print("\nОжидаем, что не принадлежит:")
for string in test_strings["invalid"]:
    result = "принадлежит" if dfa.recognize(string) else "не принадлежит"
    print(f"Строка '{string}' {result} языку.")
