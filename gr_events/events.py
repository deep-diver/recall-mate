import gradio as gr

def test_click(title):
    if title == "Analyze":
        return [
            gr.Button("Back to writing"),
            gr.Textbox(visible=False), 
            gr.Highlightedtext(visible=True)
        ]
    else:
        return [
            gr.Button("Analyze"),
            gr.Textbox(visible=True), 
            gr.Highlightedtext(visible=False)
        ]

def on_select(value, evt: gr.SelectData):  # Event handler function
    if evt is not None:
        selected_text = evt.value[0]  # Get the label of the selected entity
        selected_label = evt.value[1]
        markdown_text = f"**Selected Entity:** {selected_text}"  # Create Markdown content

        if selected_label is not None:
            return gr.Markdown(value=markdown_text)
        if selected_label is None or selected_text.strip() == "":
            return gr.Markdown(value=markdown_text)
    else:  # If no entity is selected, hide the Markdown
        return gr.Markdown(value=markdown_text)