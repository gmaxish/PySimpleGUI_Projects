import PySimpleGUI as sg
from time import time
from random import randint


def place_cell():
    cell = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while cell in snake_body:
        cell = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return cell


def convert_pos_to_pixil(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br


FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

snake_body = [(4, 4), (3, 4), (2, 4)]
DIRECTIONS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
direction = DIRECTIONS['up']

cell = place_cell()
cell_eaten = False

sg.theme('green')
field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color='black'
)
layout = [
    [field]
]

window = sg.Window('Snake', layout, return_keyboard_events=True)
start_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break

    if event.startswith("Left"):
        direction = DIRECTIONS['left']
    if event.startswith("Up"):
        direction = DIRECTIONS['up']
    if event.startswith('Right'):
        direction = DIRECTIONS['right']
    if event.startswith('Down'):
        direction = DIRECTIONS['down']

    time_since_start = time() - start_time
    if time_since_start >= 0.5:
        start_time = time()

        if snake_body[0] == cell:
            cell = place_cell()
            cell_eaten = True

        new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
        snake_body.insert(0, new_head)
        if not cell_eaten:
            snake_body.pop()
        cell_eaten = False

        if not 0 <= snake_body[0][0] <= CELL_NUM - 1 or \
                not 0 <= snake_body[0][1] <= CELL_NUM - 1 or \
                snake_body[0] in snake_body[1:]:
            break

        field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), "black")

        tl, br = convert_pos_to_pixil(cell)
        field.DrawRectangle(tl, br, 'red')

        for index, part in enumerate(snake_body):
            tl, br = convert_pos_to_pixil(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(tl, br, color)

window.close()
