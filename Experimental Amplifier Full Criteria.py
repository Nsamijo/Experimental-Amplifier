print('Enter the sound data and enter "exit" to exit the program')
while True:
    nummers = {'1':False, '2':False, '3':False, '4':False, '5':False, '6':False, '7':False, '8':False, '9':False}
    userInput = input('Enter the sound data: ')
    if userInput == 'exit':
        break
    x = 0
    resultList = {'som':0, 'base':0, 'convNum':''}
    while x < len(userInput):
        if userInput[x] in nummers and not nummers[userInput[x]]:
            nummers[userInput[x]] = True
            resultList['som'] += int(userInput[x])
            resultList['base'] += 1
        x += 1
    som = resultList['som']
    while som != 0:
        if som > 1:
            temp = som // resultList['base']
            left = som % resultList['base']
            resultList['convNum'] += str(left)
            som = temp
        else:
            resultList['convNum'] += '1'
            som = 0
    print(str(resultList['som']), str(resultList['base']), resultList['convNum'][::-1])