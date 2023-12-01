#!/usr/bin/env python3

input_lines = open("2023/input/01.txt", "r").readlines()

print(
    "Part One",
    sum(
        [
            int(str(digits[0]) + str(digits[-1]))
            for digits in [
                list(filter(lambda k: k.isdigit(), line)) for line in input_lines
            ]
        ]
    ),
)


number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_word_lut = {word: str(digit) for digit, word in enumerate([None] + number_words)}


def pipe(value, *functions):
    accumulator = value
    for func in functions:
        accumulator = func(accumulator)
    return accumulator


def find(input, strings):
    result = [None for _ in range(len(input))]
    for check_str in strings:
        i = 0
        while True:
            idx = input.find(check_str, i)
            if idx < 0:
                break
            else:
                result[idx] = check_str
                i = idx + 1
    return [r for r in result if r]


print(
    "Part Two",
    sum(
        [
            pipe(
                line,
                lambda x: find(x, number_words + [str(d) for d in range(1, 10)]),
                lambda x: [dw if dw.isdigit() else number_word_lut[dw] for dw in x],
                lambda x: x[0] + x[-1],
                lambda x: int(x),
            )
            for line in input_lines
        ]
    ),
)
