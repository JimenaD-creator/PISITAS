# PISITA - Interactive Mathematical Operations Simulation Program

Welcome to **PISITA**! This is an interactive program designed to help you practice and improve your skills in basic mathematical operations, such as addition, subtraction, multiplication, division, and fraction addition. The program is ideal for students or anyone who wants to reinforce their mathematical knowledge in a fun and dynamic way.

## Main features

- **Basic operations**: Practice addition, subtraction, multiplication, and division.
- **Fraction addition**: Learn to add fractions with different denominators and simplify the results.
- **Difficulty levels**: Choose to work with 1- to 4-digit numbers, depending on your skill level.
- **Immediate feedback**: The program tells you if your answer is correct or incorrect, and allows you to try again if you make a mistake.
- **Correct answer counter**: Keep track of your correct and incorrect answers, as well as the total number of operations performed.
- **Friendly Interface**: The program is easy to use and is designed to be interactive and fun.

## How does it work?

1. **Start**: When you run the program, you will be asked to enter your name and select the operation you want to practice.
2. **Operation Selection**: Choose between addition, subtraction, multiplication, division, or adding fractions.
3. **Difficulty Level**: For basic operations, select the number of digits you want to work with (1 to 4 digits).
4. **Problem Solving**: Solve the operations presented to you. You have up to 3 attempts to answer correctly.
5. **Feedback**: The program will tell you if your answer is correct or incorrect. If it is incorrect, you will have the opportunity to try again.
6. **Continue or Exit**: After each operation, you can choose to continue practicing or exit the program. At the end, a summary of your successes and failures will be displayed.

## Project structure

The project is organized into a single Python file (`PISITAS.py`), which contains all the functions needed to run the program. The main functions include:

- **`cifras(op)`**: Generates random numbers with the selected number of digits.
- **`sumoffrac(listnums, listdens, a)`**: Performs the sum of fractions and simplifies the result.
- **`residual(res1, res2)`**: Simplifies fractions using a list of prime numbers.
- **`programa(cont, correct, incorrect, tries)`**: Main function that controls the flow of the program, including the menu and user interaction.

## Running the program

1. **Requirements**: Make sure you have Python installed on your system.
2. **Execution**: To run the program, open a terminal and navigate to the folder where the `PISITAS.py` file is located. Then, run the following command:
```bash
python PISITAS.py
