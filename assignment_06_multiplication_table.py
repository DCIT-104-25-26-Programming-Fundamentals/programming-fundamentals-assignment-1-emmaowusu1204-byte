# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================

# -------------------------------
# Part A: Single Table
# -------------------------------
def single_table(number):
    if number <= 0:
        print("Error: Number must be positive.")
        return
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

# -------------------------------
# Part B: Tables from 1 to N
# -------------------------------
def tables_up_to_n(n):
    if n <= 0:
        print("Error: N must be positive.")
        return
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
        print("-" * 30)  # separator line

# -------------------------------
# Main Program
# -------------------------------
def main():
    # Part A
    number = int(input("Enter a number for its multiplication table: "))
    single_table(number)

    # Part B
    n = int(input("\nEnter N to generate tables from 1 to N: "))
    tables_up_to_n(n)

# Run program
if __name__ == "__main__":
    main()
