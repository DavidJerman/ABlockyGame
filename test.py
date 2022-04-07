from ursina import *


class TestCube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.white,
            textur='white_cube',
            rotation=Vec3(45, 45, 45)
        )


class TestButton(Button):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='cube',
            texture='brick',
            color=color.blue,
            highlight_color=color.red,
            pressed_color=color.yellow,
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('Button pressed!')


def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt


app = Ursina()

test_square = Entity(model='quad', color=color.red, scale=(1, 1), position=(5, 2))

sans_texture = load_texture(os.path.join('assets', 'Sans.png'))
sans = Entity(model='quad', texture=sans_texture)

test_button = TestButton()

app.run()
