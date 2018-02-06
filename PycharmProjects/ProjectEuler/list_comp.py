n = int(input())
does_list = {i for i in range(2, n) if n % i == 0}
print(does_list)
prime_list = []
for factor in does_list:
    for i in range(2, factor):
            if factor % i == 0:
                break
    else:
            prime_list.append(factor)
print(prime_list)



                                



