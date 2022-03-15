def delete_even_digits(lista: str) -> str:
    result = ""
    for c in lista:
        if c not in "02468":
            result += c
    return result
def main():
    while True:
        lista = []
        original = input()
        if original == "END":
            break
        tokens = original.split()
        for token in tokens:
           lista.append(token)
        print(delete_even_digits(original))
if __name__ == "__main__":
    main()