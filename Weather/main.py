import csv

"""
# below s code to extract data from the CSV without pandas, ots of clode for just one value!
with open("weather_data.csv","r")as data:
    data = csv.reader(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
"""

# a dataframe in pandas is the table column oF A SHEET, OR CSV
import pandas
data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
#print(type(data)) # this is a dataframe
#print(type(data["temp"])) # this is a panda series, a value within the column of the csv


datadictionary = data.to_dict()
# print(datadictionary)

templist = data["temp"].to_list() # remember the items in the CSV are lists so use [] not ()
# print(templist)

#calculate average temp without panda

average = sum(templist) / len(templist)
# print(f"The average temperature is:",round(average,1),"celcius")

#find average with panda
#averagetemp = data["temp"].mean()
# print(f"The average temp is:",round(data["temp"].mean(),1),"celcius")

#return the max with pandas
# print(f"The highest of the temperatures is:",data["temp"].max())

#you dont need to use strings for the columns i.e data["temp"], panda uses conditions
# print(data.temp) #here panda knows of the key temp in the column

#get a row within the csv using panda
# print(data[data.day =="Monday"])

# print a row that has the highest temp of the week
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

#monday temp converted to farenheit
# monday = data[data.day == "Monday"]
# mondayf = monday.temp * 9/5 + 32
# print(mondayf)

# create a datafrome from scratch
# here is a dictionary of student grades
studentdict = {
    "student" : ["Chris", "john", "Barnabus"],
    "grades" : [99,65,84]
}
studentdata = pandas.DataFrame(studentdict)
print(studentdata)
#input as a csv
studentdata.to_csv("studentdata") #creates a file in the directory of main.py
