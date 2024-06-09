
# def InsertionSort(A):
#     for i in range(1,len(A)):
#         num = A[i]
#         while i > 0 and A[i-1] > num:
#             A[i] = A[i-1]
#             i -= 1
#         A[i] = num

# nums = [1,4,3,2,4,5]
# InsertionSort(nums)
# print(nums)




# def InsertionSort(A):
#     n = len(A)
#     for i in range(n):
#         g = i
#         for j in range(i,n):
#             if A[j] > A[g]:
#                 g = j
#         A[i],A[g] = A[g],A[i]

# nums = [1,4,3,2,4,5]
# InsertionSort(nums)
# print(nums)



# def tovar(N, prices):
#     prices.sort(reverse=True) #сорт по убыв
#     total = sum(prices[:2])  #суммир 2 дорог товара
#     return total

# N = int(input("Введите количество товаров: "))
# prices = []
# for i in range(N):
#     price = int(input("Введите стоимость товара: "))
#     prices.append(price)

# print("Минимальная сумма денег, которую нужно взять с собой:", tovar(N, prices))







# def math(nums):
#     sorted_ = sorted(nums)
#     min_diff = float('inf')
#     list_ = []

#     for i in range(len(sorted_) - 1):
#         diff = abs(sorted_[i] - sorted_[i + 1])
#         if diff < min_diff:
#             min_diff = diff
#             list_ = [sorted_[i], sorted_[i + 1]]

#     return list_


# nums = [2, 7, 1, 10, 15, 3]
# list_ = math(nums)
# print("Два ближайших числа:", list_)



# def w(strings):
#     max_length = max(len(s) for s in strings)
#     align_strings = [(max_length - len(s)) * '*' + s for s in strings]
#     return align_strings

# M = int(input("Введите количество строк: "))
# strings = [input(f"Введите строку {i + 1}: ") for i in range(M)]
# align_strings = w(strings)
# print("\nстроки:")
# for t in align_strings:
#     print(t)





# def balance(arr):
#     pos_sum = sum(x for x in arr if x > 0)
#     neg_sum = sum(x for x in arr if x < 0)
    
#     r_sum = abs(neg_sum)#новый элеиент
#     new_element = r_sum - pos_sum
#     arr.append(new_element)
#     return arr

# N = int(input("Введите количество элементов в массиве: "))
# array = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]
# balanced_array = balance(array)
# print("Новый массив:",balanced_array)


import re

# def domains(email_list):

#     domain_pattern = re.compile(r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
#     domains = []
#     for email in email_list:
#         match = domain_pattern.search(email)
#         if match:
#             domains.append(match.group(1))
#     return domains


# email_list = [
#     "example1@gmail.com",
#     "example2@yahoo.com",
#     "example3@outlook.com",
#     "invalid-email",
#     "example4@example.com"
# ]

# a = domains(email_list)
# print(a)





# def words(word_list):
#     pattern = r'\b[AEIOUYaeiouyАЕЁИОУЫЭЮЯаеёиоуыэюя]\w*'
#     words = re.findall(pattern, word_list)
#     return words

# word_list = 'atletico madrid real madrid barcelona inter milan'
# a = words(word_list)
# print(a)




# import re

# def string(text):
#     reg = r'[ ,;:]'
#     # Разделение строки
#     parts = re.split(reg, text)
#     # Удаляет пустые строки, которые могут появиться из-за нескольких подряд идущих разделителей
#     parts = [part for part in parts if part]
#     return parts

# text = "дисциплина, работа; терпение: путь, к: упеху"
# split_parts = string(text)
# print(split_parts)
















