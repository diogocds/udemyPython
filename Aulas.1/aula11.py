# Prescedencia dos operadores ( ordem dos operadores )

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7
conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024

print(conta_1, 'e', conta_2)