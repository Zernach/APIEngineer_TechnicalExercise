#!pip install xmltodict
import json 
import xmltodict

def return_seat_info(file_name):

    with open(file_name) as xml_file:
    
        data_dict = xmltodict.parse(xml_file.read())
        root = data_dict['soapenv:Envelope']['soapenv:Body']['ns:OTA_AirSeatMapRS']['ns:SeatMapResponses']['ns:SeatMapResponse']['ns:SeatMapDetails']['ns:CabinClass']
        seat_list = []

        for cabin in root:

            cabin_class = cabin['ns:RowInfo'][0]['@CabinType']

            for row in cabin['ns:RowInfo']:
                
                for seat in row['ns:SeatInfo']:
                    
                    type_of = seat['ns:Features']
                    seat_id = seat['ns:Summary']['@SeatNumber']
                    availability = seat['ns:Summary']['@OccupiedInd']
                    try:
                        price = seat['ns:Fee']['@Amount']
                    except:
                        price = -1
                    
                    seat_list.append({"seat_id": seat_id,
                                    "type_of": type_of,
                                    "cabin_class": cabin_class,
                                    "availability": availability,
                                    "price": price
                                    })
                    
        return json.dumps(seat_list)

json_seat_info = return_seat_info('OTA_AirSeatMapRS.xml')
print(json_seat_info)