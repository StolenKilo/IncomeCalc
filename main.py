from tkinter import *
from PIL import ImageTk, Image

screen1 = Tk()
screen2 = Tk()

# screen1
screen1.geometry("200x600")
screen1.title("expenses")


def cleartext():
    income.delete(0, END)
    rent.delete(0, END)
    electric.delete(0, END)
    water.delete(0, END)
    trash.delete(0, END)
    ngas.delete(0, END)
    car.delete(0, END)
    cinsurance.delete(0, END)
    hinsurance.delete(0, END)
    food.delete(0, END)
    gas.delete(0, END)
    internet.delete(0, END)
    phone.delete(0, END)
    extra.delete(0, END)

clear = Button(screen1, text="Clear Entries", command=cleartext)
clear.pack()


# income
title1 = Label(screen1, text="Enter Income After Taxes")
title1.pack()
income = Entry(screen1, width=10)
income.pack()

# rent
title2 = Label(screen1, text="Enter Rent Cost")
title2.pack()
rent = Entry(screen1, width=10)
rent.pack()

# electric
title3 = Label(screen1, text="Enter Electric Cost")
title3.pack()
electric = Entry(screen1, width=10)
electric.pack()

# water
title4 = Label(screen1, text="Enter Water Cost")
title4.pack()
water = Entry(screen1, width=10)
water.pack()

# trash
title5 = Label(screen1, text="Enter Trash Cost")
title5.pack()
trash = Entry(screen1, width=10)
trash.pack()

# natural gas
title6 = Label(screen1, text="Enter Natural Gas Cost")
title6.pack()
ngas = Entry(screen1, width=10)
ngas.pack()

# car payment
title7 = Label(screen1, text="Enter Car Payment")
title7.pack()
car = Entry(screen1, width=10)
car.pack()

# car insurance
title8 = Label(screen1, text="Enter Car Insurance Cost")
title8.pack()
cinsurance = Entry(screen1, width=10)
cinsurance.pack()

# health insurance
title9 = Label(screen1, text="Enter Health Insurance Cost")
title9.pack()
hinsurance = Entry(screen1, width=10)
hinsurance.pack()

# Food Costs
title10 = Label(screen1, text="Enter Monthly Food Costs")
title10.pack()
food = Entry(screen1, width=10)
food.pack()

# Gas Costs
title11 = Label(screen1, text="Enter Monthly Gasoline Costs")
title11.pack()
gas = Entry(screen1, width=10)
gas.pack()

# Internet/TV
title12 = Label(screen1, text="Enter Internet/Tv Costs")
title12.pack()
internet = Entry(screen1, width=10)
internet.pack()

# Phone bill
title13 = Label(screen1, text="Enter Phone Costs")
title13.pack()
phone = Entry(screen1, width=10)
phone.pack()

# Additional Bills
title14 = Label(screen1, text="Enter Additional bill Costs")
title14.pack()
extra = Entry(screen1, width=10)
extra.pack()

screen2.title("expenses")
screen2.geometry("200x700")

label1 = Label(screen2, text="Expenses")
label1.pack()







def convert():


    prent = round((int(rent.get()) / int(income.get()) * 100), 2)
    prentLabel = Label(screen2, text="Rent Percentage", width=30)
    prentLabel.pack()
    prentLabel2 = Label(screen2, text=str(prent) + "%", width=10)
    prentLabel2.pack()


    pelectric = round((int(electric.get()) / int(income.get()) * 100), 2)
    pelectricLabel = Label(screen2, text="Electric Percentage", width=30)
    pelectricLabel.pack()
    pelectricLabel2 = Label(screen2, text=str(pelectric) + "%", width=10)
    pelectricLabel2.pack()


    pwater = round((int(water.get()) / int(income.get()) * 100), 2)
    pwaterLabel = Label(screen2, text="Water Percentage", width=30)
    pwaterLabel.pack()
    pwaterLabel2 = Label(screen2, text=str(pwater) + "%", width=10)
    pwaterLabel2.pack()

    ptrash = round((int(trash.get()) / int(income.get()) * 100), 2)
    ptrashLabel = Label(screen2, text="Trash Percentage", width=30)
    ptrashLabel.pack()
    ptrashLabel2 = Label(screen2, text=str(ptrash) + "%", width=10)
    ptrashLabel2.pack()

    pngas = round((int(ngas.get()) / int(income.get()) * 100), 2)
    pngasLabel = Label(screen2, text="Natural Gas Percentage", width=30)
    pngasLabel.pack()
    pngasLabel2 = Label(screen2, text=str(pngas) + "%", width=10)
    pngasLabel2.pack()

    pcar = round((int(car.get()) / int(income.get()) * 100), 2)
    pcarLabel = Label(screen2, text="Car Payment Percentage", width=30)
    pcarLabel.pack()
    pcarLabel2 = Label(screen2, text=str(pcar) + "%", width=10)
    pcarLabel2.pack()

    pcinsurance = round((int(cinsurance.get()) / int(income.get()) * 100), 2)
    pcinsuranceLabel = Label(screen2, text="Car Insurance Percentage", width=30)
    pcinsuranceLabel.pack()
    pcinsuranceLabel2 = Label(screen2, text=str(pcinsurance) + "%", width=10)
    pcinsuranceLabel2.pack()

    phinsurance = round((int(hinsurance.get()) / int(income.get()) * 100), 2)
    phinsuranceLabel = Label(screen2, text="Health Insurance Percentage", width=30)
    phinsuranceLabel.pack()
    phinsuranceLabel2 = Label(screen2, text=str(phinsurance) + "%", width=10)
    phinsuranceLabel2.pack()

    pfood = round((int(food.get()) / int(income.get()) * 100), 2)
    pfoodLabel = Label(screen2, text="Food Cost Percentage", width=30)
    pfoodLabel.pack()
    pfoodLabel2 = Label(screen2, text=str(pfood) + "%", width=10)
    pfoodLabel2.pack()

    pgas = round((int(gas.get()) / int(income.get()) * 100), 2)
    pgasLabel = Label(screen2, text="Gasoline Cost Percentage", width=30)
    pgasLabel.pack()
    pgasLabel2 = Label(screen2, text=str(pgas) + "%", width=10)
    pgasLabel2.pack()

    pinternet = round((int(internet.get()) / int(income.get()) * 100), 2)
    pinternetLabel = Label(screen2, text="Internet/Cable Percentage", width=30)
    pinternetLabel.pack()
    pinternetLabel2 = Label(screen2, text=str(pinternet) + "%", width=10)
    pinternetLabel2.pack()

    pphone = round((int(phone.get()) / int(income.get()) * 100), 2)
    pphoneLabel = Label(screen2, text="Phone Percentage", width=30)
    pphoneLabel.pack()
    pphoneLabel2 = Label(screen2, text=str(pphone) + "%", width=10)
    pphoneLabel2.pack()

    pextra = round((int(extra.get()) / int(income.get()) * 100), 2)
    pextraLabel = Label(screen2, text="Extra Bills Percentage", width=30)
    pextraLabel.pack()
    pextraLabel2 = Label(screen2, text=str(pextra) + "%", width=10)
    pextraLabel2.pack()

    extrafunds = int(income.get()) - (int(rent.get()) + int(electric.get()) + int(water.get()) + int(ngas.get()) + int(car.get()) + int(cinsurance.get())
                               + int(hinsurance.get()) + int(food.get()) + int(internet.get()) + int(phone.get()) + int(extra.get()))

    pextrafunds = Label(screen2, text="Extra Income", width=30)
    pextrafunds.pack()
    pextrafunds2 = Label(screen2, text="$" +str(extrafunds), width=10)
    pextrafunds2.pack()


convertButton = Button(screen2, text="Calculate", command=convert)
convertButton.pack()

def close():
    screen1.destroy()
    screen2.destroy()


closeButton = Button(screen2, text="Close Program", command=close)
closeButton.pack()



screen1.mainloop()
screen2.mainloop()
