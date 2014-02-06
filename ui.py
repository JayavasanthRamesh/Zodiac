import gtk, sys
global self

def drawchart(planetary_matrix):
    window=gtk.Window()
    gtk.push_rgb_visual()
    self.area = gtk.GtkDrawingArea()
    gtk.pop_visual()
    self.area.size(400, 300)
    self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
    drawable=drawing_area.window
    for i in range(0,2):
        for j in range(0,3):
            self.area.draw_rectangle(self.gc, True , i*30, j*20, 25, 20)

    window.add(self.area)
    window.show_all()
    gtk.main()

def generatechartpostions(hour,min,second,ampm,date,place):
    print hour
    print date
    print place
    planetary_matrix=[["ragu","kethu"],["moon","sun"],[],[],[],[],["uranus"],["neptune"],[],[],[],["mars","jupiter"]]
    drawchart(planetary_matrix)


class PyApp(gtk.Window):
    
    global combobox
    global hour
    global minute
    global second 
    global calendar
    global ampm
    global self

    def callback(self,widget,data=None):
        self.destroy()
        generatechartpostions(hour.get_text(),minute.get_text(),second.get_text(),ampm.get_active_text(),calendar.get_date(),combobox.get_active_text())
        

    def __init__(self):
        super(PyApp, self).__init__()
        
        global combobox
        global hour
        global minute
        global second 
        global calendar
        global ampm

        combobox = gtk.combo_box_new_text()
        self.set_title("RaaZee")
        self.set_size_request(400, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        try:
            self.set_icon_from_file("raazee.png")
        except Exception, e:
            print e.message
            sys.exit(1)

        self.fixed = gtk.Fixed()
        self.add(self.fixed)

        date_label= gtk.Label("-- Zodiac Calculator --")
        self.fixed.put(date_label,140,30)

        date_label= gtk.Label("Choose Your DOB")
        self.fixed.put(date_label,100,60)

        calendar = gtk.Calendar()
        self.fixed.put(calendar,100,80)

        time_label= gtk.Label("Time of birth")
        self.fixed.put(time_label,50,273)

        hour = gtk.Entry(2)
        hour.set_width_chars(2)
        hour.set_text("00")
        self.fixed.put(hour,130,270)

        hour_label= gtk.Label("Hr")
        self.fixed.put(hour_label,155,273)

        minute = gtk.Entry(2)
        minute.set_width_chars(2)
        minute.set_text("00")
        self.fixed.put(minute,175,270)

        minute_label= gtk.Label("min")
        self.fixed.put(minute_label,200,273)

        second = gtk.Entry(2)
        second.set_width_chars(2)
        second.set_text("00")
        self.fixed.put(second,225,270)

        sec_label= gtk.Label("sec")
        self.fixed.put(sec_label,250,273)

        ampm= gtk.combo_box_new_text()
        ampm.append_text("AM")
        ampm.prepend_text("PM")
        ampm.set_active(1)
        self.fixed.put(ampm,275,273)

        place_label= gtk.Label("Choose the nearest birth place  ")
        self.fixed.put(place_label,70,303)

        
        combobox.append_text("Chennai")
        combobox.prepend_text("Gujarat")
        combobox.append_text("Delhi")
        combobox.prepend_text("Bangalore")
        combobox.append_text("Amristar")
        combobox.prepend_text("Mumbai")
        combobox.set_active(3)
        self.fixed.put(combobox,240,300)


        Check_button=gtk.Button("Submit")
        Check_button.connect("clicked", self.callback, "cool button")
        Check_button.set_size_request(50, 40)
        self.fixed.put(Check_button, 300, 350)

        self.connect("destroy", gtk.main_quit)
        self.show_all()

PyApp()
gtk.main()