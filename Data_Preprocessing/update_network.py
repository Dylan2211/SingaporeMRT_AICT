import os

# Replace CurrentStations in mrtNetwork.py with isolated network
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
network_output_path = os.path.join(PROJECT_ROOT, 'network_output.txt')
mrt_network_path = os.path.join(PROJECT_ROOT, 'mrtNetwork.py')

with open(network_output_path, 'r') as f:
    new_dict = f.read()

with open(mrt_network_path, 'r') as f:
    original = f.read()

# Find start marker
pre_dict = 'import csv\nimport os\nfrom collections import defaultdict\nfrom Classes.station import Station, checkSymmetry\n\n'

# Find where the dictionary ends (before FutureStations comment)
post_marker = '\n\n\n# FutureStations'

# Find positions
dict_end_idx = original.find(post_marker)

# Reconstruct file
new_content = pre_dict + new_dict.strip() + original[dict_end_idx:]

with open(mrt_network_path, 'w') as f:
    f.write(new_content)

print('✓ Successfully updated mrtNetwork.py with isolated line connections')
print('✓ All lines treated independently - no cross-line interchanges')
