from shiny import ui

app_ui = ui.page_sidebar(ui.sidebar("Options"),
    ui.output_data_frame("table"),
    title="Shiny Communications",
    window_title="Shiny Communications"
)
