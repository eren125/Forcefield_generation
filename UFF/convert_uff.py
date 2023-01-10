import pandas as pd

df = pd.read_csv('UFF.ff', sep=' ')

conv_kcalmol_K =  4.184/(8.31446261815324e-3) # C_w * (1K) / R

df['sigma_A'] = df['x1']/2**(1/6)
df['epsilon_K'] = df['D1']*conv_kcalmol_K
df['# atom_type'] = df['Atom']+"_"
df['interaction'] = "lennard-jones"

df[['# atom_type', 'interaction', 'epsilon_K', 'sigma_A']].to_csv('UFF_short.def', index=False, sep="\t")
