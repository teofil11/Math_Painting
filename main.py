from canvas import Canvas
from shapqes import Rectangle, Square

# Get canvas width and height
canvas_width = int(input('Enter canvas width: '))
canvas_height = int(input('Enter canvas hqight: '))

# Get canvas color
colors = {'white': (255, 255, 255), 'black': (0, 0 , 0)}
canvas_color = input('Enter canvas color(white or black): ')

# Create canvas
canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

while True:
    shape_type = input('What do you like to draw(rectangle or square): ')

    # If user select rectangle
    if shape_type.lower() =='rectangle':
        rec_height = int(input('Enter the height of the rectangle: '))
        rec_width = int(input('Enter the width of the rectangle: '))
        rec_x = int(input('Enter x of the rectangle: '))
        rec_y = int(input('Enter y of the rectangle: '))
        red = int(input('Hoe much red should the rectangle?: '))
        green = int(input('Hoe much green?: '))
        blue = int(input('Hoe much blue?: '))

        # Create rectangle 
        rec = Rectangle(rec_height, rec_width, rec_x, rec_y, (red, green, blue))
        rec.draw(canvas)

    # If user select square
    if shape_type.lower() == 'square':
        sqr_x = int(input('Enter x of the square: '))
        sqr_y = int(input('Enter y of the square: '))
        sqr_side = int(input('Enter the side lenght of the square: '))
        red = int(input('Hoe much red should the square?: '))
        green = int(input('Hoe much green?: '))
        blue = int(input('Hoe much blue?: '))

        # Create square
        sqr = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        sqr.draw(canvas)
    
    if shape_type == 'quit':
        break

canvas.make('canvas.png')