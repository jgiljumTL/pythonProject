import skrf as rf
from pylab import *

from skrf import Network, Frequency

ring_slot = Network('RX25AF_U01283_VNA_N_BWL=0,00_BWH=0,00_GC=1,50_00.s2p')

print(ring_slot)

ring_slot.s21.plot_s_db(m=0,n=0, label='U01283')


plt.show()