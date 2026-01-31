import csv
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from mrtNetwork import CurrentStations

# MRT lines ordered from oldest to newest with official station sequences
line_sequences = {
    'NSL': [  # North-South Line - Jurong East to Marina South Pier
        'Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee',
        'Kranji', 'Marsiling', 'Woodlands', 'Admiralty', 'Sembawang', 'Canberra',
        'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio', 'Bishan', 'Braddell',
        'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut',
        'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South Pier'
    ],
    'EWL': [  # East-West Line - Tuas Link to Pasir Ris
        'Tuas Link', 'Tuas West Road', 'Tuas Crescent', 'Gul Circle', 'Joo Koon',
        'Pioneer', 'Boon Lay', 'Lakeside', 'Chinese Garden', 'Jurong East', 'Clementi',
        'Dover', 'Buona Vista', 'Commonwealth', 'Queenstown', 'Redhill', 'Tiong Bahru',
        'Outram Park', 'Tanjong Pagar', 'Raffles Place', 'City Hall', 'Bugis', 'Lavender',
        'Kallang', 'Aljunied', 'Paya Lebar', 'Eunos', 'Kembangan', 'Bedok', 'Tanah Merah',
        'Simei', 'Tampines', 'Pasir Ris', 'Expo', 'Changi Airport'
    ],
    'NEL': [  # North-East Line - HarbourFront to Punggol Coast
        'HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut',
        'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh',
        'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol', 'Punggol Coast'
    ],
    'CCL': [  # Circle Line - HarbourFront, splits at Promenade
        'HarbourFront', 'Telok Blangah', 'Labrador Park', 'Pasir Panjang', 'Haw Par Villa',
        'Kent Ridge', 'one-north', 'Buona Vista', 'Holland Village', 'Farrer Road',
        'Botanic Gardens', 'Caldecott', 'Marymount', 'Bishan', 'Lorong Chuan', 'Serangoon',
        'Bartley', 'Tai Seng', 'MacPherson', 'Paya Lebar', 'Dakota', 'Mountbatten',
        'Stadium', 'Nicoll Highway', 'Promenade', 'Bayfront', 'Marina Bay',
        'Esplanade', 'Bras Basah', 'Dhoby Ghaut'
    ],
    'DTL': [  # Downtown Line - Bukit Panjang to Expo
        'Bukit Panjang', 'Cashew', 'Hillview', 'Hume', 'Beauty World', 'King Albert Park',
        'Sixth Avenue', 'Tan Kah Kee', 'Botanic Gardens', 'Stevens', 'Newton', 'Little India',
        'Rochor', 'Bugis', 'Downtown', 'Bayfront', 'Telok Ayer', 'Chinatown', 'Fort Canning',
        'Bencoolen', 'Jalan Besar', 'Bendemeer', 'Geylang Bahru', 'Mattar', 'MacPherson',
        'Ubi', 'Kaki Bukit', 'Bedok North', 'Bedok Reservoir', 'Tampines West', 'Tampines',
        'Tampines East', 'Upper Changi', 'Expo'
    ],
    'TEL': [  # Thomson-East Coast Line - Woodlands North to Bayshore
        'Woodlands North', 'Woodlands', 'Woodlands South', 'Springleaf', 'Lentor',
        'Mayflower', 'Bright Hill', 'Upper Thomson', 'Caldecott', 'Mount Pleasant',
        'Stevens', 'Napier', 'Orchard Boulevard', 'Orchard', 'Great World', 'Havelock',
        'Outram Park', 'Maxwell', 'Shenton Way', 'Marina Bay', 'Marina South', 'Gardens by the Bay',
        'Tanjong Rhu', 'Katong Park', 'Tanjong Katong', 'Marine Parade', 'Marine Terrace',
        'Siglap', 'Bayshore'
    ],
    'BPL': [  # Bukit Panjang LRT - Loop
        'Choa Chu Kang', 'South View', 'Keat Hong', 'Teck Whye', 'Phoenix', 'Bukit Panjang',
        'Petir', 'Pending', 'Bangkit', 'Fajar', 'Segar', 'Jelapang', 'Senja', 'Ten Mile Junction'
    ],
    'SKL': [  # Sengkang LRT - East and West Loops
        'Sengkang', 'Compassvale', 'Rumbia', 'Bakau', 'Kangkar', 'Ranggung',
        'Cheng Lim', 'Farmway', 'Kupang', 'Thanggam', 'Fernvale', 'Layar', 'Tongkang', 'Renjong'
    ],
    'PGL': [  # Punggol LRT - East and West Loops
        'Punggol', 'Cove', 'Meridian', 'Coral Edge', 'Riviera', 'Kadaloor', 'Oasis', 'Damai',
        'Sam Kee', 'Teck Lee', 'Punggol Point', 'Samudera', 'Nibong', 'Sumang', 'Soo Teck'
    ]
}

line_names = {
    'NSL': 'North-South Line',
    'EWL': 'East-West Line',
    'NEL': 'North-East Line',
    'CCL': 'Circle Line',
    'DTL': 'Downtown Line',
    'TEL': 'Thomson-East Coast Line',
    'BPL': 'Bukit Panjang LRT',
    'SKL': 'Sengkang LRT',
    'PGL': 'Punggol LRT'
}

line_order = ['NSL', 'EWL', 'NEL', 'CCL', 'DTL', 'TEL', 'BPL', 'SKL', 'PGL']

output_path = os.path.join(PROJECT_ROOT, "Data", "mrt_connections.csv")
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Line', 'Line_Name', 'Station', 'Destination', 'Travel_Time_Seconds'])
    
    rows = []
    for line in line_order:
        stations = line_sequences[line]
        for i, station in enumerate(stations):
            if station in CurrentStations:
                for dest, time, lines in CurrentStations[station]:
                    if line in lines:
                        rows.append([line, line_names[line], station, dest, time])
    
    writer.writerows(rows)
    print(f'✓ Reorganized mrt_connections.csv with correct official station sequences')
    print(f'✓ Output: {output_path}')
    print(f'✓ Total connections: {len(rows)}')
    print()
    for line in line_order:
        count = sum(1 for r in rows if r[0] == line)
        num_stations = len(line_sequences[line])
        print(f'  {line} ({line_names[line]}): {num_stations} stations, {count} connections')
