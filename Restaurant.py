#!/usr/bin/env python
# coding: utf-8

# # Restaurant class
#
# restaurant class that holds the information needed for every offer given by a restaurant.
#

# In[190]:


import pandas as pd


# In[191]:


class Restaurant(object): # Restaurants interested in being on the discount list
    def __init__(self,name,location,offer,telno,website):  #Initializing offers info
        self.name=name
        self.location=location
        self.offer= offer
        self.telno = telno
        self.website=website
    def __str__(self):
        return ('name: ' + str(self.name) + "\nLocation: "  + str(self.location) +  "\nOffer: " + str(self.offer) + "\nTelephone number: "  + str(self.telno))

    def getName(self):
        return self.name
    def getLocation (self):
        return self.location
    def getOffer (self):
        return self.offer
    def getNumber (self):
        return self.telno
    def getWebsite(self):
        return self.website