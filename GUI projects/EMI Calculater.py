import tkinter as tk

# p = Principal or Loan Amount
# r = Interest Rate Per Month
# t = number of months

def Calculate():
    principal_amount=(principal.get())
   
    Rate_of_amount=(float(Rate.get())/12/100)
  
    Time_period=(Time.get())
#  emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    input_emi=(principal_amount*Rate_of_amount*pow(1+Rate_of_amount,Time_period))/(pow(1+Rate_of_amount,Time_period)-1)
    emi.set(input_emi)

    total_Payment=float(input_emi * Time_period)
    Total_Payment.set(format(total_Payment))
    total_interest=total_Payment-principal_amount
    Total_interest.set(format(total_interest))

main_window = tk.Tk(className=" EMI CALCULATER ")
main_window.geometry("600x600")
main_window.configure(bg='white')

label1=tk.Label(main_window,text="Principal amount").grid(row=0,column=0)
label2=tk.Label(main_window,text=" Rate of amount").grid(row=2,column=0)
label3=tk.Label(main_window,text=" Rate of time").grid(row=4,column=0)
Btn1=tk.Button(main_window,text="Calculate",command=Calculate).grid(row=6,column=1)


principal=tk.IntVar(main_window)
Rate=tk.IntVar(main_window)
Time=tk.IntVar(main_window)
emi=tk.IntVar(main_window)
Total_interest=tk.StringVar(main_window)
Total_Payment=tk.StringVar(main_window)


tk.Entry(main_window,textvariable=principal).grid(row=0,column=1)
tk.Entry(main_window,textvariable=Rate).grid(row=2,column=1)
tk.Entry(main_window,textvariable=Time).grid(row=4,column=1)
tk.Label(main_window,text="EMI").grid(row=8,column=1)
tk.Label(main_window,textvariable=emi).grid(row=9,column=1)
tk.Label(main_window,text="Total interest").grid(row=10,column=1)
tk.Label(main_window,textvariable=Total_interest).grid(row=11,column=1)
tk.Label(main_window,text="Total payment").grid(row=12,column=1)
tk.Label(main_window,textvariable=Total_Payment).grid(row=13,column=1)


main_window.mainloop()



