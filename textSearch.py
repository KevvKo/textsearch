import sys
from AutoComplete import autocomplete
from tkinter import *

class Textsearch:
    def __init__(self, file, k):
        self.__outputCount = k
        self.__autoComplete = autocomplete(file, k)
        self.__ui = Tk()
    
    #handle the event for entering any input into the searchfield
    def searchOutput(self, event):
        k = self.__outputCount
        #takes an infinity input of strings and searching in the given txt-file
        txt = self.__inp.get().strip()

        if(txt == ""):
            self.__matchLbl.pack_forget()
            return ""

        #close the program and say goodbye
        if(txt == "exit"):
            print("Bye bye")
            self.__ui.quit()
            
        #prints the k-number of words
        matches = self.__autoComplete.match(txt)

        l = len(matches)
        t = ""

        for i in range(k):
            if i == l: break
            if i == "": break
            t += str(matches[i]._weight) + " " + matches[i]._txt + "\n"

        #self.__matchLbl.configure(state="normal")
        self.__matchLbl.delete(0.0, END)
        self.__matchLbl["height"] = len(t.split("\n"))-1
        self.__matchLbl.insert(0.0,t)
        self.__matchLbl.pack()
        #self.__matchLbl.configure(state="disabled")

    #creating a userinterface for the search with k textfields and a input for the search
    def createUI(self):
        self.__ui.geometry("400x300")
        self.__ui.title("The Search")
        self.__ui.configure(background="#153464")

        #inserts a label as topic  
        lbl = Label(self.__ui, text= "search: ", font=("Arial bold", 14), fg="white")
        lbl.config(anchor=CENTER, background="#153464")
        lbl.pack(pady=15)

        #inserts an inputfield
        self.__inp = Entry(self.__ui, width = 45)
        self.__inp.bind("<KeyRelease>",self.searchOutput)
        self.__inp.pack()

        #insert a label for the output of matches
        self.__matchLbl = Text(self.__ui , width = 45)
        self.__ui.mainloop()

#testing the object with its default functionalitys
def run():

    file = sys.argv[1]
    k = int(sys.argv[2])

    editor = Textsearch(file, k)
    editor.createUI()

############################################################################################################################
if __name__ == "__main__":
    run()