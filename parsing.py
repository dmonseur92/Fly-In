from maps import Zone, Map, ZoneType

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
        return triage(part_list)

    except Exception as e:
        print(e)


def triage(parts: list[list[str]]) -> Map:
    new_map = Map()
    # print(parts)
    for part in parts:
        if part[0] == "nb_drones:":
            new_map.nbr_drones = int(part[1])
        elif part[0] == "hub:" or part[0] == "start_hub:" or part[0] == "end_hub:":
            parse_zone(part, new_map)
        elif part[0] == "connection:":
            new_map.connexion_list.append(part[1])

    check_connections(new_map)
    return new_map

def parse_zone(parts: list[str], map: Map) -> None:
    new_zone = Zone (
        name = parts[1],
        x = int(parts[2]),
        y = int(parts[3]),
        start = True if parts[0] == "start_hub:" else False,
        end = True if parts[0] == "end_hub:" else False,
    )
    parse_metadata(parts[4:], new_zone)
    map.zone_list.append(new_zone)


def parse_metadata(metadata: str, zone: Zone) -> None:
    data = []
    for d in metadata:
        data.append(d.strip("[]"))

    for d in data:
        key, value = d.split("=")
        if key == "color":
            zone.color = value
        elif key == "max_drones":
            zone.max_drones = int(value)
        elif key == "zone":
            zone.type = ZoneType(value.lower())
        else:
            raise ValueError(f"Invalid key {key}")
        # print(zone.name, zone.x, zone.y, zone.start, zone.end, zone.type, zone.color, zone.max_drones, )

def check_connections(map: Map) -> None:
    connexions = set()
    zone_names = [zone.name for zone in map.zone_list]

    for connexion in map.connexion_list:
        if connexion.count("-") != 1:
            raise ValueError(f"Invalid connexion: {connexion}")

        a, b = connexion.split("-")
        if not a or not b:
            raise ValueError(f"Missing connexion: {connexion}")
        if a not in zone_names or b not in zone_names :
            raise ValueError(f"Connexion for unknow zone: {connexion}")
        if connexion in connexions or f"{b}-{a}" in connexions:
            raise ValueError(f"Duplicate connexion: {connexion}")
        connexions.add(connexion)

    if not any(connexion.startswith("start-") or connexion.endswith("-start") for connexion in map.connexion_list):
        raise ValueError(f"Missing starting connexion")

    if not any(connexion.startswith("goal-") or connexion.endswith("-goal") for connexion in map.connexion_list):
        raise ValueError(f"Missing ending connexion")

if __name__ == "__main__":
    get_text_file("maps/medium/01_dead_end_trap.txt")
