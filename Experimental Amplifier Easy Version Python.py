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

#list to check which numbers have past
numbers = []

#ask for data
sound = input('Enter sound data: ')

#calculate the base and sum, while checking which number has already been past
x = 0
sumAll = 0
base = 0
while x < len(sound):
    if not sound[x] in numbers and sound[x] != '0' and sound[x].isdigit():
        numbers.append(sound[x])
        sumAll += int(sound[x])
        base += 1
    x += 1

#set our base to 10 if the base equals 1
if base == 1:
    base = 10

#convert the sum to base number
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

#print result
print(str(sumAll), str(base), convertedNum[::-1])