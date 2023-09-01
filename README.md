# DottedChart from CSV eventlog
Create a dotted chart with Python for Process Mining data analysis

After creating a virtual environment you can install all dependencies by using
pip install -r requirements.txt

File "dottedChart.py" creates an overview sorted by start.
File "dottedChartWS.py" creates a dotted chart and sorts just for teh case ID.

Make sure the colums in the CSV are named correctly:

"case:concept:name" for CaseID	
"concept:name" for Activity
"time:timestamp" for timestamp

Make sure encoding and delimiter fits your CSV. You can change it in teh following line:
df_csv = pd.read_csv('updated_aristest.csv', usecols=['time:timestamp', 'case:concept:name', 'concept:name'], encoding="ISO-8859-1", delimiter=',')
