import building
import antenna

def main():
    buildings = []
    antennas = []

    # load the file
    with open('scenarios/data_scenarios_simplest_example.in', 'r') as reader:
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
    print(grid)
    for an in antennas:
        print("hello")

        

def process(antennas):
    return antennas

if __name__ == "__main__":
    main()