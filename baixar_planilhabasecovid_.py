import wget
URL = "https://covid.ourworldindata.org/data/owid-covid-data.xlsx"
response = wget.download(URL, "owid-covid-data.xlsx")
