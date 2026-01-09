import sys
import pandas as pd

print('arguments', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']})
df['month'] = month

print(df.head())
df.to_parquet(f'output_month_{month}.parquet')

print(f"hello pipeline, month={month}")

