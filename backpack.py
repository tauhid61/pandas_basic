#Copied a dataframe from lecture video
#pasted the unformatted text in a text file
#Using this py script, formatted the text , and written into 'backpack.csv file'

import csv
list_word = [['Item', 'Category', 'Quantity', 'Weight (oz.)']]
handler = open('backpack.txt')
for line in handler:
    word = line.rstrip().split()
    list_word.append(word)

# data to be written row-wise in csv file
data = list_word
print(data)
# opening the csv file in 'w+' mode
file = open('backpack.csv', 'w+', newline ='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)
