# Coin Vortex (Wireframe Edition)

This project is a 3D physics-inspired simulation built using [Ursina](https://www.ursinaengine.org/), a Python game engine. It recreates the classic **coin vortex** or **donation funnel** — the kind seen in museums where coins spiral around a funnel and drop into the center.

This version is **minimal**, **wireframe-only**, and fully procedural — no external models are used.

---

## 🌀 How It Works

- Left-click to spawn a **coin**.
- Each coin spawns near the edge of the funnel and:
  - Orbits the funnel using **conservation of angular momentum**
  - Spirals inward over time
  - Drops straight down when it reaches the center
- The **funnel** is visualized using radial **wireframe lines** converging to the center
- A floating counter keeps track of the total coins spawned.

---

## 📁 File Overview

```
vortex_2.py       # Main simulation script
README.md         # You're reading it!
```

---

## 🧠 Key Concepts Demonstrated

- **3D wireframe rendering** in Ursina
- Procedural geometry using Ursina's `Mesh`
- Simulated physics using polar coordinates:
  - Radial inward motion (`r` decreases)
  - Angular velocity computed from angular momentum (`ω = L / r²`)
- Dynamic `Entity` creation and destruction
- Basic UI and state tracking
- Visual simulation without external assets

---

## 🧰 Requirements

- Python 3.8–3.12
- [Ursina Engine](https://pypi.org/project/ursina/)

Install with:

```bash
pip install ursina
```

---

## ▶️ Running the Simulation

```bash
python vortex_2.py
```

Left-click in the window to spawn coins.

Use your mouse to:
- **Orbit** around the scene (`right-click + drag`)
- **Zoom** with the scroll wheel
- **Pan** with middle-click drag

---

## 📸 Screenshot

*(Optional: place an image file named `screenshot.png` in the repo root to show here.)*

```markdown
![Screenshot](./screenshot.png)
```

---

## 🛠️ Future Improvements

- Add sound effects for coin drop
- Use realistic coin models via .obj
- Add floor plane or textured base
- Animate funnel spirals or distortions
- Add time-based stats (e.g. coins/sec)

---

## 👤 Author

Built by Daryl Allen as a lightweight simulation and Ursina learning project.
