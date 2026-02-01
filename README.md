Instant Universal GCD & LCM Calculator
This Python tool provides a robust engine for calculating the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) for any set of rational numbers. Unlike standard calculators that only handle integers, this project processes integers, decimals, and fractions simultaneously.
🚀 Key Features
Universal Input: Accepts whole numbers (12), decimals (0.5), and fractions (2/3).
Fractional Logic: Uses the mathematical reduction method to find GCD/LCM across mixed formats:$GCD(\frac{a}{b}, \frac{c}{d}) = \frac{GCD(a, c)}{LCM(b, d)}$$LCM(\frac{a}{b}, \frac{c}{d}) = \frac{LCM(a, c)}{GCD(b, d)}
$Auto-Simplification: All results are automatically reduced to their simplest fractional form.
Prime Detection: Identifies and lists any prime numbers found within your input set.
Error Handling: Gracefully handles division by zero and invalid text entries without crashing.
🛠️ How It Works
The project is structured into four distinct layers:
Math Engine: Implements the Euclidean algorithm for GCD and the property of products for LCM.
Input Converter: A parsing layer that normalizes all inputs into $(numerator, denominator)$ tuples.
Interface: A command-line loop that gathers user input and handles string splitting.
Analysis: The final reduction step that computes the result across the entire list of numbers.
Example
To run the script, ensure you have Python installed.
Execute the file and enter your numbers separated by commas when prompted.
Input:Plaintext
Enter all numbers: 12, 0.5, 2/3, 7
Output:Plaintext==================================================
RESULTS ANALYSIS
--------------------------------------------------
Primes Found: [7]
Final GCD: 1/6 (approx 0.1667)
Final LCM: 84
==================================================
🔧 Installation & Setup
Clone the repository:Bashgit clone https://github.com/yourusername/universal-gcd-lcm.git
Navigate to the directory:Bashcd universal-gcd-lcm
Run the script:Bashpython calculator.py
