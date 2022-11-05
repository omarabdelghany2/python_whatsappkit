from tkinter import *
from tkinter import ttk
from whats import sendwhatmsg
from openpyxl import load_workbook
import threading
from datetime import date,datetime

# Configs -----------------------------------------------------
root = Tk()
root.geometry("500x250")
root.resizable(height=False,width=False)
root.title('Whatsapp Toolkit')
root.iconbitmap('./assets/whatsapp.ico')
root.tk.call("source","azure.tcl")
root.tk.call("set_theme","dark")

# is running? indicatior -----------------------------------------------------
startState = False

# Functions -----------------------------------------------------
def mainFunction(ExcelName,QuizNo):
    global startState 
    startState = True
    loadingBar.place(x=150,y=210)
    startButton.config(state="disabled")
    try:
        book = load_workbook(f"{ExcelName}.xlsx")
    except:
        sheetErrorLabel.config(text="didn't found the excel sheet",foreground="red")
        startButton.config(state="normal")
        loadingBar.place_forget()
        return
    sheet = book.active
    rows = sheet.rows
    headers=[cell.value for cell in next (rows)]
    loadingBar.start()
    for row in rows:
        
        while(startState) :
            try :
                mobile_num=row[2].value
                name=row[1].value
                grade=row[3].value
                sendwhatmsg("+20"+str(mobile_num), str(grade)+str(name)+" درجةالطالب " ,16,59)
                sheetErrorLabel.config(text="successful sent!",foreground="green")
                loggerText.config(state=NORMAL)
                
                
                break
            except:
                sheetErrorLabel.config(text="trying again!",foreground="red")
    loadingBar.stop()
    sheetErrorLabel.config(text="Finshed!",foreground="green")
    startButton.config(state="normal")
    loadingBar.place_forget()

def mainFunctionStart():
    inputSheet = sheetNameInput.get()
    inputQuiz = sheetNumberInput.get()
    thread1 = threading.Thread(target=mainFunction,args=(inputSheet,inputQuiz))
    thread1.start()

def stop():
    global startState
    startState = False
    sheetErrorLabel.config(text="")




# TABS -----------------------------------------------------
tab_parent = ttk.Notebook(root)
sendFrame = Frame(tab_parent)
outputFrame = Frame(tab_parent)
creditsFrame = Frame(tab_parent)

# SEND FRAME WIDGETS -----------------------------------------------------
sheetNameLabel = ttk.Label(sendFrame, text="Enter the sheet name :")
sheetNumberLabel = ttk.Label(sendFrame, text="Choose the sheet number :")
sheetErrorLabel = ttk.Label(sendFrame, text="",foreground="red", justify=CENTER)
sheetNameInput = ttk.Entry(sendFrame, width=35)
sheetNumberInput = ttk.Entry(sendFrame, width=35)
cancelButton = ttk.Button(sendFrame, text="Cancel",command=stop,style="Accent.TButton")
startButton = ttk.Button(sendFrame, text="Start",command=mainFunctionStart,style="Accent.TButton")
loadingBar = ttk.Progressbar(sendFrame, orient="horizontal",mode="determinate",length=195)
# SEND FRAME WIDGETS POSTIONS -----------------------------------------------------
sheetNameLabel.place(x=20, y=55)
sheetNumberLabel.place(x=20, y=105)
sheetErrorLabel.pack()
sheetNameInput.place(x=200, y=50)
sheetNumberInput.place(x=200, y=100)
cancelButton.place(x=150, y=170)
startButton.place(x=250, y=170)

# OUTPUT FRAME WIDGETS -----------------------------------------------------
loggerText = Text(outputFrame,state=DISABLED)

# SEND FRAME WIDGETS POSTIONS -----------------------------------------------------
loggerText.pack()

# CREDITS FRAME WIDGETS -----------------------------------------------------
spaceLabel = ttk.Label(creditsFrame, text="",padding=15)
contrbuiter1 = ttk.Label(creditsFrame, text="BACKEND:Omar Abdelghany",font="Helvetica",padding=5)
contrbuiter2 = ttk.Label(creditsFrame, text="FRONTEND:Mark Wasfy",font="Helvetica",padding=5)
contactLabel = ttk.Label(creditsFrame, text="TEL:01204086820",font="Helvetica")


# CREDITS FRAME WIDGETS POSTIONS -----------------------------------------------------
spaceLabel.pack()
contrbuiter1.pack()
contrbuiter2.pack()
contactLabel.pack()

# TABS POSITIONS -------------------------------------------------
tab_parent.pack(fill="both",expand=1)
tab_parent.add(sendFrame,text="send")
tab_parent.add(outputFrame,text="output")
tab_parent.add(creditsFrame,text="credits")

# Main window -----------------------------------------------------
root.mainloop()