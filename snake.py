import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(120)

    snake = [[sh//2, sw//4+2], [sh//2, sw//4+1], [sh//2, sw//4]]
    food = [sh//2, sw//2]
    w.addch(food[0], food[1], '🍎' if sw > 40 else '*', curses.color_pair(2))

    key = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if key == curses.KEY_DOWN: new = [snake[0][0]+1, snake[0][1]]
        elif key == curses.KEY_UP: new = [snake[0][0]-1, snake[0][1]]
        elif key == curses.KEY_LEFT: new = [snake[0][0], snake[0][1]-1]
        elif key == curses.KEY_RIGHT: new = [snake[0][0], snake[0][1]+1]
        else: new = [snake[0][0], snake[0][1]+1]

        if (new[0] in [0, sh] or new[1] in [0, sw] or new in snake):
            w.clear()
            w.addstr(sh//2-1, sw//2-8, "💀 GAME OVER 💀", curses.color_pair(2))
            w.addstr(sh//2+1, sw//2-8, f"  Final Score: {score}", curses.color_pair(3))
            w.addstr(sh//2+3, sw//2-8, "  Press any key to exit", curses.color_pair(1))
            w.refresh()
            w.timeout(-1)
            w.getch()
            break

        snake.insert(0, new)

        if snake[0] == food:
            score += 10
            food = None
            while food is None:
                nf = [random.randint(1, sh-1), random.randint(1, sw-1)]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], '*', curses.color_pair(2))
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        w.addch(snake[0][0], snake[0][1], '█', curses.color_pair(1))
        w.addstr(0, 2, f" 🐍 SNAKE | Score: {score} | Arrow keys to move ", curses.color_pair(3))
        w.refresh()

curses.wrapper(main)
