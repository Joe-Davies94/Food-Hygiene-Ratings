# Import required packages
import urllib.request as urllib
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os

# Set current date - two formats
today=date.today()
d1=today.strftime("%d/%m/%Y")
d2=today.strftime("%Y-%m-%d")


# GETTING DATA FROM FOOD STANDARDS AGENCY WEBSITE

# Function to download and name xml files from food standards agency website
def scrapingFunction(url, loc):
    f = (urllib.urlopen(url)).read()
    file=open(str(loc)+".xml", "ab")
    file.write(f)

# Function inputs - URL of each Welsh xml file
print("Downloading xml data")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS551en-GB.xml", "anglesey")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS552en-GB.xml", "blaenauGwent")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS553en-GB.xml", "bridgend")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS555en-GB.xml", "caerphilly")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS556en-GB.xml", "cardiff")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS558en-GB.xml", "carmarthenshire")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS557en-GB.xml", "ceredigon")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS550en-GB.xml", "conwy")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS559en-GB.xml", "denbighshire")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS560en-GB.xml", "flintshire")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS554en-GB.xml", "gwynedd")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS561en-GB.xml", "merthyr")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS562en-GB.xml", "monmouthshire")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS563en-GB.xml", "neathPortTalbot")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS564en-GB.xml", "newport")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS565en-GB.xml", "pembrokeshire")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS566en-GB.xml", "powys")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS567en-GB.xml", "rhondda")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS568en-GB.xml", "swansea")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS569en-GB.xml", "torfaen")
scrapingFunction("http://ratings.food.gov.uk/OpenDataFiles/FHRS570en-GB.xml", "glamorgan")
scrapingFunction("https://ratings.food.gov.uk/OpenDataFiles/FHRS571en-GB.xml","wrexham")



# ANALYSE DATA AND EXPORT TO EXCEL

# Create blank dataframe
df = pd.DataFrame({
})

# function to read xml file, save to locationData, run through BeautifulSoup and save as bsLocationData
def ratingFunction(fxml, locationName):
    global df
    with open(fxml, "r") as f:
        locationData = f.read() 
    bsLocationData = BeautifulSoup(locationData, "xml")

    # Count the number of Ratings at each score
    locationRatingAll = int(len(bsLocationData.find_all("RatingValue")))
    locationRatings5 = int(len(bsLocationData.find_all("RatingValue", string="5")))
    locationRatings4 = int(len(bsLocationData.find_all("RatingValue", string="4")))
    locationRatings3 = int(len(bsLocationData.find_all("RatingValue", string="3")))
    locationRatings2 = int(len(bsLocationData.find_all("RatingValue", string="2")))
    locationRatings1 = int(len(bsLocationData.find_all("RatingValue", string="1")))
    locationRatings0 = int(len(bsLocationData.find_all("RatingValue", string="0")))
    locationRatingsAwarded = int((locationRatings5 + locationRatings4 + locationRatings3 + locationRatings2 + locationRatings1 + locationRatings0))
    locationRatingsA = int(len(bsLocationData.find_all("RatingValue", string="AwaitingInspection")))
    locationRatingsE = int(len(bsLocationData.find_all("RatingValue", string="Exempt")))

    # Add values to dataframe
    df2 = pd.DataFrame({
    "Exempt Ratings":[locationRatingsE],
    "Awaiting Rating":[locationRatingsA],
    "0/5 Ratings":[locationRatings0],
    "1/5 Ratings":[locationRatings1],
    "2/5 Ratings":[locationRatings2],
    "3/5 Ratings":[locationRatings3],
    "4/5 Ratings":[locationRatings4],
    "5/5 Ratings":[locationRatings5],
    "Ratings Awarded":[locationRatingsAwarded],
    "Total Ratings":[locationRatingAll] 
    })
    df2.index = [locationName]
    
    # Append to main dataframe
    df = df.append(df2)
    return df

# Input xml files for the ratingFunction
print("Analysing xml files")    
ratingFunction( "anglesey.xml", "Anglesey")
ratingFunction("blaenauGwent.xml", "Blaenau Gwent")
ratingFunction("bridgend.xml", "Bridgend")
ratingFunction("caerphilly.xml", "Caerphilly")
ratingFunction("cardiff.xml", "Cardiff")
ratingFunction("carmarthenshire.xml", "Carmarthenshire")
print("25%")
ratingFunction("ceredigon.xml", "Ceredigon")
ratingFunction("conwy.xml", "Conwy")
ratingFunction("denbighshire.xml", "Denbigshire")
ratingFunction("flintshire.xml", "Flintshire")
ratingFunction("gwynedd.xml", "Gwynedd")
ratingFunction("merthyr.xml", "Merthyr")
print("50%")
ratingFunction("monmouthshire.xml", "Monmouthshire")
ratingFunction("neathPortTalbot.xml", "Neath Port Talbot")
ratingFunction("newport.xml", "Newport")
ratingFunction("pembrokeshire.xml", "Pembrokeshire")
ratingFunction("powys.xml", "Powys")
print("75%")
ratingFunction("rhondda.xml", "Rhondda")
ratingFunction("swansea.xml", "Swansea")
ratingFunction("torfaen.xml", "Torfaen")
ratingFunction("glamorgan.xml", "Glamorgan")
ratingFunction("wrexham.xml", "Wrexham")
print("100%")

# Add totals row to dataframe. Replace Date figure with actual date.
df.loc["Total"] = df.sum()
df['Date']=d1

# Output dataframe to excel
df.to_excel(d2 + " - Hygiene Ratings.xlsx")


# REMOVE XML FILES

# Function to remove xml files
def removeFunction(name):
    for x in name:
        os.remove(x)

names = ["anglesey.xml", "blaenauGwent.xml", "bridgend.xml", "caerphilly.xml", 
        "cardiff.xml", "carmarthenshire.xml", "ceredigon.xml", "conwy.xml", "denbighshire.xml", 
        "flintshire.xml", "glamorgan.xml", "gwynedd.xml", "merthyr.xml", "monmouthshire.xml", 
        "neathPortTalbot.xml", "newport.xml", "pembrokeshire.xml", "powys.xml", "rhondda.xml", 
        "swansea.xml", "torfaen.xml", "wrexham.xml"]

removeFunction(names)

print("Complete")
