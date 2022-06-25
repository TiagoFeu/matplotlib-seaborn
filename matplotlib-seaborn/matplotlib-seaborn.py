import pandas as pd
import datetime as date
import matplotlib.pyplot as plt
import seaborn as sns

covid_panel = pd.read_csv("../data/microdados.csv", encoding="ISO-8859-1", on_bad_lines="skip", sep=";", parse_dates=["DataDiagnostico","DataObito"])

# ----------------------------------------------------------------------------------------------------------------------
# Evolution of cases
confirmed = covid_panel[covid_panel['Classificacao'] == 'Confirmados']
confirmed_by_day = confirmed.groupby(['DataDiagnostico']).size()
confirmed_sum = confirmed_by_day.cumsum()

# Evolution of deaths
dead = covid_panel[covid_panel['Evolucao'] == 'Óbito pelo COVID-19']
dead_by_day = dead.groupby(['DataObito']).size()
dead_sum = dead_by_day.cumsum()

# creates plot
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
ax0 = sns.lineplot(x=confirmed_sum.index, y=confirmed_sum, color='red', ax=axes[0])
ax0.set(title = 'Evolution of confirmed cases', xlabel='Date', ylabel='Number of cases')
ax1 = sns.lineplot(x=dead_sum.index, y=dead_sum, color='blue', ax=axes[1])
ax1.set(title = 'Evolution of deaths', xlabel='Date', ylabel='Number of deaths')
fig.savefig("../results/confirmed_sum.png")

# ----------------------------------------------------------------------------------------------------------------------
