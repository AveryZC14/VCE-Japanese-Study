# Header row
# Original code by fig
# modifications made by andre
#swag from both of us
# import necessary features
from re import A
#import xlrd
import random
from openpyxl import Workbook,load_workbook
from math import ceil

#initialise variables
#headings={}; tagCol=0; tags={}

# select subject
#xlFile = xlrd.open_workbook("VocabBook.xls")
#options = xlFile.sheet_names()
#vcList = xlFile.sheet_by_index(0)

wb = load_workbook('VocabBook.xlsx')

#1 is sheet1 to sheet2
#2 is sheet2 to sheet1
filter_dir = 0

def one_or_two():
    confirmed = False
    while not confirmed:
        try:
            inp = int(input("which one? (1 or 2):"))
            if inp == 1 or inp == 2:
                confirmed = True
            else:
                print("That's not 1 or 2 :(")
        except:
            print("That's not 1 or 2!!!!!")
    return(inp)


print("Which way do you want to filter?")
print()
print("1 - Sheet1 to Sheet2")
print("2 - Sheet2 to Sheet1")
print()

filter_dir = one_or_two()
if filter_dir == 1:
    from_sheet = wb["Sheet1"]
    from_sheet_2 = wb["Sheet1"]
    to_sheet = wb["Sheet2"]
elif filter_dir == 2:
    from_sheet = wb["Sheet2"]
    to_sheet = wb["Sheet1"]




wb.save('VocabBookCodeBackup.xlsx')

from_words = []
to_words = []

initial_word_amounts_je = {}
initial_word_amounts_ej = {}

#getting from_words
row_num = 0
for row in from_sheet.values:
    row_num +=1
    if (row[1] == None):
        print ("sussy")
        break
    else:
        if row[0] == None:
            from_words[str('A'+str(row_num))] = row[1]
            wb.save('VocabBook.xlsx')
        if row[3] == None:
            from_words[str('D'+str(row_num))] = 0
            wb.save('VocabBook.xlsx')
        if row[4] == None:
            from_words[str('E'+str(row_num))] = 0
            wb.save('VocabBook.xlsx')
        wordrow = []
        if row[0] == None:
            wordrow.append(row[1])
        else:
            wordrow.append(row[0])
            
        for lad in row[1:3]:
            wordrow.append(lad)
        if row[3] == None:
            wordrow.append(0)
        else:
            wordrow.append(row[3])
        if row[4] == None:
            wordrow.append(0)
        else:
            wordrow.append(row[4])
        from_words.append(wordrow)
        initial_word_amounts_je[row_num] = wordrow[3]
        initial_word_amounts_ej[row_num] = wordrow[4]



#getting to_words
row_num = 0
for row in to_sheet.values:
    row_num +=1
    if (row[1] == None):
        print ("sussy")
        break
    else:
        if row[0] == None:
            to_words[str('A'+str(row_num))] = row[1]
            wb.save('VocabBook.xlsx')
        if row[3] == None:
            to_words[str('D'+str(row_num))] = 0
            wb.save('VocabBook.xlsx')
        if row[4] == None:
            to_words[str('E'+str(row_num))] = 0
            wb.save('VocabBook.xlsx')
        wordrow = []
        if row[0] == None:
            wordrow.append(row[1])
        else:
            wordrow.append(row[0])
        for lad in row[1:3]:
            wordrow.append(lad)
        if row[3] == None:
            wordrow.append(0)
        else:
            wordrow.append(row[3])
        if row[4] == None:
            wordrow.append(0)
        else:
            wordrow.append(row[4])
        to_words.append(wordrow)
        initial_word_amounts_je[row_num] = wordrow[3]
        initial_word_amounts_ej[row_num] = wordrow[4]



#removing the first lad from the lads
from_words.pop(0)
to_words.pop(0)

#print(words)
print()
print("boutta filter some lads")
print()
print()

    
# -----------------------End of setup-----------------------

#Ideas:
#No Repeats (pop?)

# -----------------------Begin main-------------------------

filter_thresh = 0
list_index = 0
filtered_words = []
left_words = []

print("Which list do you want to filter with?")
print()
print("1 - English to Japanese list")
print("2 - Japanese to English list")
print()

filter_list = one_or_two()
if filter_list == 1:
    list_index = 3
elif filter_list == 2:
    list_index = 4


if filter_dir == 1:
    print()
    if filter_list == 1:
        print("All vocab in Sheet1 which have a score at or above the threshold in the English to Japanese list will be filtered to Sheet2.")
    elif filter_list == 2:
        print("All vocab in Sheet1 which have a score at or above the threshold in the Japanese to English list will be filtered to Sheet2.")
    print()
    while True:
        try:
            filter_thresh = int(input("what do you want the threshold to be? (whole number please):"))
            print()
            break
        except:
            print("That's not a whole number!")
    print("These will be the filtered out words:")
    print()
    for word in from_words:
        if word[list_index] >= filter_thresh:
            filtered_words.append(word)
        else:
            left_words.append(word)
            
elif filter_dir == 2:
    print()
    if filter_list == 1:
        print("All vocab in Sheet2 which have a score at or below the threshold in the English to Japanese list will be filtered to Sheet1.")
    elif filter_list == 2:
        print("All vocab in Sheet2 which have a score at or below the threshold in the Japanese to English list will be filtered to Sheet1.")
    print()
    while True:
        try:
            filter_thresh = int(input("what do you want the threshold to be? (whole number please):"))
            print()
            break
        except:
            print("That's not a whole number!")
    print("These will be the filtered out words:")
    print()
    for word in from_words:
        if word[list_index] <= filter_thresh:
            filtered_words.append(word)
        else:
            left_words.append(word)


            
for i in filtered_words:
    print (i)
    
print()
print("time to tango with some data")
print()
if filter_dir == 1:
    print("Putting the filtered words into Sheet2...")
elif filter_dir == 2:
    print("Putting the filtered words into sheet1...")

#for word in filtered_words:
#    to_words.append(word)

for row in filtered_words:
    to_sheet.append(row)
wb.save("VocabBook.xlsx")

if filter_dir == 1:
    print("Removing the filtered words from Sheet1...")
elif filter_dir == 2:
    print("Removing the filtered words from Sheet2...")


#from_sheet.delete_cols(1,5)
#from_sheet.append(["漢字","ひらがな","英語","jpn to eng","eng to jpn"])
#for row in left_words:
#    from_sheet.append(row)
filtered_nums = []
row_num = 1
for row in from_sheet.values:
    if list(row[0:5]) in filtered_words:
        filtered_nums.append(row_num)
    row_num += 1


filtered_nums.reverse()

for num in filtered_nums:
    from_sheet.delete_rows(num)

wb.save("VocabBook.xlsx")

print()
print ("Filtered! have a good day :)")
input()
    
