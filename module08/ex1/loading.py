import sys
import importlib
from typing import List


required_lib = {
    "pandas": "Data manipulation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
    "numpy": "Numerical computing ready"
}


def check_dependencies() -> List[str]:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    missing: List[str] = []

    for lib, des in required_lib.items():
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version}) - {des}")
        except ModuleNotFoundError:
            print(f"[MISSING] {lib} - Not installed")
            missing.append(lib)

    return missing


def run_analysis() -> None:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = np.random.rand(1000)
    df = pd.DataFrame(data, columns=["values"])

    print("Generating visualization...")

    plt.plot(df["values"])
    plt.title("Matrix Data Analysis")
    output_file = "matrix_analysis.png"
    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    missing = check_dependencies()

    if missing:
        print("\n❌ Some dependencies are missing.")
        for lib in missing:
            print(f" - {lib}")
        print("Install them using:")
        print(" pip install -r requirements.txt",
              "- or -", "poetry install")
        print("\nThen run this program again.")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
