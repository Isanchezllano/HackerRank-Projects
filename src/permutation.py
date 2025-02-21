from itertools import permutations


def permu (entrada):


    string = entrada[0]
    k = int(entrada[1])

    if len(string) >= k:
        perm = list(permutations(string, k))
        print(perm)


if __name__ == "__main__":
    permu(input().split())
