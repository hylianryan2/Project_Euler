palindromes = []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if (str_product := str(i * j)) == str_product[::-1]:
            palindromes.append(int(str_product))

print(max(palindromes))
