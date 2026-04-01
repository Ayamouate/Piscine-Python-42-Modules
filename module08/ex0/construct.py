import sys
import os
import site


def main() -> None:
    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.base_prefix}")
        venv_name = os.path.basename(sys.prefix)
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting"
              " the global system.")
        print("\nPackage installation path:\n", site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in")
        print(f"\nCurrent Python: {sys.base_prefix}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!"
              "\nThe machines can see everything you install.")
        print("\nTo enter the construct, run:"
              "\npython -m venv matrix_env"
              "\nsource matrix_env/bin/activate # On Unix"
              "\nmatrix_env""\nScripts""\nactivate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
