import gradio as gr
from gr_events import events
from init import css, update_position_js

with gr.Blocks(css=css) as demo:
    with gr.Column(visible=False, elem_classes=["follow-cursor"]) as info_box:
        markdown = gr.Markdown("")
        gr.Button("hello")

    with gr.Accordion("External Knowledge", open=True, elem_classes=["acc_big_font"]) as url_section:
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])

    highlighted_text = gr.HighlightedText(
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
        elem_id="highlight_txt", elem_classes=["height_500"],
        visible=False, interactive=False,
        show_legend=True, show_inline_category=False, container=False
    )

    tb_write = gr.Textbox(
        elem_id="tb_write",
        elem_classes=["txt_no_label", "height_500"],
        interactive=True,
        lines=7
    )

    with gr.Row():
        btn = gr.Button("Analyze")
        gr.Button()

    btn.click(
        events.test_click,
        btn,
        [btn, tb_write, highlighted_text],
    ).then(
        None, None, None,
        js=update_position_js
    )

    # output_text = gr.Textbox(label="Selected Entity Info")

    highlighted_text.select(
        fn=events.on_select, inputs=highlighted_text, outputs=[markdown]
    )

demo.launch()