from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input folder containing the original .txt files
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "GCD_VMs"

# Output folder
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Output file
OUTPUT_FILE = PROCESSED_DATA_DIR / "merged_vm_data.csv"

print("Reading files from:")
print(RAW_DATA_DIR)

# Find all text files
txt_files = sorted(RAW_DATA_DIR.glob("vm_*"))

print(f"Number of .txt files found: {len(txt_files)}")

if not txt_files:
    raise FileNotFoundError(
        f"No .txt files were found in: {RAW_DATA_DIR}"
    )
# Inspect the first workload file
# Merge all workload files
all_data = []

for file_path in txt_files:
    # Extract VM ID and day from filename
    # Example: vm_1218322450_1
    filename_parts = file_path.name.split("_")

    vm_id = filename_parts[1]
    day = int(filename_parts[2])

    # Read CPU and RAM values
    data = pd.read_csv(
        file_path,
        sep=r"\s+",
        header=None,
        names=["CPU", "RAM"]
    )

    # Add VM ID, day, and measurement number
    data.insert(0, "VM_ID", vm_id)
    data.insert(1, "Day", day)
    data.insert(2, "Measurement", range(1, len(data) + 1))

    all_data.append(data)

# Combine all files into one dataframe
merged_data = pd.concat(all_data, ignore_index=True)

# Save the merged dataset
merged_data.to_csv(OUTPUT_FILE, index=False)

print("\nData merging completed.")
print(f"Total rows: {len(merged_data):,}")
print(f"Unique VMs: {merged_data['VM_ID'].nunique()}")
print(f"VM-day files: {len(txt_files)}")
print(f"Output file: {OUTPUT_FILE}")