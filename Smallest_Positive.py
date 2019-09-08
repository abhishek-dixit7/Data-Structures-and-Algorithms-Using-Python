list_new =[0,-6,8,9,4,5]

def smallest_positive(list):
    min  = 999999999999
    for i in list_new:
         if i<min and i>0.0:
             min = i
    
    if len(list_new)>1:
         print(min)
         return min
        
    else:
         print("There is no smallest positive in the list as it is empty.")
         return None

smallest_positive(list_new)
            