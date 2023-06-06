import tkinter as tk
import csv 

def submit():
    customer=txt1.get()
    phonenumber=txt2.get()
    Email=txt3.get()
    productname=txt4.get()
    productamount=txt5.get()
    

    with open("exel files/tk.csv","w") as file:
        data=csv.writer(file)
        
        data.writerow([customer,phonenumber,Email,productname,productamount])

main = tk.Tk(className="  CUSTOMER DETAILES")
main.geometry("600x600")
main.configure(bg='white')

lable1=tk.Label(main,text="CUSTOMER NAME:").grid(row=0,column=0)
txt1=tk.Entry(main)
txt1.grid(row=0,column=1)

lable2=tk.Label(main,text="PHONE NUMBER:").grid(row=1,column=0)
txt2=tk.Entry(main)
txt2.grid(row=1,column=1)

lable3=tk.Label(main,text="EMAIL:").grid(row=2,column=0)
txt3=tk.Entry(main)
txt3.grid(row=2,column=1)

lable4=tk.Label(main,text="PRODUCT NAME:").grid(row=3,column=0)
txt4=tk.Entry(main)
txt4.grid(row=3,column=1)

lable5=tk.Label(main,text="PRODUCT AMOUNT:").grid(row=4,column=0)
txt5=tk.Entry(main)
txt5.grid(row=4,column=1)

btn6=tk.Button(main,text="submit",command=submit).grid(row=6,column=1)

main.mainloop()

# 2/6/2023

# import csv
# import tkinter as tk
# # from tkinter import messagebox

# def call():
#     input_value1=Txt1.get()
#     print(input_value1)

#     input_value2=Txt2.get()
#     print(input_value2)


#     input_value3=Txt3.get()
#     print(input_value3)

#     with open("tk.csv","w") as file:
#         data=csv.writer(file)
#         data.writerow([input_value1,input_value2,input_value3])



    
# main=tk.Tk(className="customer details ")
# main.geometry("400x400")

# Student_name=str()
# Student_age=str()
# Student_contact_number=str()




# label1=tk.Label(main,text="Name").grid(row=0,column=1)
# Txt1=tk.Entry(main)
# Txt1.grid(row=0,column=2)

# label2=tk.Label(main,text="Age").grid(row=1,column=1)
# Txt2=tk.Entry(main)
# Txt2.grid(row=1,column=2)

# label3=tk.Label(main,text="Contact").grid(row=2,column=1)
# Txt3=tk.Entry(main)
# Txt3.grid(row=2,column=2)

# btn1=tk.Button(main,text="submit",command=call).grid(row=3,column=2)



# # label4=tk.Label(main,text= "Student_name").grid(row=4,column=1)
# # data1=tk.Label(main,textvariable=Student_name).grid(row=5,column=1)
# # label5=tk.Label(main,text="Student_age").grid(row=6,column=1)
# # data2=tk.Label(main,textvariable=Student_age).grid(row=7,column=1)
# # label6=tk.Label(main,text="Student_contact_number").grid(row=8,column=1)
# # data3=tk.Label(main,textvariable=Student_contact_number).grid(row=9,column=1)

# main.mainloop()



