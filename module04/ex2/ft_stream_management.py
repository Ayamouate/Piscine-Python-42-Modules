import sys


if __name__ == "__main__":
    # normal output should go to stdout via ``print`` (the default)
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    arch_id = input("\nInput Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {report}\n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")
