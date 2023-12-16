from shiny import render
import pandas as pd
from pathlib import Path

def server(input, output, session):
    @output
    @render.data_frame
    def table():
        infile = Path(__file__).parent / "NATMI/toy.bulk.em/Edges_lrc2a.csv"
        return render.DataGrid(
            pd.read_csv(infile),
            row_selection_mode="multiple",
            height=350,
            filters=True
        )