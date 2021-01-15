import Restaurant
import pandas as pd

# # Procurement:
#
# Procurement class is where the fun happens. It makes a database of the restaurants and saves it on disk using panda's DataFrame data strucutre.
#
# we can see that this lodas,saves and adds new restaurants
#
# We can also query it by dimentions we want, more dimeensions are beneficial if you have any in mind
#
# TODO: Create Top N queries by different features
#

# In[192]:


class Procurement(object):

    def __init__(self):

        self.offers = pd.DataFrame()
    def Load(self,File):
        self.offers=pd.read_csv(File)
    def Save(self, File):
        self.offers.to_csv(File+ ".csv")
    def addRestaurant (self,restaurant):
        new_data = {'Name': restaurant.getName(),
        'Location': restaurant.getLocation(),
        'Offer': restaurant.getOffer(),
        'Telephone #': restaurant.getNumber(),
        'Website': restaurant.getWebsite()
               }
        self.offers = self.offers.append(new_data, ignore_index=True)
    def getByLocation(self,location):
        return self.offers[self.offers['Location']==location]#returns the offers of restaurants by location





