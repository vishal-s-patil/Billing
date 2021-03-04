from tkinter import *
import math, random
from tkinter import messagebox
class bill_app():
    def __init__(self, root):
        self.root = root
        self.root.geometry("5000x5000")
        self.root.title("Billing software")
        bg_colour = "#074463"

        #===============================initialization of variables=====================
        #===========bath variables=================
        self.cosmetic_001 = IntVar()
        self.cosmetic_002 = IntVar()
        self.cosmetic_003 = IntVar()
        self.cosmetic_004 = IntVar()
        #===========grocery variables=================
        self.grocery_001 = IntVar()
        self.grocery_002 = IntVar()
        self.grocery_003 = IntVar()
        self.grocery_004 = IntVar()
        #===========cold drinks variables=================
        self.cold_drinks_001 = IntVar()
        self.cold_drinks_002 = IntVar()
        self.cold_drinks_003 = IntVar()
        self.cold_drinks_004 = IntVar()
        #===========Bill menu vriables=====================
        self.total_cosmetic_price = StringVar()
        self.total_grocery_price = StringVar()
        self.total_cold_drink_price = StringVar()
        self.total_cosmetic_tax = StringVar()
        self.total_grocery_tax = StringVar()
        self.total_cold_drink_tax = StringVar()
        #===============customer details variables===========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
        #=========================================tille=================================
        title = Label(self.root, text = "Billing software", bg = bg_colour, font = ("times new roman", 30, "bold", "italic"),bd = 12, relief = GROOVE, fg = "black", pady = 2).pack(fill = X)
        #=========================================customer details======================
        f1 = LabelFrame(self.root, text = "customer details", fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE, font = ("times new roman", 20, "bold"))
        f1.place(x = 0, y = 80, relwidth = 1)


        c_name_lbl = Label(f1, text = "customer name", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 0)
        
        c_name_ent = Entry(f1, textvariable = self.c_name,width = 18, font = ("arial", 15)).grid(row = 0, column = 1)


        c_phone_lbl = Label(f1, text = "Phone NO.", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 2)

        c_Phone_ent = Entry(f1, textvariable = self.c_phone,width = 18, font = ("arial", 15)).grid(row = 0, column = 3)


        bill_id_lbl = Label(f1, text = "Bill id", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 4)

        bill_id_ent = Entry(f1, textvariable = self.search_bill,width = 18, font = ("arial", 15)).grid(row = 0, column = 5)


        search_btn = Button(f1, text = "search", width = 18, font = ("times new roman", 10, "bold"), fg = "gold", bg = bg_colour, bd = 6, relief = GROOVE).grid(row = 0, column = 8, padx = 15, pady = 5)

        #===================================product labes====================================
        #===================================bath=============================================
        f2 = LabelFrame(self.root, text = "Cosmetic", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f2.place(x = 0, y = 165, height = 350, width = 340)

        cosmetic_001_lbl = Label(f2, text = "cosmetic_001", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 26)

        cosmetic_001_ent = Entry(f2, textvariable = self.cosmetic_001,width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        cosmetic_002_lbl = Label(f2, text = "cosmetic_002", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 26)

        cosmetic_002_ent = Entry(f2, textvariable = self.cosmetic_002,width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        cosmetic_003_lbl = Label(f2, text = "cosmetic_003", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 26)

        cosmetic_003_ent = Entry(f2, textvariable = self.cosmetic_003,width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        cosmetic_004_lbl = Label(f2, text = "cosmetic_004", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 26)

        cosmetic_004_ent = Entry(f2, textvariable = self.cosmetic_004,width = 12, font = ("arial", 15)).grid(row = 3, column = 1)
        #====================================grocery===========================================
        f3 = LabelFrame(self.root, text = "Grocery", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f3.place(x = 340, y = 165, height = 350, width = 340)


        grocery_001_lbl = Label(f3, text = "grocery_001", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 26)

        grocery_001_ent = Entry(f3, textvariable = self.grocery_001,width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        grocery_002_lbl = Label(f3, text = "grocery_002", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 26)

        grocery_002_ent = Entry(f3, textvariable = self.grocery_002,width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        grocery_003_lbl = Label(f3, text = "grocery_003", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 26)

        grocery_003_ent = Entry(f3, textvariable = self.grocery_003,width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        grocery_004_lbl = Label(f3, text = "grocery_004", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 26)

        grocery_004_ent = Entry(f3, textvariable = self.grocery_004,width = 12, font = ("arial", 15)).grid(row = 3, column = 1)
        #=====================================cold drinks========================================
        f4 = LabelFrame(self.root, text = "Cold drinks", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f4.place(x = 680, y = 165, height = 350, width = 340)


        cold_drinks_001_lbl = Label(f4, text = "cold_drinks_001", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 26)

        cold_drinks_001_ent = Entry(f4, textvariable = self.cold_drinks_001,width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        cold_drinks_002_lbl = Label(f4, text = "cold_drinks_002", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 26)

        cold_drinks_002_ent = Entry(f4, textvariable = self.cold_drinks_002,width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        cold_drinks_003_lbl = Label(f4, text = "cold_drinks_004", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 26)

        cold_drinks_003_ent = Entry(f4, textvariable = self.cold_drinks_003,width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        cold_drinks_004_lbl = Label(f4, text = "cold_drinks_004", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 26)

        cold_drinks_004_ent = Entry(f4, textvariable = self.cold_drinks_004,width = 12, font = ("arial", 15)).grid(row = 3, column = 1)

        #===================bill area=====================================

        f6 = Frame(bd = 12, relief = GROOVE)
        f6.place(x =1020, y = 165, height = 350, width = 345)

        bill_label = Label(f6, text = "Bill", bd = 5, relief = GROOVE,fg = "white", bg = bg_colour).pack(fill = X)
        scroll_bar = Scrollbar(f6, orient = VERTICAL)
        self.txtarea = Text(f6, yscrollcommand = scroll_bar.set)
        scroll_bar.pack(fill = Y, side = RIGHT)
        scroll_bar.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH)

        #=======================billing menu===============================
        f7 = LabelFrame(self.root, text = "Billing menu", font = ("times new roman", 18, "bold"), bg = bg_colour, fg = "gold", bd = 12, relief = GROOVE)
        f7.place(x = 0, y = 515, height = 190, width = 1367)

        #=========================total=====================================
        total_cosmetic_price_lbl = Label(f7, text = "Total cosmetic price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 0, column = 0, padx = 20, pady = 13)

        total_cosmetic_price_ent = Entry(f7, textvariable = self.total_cosmetic_price,width = 10, font = ("time new roman", 10, "bold")).grid(row = 0, column = 1)


        total_grocery_price_lbl = Label(f7, text = "Total grocery price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 1, column = 0, padx = 20, pady = 13)

        total_grocery_price_ent = Entry(f7, textvariable = self.total_grocery_price,width = 10, font = ("time new roman", 10, "bold")).grid(row = 1, column = 1)


        total_cold_drink_price_lbl = Label(f7, text = "Total cold drink price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 2, column = 0, padx = 20, pady = 13)

        total_cold_drink_price_ent = Entry(f7, textvariable = self.total_cold_drink_price,width = 10, font = ("time new roman", 10, "bold")).grid(row = 2, column = 1)

        #============================tax==========================================

        total_cosmetic_price_lbl = Label(f7, text = "Total cosmetic tax", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 0, column = 2, padx = 20, pady = 13)

        total_cosmetic_price_ent = Entry(f7, textvariable = self.total_cosmetic_tax,width = 10, font = ("time new roman", 10, "bold")).grid(row = 0, column = 3)


        total_grocery_price_lbl = Label(f7, text = "Total grocery tax", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 1, column = 2, padx = 20, pady = 13)

        total_grocery_price_ent = Entry(f7, textvariable = self.total_grocery_tax,width = 10, font = ("time new roman", 10, "bold")).grid(row = 1, column = 3)


        total_cold_drink_price_lbl = Label(f7, text = "Total cold drink tax", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 2, column = 2, padx = 20, pady = 13)

        total_cold_drink_price_ent = Entry(f7, textvariable = self.total_cold_drink_tax,width = 10, font = ("time new roman", 10, "bold")).grid(row = 2, column = 3)

        #==================================buttons=============================

        f8 = Frame(f7, bd = 7, relief = GROOVE ,pady = 15)
        f8.place(x = 680, y = 16)

        total_btn = Button(f8, command = self.total, text = "Total", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 0, padx = 8, pady = 10)

        generate_bill_btn = Button(f8, command = self.bill_area,text = "Generate bill", height = 1, width = 10, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 1, padx = 8, pady = 10)

        clear_btn = Button(f8, text = "Clear", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 2, padx = 8, pady = 10)

        exit_btn = Button(f8, text = "Exit", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 3, padx = 8, pady = 10)

        #=====================
        self.welcome_bill()
        #=====================
    #===================================total calculation========================
    def total(self):
        self.total_cosmetic = str(
                self.cosmetic_001.get()*10+
                self.cosmetic_002.get()*10+
                self.cosmetic_003.get()*10+
                self.cosmetic_004.get()*10 )
        self.total_cosmetic_price.set(" Rs."+self.total_cosmetic)
        self.cosmetic_tax = round(float(self.total_cosmetic)*0.22, 2)
        self.total_cosmetic_tax.set(" Rs."+str(self.cosmetic_tax))

        self.total_grocery = str(
                self.grocery_001.get()*10+
                self.grocery_002.get()*10+
                self.grocery_003.get()*10+
                self.grocery_004.get()*10 )
        self.total_grocery_price.set(" Rs."+self.total_grocery)
        self.grocery_tax = round(0.18*float(self.total_grocery), 2)
        self.total_grocery_tax.set(" Rs."+str(self.grocery_tax))

        self.total_cold_drink = str(
                self.cold_drinks_001.get()*10+
                self.cold_drinks_002.get()*10+
                self.cold_drinks_003.get()*10+
                self.cold_drinks_004.get()*10 )
        self.total_cold_drink_price.set(" Rs."+self.total_cold_drink)
        self.cold_drinks_tax = round(float(self.total_cold_drink)*0.22, 2)
        self.total_cold_drink_tax.set(" Rs."+str(self.cold_drinks_tax))
            
    def welcome_bill(self):
            self.txtarea.delete("1.0", END)
            self.txtarea.insert(END, "\t\twelcome\n")
            self.txtarea.insert(END, f"Bill No.      :{self.bill_no.get()}\n")
            self.txtarea.insert(END, f"customer Name :{self.c_name.get()}\n")
            self.txtarea.insert(END, f"Phone No.     :{self.c_phone.get()}\n")
            self.txtarea.insert(END, "=====================================")
            self.txtarea.insert(END, "products\t\tQnt\t\tprice\n")
            self.txtarea.insert(END, "=====================================")
    
    def bill_area(self):
            if self.c_name.get() ==  "" or self.c_phone.get() == "":
                    messagebox.showerror("Error", "customer details are must")
            else:
                self.welcome_bill()
                #===========cosmetic==================
                if self.cosmetic_001.get() or self.cosmetic_002.get() or self.cosmetic_003.get() or self.cosmetic_004.get():
                        self.txtarea.insert(END, f"\n")
                if self.cosmetic_001.get() != 0:
                        self.txtarea.insert(END, f"cosmetic_001\t\t{self.cosmetic_001.get()}\t\t{self.cosmetic_001.get()*10}\n")
                if self.cosmetic_002.get() != 0:
                        self.txtarea.insert(END, f"cosmetic_002\t\t{self.cosmetic_002.get()}\t\t{self.cosmetic_002.get()*10}\n")
                if self.cosmetic_003.get() != 0:
                        self.txtarea.insert(END, f"cosmetic_003\t\t{self.cosmetic_003.get()}\t\t{self.cosmetic_003.get()*10}\n")
                if self.cosmetic_004.get() != 0:
                        self.txtarea.insert(END, f"cosmetic_004\t\t{self.cosmetic_004.get()}\t\t{self.cosmetic_004.get()*10}\n")
                
                #==========grocery==================
                if self.grocery_001.get() or self.grocery_002.get() or self.grocery_003.get() or self.grocery_004.get():
                        self.txtarea.insert(END, f"\n")
                if self.grocery_001.get() != 0:
                        self.txtarea.insert(END, f"grocery_001\t\t{self.grocery_001.get()}\t\t{self.grocery_001.get()*10}\n")
                if self.grocery_002.get() != 0:
                        self.txtarea.insert(END, f"grocery_002\t\t{self.grocery_002.get()}\t\t{self.grocery_002.get()*10}\n")
                if self.grocery_003.get() != 0:
                        self.txtarea.insert(END, f"grocery_003\t\t{self.grocery_003.get()}\t\t{self.grocery_003.get()*10}\n")
                if self.grocery_004.get() != 0:
                        self.txtarea.insert(END, f"grocery_004\t\t{self.grocery_004.get()}\t\t{self.grocery_004.get()*10}\n")

                #===========cold_drinks==================
                if self.cold_drinks_001.get() or self.cold_drinks_002.get() or self.cold_drinks_003.get() or self.cold_drinks_004.get():
                        self.txtarea.insert(END, f"\n")
                if self.cold_drinks_001.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_001\t\t{self.cold_drinks_001.get()}\t\t{self.cold_drinks_001.get()*10}\n")
                if self.cold_drinks_002.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_002\t\t{self.cold_drinks_002.get()}\t\t{self.cold_drinks_002.get()*10}\n")
                if self.cold_drinks_003.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_003\t\t{self.cold_drinks_003.get()}\t\t{self.cold_drinks_003.get()*10}\n")
                if self.cold_drinks_004.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_004\t\t{self.cold_drinks_004.get()}\t\t{self.cold_drinks_004.get()*10}\n")

                if self.total_cosmetic_tax.get() != "" and self.total_cosmetic_tax.get() != " Rs.0.0":
                        self.txtarea.insert(END, "=====================================\n")
                        self.txtarea.insert(END, f"Total cosmetic Tax\t\t\t{self.total_cosmetic_tax.get()}\n")

                if self.total_grocery_tax.get() != "" and self.total_grocery_tax.get() != " Rs.0.0":
                        self.txtarea.insert(END, "-------------------------------------\n")
                        self.txtarea.insert(END, f"Total grocery Tax\t\t\t{self.total_grocery_tax.get()}\n")

                if self.total_cold_drink_tax.get() != "" and self.total_cold_drink_tax.get() != " Rs.0.0":
                        self.txtarea.insert(END, "-------------------------------------\n")
                        self.txtarea.insert(END, f"Total cold drinks Tax\t\t\t{self.total_cold_drink_tax.get()}\n")
                self.txtarea.insert(END, "=====================================\n")

                self.Total_Bill =round(float( float(self.total_cosmetic) +
                                        float(self.total_cosmetic) +
                                        float(self.total_cosmetic) +
                                        float(self.cosmetic_tax) +
                                        float(self.grocery_tax) +
                                        float(self.cold_drinks_tax) ), 2)

                
                self.txtarea.insert(END, f"Total Bill\t\t\t Rs. {self.Total_Bill}")                         


root = Tk()
obl = bill_app(root)
root.mainloop()