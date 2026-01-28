from station import Station, checkSymmetry

CurrentStations = {
		# ========== NORTH-SOUTH LINE (Red) ==========
		"Jurong East": [("Bukit Batok", 120, ["NSL"]), ("Clementi", 300, ["NSL", "EWL"]), ("Chinese Garden", 120, ["EWL"])],
		"Bukit Batok": [("Jurong East", 120, ["NSL"]), ("Bukit Gombak", 120, ["NSL"])],
		"Bukit Gombak": [("Bukit Batok", 120, ["NSL"]), ("Choa Chu Kang", 120, ["NSL"])],
		"Choa Chu Kang": [("Bukit Gombak", 120, ["NSL"]), ("Yew Tee", 120, ["NSL"])],
		"Yew Tee": [("Choa Chu Kang", 120, ["NSL"]), ("Kranji", 120, ["NSL"])],
		"Kranji": [("Yew Tee", 120, ["NSL"]), ("Marsiling", 120, ["NSL"])],
		"Marsiling": [("Kranji", 120, ["NSL"]), ("Woodlands", 120, ["NSL"])],
		"Woodlands": [("Marsiling", 120, ["NSL"]), ("Admiralty", 120, ["NSL"]), ("Woodlands South", 300, ["NSL", "TEL"]), ("Woodlands North", 120, ["TEL"])],
		"Woodlands South": [("Woodlands", 300, ["NSL", "TEL"]), ("Springleaf", 120, ["TEL"])],  # Bidirectional to Woodlands and TEL
		"Admiralty": [("Woodlands", 120, ["NSL"]), ("Sembawang", 120, ["NSL"])],
		"Sembawang": [("Admiralty", 120, ["NSL"]), ("Canberra", 120, ["NSL"])],
		"Canberra": [("Sembawang", 120, ["NSL"]), ("Yishun", 120, ["NSL"])],
		"Yishun": [("Canberra", 120, ["NSL"]), ("Khatib", 120, ["NSL"])],
		"Khatib": [("Yishun", 120, ["NSL"]), ("Yio Chu Kang", 120, ["NSL"])],
		"Yio Chu Kang": [("Khatib", 120, ["NSL"]), ("Ang Mo Kio", 120, ["NSL"])],
		"Ang Mo Kio": [("Yio Chu Kang", 120, ["NSL"]), ("Bishan", 120, ["NSL"])],
		"Bishan": [("Ang Mo Kio", 120, ["NSL"]), ("Braddell", 120, ["NSL"]), ("Caldecott", 300, ["NSL", "CCL"]), ("Marymount", 120, ["CCL"])],  # CCL interchange
		"Braddell": [("Bishan", 120, ["NSL"]), ("Toa Payoh", 120, ["NSL"])],
		"Toa Payoh": [("Braddell", 120, ["NSL"]), ("Novena", 120, ["NSL"])],
		"Novena": [("Toa Payoh", 120, ["NSL"]), ("Newton", 120, ["NSL"])],
		"Newton": [("Novena", 120, ["NSL"]), ("Orchard", 120, ["NSL"]), ("Little India", 300, ["NSL", "DTL"]), ("Stevens", 300, ["NSL", "DTL"])],  # DTL interchange
		"Orchard": [("Newton", 120, ["NSL"]), ("Somerset", 120, ["NSL"]), ("Stevens", 300, ["NSL", "TEL"]), ("Napier", 120, ["TEL"]), ("Orchard Boulevard", 120, ["TEL"])],
		"Somerset": [("Orchard", 120, ["NSL"]), ("Dhoby Ghaut", 120, ["NSL"])],
		# Dhoby Ghaut is a 3-line interchange (NSL, NEL, CCL) with immediate adjacent stations
		"Dhoby Ghaut": [
			("Somerset", 120, ["NSL"]), ("City Hall", 120, ["NSL"]),  # NSL
			("Clarke Quay", 120, ["NEL"]), ("Little India", 120, ["NEL"]),  # NEL
			("Bras Basah", 120, ["CCL"])  # CCL
		],
		"City Hall": [("Dhoby Ghaut", 120, ["NSL"]), ("Raffles Place", 120, ["NSL"]), ("Bugis", 120, ["EWL"])],  # NSL/EWL connections
		"Raffles Place": [("City Hall", 120, ["NSL"]), ("Marina Bay", 120, ["NSL"]), ("Tanjong Pagar", 120, ["EWL"]), ("Downtown", 300, ["DTL", "NSL", "EWL"])],  # EWL connection and DTL
		"Marina Bay": [("Raffles Place", 120, ["NSL"]), ("Marina South Pier", 120, ["NSL"]), ("Bayfront", 300, ["NSL", "CCL", "TEL"]), ("Shenton Way", 120, ["TEL"]), ("Gardens by the Bay", 120, ["TEL"])],  # CCL/TEL interchange
		"Marina South Pier": [("Marina Bay", 120, ["NSL"])],
		
		# ========== EAST-WEST LINE (Green) ==========
		# Main Line
		"Pasir Ris": [("Tampines", 120, ["EWL"])],
		"Tampines": [("Pasir Ris", 120, ["EWL"]), ("Simei", 120, ["EWL"]), ("Tampines West", 300, ["EWL", "DTL"]), ("Tampines East", 120, ["DTL"])],
		"Simei": [("Tampines", 120, ["EWL"]), ("Tanah Merah", 120, ["EWL"])],
		"Tanah Merah": [("Simei", 120, ["EWL"]), ("Bedok", 120, ["EWL"]), ("Expo", 120, ["EWL"])],  # Branch to Changi
		"Bedok": [("Tanah Merah", 120, ["EWL"]), ("Kembangan", 120, ["EWL"])],
		"Kembangan": [("Bedok", 120, ["EWL"]), ("Eunos", 120, ["EWL"])],
		"Eunos": [("Kembangan", 120, ["EWL"]), ("Paya Lebar", 120, ["EWL"])],
		"Paya Lebar": [("Eunos", 120, ["EWL"]), ("Aljunied", 120, ["EWL"]), ("MacPherson", 300, ["EWL", "CCL"])],  # CCL interchange
		"Aljunied": [("Paya Lebar", 120, ["EWL"]), ("Kallang", 120, ["EWL"])],
		"Kallang": [("Aljunied", 120, ["EWL"]), ("Lavender", 120, ["EWL"])],
		"Lavender": [("Kallang", 120, ["EWL"]), ("Bugis", 120, ["EWL"])],
		"Bugis": [("Lavender", 120, ["EWL"]), ("City Hall", 120, ["EWL"]), ("Rochor", 300, ["EWL", "DTL"])],  # DTL interchange
		"Tanjong Pagar": [("Raffles Place", 120, ["EWL"]), ("Outram Park", 120, ["EWL"]), ("Maxwell", 300, ["TEL", "EWL"])],
		"Outram Park": [("Tanjong Pagar", 120, ["EWL"]), ("Tiong Bahru", 120, ["EWL"]), ("Chinatown", 300, ["EWL", "NEL", "DTL", "TEL"]), ("HarbourFront", 120, ["NEL"]), ("Havelock", 300, ["TEL", "EWL", "NEL"])],
		"Tiong Bahru": [("Outram Park", 120, ["EWL"]), ("Redhill", 120, ["EWL"])],
		"Redhill": [("Tiong Bahru", 120, ["EWL"]), ("Queenstown", 120, ["EWL"])],
		"Queenstown": [("Redhill", 120, ["EWL"]), ("Commonwealth", 120, ["EWL"])],
		"Commonwealth": [("Queenstown", 120, ["EWL"]), ("Buona Vista", 120, ["EWL"])],
		"Buona Vista": [("Commonwealth", 120, ["EWL"]), ("Dover", 120, ["EWL"]), ("one-north", 300, ["EWL", "CCL"]), ("Holland Village", 120, ["CCL"])],  # CCL interchange
		"Dover": [("Buona Vista", 120, ["EWL"]), ("Clementi", 120, ["EWL"])],
		"Clementi": [("Dover", 120, ["EWL"]), ("Jurong East", 300, ["NSL", "EWL"])],
		"Chinese Garden": [("Jurong East", 120, ["EWL"]), ("Lakeside", 120, ["EWL"])],
		"Lakeside": [("Chinese Garden", 120, ["EWL"]), ("Boon Lay", 120, ["EWL"])],
		"Boon Lay": [("Lakeside", 120, ["EWL"]), ("Pioneer", 120, ["EWL"])],
		"Pioneer": [("Boon Lay", 120, ["EWL"]), ("Joo Koon", 120, ["EWL"])],
		"Joo Koon": [("Pioneer", 120, ["EWL"]), ("Gul Circle", 120, ["EWL"])],
		"Gul Circle": [("Joo Koon", 120, ["EWL"]), ("Tuas Crescent", 120, ["EWL"])],
		"Tuas Crescent": [("Gul Circle", 120, ["EWL"]), ("Tuas West Road", 120, ["EWL"])],
		"Tuas West Road": [("Tuas Crescent", 120, ["EWL"]), ("Tuas Link", 120, ["EWL"])],
		"Tuas Link": [("Tuas West Road", 120, ["EWL"])],
		# Changi Branch
		"Expo": [("Tanah Merah", 120, ["EWL"]), ("Changi Airport", 120, ["EWL"]), ("Sungei Bedok", 300, ["EWL", "DTL"]), ("Upper Changi", 120, ["DTL"])],  # DTL interchange
		"Changi Airport": [("Expo", 120, ["EWL"])],
		
		# ========== NORTH-EAST LINE (Purple) ==========
		"HarbourFront": [("Outram Park", 120, ["NEL"]), ("Telok Blangah", 120, ["CCL"])],
		"Chinatown": [("Clarke Quay", 120, ["NEL"]), ("Outram Park", 300, ["EWL", "NEL", "DTL", "TEL"]), ("Telok Ayer", 120, ["DTL"])],
		"Clarke Quay": [("Dhoby Ghaut", 120, ["NEL"]), ("Chinatown", 120, ["NEL"])],
		"Little India": [("Dhoby Ghaut", 120, ["NEL"]), ("Farrer Park", 120, ["NEL"]), ("Rochor", 300, ["NEL", "DTL"]), ("Newton", 300, ["NEL", "NSL"])],  # DTL interchange
		"Farrer Park": [("Little India", 120, ["NEL"]), ("Boon Keng", 120, ["NEL"])],
		"Boon Keng": [("Farrer Park", 120, ["NEL"]), ("Potong Pasir", 120, ["NEL"])],
		"Potong Pasir": [("Boon Keng", 120, ["NEL"]), ("Woodleigh", 120, ["NEL"])],
		"Woodleigh": [("Potong Pasir", 120, ["NEL"]), ("Serangoon", 120, ["NEL"])],
		"Serangoon": [("Woodleigh", 120, ["NEL"]), ("Kovan", 120, ["NEL"]), ("Lorong Chuan", 300, ["NEL", "CCL"]), ("Lorong Chuan", 120, ["CCL"])],
		"Kovan": [("Serangoon", 120, ["NEL"]), ("Hougang", 120, ["NEL"])],
		"Hougang": [("Kovan", 120, ["NEL"]), ("Buangkok", 120, ["NEL"])],
		"Buangkok": [("Hougang", 120, ["NEL"]), ("Sengkang", 120, ["NEL"])],
		"Sengkang": [("Buangkok", 120, ["NEL"]), ("Punggol", 120, ["NEL"])],
		"Punggol": [("Sengkang", 120, ["NEL"])],
		
		# ========== CIRCLE LINE (Orange) ==========
		"Promenade": [("Bayfront", 120, ["CCL"]), ("Nicoll Highway", 120, ["CCL"]), ("Esplanade", 300, ["CCL", "DTL"])],  # DTL interchange
		"Nicoll Highway": [("Promenade", 120, ["CCL"]), ("Stadium", 120, ["CCL"])],
		"Stadium": [("Nicoll Highway", 120, ["CCL"]), ("Mountbatten", 120, ["CCL"])],
		"Mountbatten": [("Stadium", 120, ["CCL"]), ("Dakota", 120, ["CCL"])],
		"Dakota": [("Mountbatten", 120, ["CCL"]), ("MacPherson", 120, ["CCL"])],
		"MacPherson": [("Dakota", 120, ["CCL"]), ("Tai Seng", 120, ["CCL"]), ("Paya Lebar", 300, ["CCL", "EWL"]), ("Mattar", 120, ["DTL"])],
		"Tai Seng": [("MacPherson", 120, ["CCL"]), ("Bartley", 120, ["CCL"])],
		"Bartley": [("Tai Seng", 120, ["CCL"]), ("Lorong Chuan", 120, ["CCL"])],
		"Lorong Chuan": [("Bartley", 120, ["CCL"]), ("Serangoon", 120, ["CCL"]), ("Serangoon", 300, ["CCL", "NEL"])],
		"Marymount": [("Caldecott", 120, ["CCL"]), ("Bishan", 120, ["CCL"])],
		"Caldecott": [("Botanic Gardens", 120, ["CCL"]), ("Marymount", 120, ["CCL"]), ("Bishan", 300, ["CCL", "NSL", "TEL"]), ("Upper Thomson", 300, ["TEL", "CCL"])],
		"Botanic Gardens": [("Farrer Road", 120, ["CCL"]), ("Caldecott", 120, ["CCL"]), ("Stevens", 300, ["CCL", "DTL", "NSL", "TEL"])],  # DTL interchange
		"Farrer Road": [("Holland Village", 120, ["CCL"]), ("Botanic Gardens", 120, ["CCL"])],
		"Holland Village": [("Buona Vista", 120, ["CCL"]), ("Farrer Road", 120, ["CCL"])],
		"one-north": [("Kent Ridge", 120, ["CCL"]), ("Buona Vista", 300, ["EWL", "CCL"])],
		"Kent Ridge": [("Haw Par Villa", 120, ["CCL"]), ("one-north", 120, ["CCL"])],
		"Haw Par Villa": [("Pasir Panjang", 120, ["CCL"]), ("Kent Ridge", 120, ["CCL"])],
		"Pasir Panjang": [("Labrador Park", 120, ["CCL"]), ("Haw Par Villa", 120, ["CCL"])],
		"Labrador Park": [("Telok Blangah", 120, ["CCL"]), ("Pasir Panjang", 120, ["CCL"])],
		"Telok Blangah": [("HarbourFront", 120, ["CCL"]), ("Labrador Park", 120, ["CCL"])],
		"Bayfront": [("Marina Bay", 300, ["CCL", "NSL", "TEL"]), ("Promenade", 120, ["CCL"]), ("Downtown", 120, ["DTL"])],
		
		# ========== DOWNTOWN LINE (Blue) ==========
		"Bukit Panjang": [("Cashew", 120, ["DTL"])],
		"Cashew": [("Bukit Panjang", 120, ["DTL"]), ("Hillview", 120, ["DTL"])],
		"Hillview": [("Cashew", 120, ["DTL"]), ("Beauty World", 120, ["DTL"])],
		"Beauty World": [("Hillview", 120, ["DTL"]), ("King Albert Park", 120, ["DTL"])],
		"King Albert Park": [("Beauty World", 120, ["DTL"]), ("Sixth Avenue", 120, ["DTL"])],
		"Sixth Avenue": [("King Albert Park", 120, ["DTL"]), ("Tan Kah Kee", 120, ["DTL"])],
		"Tan Kah Kee": [("Sixth Avenue", 120, ["DTL"]), ("Stevens", 120, ["DTL"])],
		"Stevens": [("Tan Kah Kee", 120, ["DTL"]), ("Newton", 300, ["DTL", "NSL"]), ("Botanic Gardens", 300, ["DTL", "NSL", "CCL", "TEL"]), ("Orchard", 300, ["DTL", "NSL", "TEL"])],  # NSL/CCL/TEL interchange
		"Rochor": [("Bugis", 300, ["EWL", "DTL"]), ("Little India", 300, ["NEL", "DTL"]), ("Esplanade", 300, ["DTL", "CCL"])],
		"Esplanade": [("Promenade", 300, ["CCL", "DTL"]), ("Bras Basah", 120, ["DTL"]), ("Rochor", 300, ["DTL", "NEL", "CCL"])],
		"Bras Basah": [("Esplanade", 120, ["DTL"]), ("Bencoolen", 120, ["DTL"]), ("Dhoby Ghaut", 120, ["DTL", "CCL"])],
		"Bencoolen": [("Bras Basah", 120, ["DTL"]), ("Jalan Besar", 120, ["DTL"])],
		"Jalan Besar": [("Bencoolen", 120, ["DTL"]), ("Bendemeer", 120, ["DTL"])],
		"Bendemeer": [("Jalan Besar", 120, ["DTL"]), ("Geylang Bahru", 120, ["DTL"])],
		"Geylang Bahru": [("Bendemeer", 120, ["DTL"]), ("Mattar", 120, ["DTL"])],
		"Mattar": [("Geylang Bahru", 120, ["DTL"]), ("MacPherson", 120, ["DTL"]), ("Ubi", 300, ["DTL", "CCL"])],  # CCL interchange
		"Ubi": [("Mattar", 300, ["DTL", "CCL"]), ("Kaki Bukit", 120, ["DTL"])],
		"Kaki Bukit": [("Ubi", 120, ["DTL"]), ("Bedok North", 120, ["DTL"])],
		"Bedok North": [("Kaki Bukit", 120, ["DTL"]), ("Bedok Reservoir", 120, ["DTL"])],
		"Bedok Reservoir": [("Bedok North", 120, ["DTL"]), ("Tampines West", 120, ["DTL"])],
		"Tampines West": [("Bedok Reservoir", 120, ["DTL"]), ("Tampines", 300, ["DTL", "EWL"])],
		"Tampines East": [("Tampines", 120, ["DTL"]), ("Upper Changi", 120, ["DTL"])],
		"Upper Changi": [("Tampines East", 120, ["DTL"]), ("Expo", 120, ["DTL"]), ("Sungei Bedok", 120, ["DTL"])],
		"Sungei Bedok": [("Upper Changi", 120, ["DTL"]), ("Bedok South", 300, ["TEL", "DTL"]), ("Expo", 300, ["EWL", "DTL"])],
		"Telok Ayer": [("Downtown", 120, ["DTL"]), ("Chinatown", 120, ["DTL"])],
		"Downtown": [("Bayfront", 120, ["DTL"]), ("Telok Ayer", 120, ["DTL"]), ("Raffles Place", 300, ["DTL", "NSL", "EWL"])],
		
		# ========== THOMSON-EAST COAST LINE (Brown) ==========
		"Woodlands North": [("Woodlands", 120, ["TEL"])],
		"Springleaf": [("Woodlands South", 120, ["TEL"]), ("Lentor", 120, ["TEL"])],
		"Lentor": [("Springleaf", 120, ["TEL"]), ("Mayflower", 120, ["TEL"])],
		"Mayflower": [("Lentor", 120, ["TEL"]), ("Bright Hill", 120, ["TEL"])],
		"Bright Hill": [("Mayflower", 120, ["TEL"]), ("Upper Thomson", 120, ["TEL"])],
		"Upper Thomson": [("Bright Hill", 120, ["TEL"]), ("Caldecott", 300, ["TEL", "CCL"])],
		"Napier": [("Orchard Boulevard", 120, ["TEL"]), ("Orchard", 120, ["TEL"])],
		"Orchard Boulevard": [("Orchard", 120, ["TEL"]), ("Napier", 120, ["TEL"]), ("Great World", 120, ["TEL"])],
		"Great World": [("Havelock", 120, ["TEL"]), ("Orchard Boulevard", 120, ["TEL"])],
		"Havelock": [("Outram Park", 300, ["TEL", "EWL", "NEL"]), ("Great World", 120, ["TEL"])],
		"Maxwell": [("Shenton Way", 120, ["TEL"]), ("Tanjong Pagar", 300, ["TEL", "EWL"])],
		"Shenton Way": [("Marina Bay", 120, ["TEL"]), ("Maxwell", 120, ["TEL"])],
		"Gardens by the Bay": [("Marina Bay", 120, ["TEL"]), ("Tanjong Rhu", 120, ["TEL"])],
		"Tanjong Rhu": [("Gardens by the Bay", 120, ["TEL"]), ("Katong Park", 120, ["TEL"])],
		"Katong Park": [("Tanjong Rhu", 120, ["TEL"]), ("Tanjong Katong", 120, ["TEL"])],
		"Tanjong Katong": [("Katong Park", 120, ["TEL"]), ("Marine Parade", 120, ["TEL"])],
		"Marine Parade": [("Tanjong Katong", 120, ["TEL"]), ("Marine Terrace", 120, ["TEL"])],
		"Marine Terrace": [("Marine Parade", 120, ["TEL"]), ("Siglap", 120, ["TEL"])],
		"Siglap": [("Marine Terrace", 120, ["TEL"]), ("Bayshore", 120, ["TEL"])],
		"Bayshore": [("Siglap", 120, ["TEL"]), ("Bedok South", 120, ["TEL"])],
		"Bedok South": [("Bayshore", 120, ["TEL"]), ("Sungei Bedok", 300, ["TEL", "DTL"])],
		"Sungei Bedok": [("Bedok South", 300, ["TEL", "DTL"]), ("Upper Changi", 120, ["DTL"]), ("Expo", 300, ["EWL", "DTL"])],
	}

# FutureStations adds the announced Thomson-East Coast Line extension to Changi Terminal 5
# and the conversion of the existing Tanah Merah–Expo–Changi Airport stretch to TEL systems.
FutureStations = CurrentStations | {
	"Changi Terminal 5 (TE32/CR1 TEL–CRL interchange)",
	"Tanah Merah (TEL-converted)",
	"Expo (TEL-converted)",
	"Changi Airport (TEL-converted)",
}

def build_mrt_network():
	"""
	Builds the MRT network graph with Station objects.
	Returns a dictionary where keys are station names and values are Station objects
	with connections to other stations.
	
	All travel times are in seconds. Baseline station-to-station travel time with penalties as applicable.
	"""
	
	# Consolidated MRT Network Data with stations and their connections
	mrt_network_data = CurrentStations
	
	# Create all Station objects and build connections in a single pass
	mrt_network = {}
	
	# First pass: Create all Station objects with their lines
	for station_name in mrt_network_data.keys():
		# Extract lines from connections by looking at the network
		lines_set = set()
		for dest_name, travel_time, line_list in mrt_network_data[station_name]:
			lines_set.update(line_list)
		
		mrt_network[station_name] = Station(station_name, list(lines_set))
	
	# Second pass: Add connections between Station objects
	for source_name, connections_list in mrt_network_data.items():
		source_station = mrt_network[source_name]
		for dest_name, travel_time, lines in connections_list:
			if dest_name in mrt_network:
				dest_station = mrt_network[dest_name]
				source_station.add_connection(dest_station, travel_time, lines)
	
	return mrt_network