from src.day14.InputProcessor import process_file, part1

expected_results = {"test1.txt": 31,
                    "test2.txt": 165,
                    "test3.txt": 13312,
                    "test4.txt": 180697,
                    "test5.txt": 2210736}

for file in expected_results:
    reactions = process_file(file)
    assert part1(reactions) == expected_results[file]

reactions = process_file("input.txt")
part1(reactions)
