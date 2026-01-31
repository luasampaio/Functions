import random
import time
from pathlib import Path

ARQUIVO = Path("recursos/arquivo.txt")

def numero_aleatorio():
    num = random.randint(1, 95)
    print(num)

    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO.open("a", encoding="utf-8") as file:
        file.write(f"{num}\n")

def main():
    try:
        while True:
            numero_aleatorio()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExecução finalizada pelo usuário.")

if __name__ == "__main__":
    main()
