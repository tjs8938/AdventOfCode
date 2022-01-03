from src.day14.InputProcessor import process_file, part2

expected_results = {"test3.txt": 82892753,
                    "test4.txt": 5586022,
                    "test5.txt": 460664}

for file in expected_results:
    reactions = process_file(file)
    assert part2(reactions) == expected_results[file]

reactions = process_file("input.txt")
print(part2(reactions))
