def double_even_digits(original: str) -> str:
    result = ""
    for c in original:
        result += c
        if c in "02468":
            result += c
    return result
def main():
    n = int(input())
    for i in range(n):
        original = []
        line = input()
        tokens = line.split()
        for token in tokens:
            original.append(token)
        print(double_even_digits(line))
if __name__ == "__main__":
    main()
