from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input file
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "vm_percentiles.csv"

# Output file
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "vm_optimization_input.csv"

# Read VM-level percentile data
data = pd.read_csv(INPUT_FILE)

# Select the variables required for optimization
optimization_input = data[
    [
        "VM_ID",
        "Days_Available",
        "CPU_P95",
        "RAM_P95"
    ]
].copy()

# Rename P95 values as resource requirements
optimization_input = optimization_input.rename(
    columns={
        "CPU_P95": "CPU_Requirement",
        "RAM_P95": "RAM_Requirement"
    }
)

# Save the optimization input
optimization_input.to_csv(OUTPUT_FILE, index=False)

print("OPTIMIZATION INPUT PREPARATION")
print("=" * 40)

print(f"Number of VMs: {len(optimization_input)}")
print(f"Output file: {OUTPUT_FILE}")

print("\nColumns:")
print(list(optimization_input.columns))

print("\nFirst 10 VMs:")
print(optimization_input.head(10))

print("\nResource requirement summary:")
print(
    optimization_input[
        ["CPU_Requirement", "RAM_Requirement"]
    ].describe()
)

print("\nMaximum resource requirements:")
print(
    f"Maximum CPU requirement: "
    f"{optimization_input['CPU_Requirement'].max():.6f}"
)

print(
    f"Maximum RAM requirement: "
    f"{optimization_input['RAM_Requirement'].max():.6f}"
)