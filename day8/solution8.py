def execute_program(program_name):
    with open(program_name, 'r') as file:
        registers = {}

        highest_value = 0

        def get(k):
            return int(registers.get(k, 0))

        operations = {
            # Comparisons.
            "<": lambda x, y: x < y,
            ">": lambda x, y: x > y,
            "<=": lambda x, y: x <= y,
            ">=": lambda x, y: x >= y,
            "!=": lambda x, y: x != y,
            "==": lambda x, y: x == y
        }

        def should_execute(vals):
            return operations[vals[1]](get(vals[0]), int(vals[2]))

        def parse_instruction(line):
            line_split = line.split(' ')

            return line_split[0], line_split[1], int(line_split[2]), should_execute(line_split[-3:])

        for line in file.readlines():
            reg, instruction, operand, execute = parse_instruction(line)
            if not execute:
                continue

            if instruction == "inc":
                registers[reg] = get(reg) + operand
            elif instruction == "dec":
                registers[reg] = get(reg) - operand

            max_cur = max(registers.values())

            if max_cur > highest_value:
                highest_value = max_cur

        print("Highest Value:", highest_value)

        return registers


print(execute_program('./input.txt'))
