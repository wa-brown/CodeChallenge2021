import grid
import building
import antenna

def main():
    buildings = []
    antennas = []

    # load the file
    with open('data_scenarios_a_example.in', 'r') as reader:
        lines = reader.readlines()
        w, h = lines[0].strip().split(" ")
        g = grid.Grid(w, h)
        n, _, r = lines[1].strip().split(" ")
        for line in lines[2: int(n)]:
            x, y, latency, connection_speed = line.strip().split(" ")
            buildings.append(building.Building(x, y, latency, connection_speed))

        id = 0
        for line in lines[2+int(n):]:
            r, c = line.strip().split(" ")
            antennas.append(antenna.Antenna(id, r, c))
            id += 1

if __name__ == "__main__":
    main()