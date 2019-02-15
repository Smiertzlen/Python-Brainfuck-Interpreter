# Development
# To be added:
#  - Proper comments in the description and code
#  - Usable Console interpretation

from __future__ import print_function

class Memory():
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = 0

    def left(self):
        if not self.left:
            self.left = Memory(None, self)
        return self.left

    def right(self):
        if not self.right:
            self.right = Memory(self, None)
        return self.right

    def read(self, val):
        self.value = val

    def print(self):
        print(self.value)

    def inc(self):
        self.value = (self.value + 1) % 256

    def dec(self):
        self.value = (self.value - 1) % 256



def run(file, input):
    op_string = ''
    with open(file) as f:
        operation = ',.<>[]+-'
        read = f.read(1)
        while read:
            if read in operation:
                op_string += read
            read = f.read(1)
    # op_string enthält nun alle operationen aus der Datei


    index = 0
    pointer = 0
    loop_index = []
    memory = [0]
    input_index = 0

    # kann verbesser werden mit collections.deque (DLL!)

    while index < len(op_string):
        if op_string[index] == '<':
            pointer -= 1
            index += 1
            continue
        if op_string[index] == '>':
            pointer += 1
            index += 1
            continue



        # an diesem Punkt muss der Speichereintrag, an den pointer zeigt, existieren
        if pointer < 0:
            memory = ([0]*abs(pointer)) + memory
            pointer = 0
        else:
            if pointer >= len(memory):
                memory += ([0]*(pointer - len(memory) + 1))


        if op_string[index] == '[':
            if memory[pointer]:
                loop_index.append(index)
                index += 1
                continue
            # in this case, the loop will not be executed. Increase until found the corresponding ']
            depth = 1
            index += 1
            while depth:
                if op_string[index] == '[':
                    depth += 1
                else:
                    if op_string[index] == ']':
                        depth -= 1
                index += 1
            continue

        if op_string[index] == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
            index += 1
            continue
        if op_string[index] == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
            index += 1
            continue
        if op_string[index] == ']':
            if memory[pointer]:
                index = loop_index.pop()
            else:
                loop_index.pop()
                index += 1
            continue
        if op_string[index] == '.':
            print(memory[pointer])
            index += 1
            continue
        if op_string[index] == ',':
            if input_index >= len(input):
                exit(1)
            memory[pointer] = ord(input[input_index]) % 256
            input_index += 1
            index += 1
            continue

    print('Done
    if pointer < 0:
        memory = [0]*abs(pointer) + memory
        pointer = 0
    if pointer >= len(memory):
        memory.extend([0]*(pointer - len(memory) + 1))
        
    print(memory)
    test = [0]*len(memory)
    test[pointer] = 1
    print(test)

