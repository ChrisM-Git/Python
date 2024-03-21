#Tally the number of squirrels based on color
import pandas

sqdata = pandas.read_csv("squirreldata.csv")
greysq = len(sqdata[sqdata["Primary Fur Color"] == "Gray"])
cinsq = len(sqdata[sqdata["Primary Fur Color"] == "Cinnamon"])
blacksq = len(sqdata[sqdata["Primary Fur Color"] == "Black"])
print(f"Number of Grey Squirrles: {greysq}")
print(f"Number of Cinnamon Squirrles: {cinsq}")
print(f"Number of White Squirrles: {blacksq}")

datadict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [greysq, cinsq, blacksq]
}

pandas.DataFrame(datadict).to_csv("Furdata.csv")
