#   Copyright 2019 Nathan K. Samijo

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
  
#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


#variables that will be used to check which number has already passed, this way there can be no double
een = False
twee = False
drie = False
vier = False
vijf = False
zes = False
zeven = False 
acht = False 
negen = False

#get sound data, assume the user inputs correct data
sound = input('Enter sound data: ')

#check which number is in the sound data, add that into the sum, increment the base and check off the numbers this way no duplicate will be added to the sum
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

#convert the amplified sound to another base number
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

#print out the results
print(str(sound) + ' ' + str(base) + ' ' + str(convertedNumber[::-1]))