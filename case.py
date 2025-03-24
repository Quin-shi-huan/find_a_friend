class Algo:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc__type, exc_val, exc_tb):
        print("Estou saindo")

with Algo() as something:
    print("estou no meio")
