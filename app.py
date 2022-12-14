import tkinter as tk

win= tk.Tk()
win.title(" COPPER LOSE CALCULATOR")
#win.geometry("300x300")

# Primary Side Current

primary_current = tk.Label(win,text="Primary Current : ", font="verdana 14 ")
primary_current.grid(row=0,column=0,)
primary_current_entry = tk.Entry(win)
primary_current_entry.grid(row=1, column=0, sticky=tk.N)


#Primary Side Resistance


primary_resistance= tk.Label(win,text="Primary Resistance : ", font="verdana 14")
primary_resistance.grid(row=2,column=0)
primary_resistance_entry=tk.Entry(win)
primary_resistance_entry.grid(row=3,column=0)

#Secondary Side Current

secondary_current= tk.Label(win,text="Secondary Current : ",font="verdana 14")
secondary_current.grid(row=4,column=0)
secondary_current_entry=tk.Entry(win)
secondary_current_entry.grid(row=5,column=0)


#Secondary Side Resistance

secondary_resistance = tk.Label(win,text="Secondary Resistance",font="verdana 14")
secondary_resistance.grid(row=6,column=0)
secondary_resistance_entry=tk.Entry(win)
secondary_resistance_entry.grid(row=7 , column=0)

#BUTON OLUŞTURMA
result_label= tk.Label(win,font="verdana 20")
result_label.grid(row=10,column=0)

def Calculate():
    primary_current= float(primary_current_entry.get())
    primary_resistance= float(primary_resistance_entry.get())
    secondary_current = float(secondary_current_entry.get())
    secondary_resistance = float(secondary_resistance_entry.get())
    result = primary_current * primary_current * primary_resistance + secondary_resistance * secondary_current * secondary_current
    result_label["text"] = str(result)


buton = tk.Button(win,text="Calculate", command = Calculate)
buton.grid(row=8,column=0,sticky=tk.N)
result= tk.Label(win, text = "Result : ", font = "verdana 14")
result.grid(row=9,column=0)


win.mainloop()

# def   primary_resistance= float(primary_resistance.entry.get())
 #   primary_current= float(primary_current.entry.get())
  #  secondary_current=float(secondary_current.entry.get())
   # secondary_resistance=float(secondary_resistance.entry.get())
     #result=primary_current*primary_current*primary_resistance+secondary_current*secondary_current*secondary_resistance
       #r_label['text'] = str(result)
