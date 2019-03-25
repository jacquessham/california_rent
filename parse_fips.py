import pandas as pd
import io

f = open('national_county.txt', 'r')
lines = f.read().split('\n')

df = []
for i in lines:
	if len(i.split(',')) == 5:
		df.append(i.split(','))
df = pd.DataFrame(df, columns=['state','statefp','countyfp','countyname','type'])
df['fips'] = df['statefp'] + df['countyfp']
df = df.drop(['state','statefp','countyfp','type'], axis=1)
df.to_csv('countyfips.csv', index=False)
