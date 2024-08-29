import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.lineplot(x='dia', y='venda', data=df, marker='o')

plt.title('Preço da Gasolina por Dia')
plt.xlabel('Dia')
plt.ylabel('Preço')

plt.savefig('gasolina.png')

plt.show()