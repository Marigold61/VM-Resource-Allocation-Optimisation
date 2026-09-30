from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input file
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "merged_vm_data.csv"

# Read merged dataset
data = pd.read_csv(INPUT_FILE)

print("DATASET VALIDATION")
print("=" * 40)

# Basic information
print(f"Total rows: {len(data):,}")
print(f"Total columns: {len(data.columns)}")
print(f"Unique VMs: {data['VM_ID'].nunique()}")
print(f"Unique days: {data['Day'].nunique()}")
print(f"Unique VM-day combinations: {data[['VM_ID', 'Day']].drop_duplicates().shape[0]}")

# Missing values
print("\nMissing values:")
print(data.isnull().sum())

# Duplicate rows
print(f"\nDuplicate rows: {data.duplicated().sum()}")

# Measurements per VM-day
measurements_per_vm_day = (
    data.groupby(["VM_ID", "Day"])
    .size()
)

print("\nMeasurements per VM-day:")
print(measurements_per_vm_day.describe())

# CPU statistics
print("\nCPU statistics:")
print(data["CPU"].describe())

# RAM statistics
print("\nRAM statistics:")
print(data["RAM"].describe())