from Term import Term

class autocomplete:
    
    #creating the AutoComplete object  with terms from the file
    def __init__(self, filename, k):
        self.__file = open(filename, "r")
        self.__savedWords = []
        self.__matchedTerms = None
        self.__k = k
        for word in self.__file:
            self.__savedWords.append(word.strip().split(maxsplit=1))

    #returns a list, sorted bei the weights from the terms, which started with the prefix
    def match(self, prefix):
        
        self.__matchedTerms = []
        copyWords = self.__savedWords.copy()

        #loops trough the given file and returns a list with all founded elements
        for i in range(self.__k):
            index = self.__binarySearch(0, len(copyWords)-1, prefix, copyWords)

            #if there is no furher match in the list, stop search
            if (index == ""): break

            word = copyWords[index]
            
            txt = word[1]
            weight = word[0]

            self.__matchedTerms.append(Term(txt, int(weight)))
            copyWords.pop(index)

        return sorted(self.__matchedTerms)
    
    #returns the count of matches, which start with the prefix
    def matches(self, prefix):

        copyWords = self.__savedWords.copy()
        counter = 0

        #loops trough the given file and returns a list with all founded elements
        for i in range(len(copyWords)):
            index = self.__binarySearch(0, len(copyWords)-1, prefix, copyWords)

            #if there is no furher match in the list, stop search
            if (index == ""): break

            counter += 1              
            copyWords.pop(index)

        return counter

    #return the count of from the saved terms in a
    def __len__(self):
        return len(self.__savedWords)

    #processes a binary search for a given string in a file or list
    def __binarySearch(self, bottom, top, string, words):
        if string == None: return ""
        
        #checks if the word is searched string at the end of the list 
        if bottom == top:
            w = words[bottom]
            if(w[1][:len(string)]==string):
                return bottom
            else:
                return ""

        #processes the search recursive through the file or list    
        else:
            middle = (bottom+top)//2
            word = words[middle]
            if(word[1][:len(string)]==string):
                return middle

            #checks, if the substring is in the first half of the list, else search in the other half list
            if([s for s in words[:middle] if string == s[1][:len(string)]]): return self.__binarySearch(bottom, middle, string, words)
            else: return self.__binarySearch(middle+1, top, string, words)