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