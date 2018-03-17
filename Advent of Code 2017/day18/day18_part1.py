def get_proper_value(operand):
    operand = operand.strip()

    try:
        return int(operand)
    except:
        return operand

def single_operand(instruction):
    return (get_proper_value(instruction[4:]))

def double_operand(instruction):
    operands = instruction[4:].split(" ")

    return (get_proper_value(operands[0]), get_proper_value(operands[1]))

def parse_instruction(instruction):
    instruction = instruction.strip()

    mneumonic = instruction[:3].strip()
    if mneumonic in ["snd", "rcv"]:
        return (mneumonic, single_operand(instruction))
    else:
        return (mneumonic, double_operand(instruction))

class AssemblyExecutor:
    def __init__(self, instructions):
        self._insts = [parse_instruction(inst) for inst in instructions]
        self._registers = {}
        self._inst_ptr = 0

        self._sounds = []
        self._recovers = []

    def get_default(self, op):
        if op not in self._registers.keys():
            self._registers[op] = 0
        return self._registers[op]

    def get(self, op):
        return op if isinstance(op, int) \
            else self.get_default(op)

    def snd(self, X):
        self._sounds.append(self.get(X))

    def set(self, X, Y):
        self._registers[X] = self.get(Y)

    def add(self, X, Y):
        self.set(X, self.get(X) + self.get(Y))

    def mul(self, X, Y):
        self.set(X, self.get(X) * self.get(Y))

    def mod(self, X, Y):
        self.set(X, self.get(X) % self.get(Y))

    def rcv(self, X):
        if self.get(X) == 0:
            return

        last_freq = self._sounds[len(self._sounds)-1]

        if len(self._recovers) == 0:
            print("First Recovered Frequency:", last_freq)

        self._recovers.append(last_freq)

    def jgz(self, X, Y):
        if self.get(X) <= 0:
            return
        
        self._inst_ptr += self.get(Y) - 1 # minus one so when ptr incrememnt goes to desired inst.

    def execute(self):
        while 0 <= self._inst_ptr < len(self._insts):
            instruction, payload = self._insts[self._inst_ptr]

            if not hasattr(self, instruction):
                raise Exception(("Bad instruction name %s") % payload)
            getattr(self, instruction)(*payload)

            self._inst_ptr += 1

        print(self._registers)
        print(self._sounds)
        print(self._recovers)

# Answer to part 1.
with open('input.txt', 'r') as f:
    AssemblyExecutor(f.readlines()).execute()