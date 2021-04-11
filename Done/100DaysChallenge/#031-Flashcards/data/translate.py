# Data taken from:
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018

import pandas as pd
from google_trans_new import google_translator

translator = google_translator()

data = pd.read_csv('./jpwords.csv')
df = data['words'].str.split(expand=True)
df.columns = ['Japanese', 'amount']
df['amount'] = df['amount'].astype(int)
df = df[df.amount >= 500]
translated_words = [translator.translate(text=x, lang_tgt='en',
                                         lang_src='ja').capitalize()
                    for x in df['Japanese'].values]
df['English'] = translated_words
del df['amount']
df.to_json(path_or_buf='words.json', orient='index')
