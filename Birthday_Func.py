"""
Created on Wed Dec  7 21:46:08 2022

@author: U410558
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

class Birthday:
    def __init__(self, Availability_start, Availability_end, Budget, Template_Select, N):
        self.Availability_start = Availability_start
        self.Avialibility_end = Availability_end
        self.Budget = Budget 
        self.Template_Select = Template_Select
        self.N = N

    def SelectAvailability(self):
       #r = range(str(availability_start), str(availability_end))
       r = pd.date_range(start=self.availability_start,end=self.availability_end)
       start_date = str(input('Enter the start date: '))
       end_date = str(input('Enter the End date: '))
       #for i in availability_start, availability_end:
       if start_date and end_date in r:
          print('Hotel Venu is available in the mentioned dates')
       else:
          print('Venues are not available in this dates')
          
    def Population(self):
        list1 = []
        if self.N <= 50:
            print('The Population is less than 50')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
           
        elif self.N >= 51 and self.N <=100:
            print('The Population is 100')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        elif self.N >= 101 and self.N <=150:
            print('The Population is 150')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        elif self.N >= 151 and self.N <=200:
            print('The Population is 200')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        elif self.N >= 201 and self.N <=250:
            print('The Population is 250')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        elif self.N >= 251 and self.N <=300:
            print('The Population is 300')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        elif self.N >= 301 and self.N <=350:
            print('The Population is 350')
            for i in range(self.N):
                x = str(input('Enter the Names of the people'))
                list1.append(x)
        else:
            print('The above range needs an exclusive pplan')
           
            return list1, self.N
          
    def SelectCake(self):
        dict1 = {'cake1':'Chocolate', 'cake2':'Strawberry'}
        x = str(input('Select the cake template: '))
        if x == 'cake1':
            print('The order has been sent to the Bakery1')
            print('We will notify once it is done')
        elif x == 'cake2':
            print('The order has been sent to the Bakery1')
            print('We will notify once it is done')
            
    def SelectWishingcard(self):
        list1 = ['Wishingcard1', 'wishingcard2']
        x = str(input('Select the wishing card'))
        X1 = []
        for i in list1:
            if i in list1[0]:
                X1.append(str('Enter the Birthday boy name: '))
                X1.append(str('Enter the Birthday Boy dad name: '))
                X1.append(str('Enter the Birthday Boy dad name: '))
                print('The Template1 has been sent to the Printer Guy')
            else:
                print('Please select one of the template')
    
    def CateringService(self):
        Availability_suppliers = ['Jayanth', 'Rajesh', 'Brijesh', 'Ram']
        print('Availability_suppliers')
        #N = int(input('Enter the Number: '))
        N1 = int(input('The frequency of cooking per day(if three times a day, then for two days, the frequency is 6): '))
        if N1 <= 3:
            print('The base price of the catering service is 5000 Rupees')
        elif N1 > 3 and N1 <=6:
            print('The base price of the catering service is 8000 Rupees')
        elif N1 > 6 and N1 <=9:
            print('The base price of the catering service is 10000 Rupees')
        else:
            print('The base price is 15000')
           
        def get_cusine_list(self):
            #Option to choose the veg or non-veg
            if self.N <= 1000:
                N2 = int(input('Enter the number of items(For example ten items): '))
                print('The Population is below 1000')
                list4 = []
                for i in range(N2):
                    x = str(input('Enter the Name of the items'))
                    list4.append(x)
            elif self.N >= 1001 and self.N <= 1500:
                N2 = int(input('Enter the number of items(For example ten items): '))
                print('The Population is in between 1001 and 1500')
                list4 = []
                for i in range(N2):
                    x = str(input('Enter the Name of the items'))
                    list4.append(x)
            else:
                N2 = int(input('Enter the number of items(For example ten items): '))
                print('The Population is in between more than 1500')
                list4 = []
                for i in range(N2):
                    x = str(input('Enter the Name of the items'))
                    list4.append(x)
       
        if self.N <=1000 and N1 <=3:
            print('The catering service costs: 10000')
        elif self.N >= 1001 and self.N <= 1500 and N1 > 3 and N1 <=6:
            print('The catering service costs: 20000')
        elif self.N > 1500 and N1 > 6 and N1 <=9:
            print('The catering service costs: 30000')
        else:
            print('The catering service is 40000')
           
        print('The catering services may differ based on the vegetable price movements')
                
        
        def ValueAdditionFeatures(self):
            #Value addition features, where the remaining food can be sent to the oldage homes or orphanages. 
            options = ['Yes', 'No']
            for i in options:
                if i == 'Yes':
                    x = int(input('For how many people does the remaining food sufficient: '))
                    if x <= 50:
                        print('Sent to Shiridi Orphanage')
                    elif x >51 and x <=100:
                        print('Sent to Laxmi orphanage')
                    elif x >101 and x <=200:
                        print('Sent to Orphanage')
                    else:
                        print('Contact our office to know the better place')
                else:
                    print('No problem, have a great wedding')
            return 
        
        
        #list1= ([12,13,14,15,16])
       
        def PhotoGrapherSearch(self):
            availability_photographers = ['Rajesh', 'Jayanth']
            if self.Budget <= 10000:
                print('Jayanth is the best fit')
            elif self.Budget >10000 and self.Budget<20000:
                print('Rajesh is the best fit')
            else:
                print("There are no available photographers right now for the mentioned budget, will get back to you once we get an update")


        def CollectGiftItems():
            #show_QR_Code = 
            return
        
                
    
    
from fastapi import FastAPI
#app = from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hello(name: str):
  return {'Hello ' + name + '!'}         
            
            
    

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    return "recived: {}".format(request.form)

if __name__ == "__main__":
    app.run(debug=True, port=8050)            
                
                
        
            

                          