from typing import Callable


class TuringMachine:

    def __init__(self, tape: str, ptr: int) -> None:
        self.tape = tape
        self.ptr = ptr
        self.tape_cpy = ""
        self.step = 0

    def run(self) -> None:
        self.tape = self.tape_cpy = str(input("* Set mod operation: ")).upper()
        self.q0()

    def print_tape(self, cmd: str) -> None:
        print(f"Tape({self.step})[{cmd}]: [", end="")
        self.step += 1
        for i, _ in enumerate(self.tape):
            if i == self.ptr:
                print(">", end="")
            print(self.tape[i], end="")
        print("]")

    def replace(self, i: int, char: str) -> str:
        return self.tape[:i] + char + self.tape[i + 1:]

    def transition(self, cmd: str, state: Callable) -> None:
        self.print_tape(cmd)
        if cmd == 'R':
            self.ptr += 1
        elif cmd == 'L':
            self.ptr -= 1
        state()

    def q0(self) -> None:
        if self.ptr == len(self.tape):
            print(f"{self.tape_cpy} REJECT")
        elif self.tape[self.ptr] in ('0', 'I'):
            self.transition('R', self.q0)
        elif self.tape[self.ptr] == '#':
            self.transition('R', self.q1)

    def q1(self) -> None:
        if self.ptr == len(self.tape) or self.tape[self.ptr] == 'Y':
            self.transition('L', self.q2)
        elif self.tape[self.ptr] == 'I':
            self.transition('R', self.q1)
        elif self.tape[self.ptr] == '#':
            print(f"{self.tape_cpy} REJECT")

    def q2(self) -> None:
        if self.tape[self.ptr] == 'I':
            self.tape = self.replace(self.ptr, 'Y')
            self.transition('L', self.q3)
        elif self.tape[self.ptr] == '#':
            print(f"{self.tape_cpy} REJECT")

    def q3(self) -> None:
        if self.tape[self.ptr] == 'I':
            self.transition('L', self.q3)
        elif self.tape[self.ptr] == '#':
            self.transition('L', self.q4)

    def q4(self) -> None:
        if self.ptr == -1:
            for i, _ in enumerate(self.tape):
                self.ptr += 1
                if self.tape[i] == 'X':
                    self.tape = self.replace(self.ptr, 'I')
                elif self.tape[i] in ('0', '#', 'Y', 'I'):
                    self.tape = self.replace(self.ptr, ' ')
            print(f"{self.tape_cpy}={self.tape.replace(' ', '')} ACCEPT")
        elif self.tape[self.ptr] in ('0', 'X'):
            self.transition('L', self.q4)
        elif self.tape[self.ptr] == 'I':
            self.tape = self.replace(self.ptr, 'X')
            self.transition('R', self.q5)

    def q5(self) -> None:
        if self.tape[self.ptr] in ('X', '0'):
            self.transition('R', self.q5)
        elif self.tape[self.ptr] == '#':
            self.transition('R', self.q6)

    def q6(self) -> None:
        if self.ptr == len(self.tape):
            self.transition('L', self.q7)
        elif self.tape[self.ptr] == 'Y':
            self.tape = self.replace(self.ptr, 'I')
            self.transition('R', self.q6)
        elif self.tape[self.ptr] == 'I':
            self.transition('R', self.q1)

    def q7(self) -> None:
        if self.ptr < 0:
            self.transition('R', self.q0)
        elif self.tape[self.ptr] in ('I', '#', '0'):
            self.transition('L', self.q7)
        elif self.tape[self.ptr] == 'X':
            self.tape = self.replace(self.ptr, '0')
            self.transition('L', self.q7)
