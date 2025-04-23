import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

url = "https://raw.githubusercontent.com/lukakukhaleishvili/midtearm-machine-Learning-/main/luka_kukhaleishvili_1_73182468.csv"
df = pd.read_csv(url)

numeric_cols = df.select_dtypes(include='number').columns
x_col = numeric_cols[0]
y_col = numeric_cols[1]

corr_coef, p_value = pearsonr(df[x_col], df[y_col])
print(f"პირსონის კორელაცია ({x_col} და {y_col}): {corr_coef:.3f}, p-value: {p_value:.3f}")

plt.figure(figsize=(8, 6))
sns.scatterplot(x=df[x_col], y=df[y_col], color='skyblue')
plt.title(f'კორელაცია: {x_col} vs {y_col} (r = {corr_coef:.2f})')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.grid(True)
plt.tight_layout()
plt.savefig("correlation_plot.png")
plt.show()
