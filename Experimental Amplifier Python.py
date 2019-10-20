#   Copyright [2019] [Nathan K. Samijo]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#   
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


#list to check which insturments are playing, use 10 variables so a range of 1 - 9 is available
numbers = [False, False, False, False, False, False, False, False, False, False]

def getGoodInput(stuff):
    '''this function filters out bad input and converts a string to an int'''
    temp = input(stuff)
    while not temp.isdigit() and temp != 'exit':
        temp = input(stuff)

    if temp == 'exit':
        return '#'
    else:
        return temp

def updateNumberList(sound=0):
    '''check what numbers are given and by default reset out numberslist '''
    global numbers

    if sound == 0:
        numbers = [False] * 10
        return 

    length = len(sound)
    for x in range(length):
        if numbers[int(sound[x])] == False:
            numbers[int(sound[x])] = True
    return numbers

def outputCalculation():
    '''will calculate our output'''
    global numbers
    convertedToBase = ''

    def quickMaths(num, base=10):
        '''dedicated to calculating the number in another base'''
        binNum = ''
        while num != 0:
            if num > 1:
                tempNum = num // base
                left = num % base
                num = tempNum
                binNum += str(left)
            else:
                binNum += '1'
                num = 0
        return binNum[::-1]


    def getBase():
        '''get the base by checking how many numbers have been used'''
        base = 0
        for x in numbers:
            if x:
                base += 1
        return base

    def sumInstruments():
        '''calculate the sum of all the numbers'''
        som = 0
        x = 1
        while x != len(numbers):
            if numbers[x]:
                som += x
            x += 1
        return som

    if getBase() > 1:
        total = sumInstruments()
        return total, getBase(), quickMaths(total, getBase())
    else:
        return sumInstruments(), getBase(), quickMaths(sumInstruments())
    


while True:
    inputData = getGoodInput('Please enter sound data: ')
    if inputData == '#':
        break
    updateNumberList(inputData)
    processedData = outputCalculation()
    print(str(processedData[0]), str(processedData[1]), processedData[2])
    updateNumberList()