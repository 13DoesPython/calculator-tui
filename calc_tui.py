import ast
import math
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def evaluate_expression(expression: str):
    allowed_chars = set("0123456789+-*/().,^ ")
    words = "".join(c if c.isalpha() else " " for c in expression).split()

    allowed_words = {"sin", "cos", "tan", "sqrt", "log", "pi", "e", "ans", "factorial"}
    for word in words:
        if word not in allowed_words:
            raise ValueError(f"Unknown function or variable: '{word}")

    for char in expression:
        if char not in allowed_chars and not char.isalpha():
            raise ValueError(f"Invalid char: '{char}")

    safe_dict = {
        "sin": lambda x: math.sin(math.radians(x) if mode == "deg" else x),
        "cos": lambda x: math.cos(math.radians(x) if mode == "deg" else x),
        "tan": lambda x: math.tan(math.radians(x) if mode == "deg" else x),
        "sqrt": math.sqrt,
        "log": math.log,
        "pi": math.pi,
        "e": math.e,
        "factorial": math.factorial,
        "ans": LAST_ANS
    }

    evaluated_expression = expression.replace("^", "**")
    result = eval(evaluated_expression, {"__builtins__": {}}, safe_dict)

    if callable(result):
        raise ValueError("Call the function with parentheses, like sin(pi / 2).")

    return result

LAST_ANS = 0.0
expression_history = []
mode = "deg"  # Default mode is degrees

def history_menu():
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[3J")
        sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "=" * 100)
    print(Style.BRIGHT + Fore.CYAN + "Calculation History".center(100))
    print(Fore.CYAN + "=" * 100)
    
    if not expression_history:
        print("No calculations yet!")
    else:
        for index, (expr, result) in enumerate(expression_history, start=1):
            display_result = result
            if isinstance(display_result, float):
                if display_result.is_integer():
                    display_result = int(display_result)
                else:
                    display_result = round(display_result, 6)

            print(Fore.YELLOW + f"{index}. " + Fore.RESET + f"{expr} = " + Fore.GREEN + f"{display_result}")
    
    print(Fore.CYAN + "=" * 100)
    input(Fore.CYAN + "Press Enter to return to the main menu...")

def help_menu():
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[3J")
        sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "=" * 100)
    print(Style.BRIGHT + Fore.CYAN + "Help Guide".center(100))
    print(Fore.CYAN + "=" * 100)
    print("- Basic arithmetic: Use +, -, *, / for addition, subtraction, multiplication, and division.")
    print("- Power: Use ^ for exponentiation. Example: 2^3 = 8")
    print("- Square root: Use sqrt(). Example: sqrt(16) = 4")
    print("- Factorial: Use factorial(). Example: factorial(5) = 120")
    print("- Trigonometric functions: sin(), cos(), tan() use the current angle mode. Example: sin(90) in DEG mode = 1")
    print("- Logarithm: Use log() for natural logarithm. Example: log(e) = 1")
    print("- Constants: Use pi and e for mathematical constants.")
    print("- Memory: Use 'ans' to refer to the last answer.")
    print("- Commands: Type 'quit' to exit or 'clear' to reset memory and history.")
    print("- Angle mode: Type 'mode' to toggle or 'mode deg' / 'mode rad' to set it explicitly.")
    print("- History: Type 'history' to view past calculations.")
    print(Fore.CYAN + "=" * 100)

def print_menu():
    if sys.stdout.isatty():
        sys.stdout.write("\x1b[3J")
        sys.stdout.flush()
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.CYAN + "=" * 100)
    print(Style.BRIGHT + Fore.CYAN + "Advanced terminal calculator".center(100))
    print(Fore.CYAN + "=" * 100)
    print("- Arithmetic: Use +, -, *, / and parentheses. Example: (1 + 2) * 3")
    print("- Powers, roots, and factorials: Use ^, sqrt(), and factorial()")
    print("- Trigonometry: Use sin(), cos(), and tan() with the current angle mode")
    print("- Logarithms and constants: Use log(), pi, and e")
    print("- Angle mode: Type 'mode' to toggle or 'mode deg' / 'mode rad'")
    print("- Memory, history, and commands: Use 'ans', 'history', 'help', 'clear', or 'quit'")
    print(Fore.CYAN + "=" * 100)
    print("Mode: " + Fore.YELLOW + f"{mode.upper()}" + Fore.CYAN + " | Last Answer: " + Fore.GREEN + f"{LAST_ANS}")
    print(Fore.CYAN + "=" * 100)

def main():
    global LAST_ANS, mode
    message = ""

    while True:
        print_menu()
        if message:
            message_color = Fore.RED if message.startswith("Error:") else Fore.GREEN
            print(message_color + message)

        try:
            user_input = input(Fore.CYAN + "[Formula/Command]: " + Fore.WHITE).strip().lower()

            if user_input == "quit":
                sys.exit(0)

            if user_input == "":
                message = "Error: No input provided!"
                continue

            if user_input.startswith("recall "):
                number_string = user_input.removeprefix("recall ").strip()

                if not number_string.isdigit():
                    message = "Error: Use recall <number>."
                    continue
                
                index = int(number_string) - 1
                if not 0 <= index < len(expression_history):
                    message = "Error: no expression with that history number."
                    continue

                user_input = expression_history[index][0]     

            if user_input == "clear":
                LAST_ANS = 0
                expression_history.clear()
                mode = "deg"  # Reset mode to degrees
                message = "Memory and history cleared. Angle mode reset to DEGREES."
                continue

            if user_input == "help":
                help_menu()
                input(Fore.CYAN + "Press Enter to return to the main menu...")
                continue
            
            if user_input == "history":
                history_menu()
                continue

            if user_input == "mode":
                mode = "rad" if mode == "deg" else "deg"
                message = f"Angle mode changed to {mode.upper()}."
                continue

            if user_input in {"mode deg", "mode rad"}:
                mode = user_input.split()[1]
                message = f"Angle mode changed to {mode.upper()}."
                continue

            result = evaluate_expression(user_input)
            expression_history.append((user_input, result))
            LAST_ANS = result

            display_result = result
            if isinstance(display_result, float):
                if display_result.is_integer():
                    display_result = int(display_result)
                else:
                    display_result = round(display_result, 6)

            message = f"Result: {display_result}"

        except EOFError:
            return
        except ZeroDivisionError:
            message = "Error: Cannot divide by zero!"
        except (ValueError, SyntaxError) as e:
            message = f"Error: Check your math formulation '{e}'"
        except Exception as e:
            message = f"Error: {e}"

if __name__ == "__main__":
    main()