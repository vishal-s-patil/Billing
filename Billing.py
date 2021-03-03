from tkinter import *
class bill_app():
    def __init__(self, root):

        self.root = root
        self.root.geometry("1300x700")
        self.root.title("Billing software")
        bg_colour = "#074463"
        #=================================

        #=========================================tille=================================
        title = Label(self.root, text = "Billing software", bg = bg_colour, font = ("times new roman", 30, "bold", "italic"),bd = 12, relief = GROOVE, fg = "black", pady = 2).pack(fill = X)
        #=========================================customer details======================
        f1 = LabelFrame(self.root, text = "customer details", fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE, font = ("times new roman", 20, "bold"))
        f1.place(x = 0, y = 80, relwidth = 1)


        c_name_lbl = Label(f1, text = "customer name", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 0)
        
        c_name_ent = Entry(f1, width = 18, font = ("arial", 15)).grid(row = 0, column = 1)


        c_phone_lbl = Label(f1, text = "Phone NO.", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 2)

        c_Phone_ent = Entry(f1, width = 18, font = ("arial", 15)).grid(row = 0, column = 3)


        bill_id_lbl = Label(f1, text = "Bill id", fg = "gold", bg = bg_colour, font = ("times new roman", 18, "bold"), padx = 15, pady = 2).grid(row = 0, column = 4)

        bill_id_ent = Entry(f1, width = 18, font = ("arial", 15)).grid(row = 0, column = 5)


        search_btn = Button(f1, text = "search", width = 15, font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour, bd = 6, relief = GROOVE).grid(row = 0, column = 8, padx = 10)

        #===================================product labes====================================
        #===================================bath=============================================
        f2 = LabelFrame(self.root, text = "bath products", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f2.place(x = 0, y = 165, height = 350, width = 340)

        bath_soap_lbl = Label(f2, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f2, width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        bath_soap_lbl = Label(f2, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f2, width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        bath_soap_lbl = Label(f2, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f2, width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        bath_soap_lbl = Label(f2, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f2, width = 12, font = ("arial", 15)).grid(row = 3, column = 1)
        #====================================grocery===========================================
        f3 = LabelFrame(self.root, text = "grocery", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f3.place(x = 340, y = 165, height = 350, width = 340)


        bath_soap_lbl = Label(f3, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f3, width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        bath_soap_lbl = Label(f3, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f3, width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        bath_soap_lbl = Label(f3, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f3, width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        bath_soap_lbl = Label(f3, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f3, width = 12, font = ("arial", 15)).grid(row = 3, column = 1)
        #=====================================cold drinks========================================
        f4 = LabelFrame(self.root, text = "cold drinks", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f4.place(x = 680, y = 165, height = 350, width = 340)


        bath_soap_lbl = Label(f4, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f4, width = 12, font = ("arial", 15)).grid(row = 0, column = 1)


        bath_soap_lbl = Label(f4, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f4, width = 12, font = ("arial", 15)).grid(row = 1, column = 1)


        bath_soap_lbl = Label(f4, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f4, width = 12, font = ("arial", 15)).grid(row = 2, column = 1)


        bath_soap_lbl = Label(f4, text = "Bath soap", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 30, pady = 20)

        bath_soap_ent = Entry(f4, width = 12, font = ("arial", 15)).grid(row = 3, column = 1)

        #===================bill area=====================================

        f6 = Frame(bd = 12, relief = GROOVE)
        f6.place(x =1020, y = 165, height = 350, width = 345)

        bill_label = Label(f6, text = "Bill", bd = 5, relief = GROOVE,fg = "white", bg = bg_colour).pack(fill = X)
        scroll_bar = Scrollbar(f6, orient = VERTICAL)
        textarea = Text(f6, yscrollcommand = scroll_bar.set)
        scroll_bar.pack(fill = Y, side = RIGHT)
        scroll_bar.config(command = textarea.yview)
        textarea.pack(fill = BOTH)

        #=======================billing menu===============================
        f7 = LabelFrame(self.root, text = "Billing menu", font = ("times new roman", 18, "bold"), bg = bg_colour, fg = "gold", bd = 12, relief = GROOVE)
        f7.place(x = 0, y = 515, height = 190, width = 1367)

        #=========================total=====================================
        total_cosmetic_price_lbl = Label(f7, text = "Total cosmetic price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 0, column = 0, padx = 20, pady = 13)

        total_cosmetic_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 0, column = 1)


        total_grocery_price_lbl = Label(f7, text = "Total grocery price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 1, column = 0, padx = 20, pady = 13)

        total_grocery_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 1, column = 1)


        total_cold_drink_price_lbl = Label(f7, text = "Total cold drink price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 2, column = 0, padx = 20, pady = 13)

        total_cold_drink_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 2, column = 1)

        #============================tax==========================================

        total_cosmetic_price_lbl = Label(f7, text = "Total cosmetic price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 0, column = 2, padx = 20, pady = 13)

        total_cosmetic_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 0, column = 3)


        total_grocery_price_lbl = Label(f7, text = "Total grocery price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 1, column = 2, padx = 20, pady = 13)

        total_grocery_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 1, column = 3)


        total_cold_drink_price_lbl = Label(f7, text = "Total cold drink price", fg =  "gold", bg = bg_colour, font = ("times new roman", 15, "bold")).grid(row = 2, column = 2, padx = 20, pady = 13)

        total_cold_drink_price_ent = Entry(f7, width = 10, font = ("time new roman", 10, "bold")).grid(row = 2, column = 3)

        #==================================buttons=============================

        f8 = Frame(f7, bd = 7, relief = GROOVE ,pady = 15)
        f8.place(x = 680, y = 16)

        total_btn = Button(f8, text = "Total", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 0, padx = 8, pady = 10)

        generate_bill_btn = Button(f8, text = "Generate bill", height = 1, width = 10, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 1, padx = 8, pady = 10)

        clear_btn = Button(f8, text = "Clear", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 2, padx = 8, pady = 10)

        exit_btn = Button(f8, text = "Exit", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 3, padx = 8, pady = 10)
        #===================================back_end======================================================
        
root = Tk()
obl = bill_app(root)
root.mainloop()