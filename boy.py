from pico2d import *
from transitions import Machine
import math
import time


IDLE = 'IDLE'
SLEEP = 'SLEEP'
RUN = 'RUN'
AUTO_RUN = 'AUTO_RUN'


class AutoRun:
    SPEED = 6
    DRAW_SIZE = 150

    def __init__(self, boy):
        self.boy = boy

    @property
    def is_invincible(self):
        return True

    def update(self):
        boy = self.boy
        boy.min_x = self.DRAW_SIZE // 2
        boy.max_x = 800 - self.DRAW_SIZE // 2
        boy.x += boy.face_dir * self.SPEED
        if boy.x <= boy.min_x or boy.x >= boy.max_x:
            boy.x = max(boy.min_x, min(boy.max_x, boy.x))
            boy.face_dir *= -1
        boy.frame = (boy.frame + 1) % 8


class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.speed = 3
        self.min_x, self.max_x = 50, 750
        self.pressed_directions = set()
        self.idle_started_at = time.monotonic()
        self.auto_run_state = None
        self.image = load_image('animation_sheet.png')
        self.state_machine = Machine(
            model=self,
            states=[IDLE, RUN, SLEEP, AUTO_RUN],
            initial=IDLE,
            transitions=[
                {'trigger': 'sleep', 'source': IDLE, 'dest': SLEEP},
                {'trigger': 'run', 'source': IDLE, 'dest': RUN},
                {'trigger': 'run', 'source': SLEEP, 'dest': RUN},
                {
                    'trigger': 'auto_run',
                    'source': IDLE,
                    'dest': AUTO_RUN,
                    'after': 'enter_auto_run',
                },
                {
                    'trigger': 'stop_run',
                    'source': RUN,
                    'dest': IDLE,
                    'after': 'restart_idle_timer',
                },
                {
                    'trigger': 'wake',
                    'source': SLEEP,
                    'dest': IDLE,
                    'after': 'restart_idle_timer',
                },
            ],
        )

    @property
    def is_invincible(self):
        return self.auto_run_state is not None and self.auto_run_state.is_invincible

    def update(self):
        if self.state == IDLE:
            if time.monotonic() - self.idle_started_at >= 5.0:
                self.sleep()
            self.frame = (self.frame + 1) % 8
        elif self.state == RUN:
            self.x = max(
                self.min_x,
                min(self.max_x, self.x + self.face_dir * self.speed),
            )
            self.frame = (self.frame + 1) % 8
        elif self.state == AUTO_RUN:
            self.auto_run_state.update()

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and self.state == SLEEP:
                self.wake()
            elif event.key == SDLK_a and self.state == IDLE:
                self.auto_run()
            elif event.key in (SDLK_LEFT, SDLK_RIGHT):
                if self.state == AUTO_RUN:
                    return
                self.pressed_directions.add(event.key)
                self.face_dir = -1 if event.key == SDLK_LEFT else 1
                if self.state in (IDLE, SLEEP):
                    self.run()
        elif event.type == SDL_KEYUP:
            if event.key in (SDLK_LEFT, SDLK_RIGHT):
                self.pressed_directions.discard(event.key)
                if self.pressed_directions:
                    direction = (
                        SDLK_LEFT
                        if SDLK_LEFT in self.pressed_directions
                        else SDLK_RIGHT
                    )
                    self.face_dir = -1 if direction == SDLK_LEFT else 1
                elif self.state == RUN:
                    self.stop_run()

    def restart_idle_timer(self):
        self.idle_started_at = time.monotonic()
        self.frame = 0

    def enter_auto_run(self):
        self.auto_run_state = AutoRun(self)

    def draw(self):
        if self.state == SLEEP:
            row_y = 300 if self.face_dir == 1 else 200
            self.image.clip_composite_draw(
                0, row_y, 100, 100, self.face_dir * math.pi / 2, '',
                self.x, self.y - 20, 100, 100
            )
        else:
            row_y = (
                100 if self.state in (RUN, AUTO_RUN) and self.face_dir == 1
                else 0 if self.state in (RUN, AUTO_RUN)
                else 300 if self.face_dir == 1
                else 200
            )
            draw_size = (
                AutoRun.DRAW_SIZE
                if self.state == AUTO_RUN
                else 100
            )
            self.image.clip_draw(
                self.frame * 100, row_y, 100, 100,
                self.x, self.y, draw_size, draw_size
            )