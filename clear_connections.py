import re

# Read the original file
with open('mrtNetwork.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line
new_lines = []
in_currentstations = False
bracket_count = 0

for line in lines:
    if 'CurrentStations = {' in line:
        in_currentstations = True
        new_lines.append(line)
        bracket_count = 1
        continue
    
    if in_currentstations:
        # Count brackets to find the end of CurrentStations
        bracket_count += line.count('{') - line.count('}')
        
        # Check if this is a station definition line
        if '":' in line and '[' in line:
            # Extract station name and replace value with empty list
            match = re.match(r'(\s*"[^"]+"\s*:\s*)\[.*\](,?)(.*)$', line)
            if match:
                indent, comma, comment = match.groups()
                new_lines.append(f'{indent}[]{comma}{comment}\n')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
        
        # Check if we've closed the CurrentStations dictionary
        if bracket_count == 0:
            in_currentstations = False
    else:
        new_lines.append(line)

# Write the modified content
with open('mrtNetwork.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Successfully cleared all station connection values!')
