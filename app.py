import gradio as gr
from gr_events import events
from init import css, update_position_js, gen_configs

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

.stylish-button:hover, {
    background: #45a049;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
}

.stylish-button:active {
    background: #3e8e41;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    transform: translateY(0);
}

.stylish-button2 {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    color: #ffffff;
    background: #A8E6CF;
    border: none;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
}

.stylish-button2:hover, {
    background: #45a049;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
}

.stylish-button2:active {
    background: #2E8B57;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    transform: translateY(0);
}

.narrow-stylish-botton {
    padding: 4px 10px;
    margin-bottom: 5px;
}

.textspan {
    padding-left: none;
    padding-right: none;
}

.md_vertical_margin {
    margin-top: 5px;
    margin-bottom: 10px;
}

.acc_nogap > div > div {
    gap: unset;
}

.btn_no_width {
    min-width: 0px;
}

.row_nogap {
    gap: 5px;
}

.acc_only_bottom_shadow {
    border: none !important;
    box-shadow: 0px 5px 4px 0px rgba(0, 0, 0, 0.1);
}

.hidden_chat {
    opacity: 0;
    transition: opacity 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    top: 0;
    right: 0;
    width: 50%;
    height: 100%;
    background-color: white;
    z-index: -1; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 20px;
    box-shadow: rgba(0, 0, 0, 0.1) -20px 0px 20px 20px;
}

.hidden_chat_container {
    opacity: 0;
    transition: opacity 0.5s ease-in-out; /* Smooth transition */

    position: fixed;  /* Ensures it's always on top */
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.3);
    z-index: -2; /* A very high value to ensure it's on top */
}

.hidden_chat.show {
    opacity: 1;
    z-index: 9999;
}

.hidden_chat_container.show {
    opacity: 1;
    z-index: 9998;
}

.hidden_config {
    opacity: 0;
    transition: opacity 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    top: 0;
    right: 0;
    width: 50%;
    height: 100%;
    background-color: white;
    z-index: -1; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 20px;
    box-shadow: rgba(0, 0, 0, 0.1) -20px 0px 20px 20px;
}

.hidden_config.show {
    opacity: 1;
    z-index: 9999;
}

.hidden_config_container {
    opacity: 0;
    transition: opacity 0.5s ease-in-out; /* Smooth transition */

    position: fixed;  /* Ensures it's always on top */
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.3);
    z-index: -2; /* A very high value to ensure it's on top */
}

.hidden_config_container.show {
    opacity: 1;
    z-index: 9998;
}

.modal_back_btn {
    font-size: 20pt;
    background: transparent;
    box-shadow: none;
    border: none;
    width: max-content;
    border-radius: 20px;
}

.modal_back_btn:active {
    background: gray;
}

.modal_trigger {
    position: fixed;      /* Position it relative to the viewport */
    padding: 0px;
    top: 50%;            /* Center it vertically */
    right: 10px;         /* Position on the right with some margin */
    transform: translateY(-50%); /* Adjust for vertical centering */
    width: 10px;          /* Adjust width as needed */
    height: 80px;         /* Adjust height as needed */
    background-color: blue; /* Choose your button color */
    cursor: pointer;     /* Indicate it's clickable */
    border-radius: 10px;    /* Add rounded corners */
    z-index: 1000;        /* Ensure it's above other content */
    border: none;
}

.padding_20px {
    padding: 20px;
}
"""

with gr.Blocks(css=css) as demo:
    data = gr.State()

    gr.Markdown("# Recall Mate", elem_classes=["md_text_center"])

    test_btn = gr.Button("", elem_classes=["modal_trigger"])
    test_btn.click(
        None, None, None,
        js="""
function testAnimation() {
    const element1 = document.querySelector('.hidden_config_container');
    const element2 = document.querySelector('.hidden_config');

    console.log(element1);

    element1.classList.add('show');
    element2.classList.add('show');
}
"""   
    )

    with gr.Column(visible=True, elem_classes=["hidden_config_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_config"]):
        config_modal_back_btn = gr.Button("🔙", elem_classes=["modal_back_btn"])
        with gr.Column(elem_classes=["padding_20px"]):
            gr.Markdown("## 여기에 Config를 넣을 예정", elem_classes=["md_color_white"])
            gr.Slider(0, 8192, value=gen_configs['max_output_tokens'], label="MOutToken", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['temperature'], label="TEMP", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['top_p'], label="TOP P", interactive=True)
            gr.Slider(0, 100, value=gen_configs['top_k'], label="TOP K", interactive=True)

        config_modal_back_btn.click(
            None, None, None,
            js="""
function testAnimation2() {
    const element1 = document.querySelector('.hidden_config_container');
    const element2 = document.querySelector('.hidden_config');

    console.log(element1);

    element1.classList.remove('show');
    element2.classList.remove('show');
}
"""
        )

    with gr.Column(visible=True, elem_classes=["hidden_chat_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_chat"]):
        chat_modal_back_btn = gr.Button("🔙", elem_classes=["modal_back_btn"])
        gr.Markdown("## 여기에 채팅 인터페이스를 넣을 예정", elem_classes=["md_text_center", "md_color_white"])

        chat_modal_back_btn.click(
            None, None, None,
            js="""
function testAnimation2() {
    const element1 = document.querySelector('.hidden_chat_container');
    const element2 = document.querySelector('.hidden_chat');

    console.log(element1);

    element1.classList.remove('show');
    element2.classList.remove('show');
}
"""
        )

    with gr.Column(visible=False, elem_classes=["follow-cursor"]) as info_box:
        gr.Markdown("### Evaluation", elem_classes=["md_text_center"])
        markdown = gr.Markdown("", elem_classes=["md_vertical_margin"])
        gr.Button("Take Suggestion", elem_classes=["stylish-button", "narrow-stylish-botton"])
        
        with gr.Row(elem_classes=["row_nogap"]):
            chat_btn = gr.Button("💬", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            gr.Button("✨", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            gr.Button("👓", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            gr.Button("🔥", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])

            chat_btn.click(
                None, None, None,
                js="""
function testAnimation() {
    const element1 = document.querySelector('.hidden_chat_container');
    const element2 = document.querySelector('.hidden_chat');

    console.log(element1);

    element1.classList.add('show');
    element2.classList.add('show');
}
"""
            )

        with gr.Accordion("References", open=False, elem_classes=["acc_nogap", "acc_only_bottom_shadow"]) as tone_group:
            gr.Slider(0, 8192, value=gen_configs['max_output_tokens'], label="MOutToken", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['temperature'], label="TEMP", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['top_p'], label="TOP P", interactive=True)
            gr.Slider(0, 100, value=gen_configs['top_k'], label="TOP K", interactive=True)

        with gr.Accordion("Configurations", open=False, elem_classes=["acc_nogap", "acc_only_bottom_shadow"]) as tone_group:
            gr.Slider(0, 8192, value=gen_configs['max_output_tokens'], label="MOutToken", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['temperature'], label="TEMP", interactive=True)
            gr.Slider(0, 2.0, value=gen_configs['top_p'], label="TOP P", interactive=True)
            gr.Slider(0, 100, value=gen_configs['top_k'], label="TOP K", interactive=True)

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

    with gr.Accordion("External Knowledge", open=True, elem_classes=["acc_big_font", "acc_only_bottom_shadow"]) as url_section:
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