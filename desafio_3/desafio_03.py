import itertools
import os
from typing import Final
import json

# Constantes
msg_input_target_number: Final[str] = "N = "
msg_input_vector_of_numbers: Final[str] = "V = "
msg_error_number: Final[str] = "Digite um número. Digite Enter para continuar..."
msg_error_vector_of_numbers_input: Final[str] = "Formato incorreto. Siga o padrão [1, 2, ...]. Digite Enter para continuar..."

# Funções
def input_target_number() -> int:
    while True:
        os.system('cls')
        print(msg_input_target_number, end="")
        user_input = input()

        try:
            int_input = float(user_input)
        except ValueError:
            print(msg_error_number)
            input()
        else:
            return float(user_input)


def input_vector_of_numbers() -> list:
    while True:
        os.system('cls')
        print(msg_input_vector_of_numbers, end="")
        user_input = input()

        if user_input.isnumeric():
            print(msg_error_vector_of_numbers_input)
            input()
            continue

        try:
            parsed_input = json.loads(user_input)
        except:
            print(msg_error_vector_of_numbers_input)
            input()
        else:
            if(all([isinstance(item, float) or isinstance(item, int) for item in parsed_input])):
                return parsed_input
            else:
                print(msg_error_vector_of_numbers_input)
                input()
                continue


def remove_duplicates(list_of_vectors: list) -> list[list]:
    result = []
    for combination in list_of_vectors:
        new_list = list(combination)
        new_list.sort()
        if new_list not in result:
            result.append(new_list)
    return result


def create_vector_combination(vector: list, size: int) -> list[tuple]:
    unique_vector = list(set(vector))
    list_of_vectors = []
    for i in range(size):
        list_of_vectors.append(unique_vector)
    vector_combinations = itertools.product(*list_of_vectors)
    return(vector_combinations)


def sum_of_vector(vector_of_numbers: list) -> float:
    total = 0
    for value in vector_of_numbers:
        total = total + value
    return total


def find_answer(target_number: int, vector_of_numbers: list) -> list[list]:
    count = 1

    while True:
        print(count)
        vector_combination = create_vector_combination(vector_of_numbers, count)
        potential_solutions = []

        for i, vector in enumerate(vector_combination):
            sum = sum_of_vector(list(vector))
            absolute_difference = abs(target_number - sum)

            if i == 0:
                minimum_difference = absolute_difference
            if absolute_difference > minimum_difference:
                continue
            elif absolute_difference == minimum_difference:
                potential_solutions.append(vector)
            else:
                potential_solutions = []
                potential_solutions.append(vector)
                minimum_difference = absolute_difference

        if count == 1:
            first_minimum_difference = minimum_difference
            second_minimum_difference = minimum_difference
            solutions = potential_solutions
            count += 1
            continue

        if minimum_difference == 0:
            return remove_duplicates(potential_solutions)

        second_minimum_difference = minimum_difference
        if second_minimum_difference >= first_minimum_difference:
            return remove_duplicates(solutions)

        first_minimum_difference = minimum_difference
        solutions = potential_solutions
        count += 1

# Execução
def run_program():
    target_number = input_target_number()
    vector_of_numbers = input_vector_of_numbers()
    all_answers = find_answer(target_number, vector_of_numbers)
    os.system('cls')
    print(target_number)

    for answer in all_answers:
        print(answer)


run_program()
