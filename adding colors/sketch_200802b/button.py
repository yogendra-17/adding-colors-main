class RadioButton:
    
    font_regular = None
    font_bold = None
    
    @classmethod
    def cook_font(cls):
        cls.font_regular = createFont("Roboto-Regular.ttf", 100)
        cls.font_bold = createFont("Roboto-Black.ttf", 100)
        print("fonts created")
    
    
    def __init__(self, location = (0,100), color = "#000000", text = "B"):
        self.location = location
        self.color = color
        self.text = text

        self.on = False
        self.size = 20


    def toggle(self):
        self.on = not self.on

    def draw(self):
        if self.on:
            fill(self.color)
            textFont(self.font_bold, self.size)
        else:
            fill(0)
            textFont(self.font_regular, self.size)
        text(self.text, self.location[0], self.location[1])

    def button_clicked(self):
        self.toggle()
        self.draw()

    def __repr__(self):
        return str(self.__dict__)
