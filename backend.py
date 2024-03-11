import pandas as pd
from pandasai import SmartDatalake
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

import re

from pandasai.llm import OpenAI
pd.set_option('display.max_rows', None)
pd.__version__ 
def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url
    url = 'https://docs.google.com/spreadsheets/d/1ZsE6x5WGq5N2cQ_qiFP8p3fI3vx53vTjlju6mkLD-JU/edit#gid=1248152791'

new_url = convert_google_sheet_url(url)

df = pd.read_csv(new_url)
df = df.convert_dtypes(str)
df = df.apply(lambda x: x.astype(str).str.lower())


df.fillna('')
df.dtypes



null_counts = df.isnull().sum()