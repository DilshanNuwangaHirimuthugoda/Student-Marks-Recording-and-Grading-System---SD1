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

        # histrogram bar edits
    barr_width = 15
    bar1=Rectangle(Point(100,490),Point(180 + barr_width,490-(progress / Total )*200))
    bar1.draw(win)
    bar1.setFill("skyblue")
    
    bar2 = Rectangle(Point(200, 490),Point(280 + barr_width ,490 - ( trailer / Total)*200))
    bar2.draw(win)
    bar2.setFill("green")

    bar3 = Rectangle(Point(300, 490),Point(380 + barr_width, 490 - (retriever / Total)*200))
    bar3.draw(win)
    bar3.setFill("red")

    bar4 = Rectangle(Point(400, 490),Point(480 + barr_width, 490 - (Exclude / Total)*200))
    bar4.draw(win)
    bar4.setFill("yellow")

    progress_text=Text(Point(140,510),"Progress")
    progress_text.setSize(12)
    progress_text.draw(win)

    retriever_text=Text(Point(340,510),"Retriever")
    retriever_text.setSize(12)
    retriever_text.draw(win)

    trailer_text=Text(Point(240,510),"Trailer")
    trailer_text.setSize(12)
    trailer_text.draw(win)

    Exclude_text=Text(Point(440,510),"Exclude")
    Exclude_text.setSize(12)
    Exclude_text.draw(win)

    T1=Text(Point(140,510-(32)),f"{progress}")
    T1.draw(win)
    T2=Text(Point(240,510-(32)),f"{trailer}")
    T2.draw(win)
    T3=Text(Point(340,510-(32)),f"{retriever}")
    T3.draw(win)
    T4=Text(Point(440,510-(32)),f"{Exclude}")
    T4.draw(win)
            
    win.getMouse()
    win.close()
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
    
    #conditions and file writing 
        
    elif credits_at_pass==120 :
        print("Progress")
        
        with open("Progression Outcome Report.txt", "a") as  file:
            outcome ="Progress"
            
            file.write("{} - pass={} defer={} fail={} \n".format("progress",credits_at_pass,credits_at_defer,credits_at_fail))
        data.append(f"Progress - {credits_at_pass},{credits_at_defer},{credits_at_fail}")
        progress +=1
    elif credits_at_pass==100:
        print("Progress (module trailer) ")
        outcome ="Progress (module trailer) "
        with open("Progression Outcome Report.txt", "a") as  file:

            file.write("{} - pass={} defer={} fail={} \n".format("Progress (module trailer) ",credits_at_pass,credits_at_defer,credits_at_fail))
        data.append(f"Progress (module trailer) - {credits_at_pass},{credits_at_defer},{credits_at_fail}")
        trailer +=1
    elif  credits_at_fail>=80  :
        print("Exclude")
        
        with open("Progression Outcome Report.txt", "a") as  file:
            outcome ="Exclude"
            
            file.write("{} - pass={} defer={} fail={} \n".format("Exclude",credits_at_pass,credits_at_defer,credits_at_fail))
        data.append(f"Exclude - {credits_at_pass},{credits_at_defer},{credits_at_fail}")
        Exclude +=1
    else:
        print("Do not Progress  (module retriever)")
        
        with open("Progression Outcome Report.txt", "a") as  file:
            outcome ="Do not Progress  (module retriever)"
           
            file.write("{} - pass={} defer={} fail={} \n".format("Do not Progress  (module retriever)",credits_at_pass,credits_at_defer,credits_at_fail))
        data.append(f"Do not Progress  (module retriever) - {credits_at_pass},{credits_at_defer},{credits_at_fail}")
        retriever +=1
        
    results.append(f"{outcome} - {credits_at_pass}, {credits_at_defer}, {credits_at_fail}")
input_part()

#Loops for multiple inputs

def restart():

    while True:
        again=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        if again== "y":
              input_part()
        elif again=="q":
            break
        else:
            print("Invalid input")

#list
            
def print_list():
    print ("\n __List_of_result__" )
    for result in results:
        print(result)

restart()
histogram_window()
print_list()

            
