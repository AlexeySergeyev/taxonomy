# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
def load_max_templates(isshow=False):
    """Load the M. Mahlke et al. (2022) asteroid taxonomy templates and plot them."""
    names = ['Wavelength', 'A', 'B', 'C', 'Ch', 'D', 'E', 'K', 'L', 'M', 'O', 
         'P', 'Q', 'R', 'S', 'V', 'X', 'Z', 'E_A', 'E_B', 'E_C', 
         'E_Ch', 'E_D', 'E_E', 'E_K', 'E_L', 'E_M', 'E_O', 'E_P', 
         'E_Q', 'E_R', 'E_S', 'E_V', 'E_X', 'E_Z', 'e_A', 'e_B', 
         'e_C', 'e_Ch', 'e_D', 'e_E', 'e_K', 'e_L', 'e_M', 'e_O', 
         'e_P', 'e_Q', 'e_R', 'e_S', 'e_V', 'e_X', 'e_Z']
    df = pd.read_fwf('./data/template.dat', skiprows=0, header=None,
                     names=names)
    df = df[:-1]
    df.Wavelength = df.Wavelength.astype(float)
    df.set_index('Wavelength', inplace=True)
    
    fsize = 14
    if isshow:
        cond = df.index < 1.1
        fig, ax = plt.subplots(2, 3, figsize=(9, 6))
        fax = ax.ravel()
        loc = ['C', 'S', 'V', 'D', 'X', 'A']
        # loc = ['C', 'S', 'V', 'D', 'X', 'A', 'L', 'B']
        for i, curClass in enumerate(loc):
            fax[i].fill_between(df[cond].index,
                            df.loc[cond, curClass]+df.loc[cond, f'E_{curClass}'], 
                            df.loc[cond, curClass]+df.loc[cond, f'e_{curClass}'], 
                            color=plt.cm.tab10(i), 
                            alpha=0.3)
            fax[i].plot(df[cond].index, 
                    df.loc[cond, curClass], color=plt.cm.tab10(i), alpha=1.0, 
                    label=f'{curClass}-type template')
            fax[i].set_ylim([0.6, 1.55])
            fax[i].text(0.5, 1.3, f'{loc[i]}', fontsize=fsize+4)
         
        for i in range(0, 6):
            fax[i].set_xlabel(r'Wavelength ($\mu$m)', fontsize=fsize) 
        
        fig.text(0.008, 0.5, 'Normalized reflectance', 
                 ha='center', va='center', rotation='vertical',
                 fontsize=fsize)

        plt.tight_layout()
        plt.savefig('figs/mahlke_templates.png', dpi=150, facecolor='white')
        
        plt.show()
    
    return df

# %%
if __name__ == '__main__':
    df = load_max_templates(True)
