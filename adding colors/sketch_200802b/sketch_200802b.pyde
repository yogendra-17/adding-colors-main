from button import RadioButton
import itertools as it
BUTTON_SIZE = 20
PAD = BUTTON_SIZE/2
WIDTH = 800
BUTTON_LOCS = [((WIDTH-7*PAD, 3*PAD),'R1'), ((WIDTH-5*PAD, 3*PAD),'G1'), ((WIDTH - 3*PAD, 3*PAD),'B1'),
               ((WIDTH-7*PAD, 7*PAD),'R2'), ((WIDTH-5*PAD, 7*PAD),'G2'), ((WIDTH - 3*PAD, 7*PAD),'B2')]
def setup():
    global buttons
    RadioButton.cook_font()
    size(WIDTH,WIDTH)
    # font = createFont("Roboto-Regular-ttf", 20)
    # text("HELLO", 10, 10)

    buttons = {'R1': RadioButton(location = BUTTON_LOCS[0][0], color = "#FF0000", text = "R"),
               'G1': RadioButton(location = BUTTON_LOCS[1][0], color = "#00FF00", text = "G"),
               'B1': RadioButton(location = BUTTON_LOCS[2][0], color = "#0000FF", text = "B"),
               'R2': RadioButton(location = BUTTON_LOCS[3][0], color = "#FF0000", text = "R"),
               'G2': RadioButton(location = BUTTON_LOCS[4][0], color = "#00FF00", text = "G"),
               'B2': RadioButton(location = BUTTON_LOCS[5][0], color = "#0000FF", text = "B"),
               }
        
def mouseClicked():
    for b in buttons.values():
        x_low, x_high = b.location[0], b.location[0] + BUTTON_SIZE
        y_low, y_high = b.location[1] - BUTTON_SIZE * 1.5, 1.3 * b.location[1]
        if (x_low < mouseX < x_high and
            y_low < mouseY < y_high):
            b.toggle()
            b.draw()
        print(x_low, mouseX, x_high)
        print(y_low, mouseY, y_high)
        print("")
  
def mouseDragged():
    return True

step = 5

def draw_grid():
    global step, buttons
    if mousePressed:
        dx = mouseX - pmouseX
        if (1 <= step <= int(width)):
            step += dx
        if step <= 0: step = 5;
        if step >= int(width)-1: step = int(width) - 5;
    print(step)
        
    j = 1
    for (x, y) in it.product(range(0, int(width), step), range(0, int(width), step)):
        if ((x+y)/step)%2 == 0:
            col1 = color(255*buttons['R1'].on, 255*buttons['G1'].on, 255*buttons['B1'].on)
            fill(col1)
            rect(x, y, step, step)
            j += 1
        else:
            col2 = color(255*buttons['R2'].on, 255*buttons['G2'].on, 255*buttons['B2'].on)
            fill(col2)
            rect(x, y, step, step)
            j += 1
    
    if col1 == color(0) == col2:
        textSize = 30
        fill(255)
        text("Click on the some letters and drag mouse anywhere on screen", width/3, width/3, width/3, width/3) 
        noFill()
        stroke(255)
        strokeWeight(5)
        bezier(0.5 * width, 0.3 * width,
               0.5 * width, 0.1 * width,
               0.5 * width, 0.1 * width,
               buttons['R1'].location[0]-2*PAD, buttons['R1'].location[1]+2*PAD)
    
def draw():
    background(0)
    
    draw_grid()
    
    with pushMatrix():
        noStroke()
        fill(255,255,255,200)
        translate(-PAD, -2*PAD) 
        rect(BUTTON_LOCS[0][0][0], BUTTON_LOCS[0][0][1], 7*PAD, 7*PAD)
    
    for b in buttons.values():
        b.draw()
