#get sound data, assume the user inputs correct data
een = False
twee = False
drie = False
vier = False
vijf = False
zes = False
zeven = False 
acht = False 
negen = False
sound = input('Enter sound data: ')

length = len(sound)
base = 0
som = 0
x = 0
while x < length:
    temp = sound[x]
    if temp == '1' and een == False:
        een = True
        som = som + 1
        base = base + 1
    elif temp == '2' and twee == False:
        twee = True
        som = som + 2
        base = base + 1
    elif temp == '3' and drie == False:
        drie = True
        som = som + 3
        base = base + 1
    elif temp == '4' and vier == False:
        vier = True
        som = som + 4
        base = base + 1
    elif temp == '5' and vijf == False:
        vijf = True
        som = som + 5
        base = base + 1
    elif temp == '6' and zes == False:
        zes = True
        som = som + 6
        base = base + 1
    elif temp == '7' and zeven == False:
        zeven = True
        som = som + 7
        base = base + 1
    elif temp == '8' and acht == False:
        acht = True
        som = som + 8
        base = base + 1
    elif temp == '9' and negen == False:
        negen = True
        som = som + 9
        base = base + 1
    x = x + 1

convertedNumber = ''
sound = som
while som != 0:
    if som > 1:
        tempSound = som // base
        left = som - (tempSound * base)
        convertedNumber = convertedNumber + str(left)
        som = tempSound
    else:
        convertedNumber = convertedNumber + '1'
        som = 0

print(str(sound) + ' ' + str(base) + ' ' + str(convertedNumber[::-1]))