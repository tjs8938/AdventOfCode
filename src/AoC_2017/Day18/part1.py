from src.AoC_2017.Day18.DuetAssemblyComputer import DuetAssemblyComputer


def recover_frequency(filename: str) -> int:

    duet = DuetAssemblyComputer(open(filename).read().splitlines())
    duet.execute()

    return duet.played_sounds[-1]

# assert(recover_frequency("test1.txt") == 4)
recover_frequency("input.txt")
