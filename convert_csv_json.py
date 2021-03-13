import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    StarShips = []
    
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 
        for row in csvReader: 
            StarShips.append({
                'PutRequest': {
                    'Item': {
                        'Registry': {"S": row['registry']},       
                        'Name': {"S": row['name']},       
                        'ShipClass': {"S": row['ship_class']},       
                        'Description': {"S": row['description']},       
                    }
                }
            })
            # request = {}
            # item = {}
            # data_items['PutRequest'] = {}
            # item['Registry'] = {"S": row['registry']}
            # item['Name'] = {"S": row['name']}
            # item['ShipClass'] = {"S": row['ship_class']}
            # item['Description'] = {"S": row['description']}
            # request['Item'] = item
            # data_items['PutRequest'] = request
            # StarShips.append(data_items)
        data['StarShips'] = StarShips
  
    # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
    #     jsonString = json.dumps(data, indent=4)
    #     jsonf.write(jsonString)
    # res = {}
    # value = 000
    # j=1
    # sub={}

    num_ss_in_file = 25 
    for i in range(math.ceil( len(data['StarShips'])/num_ss_in_file)):
        with open(f'starfleet_{str(i):03d}.json', 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps({'StarShips': data['StarShips'][i*25: (i+1) * 25]}, indent=4)
            jsonf.write(jsonString)


    # for i in range(len(data['StarShips'])):
    #     if i % 25 == 0:
    #         jsonFilePath = f'starfleet_00{str(j)}.json'
    #         # jsonFilePath = 'starfleet_00' + str(j)+ '.json'
    #         res_obj = data['StarShips'][i:i+25]
    #         sub['StarShips'] = res_obj
    #         with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
    #             jsonString = json.dumps(sub, indent=4)
    #         j +=1
    #     else:
    #         continue
                

csvFilePath = r'startfleet.csv'
jsonFilePath = r'starfleet.json'
csv_to_json(csvFilePath, jsonFilePath)
