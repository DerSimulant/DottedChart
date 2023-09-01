import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV-Datei einlesen und Zeitformat korrigieren

#df_csv = pd.read_csv('EventlogRepair.csv', usecols=['time:timestamp', 'case:concept:name', 'concept:name'], encoding="ISO-8859-1", delimiter=';')
df_csv = pd.read_csv('updated_aristest.csv', usecols=['time:timestamp', 'case:concept:name', 'concept:name'], encoding="ISO-8859-1", delimiter=',')
df_csv['time:timestamp'] = pd.to_datetime(df_csv['time:timestamp'])

# Ein Dictionary erstellen, um jedem Ereignis eine Farbe zuzuordnen
unique_events_csv = df_csv['concept:name'].unique()
colors_csv = plt.cm.jet(np.linspace(0, 1, len(unique_events_csv)))
event_color_map_csv = dict(zip(unique_events_csv, colors_csv))

# Frühesten Zeitpunkt für jeden Fall bestimmen und sortieren
df_case_start_times = df_csv.groupby('case:concept:name')['time:timestamp'].min().sort_values()
df_csv['case_order'] = df_csv['case:concept:name'].map(df_case_start_times.reset_index().reset_index().set_index('case:concept:name')['index'])

# Daten für das Scatter-Plot vorbereiten
timestamps = df_csv['time:timestamp']
cases_order = df_csv['case_order']
colors = df_csv['concept:name'].map(event_color_map_csv)

# Diagramm erstellen
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(timestamps, cases_order, c=colors, s=10)

# Legende anzeigen
unique_labels_csv = {k: plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=v, markersize=10) for k, v in event_color_map_csv.items()}
ax.legend(unique_labels_csv.values(), unique_labels_csv.keys(), loc="upper left", bbox_to_anchor=(1,1), ncol=1)

ax.set_xlabel('Zeit')
ax.set_ylabel('Cases')
ax.set_title('Dotted Chart')
ax.invert_yaxis()  # Die y-Achse invertieren, um den frühesten Fall oben zu haben

# Die Ticks der Y-Achse anpassen, um den Case-Namen anzuzeigen
ax.set_yticks(df_case_start_times.reset_index().reset_index()['index'])
ax.set_yticklabels(df_case_start_times.index)

# Optional: Zeitraum der X-Achse anpassen
start_date = pd.Timestamp('2023-05-12')  # Setzen Sie das gewünschte Startdatum
end_date = pd.Timestamp('2023-08-30')    # Setzen Sie das gewünschte Enddatum
#für EventlogRepair
#start_date = pd.Timestamp('2020-09-12')  # Setzen Sie das gewünschte Startdatum
#end_date = pd.Timestamp('2021-11-30')    # Setzen Sie das gewünschte Enddatum
ax.set_xlim([start_date, end_date])

# Fenstertitel setzen
fig.canvas.set_window_title('Dotted Chart')

plt.tight_layout()
plt.show()
