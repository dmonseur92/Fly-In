def get_text_file(file: str):
    try:
        with open(file) as f:
            for line in f:
                parts = line.split()
                if not parts:
                    continue
                print(parts)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    get_text_file("maps/easy/01_linear_path.txt")
