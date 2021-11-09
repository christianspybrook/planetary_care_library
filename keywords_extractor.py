from pyzotero import zotero
import json
import pandas as pd
from io import StringIO

# retrieve my Zotero key
local_file = 'api_keys/zotero_api_key.txt'
with open(local_file, 'r') as api_file:
	my_key = api_file.read().rstrip('\r\n')
	api_file.close()


# instantiate Zotero object
zot = zotero.Zotero(library_id=2550849, library_type='group', 
					api_key=my_key, preserve_json_order=True)

# extract citation metadata
data = zot.everything(zot.items())
# data = zot.all_collections()

# stringify metadata list
json_str = json.dumps(data)

# make JSON object file-like and convert to DataFrame
df = pd.read_json(StringIO(json_str))

# extract 'data' column from DataFrame
data_df = pd.DataFrame(list(df['data']))

# create Series of dicts of citation tags
tag_series = data_df['tags'].explode().dropna()

# create unique list of citation tags
keywords_lst = list(set([d['tag'] for d in tag_series.values]))

# write keyword list to text file
with open('data/keywords.txt', 'w') as file:
	for word in keywords_lst:
		file.write(word + '\n')




if __name__ == '__main__':

	print('Keywords...')
	print(keywords_lst)
	print(f'{data_df.shape[0]} citations used')
	print(f'{len(keywords_lst)} unique tags found')
