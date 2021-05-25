from tkinter import *
import math, random, os
from tkinter import messagebox
class bill_app():
    def __init__(self, root):
        self.root = root
        self.root.geometry("5000x5000")
        self.root.title("Billing software")
        bg_colour = "#074463"

        #===============================initialization of variables=====================
        #===========bath variables=================
        self.lakme_compact = IntVar()
        self.Lakme_SunExpert = IntVar()
        self.NewYork_ColossalKajal = IntVar()
        self.NewYork_BabyLips = IntVar()
        self.NiveaMen_cream = IntVar()
        self.PimpleClear=IntVar()
        self.Shampoo = IntVar()
        self.Lipstick =IntVar()
        #===========grocery variables=================
        self.AashirvadAtta = IntVar()
        self.BasmatiRice = IntVar()
        self.PeanutButter = IntVar()
        self.SunflowerOil = IntVar()
        self.MTRVermicelli =IntVar()
        self.MaggiPasta=IntVar()
        self.Noodles = IntVar()
        #===========cold drinks variables=================
        self.RedBull = IntVar()
        self.Pepsi = IntVar()
        self.maaza = IntVar()
        self.MountainDew = IntVar()
        self.sprite =IntVar()
        self.PepsiBlack = IntVar()
        self.AppyFizz_1l =IntVar() 
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


        search_btn = Button(f1, command = self.find_bill,text = "search", width = 18, font = ("times new roman", 10, "bold"), fg = "gold", bg = bg_colour, bd = 6, relief = GROOVE).grid(row = 0, column = 8, padx = 15, pady = 5)

        #===================================product labes====================================
        #===================================bath=============================================
        f2 = LabelFrame(self.root, text = "Cosmetic", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f2.place(x = 0, y = 165, height = 350, width = 340)

        Lakme_Perfect_Radiance_Compact_lbl = Label(f2, text = "lakme_compact", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0,padx = 15, pady = 10)

        Lakme_Perfect_Radiance_Compact_ent = Entry(f2, textvariable = self.lakme_compact,width = 2, font = ("arial", 15)).grid(row = 0, column = 1)


        Lakme_SunExpert_SPF40_lbl = Label(f2, text = "Lakme_SunExpert", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0,padx = 15, pady = 10)

        Lakme_SunExpert_SPF40_ent = Entry(f2, textvariable = self.Lakme_SunExpert,width = 2, font = ("arial", 15)).grid(row = 1, column = 1)


        MaybellineNewYork_ColossalKajal_lbl = Label(f2, text = "NewYork_ColossalKajal", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0,padx = 15, pady = 10)

        MaybellineNewYork_ColossalKajal_ent = Entry(f2, textvariable = self.NewYork_ColossalKajal,width = 2, font = ("arial", 15)).grid(row = 2, column = 1)


        MaybellineNewYork_BabyLips_lbl = Label(f2, text = "NewYork_BabyLips", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0,padx = 15, pady = 10)

        MaybellineNewYork_BabyLips_ent = Entry(f2, textvariable = self.NewYork_BabyLips,width = 2, font = ("arial", 15)).grid(row = 3, column = 1)

        NiveaMen_cream_lbl = Label(f2, text = "NiveaMen_cream", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 4, column = 0,padx = 15, pady = 10)

        NiveaMen_cream_ent = Entry(f2, textvariable = self.NiveaMen_cream,width = 2, font = ("arial", 15)).grid(row = 4, column = 1)

        HimalayaMen_PimpleClear_lbl = Label(f2, text = "PimpleClear", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 5, column = 0,padx = 15, pady = 10)

        HimalayaMen_PimpleClear_ent = Entry(f2, textvariable = self.PimpleClear,width = 2, font = ("arial", 15)).grid(row = 5, column = 1)

        TRESemmeKeratin_Shampoo_lbl = Label(f2, text = "Shampoo", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 6, column = 0,padx = 15, pady = 10)

        TRESemmeKeratin_Shampoo_ent = Entry(f2, textvariable = self.Shampoo,width = 2, font = ("arial", 15)).grid(row = 6, column = 1)

        
        #====================================grocery===========================================
        f3 = LabelFrame(self.root, text = "Grocery", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f3.place(x = 340, y = 165, height = 350, width = 340)


        AashirvadAtta_10kg_lbl = Label(f3, text = "AashirvadAtta", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 15, pady = 10)

        AashirvadAtta_10kg_ent = Entry(f3, textvariable = self.AashirvadAtta,width = 2, font = ("arial", 15)).grid(row = 0, column = 1)


        IndiaGate_Classic_BasmatiRice_5kg_lbl = Label(f3, text = "BasmatiRice", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 15, pady = 10)

        IndiaGate_Classic_BasmatiRice_5kg_ent = Entry(f3, textvariable = self.BasmatiRice,width = 2, font = ("arial", 15)).grid(row = 1, column = 1)


        SunDrop_PeanutButter_lbl = Label(f3, text = "PeanutButter", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 15, pady = 10)

        SunDrop_PeanutButter_ent = Entry(f3, textvariable = self.PeanutButter,width = 2, font = ("arial", 15)).grid(row = 2, column = 1)


        GoldWinner_SunflowerOil_lbl = Label(f3, text = "SunflowerOil", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 15, pady = 10)

        GoldWinner_SunflowerOil_ent = Entry(f3, textvariable = self.SunflowerOil,width = 2, font = ("arial", 15)).grid(row = 3, column = 1)
        
        MaggiPasta_lbl = Label(f3, text = "MaggiPasta", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 4, column = 0, padx = 15, pady = 10)

        MaggiPasta_ent = Entry(f3, textvariable = self.MaggiPasta,width = 2, font = ("arial", 15)).grid(row = 4, column = 1)
        
        MTRVermicelli_850g_lbl = Label(f3, text = "MTRVermicelli", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 5, column = 0, padx = 15, pady = 10)

        MTRVermicelli_850g_ent = Entry(f3, textvariable = self.MTRVermicelli,width = 2, font = ("arial", 15)).grid(row = 5, column = 1)
        
        Noodles_lbl_lbl = Label(f3, text = "Noodles", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 6, column = 0, padx = 15, pady = 10)

        Noodles_ent_ent = Entry(f3, textvariable = self.Noodles,width = 2, font = ("arial", 15)).grid(row = 6,column = 1)
        

        #=====================================cold drinks========================================
        f4 = LabelFrame(self.root, text = "Cold drinks", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_colour, bd = 12, relief = GROOVE)
        f4.place(x = 680, y = 165, height = 350, width = 340)


        RedBull_lbl = Label(f4, text = "RedBull", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 0, column = 0, padx = 50, pady = 10)

        RedBull_ent = Entry(f4, textvariable = self.RedBull,width = 2, font = ("arial", 15)).grid(row = 0, column = 1)


        Pepsi_lbl = Label(f4, text = "Pepsi", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 1, column = 0, padx = 50, pady = 10)

        Pepsi_ent = Entry(f4, textvariable = self.Pepsi,width = 2, font = ("arial", 15)).grid(row = 1, column = 1)


        maaza_750ml_lbl = Label(f4, text = "maaza", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 2, column = 0, padx = 50, pady = 10)

        maaza_750ml_ent = Entry(f4, textvariable = self.maaza,width = 2, font = ("arial", 15)).grid(row = 2, column = 1)


        MountainDew_lbl = Label(f4, text = "MountainDew", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 3, column = 0, padx = 50, pady = 10)

        MountainDew_ent = Entry(f4, textvariable = self.MountainDew,width = 2, font = ("arial", 15)).grid(row = 3, column = 1)

        sprite_lbl = Label(f4, text = "sprite", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 4, column = 0, padx = 50, pady = 10)

        sprite_ent = Entry(f4, textvariable = self.sprite,width = 2, font = ("arial", 15)).grid(row = 4, column = 1)
 
        PepsiBlack_lbl = Label(f4, text = "PepsiBlack", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 5, column = 0, padx = 50, pady = 10)

        PepsiBlack_ent = Entry(f4, textvariable = self.PepsiBlack,width = 2, font = ("arial", 15)).grid(row = 5, column = 1)
 
        AppyFizz_1l_lbl = Label(f4, text = "AppyFizz_1l", font = ("times new roman", 12, "bold"), fg = "gold", bg = bg_colour).grid(row = 6, column = 0, padx = 50, pady = 10)

        AppyFizz_1l_ent = Entry(f4, textvariable = self.AppyFizz_1l,width = 2, font = ("arial", 15)).grid(row = 6, column = 1)
 
        
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

        clear_btn = Button(f8, command = self.clear, text = "Clear", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 2, padx = 8, pady = 10)

        exit_btn = Button(f8, command = self.exit, text = "Exit", height = 1, width = 7, bd = 12, relief = GROOVE, font = ("times new roman", 18, "bold"), bg = bg_colour).grid(row = 0, column = 3, padx = 8, pady = 10)

        #=====================
        self.welcome_bill()
        #=====================
    #===================================total calculation========================
    def total(self):
        self.total_cosmetic = str(
                self.lakme_compact.get()*400+
                self.Lakme_SunExpert.get()*186+
                self.NewYork_ColossalKajal.get()*221+
                self.NewYork_BabyLips.get()*208+
                self.NiveaMen_cream.get()*95 + self.PimpleClear.get()*64+
                self.Shampoo.get()*743+
                self.Lipstick.get()*800)
        self.total_cosmetic_price.set(" Rs."+self.total_cosmetic)
        self.cosmetic_tax = round(float(self.total_cosmetic)*0.22, 2)
        self.total_cosmetic_tax.set(" Rs."+str(self.cosmetic_tax))

        self.total_grocery = str(
                self.AashirvadAtta.get()*375+
                self.BasmatiRice.get()*350+
                self.PeanutButter.get()*225+
                self.SunflowerOil.get()*120+
                self.MaggiPasta.get()*22+
                self.MTRVermicelli.get()*67+
                self.Noodles.get()*10 )
        self.total_grocery_price.set(" Rs."+self.total_grocery)
        self.grocery_tax = round(0.18*float(self.total_grocery), 2)
        self.total_grocery_tax.set(" Rs."+str(self.grocery_tax))

        self.total_cold_drink = str(
                self.RedBull.get()*115+
                self.Pepsi.get()*40+
                self.maaza.get()*38+
                self.MountainDew.get()*19+
                self.sprite.get()*39+
                self.PepsiBlack.get()*30+
                self.AppyFizz_1l.get()*58 )
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
                if self.lakme_compact.get() or self.Lakme_SunExpert.get() or self.NewYork_ColossalKajal.get() or self.NewYork_BabyLips.get() or self.NiveaMen_cream.get():
                        self.txtarea.insert(END, f"\n")
                if self.lakme_compact.get() != 0:
                        self.txtarea.insert(END, f"lakme_compact\t\t{self.lakme_compact.get()}\t\t{self.lakme_compact.get()*375}\n")
                if self.Lakme_SunExpert.get() != 0:
                        self.txtarea.insert(END, f"Lakme_SunExpert\t\t{self.Lakme_SunExpert.get()}\t\t{self.Lakme_SunExpert.get()*186}\n")
                if self.NewYork_ColossalKajal.get() != 0:
                        self.txtarea.insert(END, f"NewYork_ColossalKajal\t\t{self.NewYork_ColossalKajal.get()}\t\t{self.NewYork_ColossalKajal.get()*221}\n")
                if self.NewYork_BabyLips.get() != 0:
                        self.txtarea.insert(END, f"NewYork_BabyLips\t\t{self.NewYork_BabyLips.get()}\t\t{self.NewYork_BabyLips.get()*208}\n")
                if self.NiveaMen_cream.get() != 0:
                        self.txtarea.insert(END, f"NiveaMen_cream\t\t{self.NiveaMen_cream.get()}\t\t{self.NiveaMen_cream.get()*95}\n")
                if self.PimpleClear.get() != 0:
                        self.txtarea.insert(END, f"PimpleClear\t\t{self.PimpleClear.get()}\t\t{self.PimpleClear.get()*64}\n")
                if self.Shampoo.get() != 0:
                        self.txtarea.insert(END, f"Shampoo\t\t{self.Shampoo.get()}\t\t{self.Shampoo.get()*743}\n")
                if self.Lipstick.get() != 0:
                        self.txtarea.insert(END, f"Lipstick\t\t{self.Lipstick.get()}\t\t{self.Lipstick.get()*10}\n")                  
                #==========grocery==================
                if self.AashirvadAtta.get() or self.BasmatiRice.get() or self.PeanutButter.get() or self.SunflowerOil.get():
                        self.txtarea.insert(END, f"\n")
                if self.AashirvadAtta.get() != 0:
                        self.txtarea.insert(END, f"AashirvadAtta\t\t{self.AashirvadAtta.get()}\t\t{self.AashirvadAtta.get()*375}\n")
                if self.BasmatiRice.get() != 0:
                        self.txtarea.insert(END, f"BasmatiRice\t\t{self.BasmatiRice.get()}\t\t{self.BasmatiRice.get()*350}\n")
                if self.PeanutButter.get() != 0:
                        self.txtarea.insert(END, f"PeanutButter\t\t{self.PeanutButter.get()}\t\t{self.PeanutButter.get()*225}\n")
                if self.SunflowerOil.get() != 0:
                        self.txtarea.insert(END, f"SunflowerOil\t\t{self.SunflowerOil.get()}\t\t{self.SunflowerOil.get()*120}\n")
                if self.MaggiPasta.get() != 0:
                        self.txtarea.insert(END, f"MaggiPasta\t\t{self.MaggiPasta.get()}\t\t{self.MaggiPasta.get()*22}\n")
                if self.MTRVermicelli.get() != 0:
                        self.txtarea.insert(END, f"MTRVermicelli\t\t{self.MTRVermicelli.get()}\t\t{self.MTRVermicelli.get()*67}\n")
                if self.Noodles.get() != 0:
                        self.txtarea.insert(END, f"Noodles\t\t{self.Noodles.get()}\t\t{self.Noodles.get()*10}\n")
                
                #===========cold_drinks==================
                if self.RedBull.get() or self.Pepsi.get() or self.maaza.get() or self.MountainDew.get():
                        self.txtarea.insert(END, f"\n")
                if self.RedBull.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_001\t\t{self.RedBull.get()}\t\t{self.RedBull.get()*115}\n")
                if self.Pepsi.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_002\t\t{self.Pepsi.get()}\t\t{self.Pepsi.get()*40}\n")
                if self.maaza.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_003\t\t{self.maaza.get()}\t\t{self.maaza.get()*38}\n")
                if self.MountainDew.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_004\t\t{self.MountainDew.get()}\t\t{self.MountainDew.get()*19}\n")
                if self.sprite.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_004\t\t{self.sprite.get()}\t\t{self.sprite.get()*39}\n")
                if self.PepsiBlack.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_004\t\t{self.PepsiBlack.get()}\t\t{self.PepsiBlack.get()*30}\n")
                if self.AppyFizz_1l.get() != 0:
                        self.txtarea.insert(END, f"cold drinks_004\t\t{self.AppyFizz_1l.get()}\t\t{self.AppyFizz_1l.get()*58}\n")

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

                self.save_bill()


    def save_bill(self):
            op = messagebox.askyesno("save bill", "Do u want to save bill")
            if op>0:
                self.bill_data = self.txtarea.get("1.0", END)
                f = open("bills/"+str(self.bill_no.get())+".txt", "w")
                f.write(self.bill_data)
                f.close()  
                messagebox.showinfo("saved", f"Bill no. :{self.bill_no.get()} saved successfully") 
            else:
                    return                         
    
    def find_bill(self):
            present = 0
            for i in os.listdir("bills/"):
                    if i.split(".")[0] == self.search_bill.get():
                        f = open(f"bills/{i}", "r")
                        re = f.read()
                        self.txtarea.delete('1.0', END)
                        self.txtarea.insert(END, re )
                        f.close()
                        present = 1
            if not(present):
                    messagebox.showerror("Error", "Bill not found")

    def clear(self):
        op = messagebox.askyesno("Clear", "Sure u want to clear")
        if op>0:
                self.lakme_compact.set(0)
                self.Lakme_SunExpert.set(0)
                self.NewYork_ColossalKajal.set(0)
                self.NewYork_BabyLips.set(0)
                self.NiveaMen_cream.set(0)
                self.PimpleClear.set(0)
                self.Shampoo.set(0)
                self.Lipstick.set(0)
                #===========grocery variables=================
                self.AashirvadAtta.set(0)
                self.BasmatiRice.set(0)
                self.PeanutButter.set(0)
                self.SunflowerOil.set(0)
                self.MaggiPasta.set(0)
                self.MTRVermicelli.set(0)
                self.Noodles.set(0)
                #===========cold drinks variables=================
                self.RedBull.set(0)
                self.Pepsi.set(0)
                self.maaza.set(0)
                self.MountainDew.set(0)
                self.sprite.set(0)
                self.PepsiBlack.set(0)
                self.AppyFizz_1l.set(0)

                #===========Bill menu vriables=====================
                self.total_cosmetic_price.set("")
                self.total_grocery_price.set("")
                self.total_cold_drink_price.set("")
                self.total_cosmetic_tax.set("")
                self.total_grocery_tax.set("")
                self.total_cold_drink_tax.set("")
                #===============customer details variables===========
                self.c_name.set("")
                self.c_phone.set("")
                self.bill_no.set("")
                x = random.randint(1000, 9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")

                self.welcome_bill()
        else:
                return

    def exit(self):
        op = messagebox.askyesno("Exit", "Sure u want to exit")
        if op>0:
                self.root.destroy()



root = Tk()
obl = bill_app(root)
root.mainloop()
#added comment
