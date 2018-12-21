from data_preparation import data_preparation
from results import result

# Start script
print('Run start script ...')
print('#1: Do data preparation')
data_preparation.do("daten_robinson.csv")

print('#2: Create results')
result.do("./data_preparation/data_preparation.csv")

print('End start script')
