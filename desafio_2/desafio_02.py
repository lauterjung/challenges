import os
from typing import Final
import json

# Constantes
msg_input_student_limit: Final[str] = "x = "
msg_input_arrival_time: Final[str] = "tempoChegada = "
msg_error_positive_int: Final[str] = "Digite um número inteiro positivo. Digite Enter para continuar..."
msg_error_arrival_time_input: Final[str] = "Formato incorreto. Siga o padrão [1, 2, ...]. Digite Enter para continuar..."
msg_warning_input: Final[str] = "O número do limite de alunos é maior que o vetor de tempo de chegada. " \
                                "Isso automaticamente cancela a aula."
msg_normal_class: Final[str] = "Aula normal."
msg_cancelled_class: Final[str] = "Aula cancelada."

# Funções
def input_student_limit() -> int:
    while True:
        os.system('cls')
        print(msg_input_student_limit, end="")
        user_input = input()

        try:
            int_input = int(user_input)
            if int_input < 0:
                print(msg_error_positive_int)
                continue
        except ValueError:
            print(msg_error_positive_int)
            input()
        else:
            return int(user_input)


def input_arrival_time() -> list:
    while True:
        os.system('cls')
        print(msg_input_arrival_time, end="")
        user_input = input()

        if user_input.isnumeric():
            print(msg_error_arrival_time_input)
            input()
            continue

        try:
            parsed_input = json.loads(user_input)
        except:
            print(msg_error_arrival_time_input)
            input()
        else:
            if(all([isinstance(item, float) or isinstance(item, int) for item in parsed_input])):
                return parsed_input
            else:
                print(msg_error_arrival_time_input)
                input()
                continue


def is_input_valid(student_limit: int, arrival_time: list) -> bool:
    if student_limit < len(arrival_time):
        return True
    else:
        return False


def class_status_1(student_limit: int, arrival_time: list) -> None:  # Método 1: loop
    punctual_students = 0
    for time in arrival_time:
        if time <= 0:
            punctual_students += 1
        if punctual_students >= student_limit:
            break

    if punctual_students < student_limit:
        print(msg_cancelled_class)
    else:
        print(msg_normal_class)


def class_status_2(student_limit: int, arrival_time: list) -> None:  # Método 2: sorted list
    arrival_time.sort()

    if arrival_time[student_limit] <= 0:
        print(msg_normal_class)
    else:
        print(msg_cancelled_class)

# Execução
def run_program():
    student_limit = input_student_limit()
    arrival_time = input_arrival_time()

    if is_input_valid(student_limit, arrival_time):
        # class_status_1(student_limit, arrival_time)
        class_status_2(student_limit, arrival_time)
    else:
        print(msg_warning_input)
        print(msg_cancelled_class)


run_program()
