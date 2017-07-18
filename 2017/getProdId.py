import json
import csv

with open("SA_demo_products.json") as json_file:
    json_data = json.load(json_file)

    i=0
            
    f = open("SA_demo_products_parsed.csv", 'wb+')
    fieldnames = ('Product Id', 'Title', 'coverImageURL')
    writer = csv.DictWriter(f, fieldnames=fieldnames)   
    headers = dict( (n,n) for n in fieldnames )
    writer.writerow(headers)

    try:

        for instance in json_data:
            print instance
            print i
            i = i+1
            prodID = json.dumps(instance["id"])
            prodTitle = json.dumps(instance["title"])
            prodCover = json.dumps(instance["coverImageURL"]["url"])

        ##        print prodID.replace('\"','')

            writer.writerow({'Product Id':prodID.replace('\"',''),
                                  'Title':prodTitle.replace('\"',''),
                                  'coverImageURL':prodCover.replace('\"','')})
                                                            
    finally:
        f.close()


