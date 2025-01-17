# --------------------------------------------------------------------------------------------------------
# Script for reading data for Problem 5.1 in Applied Statistics 2024-25 Problem Set:
# --------------------------------------------------------------------------------------------------------
#
# The data file contains a header and 120000 entries in five columns:
#  * Entry number (i.e. index)
#  * Phase (P)
#  * Resonance (R)
#  * Frequency (nu)
#  * Entry type (1: Signal in Control Sample, 0: Background in Control Sample, -1: Real data sample)
#
#   Author: Troels Petersen (Niels Bohr Institute, petersen@nbi.dk)
#   Date:   7th of November 2024 (latest version)
#
# --------------------------------------------------------------------------------------------------------

import numpy as np

data = np.genfromtxt('data_SignalDetection.csv', delimiter = ',', skip_header=1)
print("  Shape of data: ", data.shape)

index = data[:,0].astype(int)
P     = data[:,1]
R     = data[:,2]
freq  = data[:,3]
type  = data[:,4].astype(int)

print(index[0:3])
print(P[0:3])
print(R[0:3])
print(freq[0:3])
print(type[0:3])
