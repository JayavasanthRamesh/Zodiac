import birthchartgenerator
import gtk, sys
global self

def expose_handler(widget,event):
    w, h = widget.window.get_size()
    xgc = widget.window.new_gc()
    xgc.set_rgb_fg_color(gtk.gdk.color_parse("white"))
    widget.window.draw_rectangle(xgc, True, 0, 0, 100, 100)           # black
    xgc.line_width = 6
    widget.window.draw_rectangle(xgc, True, 100, 100, 100, 100)  
    widget.window.draw_rectangle(xgc, True, 200, 200, 100, 100)  

def drawchart(result):
    win = gtk.Window()

# Organize widgets in a vertical box:
    #vbox = gtk.VBox()
    #win.add(vbox)

# Create an area to draw in:
    #drawing_area = gtk.DrawingArea()
    #drawing_area.set_size_request(400, 400)
    #vbox.pack_start(drawing_area)
    #textbox = gtk.TextView()
    #text = gtk.TextBuffer()
    #text.set_text(result)
    #set_wrap_mode(gtk.WRAP_WORD)
    #textbox.set_buffer(text)
    #textbox.set_line_wrap()
    #win.add(textbox)

    #drawing_area.connect("expose-event", expose_handler)
    message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
    message.set_markup(result)
    message.run()
    
    drawing_area.show()
    win.show_all()
    gtk.main()

def result_display(result):
    
    end=""
    gender="He"
    count=0
    for x in result:
        if(count):
            s=''.join(x)
            s=s.replace("The native",gender)
            s=s.replace("The person",gender)
            end+=s
        else:
            end+='.'.join(x) 
        count=count+1
    return end

def generatechartpostions(hour,mins,date,place):

    result=birthchartgenerator.getplanet_matrix(hour,mins,date[2],date[1],date[0],place)
    end=result_display(result)
    drawchart(end)

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
        generatechartpostions(hour.get_text(),minute.get_text(),calendar.get_date(),combobox.get_active_text())
        

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


        sec_label= gtk.Label("24 Hour format")
        self.fixed.put(sec_label,250,273)

        

        place_label= gtk.Label("Choose the nearest birth place  ")
        self.fixed.put(place_label,70,303)

        
        combobox.append_text("chennai")
        combobox.prepend_text("gujarat")
        combobox.append_text("delhi")
        combobox.prepend_text("bangalore")
        combobox.append_text("amristar")
        combobox.prepend_text("mumbai")
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
