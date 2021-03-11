import building
import antenna

def main():
    fileName = 'data_scenarios_a_example.in'
    buildings = []
    antennas = []

    # load the file
    with open(fileName, 'r') as reader:
        lines = reader.readlines()
        w, h = lines[0].strip().split(" ")
        grid = [[0]* int(w) for _ in range(int(h))]
        n, _, r = lines[1].strip().split(" ")
        for line in lines[2: int(n)]:
            x, y, latency, connection_speed = line.strip().split(" ")
            buildings.append(building.Building(x, y, latency, connection_speed))
            grid[int(y)][int(x)] = 1
        id = 0
        for line in lines[2+int(n):]:
            r, c = line.strip().split(" ")
            antennas.append(antenna.Antenna(id, r, c))
            id += 1

    # process
    antennas = process(h, w, grid, antennas)
    for a in antennas:
        print(a.x)

    # output
    outfile = fileName.split('.')[0] + '.out'
    with open(outfile, 'w') as writer:
        writer.write(f'{len(antennas)}\n')
        for an in antennas:
            writer.write(f'{an.id} {an.x} {an.y}\n')


def process(h, w, grid, antennas):
    count = 0
    for y in range(int(h)):
        for x in range(int(w)):
            if count > len(antennas):
                return antennas
            if grid[y][x] is 1:
                antennas[count].set_coords(x, y)
                count += 1
    return antennas

if __name__ == "__main__":
    main()