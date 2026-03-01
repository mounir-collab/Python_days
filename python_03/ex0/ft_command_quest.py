import sys

if __name__ == "__main__":

    print("=== Command Quest ===")

    total_arguments = len(sys.argv)
    program_name = sys.argv[0]
    if total_arguments == 1:
        print("No arguments provided!")
        print("Program name:", program_name)
        print(f"Total arguments:{total_arguments}\n")
    else:
        print("Program name:", program_name)
        print("Arguments received:", total_arguments - 1)
        i = 1
        while i < total_arguments:
            print(f"Argument {i}:", sys.argv[i])
            i += 1
        print(f"Total arguments:{total_arguments}\n")
