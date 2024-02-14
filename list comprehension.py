#wyrazenie listowne

numbers = [1, 2, 3, 4, 5, 6]

expo2 = []
for number in numbers:
    expo2.append(number**2)
print(expo2)

twoExpo2 = [number**2 for number in numbers]



#inny zapis
twoExpo2 = [number**2
         for number in numbers
        ]

#wiekszy zakres liczb:
twoExpo2 = [number **2
            for number in range(20)
            ]


print(twoExpo2)
#----------------------------------------

evenNumbers = []
for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)
        
print(evenNumbers)


evenNumbers2 = [number for number in numbers
                if number % 2 == 0
                ]

#wiekszy zakres liczb:
evenNumbers2 = [number for number in range(20)
                if number % 2 == 0
                ]

print(evenNumbers2)


