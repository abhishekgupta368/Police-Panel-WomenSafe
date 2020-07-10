from operator import itemgetter 
from abc import ABCMeta, abstractmethod

class CountryStateData():
    def __init__(self):
        self.states={
            'Andaman And Nicobar':	[11.66702557,92.73598262],
            "Andhra Pradesh":	[14.7504291,78.57002559],
            'Arunachal Pradesh':[27.10039878,93.61660071],
            'Assam': [26.7499809,94.21666744],
            'Bihar': [25.78541445,87.4799727],
            'Chandigarh': [30.71999697,76.78000565],
            'Chhattisgarh': [22.09042035,82.15998734],
            'Dadra And Nagar Haveli':[20.26657819,73.0166178],
            "Delhi":[28.6699929,77.23000403],
            "Goa":[15.491997,73.81800065],
            "Haryana": [28.45000633,77.01999101],
            "Himachal Pradesh": [31.10002545,77.16659704],
            "Jammu And Kashmir":[34.29995933,74.46665849],
            "Jharkhand": [23.80039349,86.41998572],
            "Karnataka":[ 12.57038129,76.91999711],
            "Kerala": [8.900372741,76.56999263],
            "Lakshadweep": [10.56257331,72.63686717],
            "Madhya Pradesh": [21.30039105,76.13001949],
            "Maharashtra": [19.25023195,73.16017493],
            "Manipur": [24.79997072,93.95001705],
            "Meghalaya":[25.57049217,91.8800142],
            "Mizoram": [23.71039899,92.72001461],
            "Nagaland":[25.6669979,94.11657019],
            "Orissa":[19.82042971,85.90001746],
            "Puducherry":[11.93499371,79.83000037],
            "Punjab":[31.51997398,75.98000281],
            "Rajasthan":[26.44999921,74.63998124],
            "Sikkim": [27.3333303,88.6166475],
            "Tamil Nadu": [12.92038576,79.15004187],
            "Tripura":[23.83540428,91.27999914],
            "Uttar Pradesh":[27.59998069,78.05000565],
            "Uttaranchal":[30.32040895,78.05000565],
            "West Bengal":[22.58039044,88.32994665],
        }
    def getCityList(self):
        return list(map(itemgetter(0), self.states.items())) 
    
    def getCityCoodinates(self):
        return list(map(itemgetter(1), self.states.items())) 
    
    def getStatesData(self):
        return self.states
    
    def getCoodinates(self,name):
        return self.states[name]