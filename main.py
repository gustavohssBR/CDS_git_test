def gether_data():
    n1 = int(input("primeiro valor: "))
    n2 = int(input("segundo valor: "))

    return n1, n2

def print_message(n1, n2):
    print(f'os valores {n1} e {n2} somando dão: {n1+n2}')


def main():
    n1, n2 = gether_data()

    print_message(n1,n2)

    return None

if __name__ == "__main__":
    main()