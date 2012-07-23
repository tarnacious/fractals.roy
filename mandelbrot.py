import sys
from termcolor import cprint

def plot_function(z, c):
    return (z * z) + c

def has_escaped(z):
    mag = (z.real * z.real) + (z.imag * z.imag)
    return (mag > 10000)

def plot_mandelbrot_point(x, y):
    c = complex(x,y)
    z = complex(0,0)
    for i in range(20):
        if has_escaped(z):
            return (True, i)
        z = plot_function(z, c)
    return (False, None)

def plot_julia_point(k):
    def _plot_julia_point(x,y):
        z = complex(x,y)
        for i in range(20):
            if has_escaped(z):
                return (True, i)
            z = plot_function(z, k)
        return (False, None)
    return _plot_julia_point


def print_point(char,background):
    colours = ['on_red',
               'on_green',
               'on_yellow',
               'on_blue',
               'on_magenta',
               'on_cyan',
               'on_white']
    background = background % len(colours)
    cprint(char,'white',colours[background], end = '')

def draw(width, height, x1, y1, x2, y2, fun):

    step_x = abs(x1 - x2) / width
    step_y = abs(y1 - y2) / height

    for y in range(height):
        for x in range(width):
            point_x = x1 + (x * step_x) 
            point_y = y1 - (y * step_y)
            (escapes, time) = fun(point_x, point_y)

            if escapes:
                print_point(" ", time)
            else:
                sys.stdout.write(" ")
           
                
        print("")


if __name__ == '__main__':
    draw(70, 30, -2.0, 1.0, 1.0, -1.0, plot_mandelbrot_point)
    draw(70, 30, -2.0, 2.0, 2.0, -2.0, plot_julia_point(complex(0,0)))
    draw(70, 30, -2.0, 2.0, 2.0, -2.0, plot_julia_point(complex(0.835, -0.2321)))
    draw(70, 30, -2.0, 2.0, 2.0, -2.0, plot_julia_point(complex(1 - 1.61803399,0)))

