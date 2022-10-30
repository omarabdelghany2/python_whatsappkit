
import datetime
import time
from whats import sendwhatmsg
from qt import QtWidgets
from openpyxl import load_workbook




def myprogStart(ExcelName,QuizNo):
    book = load_workbook('ayman_data.xlsx')
    sheet = book.active

    rows = sheet.rows
    headers=[cell.value for cell in next (rows)]
    print(headers)
    for row in rows:
        
        while(True) :
            try :
                mobile_num=row[2].value
                name=      row[1].value
                grade=      row[3].value
                QtWidgets.QApplication.processEvents()
                sendwhatmsg("+20"+str(mobile_num), str(grade)+str(name)+"درجةالطالب " ,16,59)
                print("successful sent!")
                break

            except:
                print("trying again")
           
        
 