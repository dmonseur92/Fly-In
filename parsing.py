from maps import Zone, StartZone, EndZone

def get_text_file(file: str) -> list[list[str]]:
    part_list: list[list[str]] = []
    try:
        with open(file) as f:
            for line in f:
                parts: list[str] = line.split()
                if not parts:
                    continue
                part_list.append(parts)
        triage(part_list)

    except Exception as e:
        print(e)


def triage(parts: list[list[str]]) -> None:
    for part in parts:
        if part[0] == "nb_drones:":
            print("nb_drones")
        if part[0] == "start_hub:":
            print("Start")
        elif part[0] == "hub:":
            print("Normal")
        elif part[0] == "end_hub:":
            print("End")
        else:
            print("0")


if __name__ == "__main__":
    get_text_file("maps/easy/01_linear_path.txt")
