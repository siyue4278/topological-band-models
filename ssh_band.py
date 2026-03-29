import numpy as np
import matplotlib.pyplot as plt

#参数
t1 = 0.5
t2 = 1.0

#k空间
k_list = np.linspace(-np.pi,np.pi,400)

E1 = []
E2 = []

for k in k_list:
    #构造哈密顿量

    H = np.array([
        [0,t1 + t2*np.exp(-1j*k)],
        [t1 + t2*np.exp(1j*k),0]
    ])

    #求本征值
    E = np.linalg.eigvals(H)

    E1.append(np.real(E[0]))
    E2.append(np.real(E[1]))

#画图
plt.plot(k_list,E1)
plt.plot(k_list,E2)

plt.xlabel("k")
plt.ylabel("Energy")
plt.title("SSh Band Structure")

plt.show()