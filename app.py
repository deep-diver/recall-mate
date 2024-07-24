import gradio as gr

STYLES = """
.txt_no_label > label > span {
    display: none;
}

.txt_no_border > label > textarea {
    border: none;
    box-shadow: none;
}

.acc_big_font > button > span {
    font-size: 15pt;
    font-weight: bold;
}

.important {
    background-color: yellow;
}

.height_500 {
    height: 500px;
}

.height_500 > label > textarea {
    height: 480px !important;
    border: none;
    box-shadow: none;
}

#highlight_txt > label {
    display: none; 
}

.follow-cursor {
    position: fixed !important;  /* Use fixed positioning for the viewport */
    z-index: 100;      /* Ensure it's above other elements */
    /* Add any additional styling here */
}
"""


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
            return gr.Markdown(
                value=markdown_text, visible=True
            )

        if selected_label is None or selected_text.strip() == "":
            return gr.Markdown(
                value=markdown_text, visible=False
            )            
    else:  # If no entity is selected, hide the Markdown
        return gr.Markdown(visible=False)


with gr.Blocks(css=STYLES) as demo:
    with gr.Accordion("External Knowledge", open=True, elem_classes=["acc_big_font"]) as url_section:
        with gr.Column():
            with gr.Row():
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                # gr.Button("Confirm")
                # gr.Button("Remove")

            with gr.Row():
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                # gr.Button("Confirm")
                # gr.Button("Remove")

            with gr.Row():
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                # gr.Button("Confirm")
                # gr.Button("Remove")

            with gr.Row():
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                # gr.Button("Confirm")
                # gr.Button("Remove")

    highlighted_text = gr.HighlightedText(
        # value=[
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighte
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "3"),  # Unhighlighted
        #     ("This is some", "1"),  # Unhighlighted
        #     ("highlighted", "2"),  # Highlighted with label "important"
        #     ("text in Gradio", "100"),  # Unhighlighted
        # ],
        value={
            "text": "This is some sample text with entities.",  # The complete text
            "entities": [
                {
                    "entity": "Entity Type 1",  # Category or label for the entity
                    "start": 5,                  # Start character index of the entity in the text
                    "end": 10,                   # End character index of the entity (exclusive)
                },
                {
                    "entity": "Entity Type 2",
                    "start": 21,
                    "end": 28,
                },
                # ... more entities ...
            ],
        },
        elem_id="highlight_txt",
        elem_classes=["height_500"],
        visible=False,
        interactive=False
    )

    tb_write = gr.Textbox(
        elem_id="tb_write",
        elem_classes=["txt_no_label", "height_500"],
        interactive=True
    )

    with gr.Row():
        btn = gr.Button("Analyze")
        gr.Button()

    btn.click(
        test_click,
        btn,
        [btn, tb_write, highlighted_text],
    ).then(
        None, None, None,
        js="""
function updatePosition() {
    const markdownElem = document.querySelector('.follow-cursor');

    document.addEventListener('mousemove', (event) => {
        let mouseX = event.clientX;
        let mouseY = event.clientY;

        console.log(mouseX);
        console.log(mouseY);

        if (markdownElem) {
            markdownElem.style.top = (mouseY + 10) + 'px'; // Adjust for offset
            markdownElem.style.left = (mouseX + 10) + 'px'; // Adjust for offset
        }
    });
}
"""
    )

    output_text = gr.Textbox(label="Selected Entity Info")
    markdown = gr.Markdown(
        "", visible=False, elem_classes=["follow-cursor"]
    ) 

    highlighted_text.select(
        fn=on_select, inputs=highlighted_text, outputs=[markdown]
    )


    # text_input.change(
    #     lambda x: [
    #         ("This is some", "1"),  # Unhighlighted
    #         ("highlighted", "2"),  # Highlighted with label "important"
    #         ("text in Gradio", "3"),  # Unhighlighted            
    #     ],
    #     inputs=text_input,
    #     outputs=highlighted_text,
    # )    

demo.launch()
