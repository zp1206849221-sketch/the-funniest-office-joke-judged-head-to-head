import os

JOKE = "My out-of-office reply is just 'Per my last email' — so I'm on vacation, and still undefeated in every argument at work."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
