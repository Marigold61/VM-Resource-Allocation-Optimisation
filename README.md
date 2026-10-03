# VM-Resource-Allocation-Optimisation

## Dataset

The dataset is based on the Google Cluster Data (Borg) trace.

[Google Cluster Data – Official Repository](https://github.com/google/cluster-data)

The original raw dataset is not included in this repository due to its size. The processed VM optimisation input is provided for reproducibility.

## Optimisation Methods

The following methods were implemented and compared:

- First-Fit – baseline heuristic
- Best Fit Decreasing (BFD) – heuristic optimisation
- Integer Linear Programming (ILP): No feasible solution returned within the 30-minute time limit
- Genetic Algorithm (GA) – metaheuristic optimisation

Server capacity:

- CPU: 100 normalised units
- RAM: 200 normalised units

## Results

- Theoretical Lower Bound: 81 servers (mathematical lower bound)
- First-Fit: 84 servers (baseline allocation)
- Best Fit Decreasing (BFD): 82 servers (heuristic optimisation)
- Genetic Algorithm (GA): 81 servers (feasible solution matching the lower bound)
- Integer Linear Programming (ILP): No solution returned (30-minute time limit)

The GA achieved a feasible allocation of 251 VMs using 81 servers, matching the theoretical lower bound.

## Project Structure

```text
data/
├── raw/
└── processed/

src/
├── 01_merge_data.py
├── 02_validate_data.py
├── 03_descriptive_analysis.py
├── 04_vm_percentiles.py
├── 05_prepare_optimization_input.py
├── 06_baseline.py
├── 07_ilp.py
├── 08_bfd.py
└── 09_ga.py

results/
└── vm_optimization_comparison.xlsx
