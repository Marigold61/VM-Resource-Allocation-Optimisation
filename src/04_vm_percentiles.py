from pathlib import Path
import pandas as pd

# Find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input file
INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "merged_vm_data.csv"

# Output file
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "vm_percentiles.csv"

# Read merged dataset
data = pd.read_csv(INPUT_FILE)

# Calculate statistics for each VM
vm_summary = (
    data.groupby("VM_ID")
    .agg(
        Days_Available=("Day", "nunique"),
        CPU_Average=("CPU", "mean"),
        CPU_P50=("CPU", lambda x: x.quantile(0.50)),
        CPU_P95=("CPU", lambda x: x.quantile(0.95)),
        CPU_P99=("CPU", lambda x: x.quantile(0.99)),
        RAM_Average=("RAM", "mean"),
        RAM_P50=("RAM", lambda x: x.quantile(0.50)),
        RAM_P95=("RAM", lambda x: x.quantile(0.95)),
        RAM_P99=("RAM", lambda x: x.quantile(0.99)),
    )
    .reset_index()
)

# Save VM-level results
vm_summary.to_csv(OUTPUT_FILE, index=False)

print("VM-LEVEL PERCENTILE ANALYSIS")
print("=" * 40)

print(f"Unique VMs: {vm_summary['VM_ID'].nunique()}")
print(f"Output rows: {len(vm_summary)}")
print(f"Output file: {OUTPUT_FILE}")

print("\nMaximum VM-level requirements:")
print(f"Maximum CPU P95: {vm_summary['CPU_P95'].max():.6f}")
print(f"Maximum RAM P95: {vm_summary['RAM_P95'].max():.6f}")

print("\nVMs with RAM P95 above 100:")
print(
    vm_summary[
        vm_summary["RAM_P95"] > 100
    ][["VM_ID", "Days_Available", "RAM_P95"]]
)
print("\nDays available per VM:")
print(
    vm_summary["Days_Available"]
    .value_counts()
    .sort_index()
)
print("\nSummary of days available:")
print(f"Mean days available: {vm_summary['Days_Available'].mean():.2f}")
print(f"Median days available: {vm_summary['Days_Available'].median():.0f}")