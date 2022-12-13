import pickle,json
import numpy as np


class housing():
    def __init__(self,Avg_AreaIncome,Avg_AreaHouseAge,Avg_AreaNumberofRooms,Avg_AreaNumberofBedrooms,AreaPopulation):
        self.Avg_AreaIncome=Avg_AreaIncome
        self.Avg_AreaHouseAge=Avg_AreaHouseAge
        self.Avg_AreaNumberofRooms=Avg_AreaNumberofRooms
        self.Avg_AreaNumberofBedrooms=Avg_AreaNumberofBedrooms
        self.AreaPopulation=AreaPopulation
       
    def load_model(self):

       
        with open ('lin_reg.pkl','rb') as f:
            self.lin_reg=pickle.load(f)
   
        with open ('column.json','r') as m:
            self.data=json.load(m)
    
    def prediction(self):
        self.load_model()
       
        array=np.zeros(5)
        array[0]=self.Avg_AreaIncome
        array[1]=self.Avg_AreaHouseAge
        array[2]=self.Avg_AreaNumberofRooms 
        array[3]=self.Avg_AreaNumberofBedrooms
        array[4]=self.AreaPopulation
        

        print('test_array',array)
        result=self.lin_reg.predict([array])[0]
        print(result)
        return result
if __name__=="__main__":
    pred=housing(29000,7,5,2,40000)
    pred.prediction()


