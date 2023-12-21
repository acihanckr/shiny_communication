from shiny import render, reactive, ui
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pathlib import Path
import re
from shiny_data import column_dict

infile = Path(__file__).parent / "NATMI/toy.bulk.em/Edges_lrc2a.csv"
df = pd.read_csv(infile)

def server(input, output, session):

    @output
    @render.data_frame
    @reactive.event(*[input._map[column_dict[k]["selection_id"]] for k in column_dict.keys()])
    def table():
        print("rendered!")
        with reactive.isolate():
            subset_cols = input.subset_by()
        return render.DataGrid(
            df,
            row_selection_mode="multiple",
            height=350,
            filters=True
        )