# Funções
def x_to_reverse_number(x: int) -> int:
    string_x = str(x)
    reverse_string_x = string_x[::-1]
    return int(reverse_string_x)

# Execução
end = 1000000
result_list = []

for i in range(11, end-1):
    string_number = str(i)
    start_number = int(string_number[0])
    end_number = int(string_number[len(string_number)-1])

    if end_number == 0:
        continue

    if ((start_number + end_number) % 2) != 0:
        reverse_i = x_to_reverse_number(i)
        result_list.append(f"{i} + {reverse_i} = {i + reverse_i}")

print("\n".join(result_list))
print(f"Existem {len(result_list)} números com essa propriedade de 1 até {end}")

# Output .txt
output_file = open("output_01a.txt", "w")
output_file.write("\n".join(result_list))
output_file.write(f"\nExistem {len(result_list)} números com essa propriedade de 1 até {end}")
output_file.close()