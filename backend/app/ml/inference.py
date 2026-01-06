import numpy as np 

class SimpleAnomlyModel:
    def __init__(self,threshold:float=0.8):
        self.threshold=threshold
    

    def predict(self,values):
        values=np.array(values)

        score=values.mean()

        if score>self.threshold:
            return {
                "prediction":"Anomly",
                "score":float(score)
            }
        else:
            return {
                "prediction":"Normal",
                "score":float(score)  
            }