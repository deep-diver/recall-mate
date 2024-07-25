import gradio as gr
from gr_events import events
from init import css, update_position_js

css = """
.main {
    width: 90%;
    margin: auto;
}

.md_text_center {
    text-align: center;
}

.txt_no_label > label > span {
    display: none;
}

.txt_no_border > label > textarea {
    border: none;
    box-shadow: none;
}

.acc_big_font > button > span {
    font-size: 12pt;
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
    width: 100px;
    border: 1px solid;
    border-radius: 10px;
    padding: 10px;
    background: white;
    box-shadow: 0 2px 9px rgba(0, 0, 0, 0.7);
}

.category-legend {
    border-bottom: 1px dashed;
    padding-bottom: 10px;
}

.stylish-button {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    color: #ffffff;
    background: #4CAF50;
    border: none;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
}

.stylish-button:hover {
    background: #45a049;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
}

.stylish-button:active {
    background: #3e8e41;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    transform: translateY(0);
}

.textspan {
    padding-left: none;
    padding-right: none;
}
"""

with gr.Blocks(css=css) as demo:
    data = gr.State(
{
  "text": "The old bookstore, tucked away on a forgotten side street, was an oasis of calm in the relentless storm of progress. Its dusty shelves, crammed with forgotten tomes and faded paperbacks, held more stories than any digital archive could ever contain.  Mr. Finch, the proprietor, a man whose age seemed to exist outside the boundaries of time itself, sat behind a worn counter, his fingers tracing the spine of a leather-bound volume.  He looked up as a young woman, her face illuminated by the cool blue glow of a neural implant, hurried in.  “Excuse me,” she said breathlessly, her voice a touch too loud for the hushed interior, “Do you have any… well, actual books?  Not the digital downloads, the real ones.”  Mr. Finch regarded her with a gaze that seemed to penetrate the digital veil of the 22nd century.  “What exactly,” he asked, his voice a low rumble, “are you looking for?”  The young woman hesitated, as if surprised by the question, then stammered, “Something… real. Something I can touch.” The old man smiled, a slow unfolding of wisdom. “Then you’ve come to the right place.” He gestured towards the labyrinthine shelves.  “Get lost.”  The young woman, a flicker of hope in her eyes, disappeared into the stacks, leaving behind the relentless march of progress, if only for a little while.",
  "entities": [
    {
      "start": 0,
      "end": 65,
      "entity": "While evocative, this description is a bit heavy-handed. Consider subtler ways to contrast the bookstore with the outside world."
    },
    {
      "start": 132,
      "end": 170,
      "entity": "This description, while vivid, leans into cliché. Find a fresher way to describe his age and wisdom."
    },
    {
      "start": 368,
      "end": 481,
      "entity": "This exchange, while highlighting the core theme, feels a bit on-the-nose. Consider more nuanced dialogue that reveals their motivations and desires."
    },
    {
      "start": 522,
      "end": 597,
      "entity": "The ending, while hopeful, is a touch abrupt. Consider a final image or thought that lingers with the reader." 
    }
  ]
}
    )

    gr.Markdown("# Recall Mate", elem_classes=["md_text_center"])

    with gr.Column(visible=False, elem_classes=["follow-cursor"]) as info_box:
        gr.Markdown("### Evaluation", elem_classes=["md_text_center"])
        markdown = gr.Markdown("")
        gr.Button("Take Suggestion", elem_classes=["stylish-button"])

    highlighted_text = gr.HighlightedText(
        value=data.value,
        elem_id="highlight_txt", elem_classes=["height_500"],
        visible=False, interactive=False,
        show_inline_category=False, container=False
    )

    tb_write = gr.Textbox(
        value="The old bookstore, tucked away on a forgotten side street, was an oasis of calm in the relentless storm of progress. Its dusty shelves, crammed with forgotten tomes and faded paperbacks, held more stories than any digital archive could ever contain.  Mr. Finch, the proprietor, a man whose age seemed to exist outside the boundaries of time itself, sat behind a worn counter, his fingers tracing the spine of a leather-bound volume.  He looked up as a young woman, her face illuminated by the cool blue glow of a neural implant, hurried in.  “Excuse me,” she said breathlessly, her voice a touch too loud for the hushed interior, “Do you have any… well, actual books?  Not the digital downloads, the real ones.”  Mr. Finch regarded her with a gaze that seemed to penetrate the digital veil of the 22nd century.  “What exactly,” he asked, his voice a low rumble, “are you looking for?”  The young woman hesitated, as if surprised by the question, then stammered, “Something… real. Something I can touch.” The old man smiled, a slow unfolding of wisdom. “Then you’ve come to the right place.” He gestured towards the labyrinthine shelves.  “Get lost.”  The young woman, a flicker of hope in her eyes, disappeared into the stacks, leaving behind the relentless march of progress, if only for a little while.",
        elem_id="tb_write",
        elem_classes=["txt_no_label", "height_500"],
        interactive=True,
        lines=7
    )

    with gr.Row():
        btn = gr.Button("Analyze", elem_classes=["stylish-button"])
        gr.Button(elem_classes=["stylish-button"])

    with gr.Accordion("External Knowledge", open=True, elem_classes=["acc_big_font"]) as url_section:
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
        gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])

    btn.click(
        events.test_click, 
        [btn, tb_write],
        [btn, tb_write, highlighted_text, data],
    ).then(
        None, None, None,
        js=update_position_js
    )

    highlighted_text.select(
        fn=events.on_select, inputs=[highlighted_text, data, markdown], outputs=[markdown]
    )

demo.launch()