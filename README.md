# Two-Body-Gravitational-Simulator

A Python numerical simulation of gravitational attraction between two bodies, using the **Euler integration method** to compute position, velocity, and acceleration of a moving body under the gravitational influence of a fixed body.

## 📌 What the program does

Based on user-provided inputs (mass of the fixed body, initial distance between the bodies, initial velocity, and time resolution), the program simulates the trajectory of the moving body step by step, applying classic physics equations:

- **Newton's Law of Universal Gravitation**
  `a = G * m / d²`

- **Position equation (uniformly accelerated motion)**
  `S = S0 + V0*T + (A*T²)/2`

- **Velocity equation (uniformly accelerated motion)**
  `V = V0 + A*T`

At each time step, the program recalculates the distance between the bodies, the resulting gravitational acceleration, the new position, and the new velocity, simulating how gravity changes dynamically as the bodies move closer or farther apart.

## ⚙️ Features

- Input values in scientific notation (mantissa + exponent)
- Step-by-step simulation with results printed to the terminal
- Export of data (position, velocity, and acceleration) to `.txt` files
- Graph generation using `matplotlib` to visualize:
  - Position over time
  - Velocity over time
  - Acceleration over time
- Input validation (prevents crashes from invalid or negative values)
- Protection against division by zero (collision between bodies)
- Protection against infinite loops (maximum iteration limit)
- Ability to run multiple simulations with new parameters without restarting the program

## 🧠 Concepts applied

- Physics: universal gravitation, kinematics (uniformly accelerated motion)
- Numerical methods: Euler integration for dynamic systems
- Programming: function-based structure, input validation, file handling, data visualization

## ▶️ How to run

### Requirements
```bash
pip install matplotlib
```

### Running
```bash
python simulador_gravitacional.py
```

The program will ask, in sequence, for:
1. Mass of the fixed body (in Kg, with scientific notation exponent)
2. Initial distance between the bodies (with exponent)
3. Desired final displacement of the simulation (with exponent)
4. Initial velocity of the moving body (m/s)
5. Time resolution (number of simulated instants per second)

At the end, you can export the data and view the generated graphs.

## 📊 Example use case

Simulate an object falling toward a planet, observing how gravitational acceleration increases as distance decreases — visualized through the automatically generated position, velocity, and acceleration graphs.

## ⚠️ Known limitations

- The model only considers one-dimensional motion (a straight line between the two bodies)
- Simulation accuracy depends directly on the chosen time resolution (larger time steps reduce physical precision)
- The reference body (m2) is treated as fixed; the full two-body problem (both bodies moving under mutual attraction) is not simulated

Project developed as an exercise in computational physics and Python programming.
