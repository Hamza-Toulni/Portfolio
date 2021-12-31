import numpy as np

def calculate(list):
    if len(list)!= 9:
        raise ValueError("'List must contain nine numbers.")
    else:
        a_array = np.asarray(list)
        r_array = np.array(a_array).reshape(3,3)
        
        m = np.mean(r_array).tolist()
        m0 = np.mean(r_array, axis = 0).tolist()
        m1 = np.mean(r_array, axis = 1).tolist()
        
        v = np.var(r_array).tolist()
        v0 = np.var(r_array, axis = 0).tolist()
        v1 = np.var(r_array, axis = 1).tolist()
        
        std = np.std(r_array).tolist()
        std0 = np.std(r_array, axis = 0).tolist()
        std1 = np.std(r_array, axis = 1).tolist()
        
        ma = np.max(r_array).tolist()
        ma0 = np.max(r_array, axis = 0).tolist()
        ma1 = np.max(r_array, axis = 1).tolist()
        
        mi = np.min(r_array).tolist()
        mi0 = np.min(r_array, axis = 0).tolist()
        mi1 = np.min(r_array, axis =1).tolist()
        
        s = np.sum(r_array).tolist()
        s0 = np.sum(r_array, axis = 0).tolist()
        s1 = np.sum(r_array, axis = 1).tolist()
        
        calculations = {
            "mean" : [m0,m1,m],
            "variance" : [v0,v1,v],
            "standard deviation" : [std0, std1,std],
            "max" : [ma0,ma1,ma],
            "min" : [mi0,mi1,mi],
            "sum" : [s0,s1,s]           
        }
        return calculations