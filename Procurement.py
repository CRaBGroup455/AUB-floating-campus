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
        return self.offers[self.offers['Location']==location] # Rhis is an SQL like query implementd in Pandas
                                                                #returns the offers of restaurants by location
