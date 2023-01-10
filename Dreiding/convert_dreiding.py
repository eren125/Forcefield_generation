import pandas as pd

df = pd.read_csv('Dreiding.ff', sep=' ')

conv_kcalmol_K =  4.184/(8.31446261815324e-3) # C_w * (1K) / R

df['sigma_A'] = df['R_0']/2**(1/6)
df['epsilon_K'] = df['D_0']*conv_kcalmol_K
df['# atom_type'] = df['atom']+"_"
df['interaction'] = "lennard-jones"

df[['# atom_type', 'interaction', 'epsilon_K', 'sigma_A']].to_csv('Dreiding.def', index=False, sep="\t")
