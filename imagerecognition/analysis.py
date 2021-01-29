import boto3

def detect_labels_local_file(photo):

    #define service used
    client=boto3.client('rekognition')
    #define result varible
    resp = ''

    #Open image file
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
    #debug resposes 
    # print('Detected labels in ' + photo)    
    # print(response['Labels'])

    #Iterate thru all detected labels
    for label in response['Labels']:
        #debug msg 
        # print (label['Name'] + ' : ' + str(label['Confidence']))
        #Since result set is displayed by highest possbility first. We decided to only take the most possible result only. 
        #So if the result is empty, add the highest possble one
        if possible_outcome(label) != 'NOT Matched':
            if not resp:
                # resp.append(label['Name'] + ' : ' + str(label['Confidence']))
                resp = possible_outcome(label)
                print(resp)
    #if there is no detected label found, then return no match.
    if not resp:
        return "No Match"
    return resp

#Function to detect the label that we want to file. In this case car search 
def possible_outcome(label):
    switcher={
        'Truck':'truck',
        'Wagon': 'wagon',
        'Sedan':'sedan',
        'Coupe': 'coupe',
        'Hatchback': 'hatchback',
        'Suv': 'suv',
        'Pickup Truck': 'pickup',
        'Convertible':'convertible',

    }
    #debug messag
    # print(switcher.get(label['Name'],'NOT Matched'))
    return switcher.get(label['Name'],'NOT Matched')

