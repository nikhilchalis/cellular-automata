import cellpylib as cpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class CustomRule(cpl.BaseRule):

    def __call__(self, n, c, t):
        # if currently dead
        if n[1][1] == 0:
            if np.sum(n) == 3:
                return 1
            else:
                return 0
        
        # if currently alive
        else:
            if np.sum(n)-1 == 1 or np.sum(n)-1 == 3 or np.sum(n)-1 == 4:
                return 1
            else:
                return 0


rule = CustomRule()

cellular_automaton = cpl.init_simple2d(rows=60, cols=60)
cellular_automaton[:, 20:30, 25] = 1
cellular_automaton[:, 20:25, 26] = 1
cellular_automaton[:, 25:30, 27] = 1
cellular_automaton[:, 20:30, 28] = 1
cellular_automaton[:, 20:30, 30] = 1
cellular_automaton[:, 32, 25:30] = 1

FRAMES = 500
cellular_automaton = cpl.evolve2d(cellular_automaton, timesteps=FRAMES, neighbourhood='Moore', apply_rule=rule, memoize='recursive')

fig, ax = plt.subplots()
ax.set_xlim((0, 60))
ax.set_ylim((60, 0))

img = ax.imshow(cellular_automaton[0], interpolation='nearest', cmap='gray')

def init():
    img.set_data(cellular_automaton[0])
    return (img,)

def animate(i):
    img.set_data(cellular_automaton[i])
    return (img,)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=FRAMES, interval=50, blit=True, repeat=False)

plt.show()
