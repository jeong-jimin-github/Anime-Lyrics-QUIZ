import pandas as pd

def write_df_to_local(df, file_path):
    df.to_csv(file_path, index=False)
sheet_url = 'https://docs.google.com/spreadsheets/d/1O0qIhEPa2TJNwaU5MVk9NjwH7FOx8wrqouf_KA5AMgY/export?format=csv'
df = pd.read_csv(sheet_url)
file_path = 'data.csv'
write_df_to_local(df, file_path)
