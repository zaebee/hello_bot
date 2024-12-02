from typing import Generator
y_max = 10
x_max = 10


def render_axis(points: list[tuple[int, int]]):
    return {y: ' ' * (x - 1) + '+' for x, y in points}

boarders = lambda x, y: [*['|'] * y, *['_'] * x]

def printer(boarders: list[str], points = None):
    points = points or []
    points = render_axis(points)
    for index, boarder in enumerate(boarders):
        x = points.get(y_max - index, '')
        if boarder == '|':
            if boarders[index + 1] == '_':
                print(boarder + x, end = '')
            else:
                print(boarder + x)
        elif boarder == '_':
            print(boarder, end='')

points = [(-2,-3), (5,7), (9,9)]
print(render_axis(points))


def show():
    printer(boarders(20, 10), [(15, 10), (5, 3), (1,2)])

show()