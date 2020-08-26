#!pip install xmltodict
import json 
import xmltodict

def return_seat_info(file_name):
    """
    Takes the file_name of an XML file containing airplane seat information,
    and returns only the most relevant information in a clean, concise, JSON object.
    """

    with open(file_name) as xml_file:
        
        # Convert XML file to a navigable dict object.
        data_dict = xmltodict.parse(xml_file.read())

        # Peel back the dict objects layers til we get to the info that we need.
        root = data_dict['soapenv:Envelope']['soapenv:Body']['ns:OTA_AirSeatMapRS']['ns:SeatMapResponses']['ns:SeatMapResponse']['ns:SeatMapDetails']['ns:CabinClass']
        
        # Generate a seat_list and iterate through all cabins, all rows, and all seats.
        seat_list = []
        for cabin in root:

            cabin_class = cabin['ns:RowInfo'][0]['@CabinType']

            for row in cabin['ns:RowInfo']:
                
                for seat in row['ns:SeatInfo']:
                    
                    type_of = seat['ns:Features']
                    seat_id = seat['ns:Summary']['@SeatNumber']
                    availability = seat['ns:Summary']['@OccupiedInd']

                    # Check if price info is available. If not available, assign price as -1.
                    try:
                        price = seat['ns:Fee']['@Amount']
                    except:
                        price = -1
                    
                    # Cram the info from this seat into a dict, and add dict to seat_list.
                    seat_list.append({"seat_id": seat_id,
                                    "type_of": type_of,
                                    "cabin_class": cabin_class,
                                    "availability": availability,
                                    "price": price
                                    })
                    
        return json.dumps(seat_list)

json_seats = return_seat_info("OTA_AirSeatMapRS.xml")
print(json_seats)
with open('seats_info.json', 'w') as json_file:
    json.dump(json_seats, json_file)