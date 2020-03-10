class  Term:
    
    #creating an object for the class Term with the term as text and the weight 
    def __init__(self, text, weight ):
        if weight < 0: return

        self._txt = text.strip()
        self._weight = weight

    #compare the object of equality 
    def __eq__(self,other):
        if(isinstance(other, Term)):
            return self._txt[:3] == other._txt[:3] and self._weight == other._weight
        else: return NotImplemented

    #compare the object of not equality 
    def __ne__(self, other):
        if(isinstance(other, Term)):
            return self._txt[:3] != other._txt[:3] or self._weight != other._weight    
        else: return NotImplemented

    #compare the object of less then   
    def __lt__(self, other):
        if(isinstance(other, Term)):
            #checks if the weights adifferent and compare them
            if(self._weight != other._weight):
                return  self._weight > other._weight
            #if the weights are equal, compare the txt    
            else: return self._txt[:3] > other._txt[:3]
        else: return NotImplemented
    
    #compare the object of less equal to <=      
    def __le__(self, other):
        if(isinstance(other, Term)):
            #checks if the weights adifferent and compare them
            if(self._weight != other._weight):
                return self._weight >= other._weight   
            #if the weights are equal, compare the txt    
            else: return self._txt[:3] >= other._txt[:3]
        else: return NotImplemented
    
    #compare the object of greater then
    def __gt__(self, other):
        if(isinstance(other, Term)):
            #checks if the weights adifferent and compare them
            if(self._weight != other._weight):
                return self._weight < other._weight    
            #if the weights are equal, compare the txt    
            else: return self._txt[:3] < other._txt[:3]
        else: return NotImplemented
    
    #compare the object of greater equal
    def __ge__(self, other):
        if(isinstance(other, Term)):
            #checks if the weights adifferent and compare them
            if(self._weight != other._weight):
                return self._weight <= other._weight
            #if the weights are equal, compare the txt    
            else: return self._txt[:3] <= other._txt[:3]    
        else: return NotImplemented       
    
    #returns the term as string with the text and the weight
    def __str__(self):
        return str(self._weight) + " " + str(self._txt)