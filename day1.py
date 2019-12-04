def part1(s):
    masses = set(map(int, s.split()))
    tot_fuel = set(map(lambda x: x//3 - 2, masses))
    return sum(tot_fuel)

def part2(s):
    masses = set(map(int, s.split()))
    tot_fuel = 0
    for m in masses:
        while m//3 > 1:
            tot_fuel += m//3 - 2
    return tot_fuel
