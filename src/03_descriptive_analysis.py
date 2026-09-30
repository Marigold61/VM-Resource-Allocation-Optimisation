from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input file
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "merged_vm_data.csv"

# Read merged dataset
data = pd.read_csv(INPUT_FILE)

print("DESCRIPTIVE ANALYSIS")
print("=" * 40)

# CPU percentiles
cpu_percentiles = data["CPU"].quantile([0.50, 0.95, 0.99])

# RAM percentiles
ram_percentiles = data["RAM"].quantile([0.50, 0.95, 0.99])

print("\nCPU Percentiles:")
print(f"P50: {cpu_percentiles[0.50]:.6f}")
print(f"P95: {cpu_percentiles[0.95]:.6f}")
print(f"P99: {cpu_percentiles[0.99]:.6f}")
print(f"Maximum: {data['CPU'].max():.6f}")

print("\nRAM Percentiles:")
print(f"P50: {ram_percentiles[0.50]:.6f}")
print(f"P95: {ram_percentiles[0.95]:.6f}")
print(f"P99: {ram_percentiles[0.99]:.6f}")
print(f"Maximum: {data['RAM'].max():.6f}")

# Full descriptive statistics
summary = data[["CPU", "RAM"]].describe().T

print("\nFull descriptive statistics:")
print(summary)

# Number of observations above 100 RAM
ram_above_100 = (data["RAM"] > 100).sum()

print(f"\nRAM observations above 100: {ram_above_100:,}")
print(
    f"Percentage of RAM observations above 100: "
    f"{(ram_above_100 / len(data)) * 100:.4f}%"
)