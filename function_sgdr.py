import numpy as np
import matplotlib.pyplot as plt

learning_rate = 1e-3

def sgdr(learning_rate, epochs, iterations, T_i, T_mult):
    lr_max = learning_rate
    lr_min = learning_rate / 5
    lr_tmp = 0

    T_cur = 0

    lrs = []
    for epoch in range(epochs):
        for iteration in range(iterations):
            if(lr_tmp == lr_min):
                T_cur = 0
                if(epoch == 0): pass
                else:
                    T_i *= T_mult
            lr_tmp = lr_min + 0.5*(lr_max-lr_min)*(1+np.cos(T_cur/T_i*np.pi))
            lrs.append(lr_tmp)
            print("E:%3d, I:%4d |   T_cur:%.5f, LR:%.5f" %(epoch, iteration, T_cur/T_i, lr_tmp))
            T_cur = int(T_cur) + ((iteration+1) / iterations)
    return lrs

lrs1 = sgdr(learning_rate=1e-3, epochs=100, iterations=1000, T_i=10, T_mult=1)
lrs2 = sgdr(learning_rate=1e-3, epochs=100, iterations=1000, T_i=10, T_mult=2)
lrs3 = sgdr(learning_rate=1e-3, epochs=100, iterations=1000, T_i=20, T_mult=2)

plt.figure(figsize=(10, 3))
plt.plot(lrs1, label="T_0=10, T_mult=1", alpha=0.7)
plt.plot(lrs2, label="T_0=10, T_mult=2", alpha=0.7)
plt.plot(lrs3, label="T_0=20, T_mult=2", alpha=0.7)
plt.ylabel("Learning Rate")
plt.xlabel("Iteration (1k Iteration = 1 Epoch)")
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("sample.png")
