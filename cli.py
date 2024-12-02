from typing import Generator


def render_axis(points: list[tuple[int, int]]):
    return {y: ' ' * (x - 1) + '+' for x, y in points}


def printer(size: tuple[int, int], points = None):
    x_max, y_max = size
    boarders = [*['|'] * y_max, *['_'] * x_max]
    points = render_axis(points or [])
    print(y_max)
    for index, boarder in enumerate(boarders):
        x = points.get(y_max - index, '')
        if boarder == '|':
            end = '' if boarders[index + 1] == '_' else '\n'
            print(boarder + x, end=end)
        elif boarder == '_':
            print(boarder, end='')
    print(x_max)


points = [(15, 10), (5,7), (9,9)]

def show():
    printer((20, 10), points)

show()