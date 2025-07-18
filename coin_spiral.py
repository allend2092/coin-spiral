from ursina import *
import math, random

# ─── Parameters ──────────────────────────────────────────────────
R_MAX         = 5
FUNNEL_HEIGHT = 3
DROP_RADIUS   = 0.20

app = Ursina(title='Coin Vortex - Wireframe Fix')

window.color = color.black
window.exit_button.visible = False

# ─── Funnel: wireframe spiral lines ─────────────────────────────
funnel = Entity()
line_count = 80
step_angle = 2 * math.pi / line_count
for i in range(line_count):
    angle = i * step_angle
    x = math.cos(angle) * R_MAX
    z = math.sin(angle) * R_MAX
    line = Entity(
        model=Mesh(
            vertices=[Vec3(x, 0, z), Vec3(0, -FUNNEL_HEIGHT, 0)],  # ⬅ fixed
            mode='line'
        ),
        color=color.gray,
        parent=funnel
    )


# ─── Lighting ───────────────────────────────────────────────────
AmbientLight(color=color.rgba(255, 255, 255, 255))

# ─── On-screen coin counter ─────────────────────────────────────
coin_count = 0
counter = Text(text='Coins: 0', origin=(-.8, .45), scale=2)

# ─── Coin entity class ──────────────────────────────────────────
class Coin(Entity):
    def __init__(self):
        super().__init__(
            model='sphere',
            scale=(0.25, 0.05, 0.25),
            color=color.yellow,
            wireframe=True
        )
        self.r        = R_MAX - 0.1
        self.theta    = random.uniform(0, math.tau)
        self.L        = (self.r ** 2) * 1.5
        self.radial_v = 0.4
        self.dropping = False
        self.drop_v   = 3.0
        self.update_position()

    def update_position(self):
        x = self.r * math.cos(self.theta)
        z = self.r * math.sin(self.theta)
        y = -FUNNEL_HEIGHT * (1 - self.r / R_MAX)
        self.position = (x, y, z)
        self.rotation = (0, -math.degrees(self.theta), 90)

    def update(self):
        dt = time.dt
        if self.dropping:
            self.y -= self.drop_v * dt
            if self.y < -FUNNEL_HEIGHT - 2:
                destroy(self)
            return

        self.r -= self.radial_v * dt
        if self.r <= DROP_RADIUS:
            self.dropping = True
            return

        omega = self.L / (self.r ** 2)
        self.theta += omega * dt
        self.update_position()

# ─── Input & spawning ───────────────────────────────────────────
def spawn_coin():
    global coin_count
    coin_count += 1
    counter.text = f'Coins: {coin_count}'
    Coin()

def input(key):
    if key == 'left mouse down':
        spawn_coin()

# ─── Camera ─────────────────────────────────────────────────────
EditorCamera(rotation_speed=80, panning_speed=10, zoom_speed=200)

# ─── Run ─────────────────────────────────────────────────────────
app.run()
