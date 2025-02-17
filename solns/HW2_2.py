import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['mathtext.default'] = 'regular'

P_G = 0.85
P_B = 0.15

reliability = np.linspace(0.0, 1.0, 100, endpoint=True)
P_WB_given_B = reliability 
P_WB_given_G = 1 - P_WB_given_B

P_B_given_WB = P_WB_given_B*P_B/(P_WB_given_B*P_B + P_WB_given_G*P_G)
plt.plot(reliability, P_B_given_WB, 'k-')
plt.xticks(np.arange(0, 1.1, 0.1))
plt.title('$P(B|W_B)$ = Probability cab Blue given witness says they saw Blue')
plt.plot([0, 0.50], [0.15, 0.15], 'k-.')
plt.plot([0.50, 0.50], [0.0, 0.15], 'k--')
plt.plot([0.5, 0.5], [0.15, 0.15], 'k.')
plt.ylabel('$P(B|W_B)$')
plt.xlabel('$P(W_B|B)$ (reliability of witness)')
plt.arrow(0.5, 0.0725, 0.05, 0, head_width=0.02, head_length=0.02, fc='k', ec='k')
plt.text(0.58, 0.0725, 'Witness provides useful info.', ha='left', va='center')
plt.legend(['Witness Reliability', 'P(B) = 0.15'])
plt.grid()
plt.savefig("HW2_2b.png")
plt.savefig("HW2_2b.svg", transparent=True)