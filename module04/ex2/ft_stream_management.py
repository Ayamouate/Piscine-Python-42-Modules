import sys


if __name__ == "__main__":
    # normal output should go to stdout via ``print`` (the default)
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    arch_id = input("\nInput Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {report}\n")
    print("[ALERT] System diagnostic:"
          "Communication channels verified", file=sys.stderr)
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")
