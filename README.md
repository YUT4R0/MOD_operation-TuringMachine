# Turing Machine Simulator for Modulo Operation

This Python script simulates a single tape Turing machine that performs the modulo operation (remembering that a Turing machine is a mathematical model of computation that defines an abstract machine that manipulates symbols on a strip of tape according to a table of rules).

## Disclaimer:
- It only works with **positive integer numbers**.
- Due to a recursive solution, this program cannot deal with larger numbers like 11 % 12, 37 % 12, and so on.

## Features
- **Turing Machine Simulation**: The script accurately simulates the behavior of a Turing machine, including states, tape movements, and transitions.
- **Modulo Operation**: Implements the logic to perform the modulo operation, which returns the remainder of the division of two numbers.
- **Configurable Input**: The machine can be configured with different inputs to perform the modulo operation on various pairs of integers.

## Files
- `main.py`: main loop and runs TM.
- `TM.py`: The turning machine class.

## Usage
1. **Setup**: Ensure you have Python installed on your system.
2. **Run the Script**: Execute the script using the command:
    ```sh
    python main.py
    ```
3. **Input**: Modify the input variables within the script to change the numbers for which you want to compute the modulo.

## Example
Consider the following example where we compute `a mod b = c`:
- The variables 'a', 'b', and 'n' are integers represented by 'I' enumeration and 'mod' by '#';
- So if you wanna compute "5 mod 3", it must be typed like `IIIII#III`;
- As a result, you would get 1, on the terminal, you get `IIIII#III=I` (Followed by a message that indicates if the operation is acceptable);

## Code Overview
Here is a brief overview of the main components of the script:

### States and Transition Rules
The script defines a set of states and transition rules that guide the Turing machine's behavior. Each state dictates how the machine reads and writes symbols on the tape and how it moves the tape head.

### Tape Representation
The tape is represented as a list of symbols. The machine reads and writes to this tape based on the current state and the symbol under the tape head.

### Modulo Logic
The modulo logic is implemented through the state transitions. The machine repeatedly subtracts the divisor from the dividend, keeping track of the remainder until it finds the result.

# Statechart of the same TM (but using multiple-tape):
![WhatsApp Image 2024-07-03 at 17 20 03_d757aedb](https://github.com/user-attachments/assets/165f2bdd-a98a-4df0-b4f3-4b3ac404252c)
