from shiny import App, ui, render, reactive
import pandas as pd
from pathlib import Path
import tempfile

app_ui = ui.page_fluid(
    ui.card(
        ui.card_header("Excel to Text Converter"),
        ui.output_text("status"),
        ui.input_file("file", "Choose Excel file", accept=[".xlsx", ".xls"]),
        ui.input_text("filename", "Enter filename:", value="output.csv"),
        ui.input_text_area("text_content", "Edit content if needed:", width="100%", height="500px"),
        ui.download_button("download", "Download as TXT"),
    )
)

def server(input, output, session):
    excel_content = reactive.value("")

    @reactive.calc
    @reactive.event(input.file)
    def df_loaded():
        if input.file() is not None:
            # Read the uploaded Excel file
            file_path = input.file()[0]["datapath"]
            df = pd.read_excel(file_path)
            excel_content.set(df)
            
            return df.to_csv(sep = ";", index = False)

    @reactive.effect
    @reactive.event(df_loaded)
    def _():
        ui.update_text_area("text_content", value=df_loaded())
    
    @render.text
    def status():
        if input.file() is None:
            return "Please upload an Excel file"
        return "File uploaded successfully!"
    
    @render.download(filename=lambda: f"{input.filename()}")
    def download():
        if input.file() is not None:
            yield input.text_content()
    
app = App(app_ui, server)
