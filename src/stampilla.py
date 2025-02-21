n=int(input())
stamps=list(input().split())

if len(stamps) ==n:
    if len(stamps) > 0 and len(stamps)<1000:
        countrys=set(stamps)
        print(len(countrys))

#Código menos legible, pero optimizando los pasos, igual le hace falta la comprobacion del rango dentro de los parámetros 0 y 1000
distinct_country = set()

for _ in range(int(input())):
    country = input()
    distinct_country.add(country)

print(len(distinct_country))
