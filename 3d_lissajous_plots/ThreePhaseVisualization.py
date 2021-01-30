"""
@author: raggarwal
"""

import numpy as np
import matplotlib.pyplot as plt


f = 1           # sine frequency, Hz
w = 2*np.pi*f   # sine frequency, rad/s
T = 1/f         # period of oscillation, s
a = 1           # amplitude, V

n = 75 # number of points
tvals = np.linspace(0, 1/f, n)

# phase voltages
v_a = np.zeros_like(tvals)
v_b = np.zeros_like(tvals)
v_c = np.zeros_like(tvals)

for i in range(len(tvals)):
    t = tvals[i]
    v_a[i] = np.sin(w*t);
    v_b[i] = np.sin(w*(t-T/3))
    v_c[i] = np.sin(w*(t-2*T/3))
    
    
    
#plt.style.use('default')
#plt.style.use('science')
plt.close('all')
fig1, ax1 = plt.subplots(constrained_layout = True);
ax1.plot(tvals, v_a, label = "Phase A");
ax1.plot(tvals, v_b, label = "Phase B");
ax1.plot(tvals, v_c, label = "Phase C");
ax1.legend(loc = 'best');
ax1.set_xlabel("Time [s]");
ax1.set_ylabel("Voltage [V]");
ax1.set_title("Phase Voltages")
    

fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.scatter(v_a, v_b, v_c, label = 'all phases')
ax2.scatter(v_a, v_b, zdir='z', marker = "+", color = 'k', zs = -1, label = 'phases a and b');
ax2.scatter(v_b, v_c, zdir='x', marker = "x", color = 'k', zs = -1, label = 'phases b and c');
ax2.scatter(v_c, v_a, zdir='y', marker = "_", color = 'k', zs = -1, label = 'phases c and a');
ax2.set_xlabel("va [V]");
ax2.set_ylabel("vb [V]");
ax2.set_zlabel("vc [V]");
ax2.set_title("Phase Voltage Lissajous")
plt.legend(loc='best')


# make the panes transparent
ax2.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

alpha = .5
ax2.xaxis._axinfo["grid"]['color'] =  (0,0,0,alpha)
ax2.yaxis._axinfo["grid"]['color'] =  (0,0,0,alpha)
ax2.zaxis._axinfo["grid"]['color'] =  (0,0,0,alpha)

