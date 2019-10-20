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

numbers = []
sound = input('Enter sound data: ')
while not sound.isdigit():
    sound = input('Enter sound data: ')

x = 0
sumAll = 0
base = 0
sound.replace('0', '')
while x < len(sound):
    if not sound[x] in numbers:
        numbers.append(sound[x])
        sumAll += int(sound[x])
        base += 1
    x += 1

convertedNum = ''
num = sumAll
while num != 0:
    if num > 1:
        tempNum = num // base
        left = num % base
        num = tempNum
        convertedNum = str(left)
    else:
        convertedNum += '1'
        num = 0

print(str(sumAll), str(base), convertedNum[::-1])