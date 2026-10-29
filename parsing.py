from maps import Zone, Map

def get_text_file(file: str) -> list[list[str]]:
    part_list: list[list[str]] = []
    try:
        with open(file) as f:
            for line in f:
                parts: list[str] = line.split()
                if not parts:
                    continue
                part_list.append(parts)
        # print(part_list)
        triage(part_list)

    except Exception as e:
        print(e)


def triage(parts: list[list[str]]) -> None:
    new_map = Map()
    for part in parts:
        if part[0] == "nb_drones:":
            new_map.nbr_drones = int(part[1])
            print(new_map.nbr_drones)
        if part[0] == "hub:" or part[0] == "start_hub:" or part[0] == "end_hub:":
            parse_zone(part, new_map)

def parse_zone(parts: list[str], map: Map) -> None:
    new_zone = Zone (
        name = parts[1],
        x = int(parts[2]),
        y = int(parts[3]),
        start = True if parts[0] == "start_hub:" else False,
        end = True if parts[0] == "end_hub:" else False,
    )
    map.zone_list.append(new_zone)
    for zone in map.zone_list:
        print(zone.name)

# def parse_start(zone: list[str]) -> None:

# def parse_end(zone: list[str]) -> None:


if __name__ == "__main__":
    get_text_file("maps/easy/01_linear_path.txt")
