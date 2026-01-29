# Generate MRT Network with Isolated Lines
# Each line treated independently - no interchange connections

nsl_stations = [
    "Jurong East", "Bukit Batok", "Bukit Gombak", "Choa Chu Kang", "Yew Tee", "Kranji",
    "Marsiling", "Woodlands", "Admiralty", "Sembawang", "Canberra", "Yishun", "Khatib",
    "Yio Chu Kang", "Ang Mo Kio", "Bishan", "Braddell", "Toa Payoh", "Novena", "Newton",
    "Orchard", "Somerset", "Dhoby Ghaut", "City Hall", "Raffles Place", "Marina Bay", "Marina South Pier"
]

ewl_stations = [
    "Pasir Ris", "Tampines", "Simei", "Tanah Merah", "Bedok", "Kembangan", "Eunos", "Paya Lebar",
    "Aljunied", "Kallang", "Lavender", "Bugis", "City Hall", "Raffles Place", "Tanjong Pagar",
    "Outram Park", "Tiong Bahru", "Redhill", "Queenstown", "Commonwealth", "Buona Vista", "Dover",
    "Clementi", "Jurong East", "Chinese Garden", "Lakeside", "Boon Lay", "Pioneer", "Joo Koon",
    "Gul Circle", "Tuas Crescent", "Tuas West Road", "Tuas Link"
]

ewl_changi_branch = ["Tanah Merah", "Expo", "Changi Airport"]

nel_stations = [
    "HarbourFront", "Outram Park", "Chinatown", "Clarke Quay", "Dhoby Ghaut", "Little India",
    "Farrer Park", "Boon Keng", "Potong Pasir", "Woodleigh", "Serangoon", "Kovan", "Hougang",
    "Buangkok", "Sengkang", "Punggol", "Punggol Coast"
]

ccl_stations = [
    "Dhoby Ghaut", "Bras Basah", "Esplanade", "Promenade", "Nicoll Highway", "Stadium", "Mountbatten",
    "Dakota", "Paya Lebar", "MacPherson", "Tai Seng", "Bartley", "Serangoon", "Lorong Chuan",
    "Bishan", "Marymount", "Caldecott", "Botanic Gardens", "Farrer Road", "Holland Village",
    "Buona Vista", "one-north", "Kent Ridge", "Haw Par Villa", "Pasir Panjang", "Labrador Park",
    "Telok Blangah", "HarbourFront", "Bayfront", "Marina Bay"
]

dtl_stations = [
    "Bukit Panjang", "Cashew", "Hillview", "Hume", "Beauty World", "King Albert Park", "Sixth Avenue",
    "Tan Kah Kee", "Botanic Gardens", "Stevens", "Newton", "Little India", "Rochor", "Bugis",
    "Promenade", "Bayfront", "Downtown", "Telok Ayer", "Chinatown", "Fort Canning", "Bencoolen",
    "Jalan Besar", "Bendemeer", "Geylang Bahru", "Mattar", "MacPherson", "Ubi", "Kaki Bukit",
    "Bedok North", "Bedok Reservoir", "Tampines West", "Tampines", "Tampines East", "Upper Changi", "Expo"
]

tel_stations = [
    "Woodlands North", "Woodlands", "Woodlands South", "Springleaf", "Lentor", "Mayflower",
    "Bright Hill", "Upper Thomson", "Caldecott", "Mount Pleasant", "Stevens", "Napier",
    "Orchard Boulevard", "Orchard", "Great World", "Havelock", "Outram Park", "Maxwell",
    "Shenton Way", "Marina Bay", "Marina South", "Gardens by the Bay", "Tanjong Rhu", "Katong Park",
    "Tanjong Katong", "Marine Parade", "Marine Terrace", "Siglap", "Bayshore"
]

# Build connections dictionary
connections = {}

def add_line_connections(stations, line_code):
    """Add bidirectional connections for a line"""
    for i, station in enumerate(stations):
        if station not in connections:
            connections[station] = []
        
        # Connect to previous station
        if i > 0:
            connections[station].append((stations[i-1], 120, [line_code]))
        
        # Connect to next station
        if i < len(stations) - 1:
            connections[station].append((stations[i+1], 120, [line_code]))

# Add all lines
add_line_connections(nsl_stations, "NSL")
add_line_connections(ewl_stations, "EWL")
add_line_connections(ewl_changi_branch, "EWL")  # Changi branch
add_line_connections(nel_stations, "NEL")
add_line_connections(ccl_stations, "CCL")
add_line_connections(dtl_stations, "DTL")
add_line_connections(tel_stations, "TEL")

# Generate the Python code
print("CurrentStations = {")

# Group by line
lines = [
    ("NORTH-SOUTH LINE (Red)", nsl_stations, "NSL"),
    ("EAST-WEST LINE (Green)", ewl_stations + ["Expo", "Changi Airport"], "EWL"),
    ("NORTH-EAST LINE (Purple)", nel_stations, "NEL"),
    ("CIRCLE LINE (Orange)", ccl_stations, "CCL"),
    ("DOWNTOWN LINE (Blue)", dtl_stations, "DTL"),
    ("THOMSON-EAST COAST LINE (Brown)", tel_stations, "TEL")
]

for line_name, stations, line_code in lines:
    print(f"\t\t# ========== {line_name} ==========")
    for station in stations:
        if station in connections:
            conns = [c for c in connections[station] if line_code in c[2]]
            if conns:
                print(f'\t\t"{station}": {conns},')
            else:
                print(f'\t\t"{station}": [],')
        else:
            print(f'\t\t"{station}": [],')
    print()

# Add any stations that might be missing
all_stations_in_lines = set()
for _, stations, _ in lines:
    all_stations_in_lines.update(stations)

missing_stations = set(connections.keys()) - all_stations_in_lines
if missing_stations:
    print("\t\t# ========== ADDITIONAL STATIONS ==========")
    for station in sorted(missing_stations):
        if station in connections:
            print(f'\t\t"{station}": {connections[station]},')

print("\t}")
