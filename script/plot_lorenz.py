import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def lorenz_curve(values):
    """Return (x, y) for Lorenz curve given 1D array-like values."""
    vals = np.asarray(values, dtype=float)
    if vals.size == 0:
        return np.array([0, 1.0]), np.array([0, 1.0])
    
    # Sort values in ascending order
    vals = np.sort(vals)
    
    # Cumulative sum
    cum = np.cumsum(vals)
    total = cum[-1]
    
    if total == 0:
        # All zeros -> equality line
        x = np.linspace(0, 1, len(vals) + 1)
        y = x.copy()
        return x, y
    
    # Prepend zero and normalize
    y = np.concatenate(([0.], cum / total))
    x = np.linspace(0, 1, y.size)  # population share
    return x, y

def gini_from_lorenz(x, y):
    """Compute Gini coefficient from Lorenz curve points (x,y)."""
    # Gini = 1 - 2 * area under Lorenz curve
    area = np.trapz(y, x)
    return 1.0 - 2.0 * area

def plot_lorenz(values, title='Lorenz Curve', savepath='lorenz_curve.png'):
    """Plot Lorenz curve and calculate Gini coefficient."""
    x, y = lorenz_curve(values)
    gini = gini_from_lorenz(x, y)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot equality line
    ax.plot(x, x, color='black', linestyle='--', linewidth=2, label='Perfect Equality')
    
    # Plot Lorenz curve
    ax.plot(x, y, color='#2E86AB', linewidth=2.5, label='Lorenz Curve')
    
    # Fill area between curves
    ax.fill_between(x, y, x, where=(x >= 0), color='#A23B72', alpha=0.3, 
                     label='Inequality Area')
    
    # Labels and formatting
    ax.set_xlabel('Cumulative Share of Countries', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cumulative Share of Routes', fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.7)
    
    # Add Gini coefficient text box
    textstr = f'Gini Coefficient = {gini:.4f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8, edgecolor='black', linewidth=1.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=props, fontweight='bold')
    
    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
    
    # Save figure
    fig.tight_layout()
    fig.savefig(savepath, bbox_inches='tight', dpi=300)
    print(f'Lorenz curve saved to: {savepath}')
    print(f'Gini Coefficient: {gini:.4f}')
    
    plt.show()
    
    return fig, ax, gini

if __name__ == '__main__':
    # Load data from CSV
    df = pd.read_csv('gini_coef.csv')
    
    print(f"Loaded data for {len(df)} countries")
    print(f"Total routes: {df['Routes'].sum()}")
    print(f"Mean routes per country: {df['Routes'].mean():.2f}")
    print(f"Median routes per country: {df['Routes'].median():.2f}")
    print(f"Max routes: {df['Routes'].max()} ({df.loc[df['Routes'].idxmax(), 'Country']})")
    print(f"Min routes: {df['Routes'].min()} ({df.loc[df['Routes'].idxmin(), 'Country']})")
    print("\n" + "="*60 + "\n")
    
    # Plot Lorenz curve
    routes = df['Routes'].values
    fig, ax, gini = plot_lorenz(routes, 
                                 title='Lorenz Curve: Distribution of Routes Across Countries',
                                 savepath='lorenz_curve.png')
