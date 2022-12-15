# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:16:13 2022

@author: U410558
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Marriage():
    #Discount integration for the shopping for both bride and groom
    #Destination shopping for the marriages
    #Option to upload the pictures for proof
    #Brahmin search 
        
    def __init__(self, availability_start, availability_end, Budget, Groom, Bride, state, N):
        #self.start_date = start_date
        #self.end_date = end_date
        self.availability_start = availability_start
        self.availability_end = availability_end
        self.Budget = Budget
        self.Groom = Groom
        self.Bride = Bride
        self.state = state
        self.N = N
        
   # Having an option to select the groom or bride side
   
    def BrideOrGroom(self):
       if self.Groom:
           print('Here you go BrideGroom, have a nice wedding')
       else:
            print('Here you go Bride, have a nice wedding')
           
            return 
      
        
   # Integrating with the available resorts or rooms nearby or destination for bachelor party 
   
    def BachelorParty():
       #if self.Groom:
           
       return
       
    def BrahminSearch(self):
        list1_Brahmin = []
        for i in range(self.availability_start, self.availability_end):
            
            return
    #Wedding cards printing function, designing your own wedding card
    
    def WeddingCards(self):
        #Wedding cards printing function, designing your own wedding card
        available_Printer_Shops = ['Jayanth', 'Rajesh']
        templates = {'Template1': 'TEMP'} #TEMP(template images of the wedding cards)
        for i in templates:
            x = i
            x1 = []
            if x == 'Template1':
                x1.append(str(input('Enter the Bride name: ')))
                x1.append(str(input('Enter the Bride Groom name: ')))
                x1.append(str(input('Enter the Brides Father name: ')))
                x1.append(str(input('Enter the Groom Father name: ')))
                x1.append(str(input('Enter the Marriage Dates: ')))
            else:
                print('Please select the template')
                
            print('The marriage date is', x1[4])
            #Text that should be related to the bride or groom
        
        
            return
    
    def Shopping(self):
        Type_Of_Shopping = ['Online Shopping', 'Instore Shopping', 'Garments', 'Jewelery', 'SilverItems']
        if self.Groom:
            exhibitions = {'Exhibition':'https://www.google.com'}
            for i in Type_Of_Shopping:
                if i == Type_Of_Shopping[0]:
                    print('Go to Myntra and do the shopping')
                elif i == Type_Of_Shopping[1]:
                    print('Go to Kalamandir and do the shopping')
                elif i == Type_Of_Shopping[2]:
                    print('Go to RS brothers')
                elif i == Type_Of_Shopping[3]:
                    print('Go to Tanishq')
                elif i == Type_Of_Shopping[4]:
                    print('Go to CMR')
                else:
                    print('Select any one of the given things in the list')
        elif self.Bride:
            exhibitions = {'Exhibition':'https://www.google.com'}
            for i in Type_Of_Shopping:
                if i == Type_Of_Shopping[0]:
                    print('Go to Myntra and do the shopping')
                elif i == Type_Of_Shopping[1]:
                    print('Go to Kalamandir and do the shopping')
                elif i == Type_Of_Shopping[2]:
                    print('Go to RS brothers')
                elif i == Type_Of_Shopping[3]:
                    print('Go to Tanishq')
                elif i == Type_Of_Shopping[4]:
                    print('Go to CMR')
                else:
                    print('Select any one of the given things in the list')
        else:
            print('You should be either bride or groom to do the shopping')
       
        return    
    def Boutique(self):
        
        return 
    
    def Florist(self):
        
        return 
    def SelectPopulation(self):
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

    def SelectVenue(self):
       #r = range(str(availability_start), str(availability_end))
       r = pd.date_range(start=self.availability_start,end=self.availability_end)
       start_date = str(input('Enter the start date: '))
       end_date = str(input('Enter the End date: '))
       #for i in availability_start, availability_end:
       if start_date and end_date in r:
          print('Hotel Daspala is available in the mentioned dates')
       else:
          print('Venues are not available in this dates')
    #Photographers selection in a town or in proximity 
    def AlcoholPermits(self):
        AllowedLocations = ['Telangana', 'Karnataka', 'MadhyaPradesh']
        if self.state in AllowedLocations:
            print('No permit is required')
        else:
            Procedure = {'Doc1':'Adhar card of the responsible person', 'People':'People Present in the Party', 'Link':'https://www.wikiprocedure.com/index.php/Hyderabad_-_Obtain_Liquor_Possession_Permit_for_serving_in_Special_Occassions#:~:text=This%20permit%20is%20for%20a,used%20for%20holding%20a%20function).'}
            print(Procedure.values())
        return
    
    #Pre wedding shoot, photoshoot (Should include in the photo shoot function)
    def Haldi(self):
        
        return
    
    def Mehendi(self):
        
        return
    
    def Sangeeth(self):
        #Food, drinks 
        return
    
    def SelectSuppliers(self):
        availability_suppliers = ['Jayanth', 'Rajesh']
        if self.Budget <= 1000000:
            print('The Supplier Jayanth is the best fit')
        else:
            print('The Supplier Rajesh is the best fit')
        def get_items_list(N):
            if N <= 1000:
                list2 = ['2000 Cups', '1500 Plates', '5 trays for cooking', '3 samianas']
                print(list2)
            elif N >= 1001 and N <= 1500:
                list3 = ['2500 Cups', '2000 Plates', '6 trays for cooking', '4 samianas']
                print(list3)
            else:
                print('Select the amount of people inorder to view the list')
        
        def PhotographerSearch(Photo_Budget):
            availability_photographers = ['Jayanth', 'Rajesh']
            if Photo_Budget <=80000:
                print('Jayanth is the best fit')
            elif Photo_Budget >= 100000 and Photo_Budget <=200000:
                print('Rajesh is the best fit')
            else:
                print('Mentioned Budget is not in the range, please contact our sales dept.')
            
            return
        
        def FlexService(length, height):
            if length <= 80 and height <= 80:
                print('The cost for the above mentioned lenght and height is 2000')
            elif length >= 81 and height <= 120: 
                print('The cost for the above mentioned lenght and height is 2000')
            else:
                print('The above mentioned length and breadth is not in the range, please contact our sales dep')
            
            list_Flex = []
            print('List the names of the people whose names you want to have on Flex and upload the images')
            list_Flex.append(str(input('Enter the bride name: ')))
            list_Flex.append(str(input('Enter the bride Groom name: ')))
            list_Flex.append(str(input('Enter the bride Familys name: ')))
            list_Flex.append(str(input('Enter the bride groom familys name: ')))
            
            templates = {'Template2': 'TEMP'} #TEMP(template images of the wedding cards)
            for i in templates:
                x = i
                x1 = []
                if x == 'Template1':
                    x1.append('Template1 has been selected')
                else:
                    print('Please select the template')
                
            print('The List and Template has been sent to the Flex team, will update you once its done')
            
            
            return x1, list_Flex
        
            
    
    def SelectTravelService(self,From,To):
        #from = Place
        self.availability_suppliers = ['Jayanth', 'Rajesh']
        
        
    
         
        
    def CateringService(self):
        self.availability_suppliers = ['Jayanth', 'Rajesh', 'Brijesh', 'Ram']
        print('self.availability_suppliers')
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
           
        def get_cusine_list():
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
        
    def ValueAdditionFeatures():
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
    


        #Post wedding poojas, post wedding shoot 
    def ReturnGifts(self):
        for i in range(self.N):
            
            
            return 
        
    def HoneyMoon(Budget1, Destination):
        Pre_Defined_Destinations = ['Shimla', 'Manali', 'Bali']
        if Budget1 >= 25000 and Budget1 <= 50000:
            
            
        
        #Honey moon packages 
            return 
    
    #Note to tell the unnecessary money given on the way.
    
    