import pandas as pd

# Read the data from the file
data = pd.read_csv('wonders_of_world.csv')
df = pd.DataFrame(data, columns=['Latitude', 'Longitude'])
df.to_csv('wonders_cord.csv', index=False)