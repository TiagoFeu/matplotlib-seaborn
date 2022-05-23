import pandas as pd
import datetime as date
import matplotlib.pyplot as plt
import seaborn as sns

covid_panel = pd.read_csv("../data/microdados.csv", encoding="ISO-8859-1", on_bad_lines="skip", sep=";", parse_dates=["DataDiagnostico","DataObito"])

# Evolution of cases
confirmed = covid_panel[covid_panel['Classificacao'] == 'Confirmados']
confirmed_by_day = confirmed.groupby(['DataDiagnostico']).size()
confirmed_sum = confirmed_by_day.cumsum()

# Evolution of deaths
dead = covid_panel[covid_panel['Evolucao'] == 'Óbito pelo COVID-19']
dead_by_day = dead.groupby(['DataObito']).size()
dead_sum = dead_by_day.cumsum()

plot = sns.lineplot(x=confirmed_sum.index, y=confirmed_sum, color='red')
plot = sns.lineplot(x=dead_sum.index, y=dead_sum, color='blue')
fig = plot.get_figure()
fig.savefig("../results/confirmed_sum.png")

