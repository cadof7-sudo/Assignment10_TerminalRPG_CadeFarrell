MAPS = {
    "village": [
        "###########",
        "#..E..M..G#",
        "#.###.##..#",
        "#...H....#",
        "###...####",
        "#..S.....#",
        "##########"
    ],
    "woods": [
        "#############",
        "#....#......#",
        "#.##.#.###..#",
        "#....#...#..#",
        "##.###.#.#.##",
        "#.....#.....#",
        "#.#####.###.#",
        "#.....D.....#",
        "#############"
    ]
}
# Symbols: # wall, E elder, M merchant, G guard, H healer, S seer, D dragon lair.

def display_map(player):
    layout = MAPS[player.map_name]
    px, py = player.position
    print(f"\n--- {player.map_name.upper()} ---")
    for y, line in enumerate(layout):
        row = list(line)
        if y == py and px < len(row):
            row[px] = "@"
        print("".join(row))
    print("@ You | # Wall | NPC letters mark places to visit")

def can_move(map_name, x, y):
    layout = MAPS[map_name]
    return 0 <= y < len(layout) and 0 <= x < len(layout[y]) and layout[y][x] != "#"

def symbol_at(player):
    x, y = player.position
    return MAPS[player.map_name][y][x]
