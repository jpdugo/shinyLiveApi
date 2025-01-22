from shiny import App, Inputs, Outputs, Session, reactive, render, req, ui
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
        ui.input_action_button("clear_file", "Clear File Input"),  # Add a button to clear the file input
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    excel_content = reactive.value("")

    @reactive.calc
    @reactive.event(input.file)
    def df_loaded():
        req(input.file())
        try:
            file_path = input.file()[0]["datapath"]
            df = pd.read_excel(file_path)
            excel_content.set(df)
            return df.to_csv(sep=";", index=False)
        except Exception as e:
            return f"Error processing file: {e}"

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

    @reactive.effect
    @reactive.event(input.clear_file)  # Add an event to clear the file input
    def _():
        ui.update_text_area("text_content", value="")

app = App(app_ui, server)
