import yaml
import sys

filename = sys.argv[1]
baseline_filename = sys.argv[2]

with open(filename, "r") as stream:
    exp_results = yaml.safe_load(stream)
    
baseline_vals = {}

for line in open(baseline_filename, 'r').readlines():
    tokens = line.strip().split(',')
    problem = tokens[0]
    baseline_vals[problem] = float(tokens[1])

# print(baseline_vals)

BLOCK_REWARD = 4.0
for problem in exp_results:
    found_mev = exp_results[problem]
    baseline_mev = baseline_vals[problem] + BLOCK_REWARD
    if found_mev <  baseline_mev:
        print(problem, found_mev, baseline_mev)
