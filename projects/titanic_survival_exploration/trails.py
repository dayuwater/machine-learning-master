# trail 1 -> 79.91
if passenger['Sex']=='female':
            predictions.append(1)
elif passenger['Age']<10:
    if passenger['Pclass']<3:
            predictions.append(1)
    else:
            predictions.append(0)
else:
    predictions.append(0)  



# trail 2 -> 80.13
 if passenger['Sex']=='female':
            predictions.append(1)
        
        elif passenger['Age']<18 and passenger['Pclass']<2:
           
            predictions.append(1)
       
        elif passenger['Age']<10 and passenger['Pclass']<3:
           
            predictions.append(1)
            
            
        else:
            predictions.append(0)

# trail 3 -> 80.92
if passenger['Sex']=='female':
            predictions.append(1)
        
        elif passenger['Age']<18 and passenger['Pclass']<2:
           
            predictions.append(1)
       
        elif passenger['Age']<10 and passenger['Pclass']<3:
           
            predictions.append(1)
            
        elif passenger['Age']<10 and passenger['SibSp']<3:
           
            predictions.append(1)
            
            
        else:
            predictions.append(0)


# trail 4 ->81.03
 
        if passenger['Sex']=='female':
            if passenger['Age'] < 10 and passenger['Pclass'] < 2:
                predictions.append(0)
            else:
                predictions.append(1)
        
        elif passenger['Age']<18 and passenger['Pclass']<2:
           
            predictions.append(1)
       
        elif passenger['Age']<10 and passenger['Pclass']<3:
           
            predictions.append(1)
            
        elif passenger['Age']<10 and passenger['SibSp']<3:
           
            predictions.append(1)
            
            
        else:
            predictions.append(0)

# trail 5 -> 81.71%
if passenger['Sex']=='female':
            if passenger['Age'] < 14 and passenger['Pclass'] < 2:
                predictions.append(0)
            elif passenger['Age'] < 10 and passenger['SibSp'] > 2:
                predictions.append(0)
            else:
                predictions.append(1)
        
        elif passenger['Age']<18 and passenger['Pclass']<2:
           
            predictions.append(1)
       
        elif passenger['Age']<10 and passenger['Pclass']<3:
           
            predictions.append(1)
            
        elif passenger['Age']<10 and passenger['SibSp']<3:
           
            predictions.append(1)
            
            
        else:
            predictions.append(0)

# trail 6 -> 82.60%
if passenger['Sex']=='female':
            if passenger['Age'] < 14 and passenger['Pclass'] < 2:
                predictions.append(0)
            elif passenger['Age'] < 10 and passenger['SibSp'] > 2:
                predictions.append(0)
            elif (passenger['Age'] > 40 and passenger['Age'] < 50) and passenger['Pclass'] > 2:
                predictions.append(0)
            else:
                predictions.append(1)
        
        elif passenger['Age']<18 and passenger['Pclass']<2:
           
            predictions.append(1)
       
        elif passenger['Age']<10 and passenger['Pclass']<3:
           
            predictions.append(1)
            
        elif passenger['Age']<10 and passenger['SibSp']<3:
           
            predictions.append(1)
            
            
        else:
            predictions.append(0)
        
        


