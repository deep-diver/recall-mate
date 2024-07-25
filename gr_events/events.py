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

def on_select(value, data, evt: gr.SelectData):  # Event handler function
    print(data)

    selected_text = evt.value[0]  # Get the label of the selected entity
    selected_label = evt.value[1]

    print(evt.value)
    print(evt.index)

    eval = ""
    for entity in data["entities"]:
        start = entity["start"]
        end = entity["end"]

        if entity["entity"] == selected_label and \
            data["text"][start:end] == selected_text:
            eval = entity["entity"]

    return gr.Markdown(value=eval)