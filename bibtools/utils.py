import pandas as pd
from itertools import islice

def entries_to_csv(entries, filename):
    "Saves an iterable of pybtex.database.Entry to a csv"
    entries_to_df(entries).to_csv(filename)

def entries_to_df(entries):
    "Converts an iterable of pybtex.database.Entry to a pandas.DataFrame"
    df = pd.DataFrame.from_dict(entry_to_dict(e) for e in entries)
    df = df.assign(url=df.apply(lambda row: row['url'] or row['URL'], axis=1))
    df = df.drop(columns=['URL']) # Merging column URL into url
    return df

def persons_to_dict(persons, n=3, formatter=None):
    "Formats the first n of pybtex.database.Person as a dict, optionally using formatter"
    formatter = formatter or str
    return {"author{}".format(i): formatter(p) for i, p in enumerate(islice(persons, 0, n))}

def entry_to_dict(entry):
    "Converts a pybtex.database.Entry to a {str:str} dict"
    d = entry.fields
    d.update(persons_to_dict(entry.persons.get('author', [])))
    return {str(k) : str(v) for k, v in d.items()}
