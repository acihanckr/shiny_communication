from shiny import ui
from shiny_data import column_dict
import pandas as pd
from pathlib import Path
from pandas.api.types import is_numeric_dtype

infile = Path(__file__).parent / "NATMI/toy.bulk.em/Edges_lrc2a.csv"
js_file = Path(__file__).parent / "shiny_js.js"
df = pd.read_csv(infile)

accs = list()
for k in column_dict.keys():
    if is_numeric_dtype(df[k]):
        accs.append(ui.accordion_panel(k, ui.input_slider(column_dict[k]["selection_id"],"", df[k].min()-1,df[k].max()+1, df[k].max())))
    else:
        accs.append(ui.accordion_panel(k, ui.input_checkbox_group(column_dict[k]["selection_id"],"", choices=df[k].unique().tolist())))

app_ui = ui.page_sidebar(ui.sidebar("Options",
    ui.input_selectize("subset_by","Subset by",choices=df.columns.tolist(),selected=[],multiple=True),
    ui.accordion(*accs,id="subset_accs", open=True)),
    ui.head_content(ui.include_js(js_file)),
    ui.output_data_frame("table"),
    title="Shiny Communications",
    window_title="Shiny Communications"
)
