from station import Station, checkSymmetry

CurrentStations = {
	# ========== NORTH-SOUTH LINE (Red) ==========
	"Jurong East": [("Bukit Batok", 120, ["NSL"])],
	"Bukit Batok": [("Jurong East", 120, ["NSL"]), ("Bukit Gombak", 120, ["NSL"])],
	"Bukit Gombak": [("Bukit Batok", 120, ["NSL"]), ("Choa Chu Kang", 120, ["NSL"])],
	"Choa Chu Kang": [("Bukit Gombak", 120, ["NSL"]), ("Yew Tee", 120, ["NSL"])],
	"Yew Tee": [("Choa Chu Kang", 120, ["NSL"]), ("Kranji", 120, ["NSL"])],
	"Kranji": [("Yew Tee", 120, ["NSL"]), ("Marsiling", 120, ["NSL"])],
	"Marsiling": [("Kranji", 120, ["NSL"]), ("Woodlands", 120, ["NSL"])],
	"Woodlands": [("Marsiling", 120, ["NSL"]), ("Admiralty", 120, ["NSL"])],
	"Admiralty": [("Woodlands", 120, ["NSL"]), ("Sembawang", 120, ["NSL"])],
	"Sembawang": [("Admiralty", 120, ["NSL"]), ("Canberra", 120, ["NSL"])],
	"Canberra": [("Sembawang", 120, ["NSL"]), ("Yishun", 120, ["NSL"])],
	"Yishun": [("Canberra", 120, ["NSL"]), ("Khatib", 120, ["NSL"])],
	"Khatib": [("Yishun", 120, ["NSL"]), ("Yio Chu Kang", 120, ["NSL"])],
	"Yio Chu Kang": [("Khatib", 120, ["NSL"]), ("Ang Mo Kio", 120, ["NSL"])],
	"Ang Mo Kio": [("Yio Chu Kang", 120, ["NSL"]), ("Bishan", 120, ["NSL"])],
	"Bishan": [("Ang Mo Kio", 120, ["NSL"]), ("Braddell", 120, ["NSL"]), ("Lorong Chuan", 120, ["CCL"]), ("Marymount", 120, ["CCL"])],
	"Braddell": [("Bishan", 120, ["NSL"]), ("Toa Payoh", 120, ["NSL"])],
	"Toa Payoh": [("Braddell", 120, ["NSL"]), ("Novena", 120, ["NSL"])],
	"Novena": [("Toa Payoh", 120, ["NSL"]), ("Newton", 120, ["NSL"])],
	"Newton": [("Novena", 120, ["NSL"]), ("Orchard", 120, ["NSL"])],
	"Orchard": [("Newton", 120, ["NSL"]), ("Somerset", 120, ["NSL"])],
	"Somerset": [("Orchard", 120, ["NSL"]), ("Dhoby Ghaut", 120, ["NSL"])],
	"Dhoby Ghaut": [("Somerset", 120, ["NSL"]), ("City Hall", 120, ["NSL"]), ("Bras Basah", 120, ["CCL"])],
	"City Hall": [("Dhoby Ghaut", 120, ["NSL"]), ("Raffles Place", 120, ["NSL"])],
	"Raffles Place": [("City Hall", 120, ["NSL"]), ("Marina Bay", 120, ["NSL"])],
	"Marina Bay": [("Raffles Place", 120, ["NSL"]), ("Marina South Pier", 120, ["NSL"]), ("Bayfront", 120, ["CCL"])],
	"Marina South Pier": [("Marina Bay", 120, ["NSL"])],

	# ========== EAST-WEST LINE (Green) ==========
	"Pasir Ris": [("Tampines", 120, ["EWL"])],
	"Tampines": [("Pasir Ris", 120, ["EWL"]), ("Simei", 120, ["EWL"])],
	"Simei": [("Tampines", 120, ["EWL"]), ("Tanah Merah", 120, ["EWL"])],
	"Tanah Merah": [("Simei", 120, ["EWL"]), ("Bedok", 120, ["EWL"]), ("Expo", 120, ["EWL"])],
	"Bedok": [("Tanah Merah", 120, ["EWL"]), ("Kembangan", 120, ["EWL"])],
	"Kembangan": [("Bedok", 120, ["EWL"]), ("Eunos", 120, ["EWL"])],
	"Eunos": [("Kembangan", 120, ["EWL"]), ("Paya Lebar", 120, ["EWL"])],
	"Paya Lebar": [("Eunos", 120, ["EWL"]), ("Aljunied", 120, ["EWL"]), ("Dakota", 120, ["CCL"]), ("MacPherson", 120, ["CCL"])],
	"Aljunied": [("Paya Lebar", 120, ["EWL"]), ("Kallang", 120, ["EWL"])],
	"Kallang": [("Aljunied", 120, ["EWL"]), ("Lavender", 120, ["EWL"])],
	"Lavender": [("Kallang", 120, ["EWL"]), ("Bugis", 120, ["EWL"])],
	"Bugis": [("Lavender", 120, ["EWL"]), ("City Hall", 120, ["EWL"])],
	"Tanjong Pagar": [("Raffles Place", 120, ["EWL"]), ("Outram Park", 120, ["EWL"])],
	"Outram Park": [("Tanjong Pagar", 120, ["EWL"]), ("Tiong Bahru", 120, ["EWL"])],
	"Tiong Bahru": [("Outram Park", 120, ["EWL"]), ("Redhill", 120, ["EWL"])],
	"Redhill": [("Tiong Bahru", 120, ["EWL"]), ("Queenstown", 120, ["EWL"])],
	"Queenstown": [("Redhill", 120, ["EWL"]), ("Commonwealth", 120, ["EWL"])],
	"Commonwealth": [("Queenstown", 120, ["EWL"]), ("Buona Vista", 120, ["EWL"])],
	"Buona Vista": [("Commonwealth", 120, ["EWL"]), ("Dover", 120, ["EWL"]), ("Holland Village", 120, ["CCL"]), ("one-north", 120, ["CCL"])],
	"Dover": [("Buona Vista", 120, ["EWL"]), ("Clementi", 120, ["EWL"])],
	"Clementi": [("Dover", 120, ["EWL"]), ("Jurong East", 120, ["EWL"])],
	"Chinese Garden": [("Jurong East", 120, ["EWL"]), ("Lakeside", 120, ["EWL"])],
	"Lakeside": [("Chinese Garden", 120, ["EWL"]), ("Boon Lay", 120, ["EWL"])],
	"Boon Lay": [("Lakeside", 120, ["EWL"]), ("Pioneer", 120, ["EWL"])],
	"Pioneer": [("Boon Lay", 120, ["EWL"]), ("Joo Koon", 120, ["EWL"])],
	"Joo Koon": [("Pioneer", 120, ["EWL"]), ("Gul Circle", 120, ["EWL"])],
	"Gul Circle": [("Joo Koon", 120, ["EWL"]), ("Tuas Crescent", 120, ["EWL"])],
	"Tuas Crescent": [("Gul Circle", 120, ["EWL"]), ("Tuas West Road", 120, ["EWL"])],
	"Tuas West Road": [("Tuas Crescent", 120, ["EWL"]), ("Tuas Link", 120, ["EWL"])],
	"Tuas Link": [("Tuas West Road", 120, ["EWL"])],
	"Expo": [("Tanah Merah", 120, ["EWL"]), ("Changi Airport", 120, ["EWL"])],
	"Changi Airport": [("Expo", 120, ["EWL"])],

	# ========== NORTH-EAST LINE (Purple) ==========
	"HarbourFront": [("Outram Park", 120, ["NEL"]), ("Telok Blangah", 120, ["CCL"]), ("Bayfront", 120, ["CCL"])],
	"Chinatown": [("Outram Park", 120, ["NEL"]), ("Clarke Quay", 120, ["NEL"])],
	"Clarke Quay": [("Chinatown", 120, ["NEL"]), ("Dhoby Ghaut", 120, ["NEL"])],
	"Little India": [("Dhoby Ghaut", 120, ["NEL"]), ("Farrer Park", 120, ["NEL"])],
	"Farrer Park": [("Little India", 120, ["NEL"]), ("Boon Keng", 120, ["NEL"])],
	"Boon Keng": [("Farrer Park", 120, ["NEL"]), ("Potong Pasir", 120, ["NEL"])],
	"Potong Pasir": [("Boon Keng", 120, ["NEL"]), ("Woodleigh", 120, ["NEL"])],
	"Woodleigh": [("Potong Pasir", 120, ["NEL"]), ("Serangoon", 120, ["NEL"])],
	"Serangoon": [("Woodleigh", 120, ["NEL"]), ("Kovan", 120, ["NEL"]), ("Bartley", 120, ["CCL"]), ("Lorong Chuan", 120, ["CCL"])],
	"Kovan": [("Serangoon", 120, ["NEL"]), ("Hougang", 120, ["NEL"])],
	"Hougang": [("Kovan", 120, ["NEL"]), ("Buangkok", 120, ["NEL"])],
	"Buangkok": [("Hougang", 120, ["NEL"]), ("Sengkang", 120, ["NEL"])],
	"Sengkang": [("Buangkok", 120, ["NEL"]), ("Punggol", 120, ["NEL"]), ("Compassvale", 120, ["SKL"]), ("Ranggung", 120, ["SKL"]), ("Cheng Lim", 120, ["SKL"]), ("Renjong", 120, ["SKL"])],
	"Punggol": [("Sengkang", 120, ["NEL"]), ("Punggol Coast", 120, ["NEL"]), ("Cove", 120, ["PGL"]), ("Damai", 120, ["PGL"]), ("Sam Kee", 120, ["PGL"]), ("Soo Teck", 120, ["PGL"])],
	"Punggol Coast": [("Punggol", 120, ["NEL"])],

	# ========== CIRCLE LINE (Orange) ==========
	"Bras Basah": [("Dhoby Ghaut", 120, ["CCL"]), ("Esplanade", 120, ["CCL"])],
	"Esplanade": [("Bras Basah", 120, ["CCL"]), ("Promenade", 120, ["CCL"])],
	"Promenade": [("Esplanade", 120, ["CCL"]), ("Nicoll Highway", 120, ["CCL"])],
	"Nicoll Highway": [("Promenade", 120, ["CCL"]), ("Stadium", 120, ["CCL"])],
	"Stadium": [("Nicoll Highway", 120, ["CCL"]), ("Mountbatten", 120, ["CCL"])],
	"Mountbatten": [("Stadium", 120, ["CCL"]), ("Dakota", 120, ["CCL"])],
	"Dakota": [("Mountbatten", 120, ["CCL"]), ("Paya Lebar", 120, ["CCL"])],
	"MacPherson": [("Paya Lebar", 120, ["CCL"]), ("Tai Seng", 120, ["CCL"])],
	"Tai Seng": [("MacPherson", 120, ["CCL"]), ("Bartley", 120, ["CCL"])],
	"Bartley": [("Tai Seng", 120, ["CCL"]), ("Serangoon", 120, ["CCL"])],
	"Lorong Chuan": [("Serangoon", 120, ["CCL"]), ("Bishan", 120, ["CCL"])],
	"Marymount": [("Bishan", 120, ["CCL"]), ("Caldecott", 120, ["CCL"])],
	"Caldecott": [("Marymount", 120, ["CCL"]), ("Botanic Gardens", 120, ["CCL"])],
	"Botanic Gardens": [("Caldecott", 120, ["CCL"]), ("Farrer Road", 120, ["CCL"])],
	"Farrer Road": [("Botanic Gardens", 120, ["CCL"]), ("Holland Village", 120, ["CCL"])],
	"Holland Village": [("Farrer Road", 120, ["CCL"]), ("Buona Vista", 120, ["CCL"])],
	"one-north": [("Buona Vista", 120, ["CCL"]), ("Kent Ridge", 120, ["CCL"])],
	"Kent Ridge": [("one-north", 120, ["CCL"]), ("Haw Par Villa", 120, ["CCL"])],
	"Haw Par Villa": [("Kent Ridge", 120, ["CCL"]), ("Pasir Panjang", 120, ["CCL"])],
	"Pasir Panjang": [("Haw Par Villa", 120, ["CCL"]), ("Labrador Park", 120, ["CCL"])],
	"Labrador Park": [("Pasir Panjang", 120, ["CCL"]), ("Telok Blangah", 120, ["CCL"])],
	"Telok Blangah": [("Labrador Park", 120, ["CCL"]), ("HarbourFront", 120, ["CCL"])],
	"Bayfront": [("HarbourFront", 120, ["CCL"]), ("Marina Bay", 120, ["CCL"])],

	# ========== DOWNTOWN LINE (Blue) ==========
	"Bukit Panjang": [("Cashew", 120, ["DTL"]), ("Phoenix", 120, ["BPL"]), ("Petir", 120, ["BPL"])],
	"Cashew": [("Bukit Panjang", 120, ["DTL"]), ("Hillview", 120, ["DTL"])],
	"Hillview": [("Cashew", 120, ["DTL"]), ("Hume", 120, ["DTL"])],
	"Hume": [("Hillview", 120, ["DTL"]), ("Beauty World", 120, ["DTL"])],
	"Beauty World": [("Hume", 120, ["DTL"]), ("King Albert Park", 120, ["DTL"])],
	"King Albert Park": [("Beauty World", 120, ["DTL"]), ("Sixth Avenue", 120, ["DTL"])],
	"Sixth Avenue": [("King Albert Park", 120, ["DTL"]), ("Tan Kah Kee", 120, ["DTL"])],
	"Tan Kah Kee": [("Sixth Avenue", 120, ["DTL"]), ("Botanic Gardens", 120, ["DTL"])],
	"Stevens": [("Botanic Gardens", 120, ["DTL"]), ("Newton", 120, ["DTL"])],
	"Rochor": [("Little India", 120, ["DTL"]), ("Bugis", 120, ["DTL"])],
	"Downtown": [("Bayfront", 120, ["DTL"]), ("Telok Ayer", 120, ["DTL"])],
	"Telok Ayer": [("Downtown", 120, ["DTL"]), ("Chinatown", 120, ["DTL"])],
	"Fort Canning": [("Chinatown", 120, ["DTL"]), ("Bencoolen", 120, ["DTL"])],
	"Bencoolen": [("Fort Canning", 120, ["DTL"]), ("Jalan Besar", 120, ["DTL"])],
	"Jalan Besar": [("Bencoolen", 120, ["DTL"]), ("Bendemeer", 120, ["DTL"])],
	"Bendemeer": [("Jalan Besar", 120, ["DTL"]), ("Geylang Bahru", 120, ["DTL"])],
	"Geylang Bahru": [("Bendemeer", 120, ["DTL"]), ("Mattar", 120, ["DTL"])],
	"Mattar": [("Geylang Bahru", 120, ["DTL"]), ("MacPherson", 120, ["DTL"])],
	"Ubi": [("MacPherson", 120, ["DTL"]), ("Kaki Bukit", 120, ["DTL"])],
	"Kaki Bukit": [("Ubi", 120, ["DTL"]), ("Bedok North", 120, ["DTL"])],
	"Bedok North": [("Kaki Bukit", 120, ["DTL"]), ("Bedok Reservoir", 120, ["DTL"])],
	"Bedok Reservoir": [("Bedok North", 120, ["DTL"]), ("Tampines West", 120, ["DTL"])],
	"Tampines West": [("Bedok Reservoir", 120, ["DTL"]), ("Tampines", 120, ["DTL"])],
	"Tampines East": [("Tampines", 120, ["DTL"]), ("Upper Changi", 120, ["DTL"])],
	"Upper Changi": [("Tampines East", 120, ["DTL"]), ("Expo", 120, ["DTL"])],

	# ========== THOMSON-EAST COAST LINE (Brown) ==========
	"Woodlands North": [("Woodlands", 120, ["TEL"])],
	"Woodlands South": [("Woodlands", 120, ["TEL"]), ("Springleaf", 120, ["TEL"])],
	"Springleaf": [("Woodlands South", 120, ["TEL"]), ("Lentor", 120, ["TEL"])],
	"Lentor": [("Springleaf", 120, ["TEL"]), ("Mayflower", 120, ["TEL"])],
	"Mayflower": [("Lentor", 120, ["TEL"]), ("Bright Hill", 120, ["TEL"])],
	"Bright Hill": [("Mayflower", 120, ["TEL"]), ("Upper Thomson", 120, ["TEL"])],
	"Upper Thomson": [("Bright Hill", 120, ["TEL"]), ("Caldecott", 120, ["TEL"])],
	"Mount Pleasant": [("Caldecott", 120, ["TEL"]), ("Stevens", 120, ["TEL"])],
	"Napier": [("Stevens", 120, ["TEL"]), ("Orchard Boulevard", 120, ["TEL"])],
	"Orchard Boulevard": [("Napier", 120, ["TEL"]), ("Orchard", 120, ["TEL"])],
	"Great World": [("Orchard", 120, ["TEL"]), ("Havelock", 120, ["TEL"])],
	"Havelock": [("Great World", 120, ["TEL"]), ("Outram Park", 120, ["TEL"])],
	"Maxwell": [("Outram Park", 120, ["TEL"]), ("Shenton Way", 120, ["TEL"])],
	"Shenton Way": [("Maxwell", 120, ["TEL"]), ("Marina Bay", 120, ["TEL"])],
	"Marina South": [("Marina Bay", 120, ["TEL"]), ("Gardens by the Bay", 120, ["TEL"])],
	"Gardens by the Bay": [("Marina South", 120, ["TEL"]), ("Tanjong Rhu", 120, ["TEL"])],
	"Tanjong Rhu": [("Gardens by the Bay", 120, ["TEL"]), ("Katong Park", 120, ["TEL"])],
	"Katong Park": [("Tanjong Rhu", 120, ["TEL"]), ("Tanjong Katong", 120, ["TEL"])],
	"Tanjong Katong": [("Katong Park", 120, ["TEL"]), ("Marine Parade", 120, ["TEL"])],
	"Marine Parade": [("Tanjong Katong", 120, ["TEL"]), ("Marine Terrace", 120, ["TEL"])],
	"Marine Terrace": [("Marine Parade", 120, ["TEL"]), ("Siglap", 120, ["TEL"])],
	"Siglap": [("Marine Terrace", 120, ["TEL"]), ("Bayshore", 120, ["TEL"])],
	"Bayshore": [("Siglap", 120, ["TEL"])],

	# ========== BUKIT PANJANG LRT (BP) ==========
	"Choa Chu Kang": [("Bukit Gombak", 120, ["NSL"]), ("Yew Tee", 120, ["NSL"]), ("South View", 120, ["BPL"])],
	"South View": [("Choa Chu Kang", 120, ["BPL"]), ("Keat Hong", 120, ["BPL"])],
	"Keat Hong": [("South View", 120, ["BPL"]), ("Teck Whye", 120, ["BPL"])],
	"Teck Whye": [("Keat Hong", 120, ["BPL"]), ("Phoenix", 120, ["BPL"])],
	"Phoenix": [("Teck Whye", 120, ["BPL"]), ("Bukit Panjang", 120, ["BPL"])],
	"Petir": [("Bukit Panjang", 120, ["BPL"]), ("Pending", 120, ["BPL"])],
	"Pending": [("Petir", 120, ["BPL"]), ("Bangkit", 120, ["BPL"])],
	"Bangkit": [("Pending", 120, ["BPL"]), ("Fajar", 120, ["BPL"])],
	"Fajar": [("Bangkit", 120, ["BPL"]), ("Segar", 120, ["BPL"])],
	"Segar": [("Fajar", 120, ["BPL"]), ("Jelapang", 120, ["BPL"])],
	"Jelapang": [("Segar", 120, ["BPL"]), ("Senja", 120, ["BPL"])],
	"Senja": [("Jelapang", 120, ["BPL"]), ("Ten Mile Junction", 120, ["BPL"])],
	"Ten Mile Junction": [("Senja", 120, ["BPL"]), ("Choa Chu Kang", 120, ["BPL"])],

	# ========== SENGKANG LRT (SK) ==========
	"Compassvale": [("Sengkang", 120, ["SKL"]), ("Rumbia", 120, ["SKL"])],
	"Rumbia": [("Compassvale", 120, ["SKL"]), ("Bakau", 120, ["SKL"])],
	"Bakau": [("Rumbia", 120, ["SKL"]), ("Kangkar", 120, ["SKL"])],
	"Kangkar": [("Bakau", 120, ["SKL"]), ("Ranggung", 120, ["SKL"])],
	"Ranggung": [("Kangkar", 120, ["SKL"]), ("Sengkang", 120, ["SKL"])],
	"Cheng Lim": [("Sengkang", 120, ["SKL"]), ("Farmway", 120, ["SKL"])],
	"Farmway": [("Cheng Lim", 120, ["SKL"]), ("Kupang", 120, ["SKL"])],
	"Kupang": [("Farmway", 120, ["SKL"]), ("Thanggam", 120, ["SKL"])],
	"Thanggam": [("Kupang", 120, ["SKL"]), ("Fernvale", 120, ["SKL"])],
	"Fernvale": [("Thanggam", 120, ["SKL"]), ("Layar", 120, ["SKL"])],
	"Layar": [("Fernvale", 120, ["SKL"]), ("Tongkang", 120, ["SKL"])],
	"Tongkang": [("Layar", 120, ["SKL"]), ("Renjong", 120, ["SKL"])],
	"Renjong": [("Tongkang", 120, ["SKL"]), ("Sengkang", 120, ["SKL"])],

	# ========== PUNGGOL LRT (PG) ==========
	"Cove": [("Punggol", 120, ["PGL"]), ("Meridian", 120, ["PGL"])],
	"Meridian": [("Cove", 120, ["PGL"]), ("Coral Edge", 120, ["PGL"])],
	"Coral Edge": [("Meridian", 120, ["PGL"]), ("Riviera", 120, ["PGL"])],
	"Riviera": [("Coral Edge", 120, ["PGL"]), ("Kadaloor", 120, ["PGL"])],
	"Kadaloor": [("Riviera", 120, ["PGL"]), ("Oasis", 120, ["PGL"])],
	"Oasis": [("Kadaloor", 120, ["PGL"]), ("Damai", 120, ["PGL"])],
	"Damai": [("Oasis", 120, ["PGL"]), ("Punggol", 120, ["PGL"])],
	"Sam Kee": [("Punggol", 120, ["PGL"]), ("Teck Lee", 120, ["PGL"])],
	"Teck Lee": [("Sam Kee", 120, ["PGL"]), ("Punggol Point", 120, ["PGL"])],
	"Punggol Point": [("Teck Lee", 120, ["PGL"]), ("Samudera", 120, ["PGL"])],
	"Samudera": [("Punggol Point", 120, ["PGL"]), ("Nibong", 120, ["PGL"])],
	"Nibong": [("Samudera", 120, ["PGL"]), ("Sumang", 120, ["PGL"])],
	"Sumang": [("Nibong", 120, ["PGL"]), ("Soo Teck", 120, ["PGL"])],
	"Soo Teck": [("Sumang", 120, ["PGL"]), ("Punggol", 120, ["PGL"])],
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
