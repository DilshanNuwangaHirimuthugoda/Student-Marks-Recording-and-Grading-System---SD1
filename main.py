progress_counts=0
retriever_counts=0
trailer_counts=0
Exclude_counts=0
outcome=0
progress=0
trailer=0
retriever=0
Exclude=0
results = []
data = []

valied_marks=[0,20,40,60,80,100,120]

from graphics import *
def histogram_window():
    #OPEN THE WINDOW 
    # #open a window object called "win" with size and title 
    # Set the background colour of the window
    
    win = GraphWin ("Histogram", 800, 600)
    win.setBackground("Mint Cream")
    heading = Text(Point(200, 30), 'Histogram Results')

   
    #histogram heading & line

    heading.setTextColor("grey")
    heading.setSize(23)
    heading.setStyle("bold")
    heading.setFace("helvetica")
    heading.draw(win)

    line= Line(Point(20,50),Point(375,50))
    line.draw(win)

    line=Line(Point(50,490),Point(550,490))
    line.draw(win)

    Total=progress+retriever+trailer+Exclude

    Total_text=Text(Point(185,550),str(Total) + " Outcomes in Total")
    Total_text.setSize(15)
    Total_text.setStyle("bold")
    Total_text.setFace("helvetica")
    Total_text.setTextColor("grey")
    Total_text.draw(win)
#Input parts

def input_part():
    global progress,trailer,retriever,Exclude
    while True:
        try:
            credits_at_pass=int(input("Please enter your credits at pass: "))
            if credits_at_pass in valied_marks:
                 break
            else:
                 print("out of range")
                 print("Only valied ( 0,20,40,60,80,100,120)")
        except ValueError:
            print("Integer required")

    while True:
        try :
            credits_at_defer=int(input("Please enter your credit at defer: "))
            if credits_at_defer in valied_marks:
                 break
            else:
                 print("out of range")
                 print("Only valied ( 0,20,40,60,80,100,120)")
        except ValueError:
            print("Integer required")

    while True:
        try :
            credits_at_fail=int(input("Please enter your credit at fail: "))
            if credits_at_fail in valied_marks:
                 break
            else:
                 print("out of range")
                 print("Only valied ( 0,20,40,60,80,100,120)")
        except ValueError:
            print("Integer required")

    total_credit=credits_at_pass + credits_at_defer + credits_at_fail
    if total_credit !=120:
        print("Total Incorrect")
        return