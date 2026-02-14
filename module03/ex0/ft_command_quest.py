import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) > 1:
        print("Program name:", sys.argv[0])
        print("Arguments received:", len(sys.argv) - 1)
        for i in sys.argv[1:]:
            print("Argument 1:", i)
        print("Total arguments:", len(sys.argv))

    else:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
        print("Total arguments: 1")
