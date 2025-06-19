student={}
student["ramesh"]=80
student["suresh"]=70
student["hari"]=98
student["priya"]=65

userInput=input("Enter a name\n")
if userInput in student:
    print("Number secured by" ,userInput ,"is",student.get(userInput))
else:
    print("student not found")