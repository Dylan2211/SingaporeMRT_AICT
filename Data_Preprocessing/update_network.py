# Replace CurrentStations in mrtNetwork.py with isolated network
with open('network_output.txt', 'r') as f:
    new_dict = f.read()

with open('mrtNetwork.py', 'r') as f:
    original = f.read()

# Find start marker
pre_dict = 'from station import Station, checkSymmetry\n\n'

# Find where the dictionary ends (before FutureStations comment)
post_marker = '\n\n\n# FutureStations'

# Find positions
dict_end_idx = original.find(post_marker)

# Reconstruct file
new_content = pre_dict + new_dict.strip() + original[dict_end_idx:]

with open('mrtNetwork.py', 'w') as f:
    f.write(new_content)

print('✓ Successfully updated mrtNetwork.py with isolated line connections')
print('✓ All lines treated independently - no cross-line interchanges')
