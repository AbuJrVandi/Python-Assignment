#!/usr/bin/env python3
"""
Basic Calculator Program
Intro to Python Assignment

This program asks the user to input two numbers and a mathematical operation,
then performs the calculation and displays the result.
"""

def main():
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /")
    print("-" * 30)
    
    try:
        # Get first number from user
        num1 = float(input("Enter the first number: "))
        
        # Get second number from user
        num2 = float(input("Enter the second number: "))
        
        # Get operation from user
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
