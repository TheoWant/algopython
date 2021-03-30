# #1
# import math
# 
# nombre = int(input("entrez un nombre "))
# if nombre >= 0:
#     print(math.sqrt(nombre))
# else:
#     print("votre nombre est négatif")



# #2
# mot1 = input("entrez un premier mot  ")
# mot2 = input("entrez un second mot  ")
# 
# if mot1 > mot2:
#     print("le premier mot est plus long")
# elif mot2 > mot1:
#     print("le deuxieme mot est plus long")
# else:
#     print("les mots sont de meme longueur")



# #3
# pSeuil = 2.3
# vSeuil = 7.41
# 
# p = float(input('entrez la pression'))
# v = float(input('entrez le volume'))
# 
# if p > pSeuil and v > vSeuil:
#     print("arretez tout !") 
# elif p > pSeuil and v < vSeuil:
#     print("augmentez le volume")
# elif p < pSeuil and v > vSeuil:
#     print("diminuez le volume")
# else:
#     print("tout va bien")



# #4
# a = 0
# b = 10
# 
# while a < b:
#     a+=1
#     print(a)
# 
# while b > 0:
#     b-=1
#     if (b % 2) != 0:
#         print(b)

# #5
# n = int(input("Entrez un entier entre 1 et 10 "))
# while not(1 <= n <= 10):
#     n = int(input("Entrez un entier entre 1 et 10 "))
#     
# print("Valeur=", n)


# #7
# for i in range (1,15,3):
#     print(i)

# #8
# for i in range (1,11):
#     if i == 5:
#         break
# 
# print(i)

# #9
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i, end=" ")
# print()

#10

