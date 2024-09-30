from idlelib.pyshell import extended_linecache_checkcache

from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('Dark Rash.png')

def draw_idle_character():
    global frame1

    if frame1 == 0:
        character.clip_draw(5, 370, 60, 52, x, y)
    elif frame1 == 1:
        character.clip_draw(82, 370, 69, 59, x, y + 3)
    elif frame1 == 2:
        character.clip_draw(168, 370, 81, 68, x, y + 8)
    elif frame1 == 3:
        character.clip_draw(268, 370, 86, 74, x, y + 11)
    elif frame1 == 4:
        character.clip_draw(376, 370, 86, 77, x, y + 12)
    elif frame1 == 5:
        character.clip_draw(376, 370, 86, 77, x, y + 12)
    elif frame1 == 6:
        character.clip_draw(488, 370, 86, 78, x, y + 13)
    elif frame1 == 7:
        character.clip_draw(488, 370, 86, 78, x, y + 13)
    elif frame1 == 8:
        character.clip_draw(596, 370, 81, 64, x, y + 7)
    elif frame1 == 9:
        character.clip_draw(596, 370, 81, 64, x, y + 7)
    elif frame1 == 10:
        character.clip_draw(596, 370, 81, 64, x, y + 7)
    elif frame1 == 11:
        character.clip_draw(699, 370, 80, 64, x, y + 4)
    elif frame1 == 12:
        character.clip_draw(699, 370, 80, 64, x, y + 4)
    elif frame1 == 13:
        character.clip_draw(796, 370, 74, 58, x, y)
    elif frame1 == 14:
        character.clip_draw(893, 370, 60, 52, x, y)

def draw_running_left_character():
    global frame2

    character.clip_draw(frame2*74, 642, 72, 65, x, y + 6)

def draw_running_right_character():
    global frame2

    character.clip_composite_draw(frame2 * 74, 642, 72, 65, 0, 'h', x, y + 6, 72, 65)

def handle_events():
    global running
    global frame1
    global dirx
    global diry
    global flip

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                flip = 1
                dirx += 1
            elif event.key == SDLK_LEFT:
                flip = 0
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                flip = 0
                dirx -= 1
                frame1 = 0
            elif event.key == SDLK_LEFT:
                flip = 1
                dirx += 1
                frame1 = 0
            elif event.key == SDLK_UP:
                diry -= 1
                frame1 = 0
            elif event.key == SDLK_DOWN:
                diry += 1
                frame1 = 0

running = True
x = 800 // 2
y = 30
frame1 = 0
frame2 = 0
dirx = 0
diry = 0
flip = 0

while running:
    clear_canvas()
    background.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    if dirx == 0 and diry == 0:
        draw_idle_character()
    else:
        if flip == 1:
            draw_running_right_character()
        elif flip == 0:
            draw_running_left_character()
    update_canvas()
    handle_events()
    frame1 += 1
    frame2 += 1
    if frame1 == 15:
        frame1 = 0
    if frame2 == 6:
        frame2 = 0
    x += dirx * 10
    y += diry * 10
    if x > 750:
        x = 750
    if x < 50:
        x = 50
    if y > 550:
        y = 550
    if y < 30:
        y = 30
    delay(0.05)

close_canvas()