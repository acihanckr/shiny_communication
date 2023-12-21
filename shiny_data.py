import pandas as pd
from pathlib import Path
from pandas.api.types import is_numeric_dtype
import re

infile = Path(__file__).parent / "NATMI/toy.bulk.em/Edges_lrc2a.csv"
df = pd.read_csv(infile)

column_dict = {k:{"active":False} for k in df.columns.tolist()}

for k in column_dict.keys():
    id_str = re.sub(r'\W+',"",k)
    if is_numeric_dtype(df[k]):
        column_dict[k]["typ"] = "cont"
        column_dict[k]["limits"] = [df[k].min(), df[k].max()]
        column_dict[k]["selection_id"] = id_str+"_slider"
    else:
        column_dict[k]["typ"] = "fact"
        column_dict[k]["levels"] = df[k].unique().tolist()
        column_dict[k]["selection_id"] = id_str+"_checkbox"
if __name__ == "__main__":
    print(column_dict)