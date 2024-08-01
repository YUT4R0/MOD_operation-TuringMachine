from TM import TuringMachine

print("<===== TURING MACHINE: MOD operation simulator =====>")
print("> This script basically simulates a simple mod operation (a mod b = n);")
print("> where 'a', 'b' and 'n' are integers represented by 'I' and 'mod' by '#;")
print("> Type something for example: 'III#II';")
print("> The result must be 'I';")

running = True
while running:
    TAPE = ""
    PTR = 0
    TM = TuringMachine(TAPE, PTR)
    TM.run()
    op = str(input("* Wanna play again (y/n)?: ")).upper()
    while op not in ('Y', 'N'):
        print(f"[!!!] Invalid operation: '{op}'.")
        op = str(input("* Wanna play again (y/n)?: "))
    if op == 'N':
        print("% Exiting program...")
        break
