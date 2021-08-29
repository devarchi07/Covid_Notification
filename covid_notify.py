from typing import final
import requests
from bs4 import BeautifulSoup as bs
from notifypy import Notify
import os


def getval(url):  # functions to get the values from websites using request
    res = requests.get(url)
    return(res.text)


def notifi(title1, message1):  # function to send notifications
    notification = Notify()
    notification.title = title1
    notification.message = message1
    notification.audio = "C:/Users/user/Downloads/Music/swiftly-610.wav"
    notification.icon = "C:/Users/user/Desktop/project/simple app/covid.png"
    notification.send()


def sublist(lst, n):  # function to print sublist from a given list
    sub = []
    result = []
    for i in lst:
        sub += [i]
        if len(sub) == n:
            result += [sub]
            sub = []
    if sub:
        result += [sub]
    return result


if __name__ == "__main__":
    # getting total vaccinated details
    html = getval("https://www.mohfw.gov.in/#")
    nice_html = bs(html, "html.parser")
    vaccinated = nice_html.find(class_="coviddata")
    vaccine = nice_html.find(class_="totalvac")
    res = vaccine.get_text()+vaccinated.get_text()
    print(res)
    # getting the values of the website through beautiful soup
    html1 = getval("https://prsindia.org/covid-19/cases")
    html2 = bs(html1, "html.parser")
    data_list = []
    # loop  to stores the values of the states recived from websites into a list
    for items in html2.find_all("td")[6:223]:
        items1 = items.get_text()
        data_list.append(items1)

    # sending the notification of total vaccine
    notifi(vaccine.get_text(), vaccinated.get_text())
    final_list = sublist(data_list, 6)

    states = ["Delhi", "Maharashtra", "West Bengal"]

    for i in range(0, 36):  # final loop to get the requird states data and send notifications
        # print(final_list[i][0])
        if final_list[i][1] in states:
            notititle = f"{final_list[i][1]}"
            notimessage = f"Confirmed Cases:{final_list[i][2]}\n Active Cases:{final_list[i][3]}\n Discharged:{final_list[i][4]}\n Deaths:{final_list[i][5]}"
            print(notimessage)
            print(notititle)
            notifi(notititle, notimessage)
