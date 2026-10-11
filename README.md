# Calculator TUI

A terminal calculator for arithmetic, powers, and common math functions.

## Features

- Basic arithmetic and parentheses
- Powers with `^` and square roots with `sqrt()`
- Factorials with `factorial()`
- Trigonometric functions: `sin()`, `cos()`, and `tan()`
- `log()`, plus the constants `pi` and `e`
- Reuse the previous result with `ans`
- Clear memory with `clear` or exit with `quit`
- Help menu with `help` command

## Get the files

Clone the GitHub repository and enter its folder:

```bash
git clone https://github.com/13DoesPython/advanced-calculator.git
cd advanced-calculator
```

## Usage

From inside the cloned `advanced-calculator` folder, run `calc_tui.py`:

```bash
python calc_tui.py
```

At the prompt, enter an equation and press Enter. For example, `2 + 3` returns `5`. Use `ans` to reuse the last result, `clear` to reset memory, or `quit` to exit. The program requires Python 3.10 or newer and Colorama. Note that the program does not support implicit multiplication, so `2(3)` is invalid; use `2 * 3` instead. Also the equation you type will be solved by the BEDMAS order of operations rule. Lastly, the program does not support complex numbers, so `sqrt(-1)` will return an error.

## Version history

- 0.2.5: Added history feature to view previous calculations
- 0.2.1: Bug fixes and improvements
- 0.2.0:
    - Added help menu for user guidance
    - Added input prompt color for better visibility
    - Added new method to safe_dict: `factorial()` for calculating factorials
- 0.1.0: Initial release