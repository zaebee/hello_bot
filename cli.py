from typing import Generator


def render_axis(points: list[tuple[int, int]]):
    return {y: ' ' * (x - 1) + '+' for x, y in points}


def printer(size: tuple[int, int], points = None):
    x_max, y_max = size
    borders = [*['|'] * y_max, *['_'] * x_max]
    points = render_axis(points or [])
    print(f'{y_max}')
    for index, border in enumerate(borders):
        x = points.get(y_max - index, '')
        end = '' if border == '_' or borders[index + 1] == '_' else '\n'
        print(border + x, end=end)
    print(f'{x_max}')



if __name__ == '__main__':
    # TODO: read points from console args. Like, --points 3,4 1,1 5,5
    points = [(1, 1), (15, 10), (5,7), (9,9)]
    printer((20, 10), points)