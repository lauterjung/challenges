# Funções
def x_to_reverse_number(x: int) -> int:
    string_x = str(x)
    reverse_string_x = string_x[::-1]
    return int(reverse_string_x)

def check_all_odd_digits(x: int) -> bool:
    string_x = str(x)
    for digit in string_x:
        if int(digit) % 2 == 0:
            return False
    return True

# Execução
end = 1000000
result_list = []

for x in range(11, end-1):
    string_number = str(x)
    end_number = string_number[len(string_number)-1]
    
    if end_number == "0":
        continue

    reverse_x = x_to_reverse_number(x)
    result = x + reverse_x

    if check_all_odd_digits(result) == True:
        result_list.append(f"{x} + {reverse_x} = {result}")

print("\n".join(result_list))
print(f"Existem {len(result_list)} números com essa propriedade de 1 até {end}")

# Output .txt
output_file = open("output_01b.txt", "w")
output_file.write("\n".join(result_list))
output_file.write(f"\nExistem {len(result_list)} números com essa propriedade de 1 até {end}")
output_file.close()