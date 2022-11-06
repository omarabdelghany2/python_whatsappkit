from tkinter import *
from tkinter import ttk
from functions.whats import sendwhatmsg
from openpyxl import load_workbook
import threading
from datetime import date,datetime
import os


class MainApplication:
    def __init__(self, master):
        self.master = master
        
        self.tab_parent = ttk.Notebook(self.master)
        self.sendFrame = ttk.Frame(self.tab_parent)
        self.outputFrame = ttk.Frame(self.tab_parent)
        self.creditsFrame = ttk.Frame(self.tab_parent)
        
        self.tab_parent.pack(fill="both",expand=1)
        self.tab_parent.add(self.sendFrame,text="send")
        self.tab_parent.add(self.outputFrame,text="output")
        self.tab_parent.add(self.creditsFrame,text="credits")

        self.main_window = MainWindow(self.sendFrame,self.sendToOutput)
        self.output_window = OutputWindow(self.outputFrame)
        self.credits_window = CreditWindow(self.creditsFrame)

    def sendToOutput(self,name,grade,number):
        msg = self.output_window.msgTemplate(name,grade,number)
        self.output_window.insertLog(msg)


class MainWindow():
    def __init__(self,root,msgSystem):
        self.ENGINE = False
        # SEND FRAME WIDGETS -----------------------------------------------------
        self.sheetNameLabel = ttk.Label(root, text="Select the sheet file :")
        self.sheetNumberLabel = ttk.Label(root, text="Enter the exam number :")
        self.sheetErrorLabel = ttk.Label(root, text="",foreground="red", justify=CENTER)
        # self.sheetNameInput = ttk.Entry(root, width=35)
        self.sheetFilePicker = StringVar(root)
        self.sheetNameInput = ttk.OptionMenu(root,self.sheetFilePicker,"please pick file",*self.getExcelFilesFunction())
        self.sheetNumberInput = ttk.Entry(root, width=35)
        self.cancelButton = ttk.Button(root, text="Cancel",command=self.exit,style="Accent.TButton")
        self.startButton = ttk.Button(root, text="Start",command=self.send,style="Accent.TButton")
        self.loadingBar = ttk.Progressbar(root, orient="horizontal",mode="indeterminate",length=195)
        # SEND FRAME WIDGETS POSTIONS -----------------------------------------------------
        self.sheetNameLabel.place(x=20, y=55)
        self.sheetNumberLabel.place(x=20, y=105)
        self.sheetErrorLabel.pack()
        self.sheetNameInput.place(x=200, y=50)
        self.sheetNameInput.config(width=32)
        self.sheetNumberInput.place(x=200, y=100)
        self.cancelButton.place(x=150, y=170)
        self.startButton.place(x=250, y=170)

        self.msgSystem = msgSystem
    
    def enable_engine(self):
        self.ENGINE = True

    def disable_engine(self):
        self.ENGINE = False

    def sendFunction(self):
        self.startButton.config(state="disabled")
        self.sheetErrorLabel.config(text="")
        self.enable_engine()
        try:
            book = load_workbook(f"./data/{self.sheetFilePicker.get()}")
        except:
            self.sheetErrorLabel.config(text="didn't found the excel sheet",foreground="red")
            self.startButton.config(state="normal")
            return
        self.loadingBar.place(x=150,y=210)
        sheet = book.active
        rows = sheet.rows
        headers=[cell.value for cell in next (rows)]
        self.loadingBar.start()
        while(self.ENGINE):
            for row in rows:
                try :
                    mobile_num=row[2].value
                    name=row[1].value
                    grade=row[3].value
                    sendwhatmsg(
                        f"+20{mobile_num}",self.msgTemplateFunction(name,grade),16,59
                    )
                    self.sheetErrorLabel.config(text="successful sent!",foreground="green")
                    self.msgSystem(name,grade,mobile_num)
                    break
                except:
                    self.sheetErrorLabel.config(text="trying again!",foreground="red")
        self.disable_engine()
        self.startButton.config(state="normal")
        self.loadingBar.place_forget()
        self.sheetErrorLabel.config(text="Finshed!",foreground="green")

    def msgTemplateFunction(self,name,grade):
        return f"الطالب : {name} -- الدرجة : {grade}"

    def getExcelFilesFunction(self):
        files = os.listdir("./data")
        func = lambda itm : ".xlsx" in itm
        result = list(filter(func,files))
        return result

    def send(self):
        thread = threading.Thread(target=self.sendFunction)
        thread.start()
       
    def exit(self):
        self.ENGINE = False
        self.sheetErrorLabel.config(text="")
        self.loadingBar.config()


class OutputWindow():
    def __init__(self,root):
        # OUTPUT FRAME WIDGETS -----------------------------------------------------
        self.loggerText = Text(root,state=DISABLED)
        # OUTPUT FRAME WIDGETS POSTIONS -----------------------------------------------------
        self.loggerText.pack()

    def insertLog(self,msg):
        self.loggerText.config(state=NORMAL)
        self.loggerText.insert(END, msg + "\n")
        self.loggerText.config(state=DISABLED)

    def msgTemplate(self,name,grade,mobile):
        loggerMsg = f"""
        Date: {date.today()}
        Time: {datetime.now().strftime("%H:%M:%S")}
        Phone: {mobile}
        Message: {grade} {name} درجة الطالب 
        -------------------------------------------
        """
        return loggerMsg


class CreditWindow():
    def __init__(self,root):
        # CREDITS FRAME WIDGETS -----------------------------------------------------
        spaceLabel = ttk.Label(root, text="",padding=15)
        contrbuiter1 = ttk.Label(root, text="BACKEND:Omar Abdelghany",font="Helvetica",padding=5)
        contrbuiter2 = ttk.Label(root, text="FRONTEND:Mark Wasfy",font="Helvetica",padding=5)
        contactLabel = ttk.Label(root, text="TEL:01204086820",font="Helvetica")
        # CREDITS FRAME WIDGETS POSTIONS -----------------------------------------------------
        spaceLabel.pack()
        contrbuiter1.pack()
        contrbuiter2.pack()
        contactLabel.pack()


def main(): 
    root = Tk()
    root.geometry("500x250")
    root.resizable(height=False,width=False)
    root.title('Whatsapp Toolkit')
    root.iconbitmap('./assets/whatsapp.ico')
    root.tk.call("source","theme/forest-dark.tcl")
    ttk.Style().theme_use("forest-dark")
    MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()