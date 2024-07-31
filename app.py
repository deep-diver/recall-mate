import gradio as gr
from gr_events import events
from init import css
from init import (
    update_position_js,
    stats_js,
    show_bg_js, hide_bg_js,
    show_config_js, hide_config_js,
    show_chat_js, hide_chat_js,
    show_preview_js, hide_preview_js
)
from init import gen_configs

css = """
.gradio-container {
    flex-grow: none !important;
    padding: 0px !important;
    margin: 0px !important;
    max-width: unset !important;
    padding-left: 30px !important;
    padding-right: 30px !important;
    padding-top: 20px !important;
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

#tb_write {
    padding: 0px;
}

#tb_write > label > textarea{
    line-height: var(--scale-3);
}

#highlight_txt {
    overflow: scroll !important;
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
    min-width: unset;
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

.stylish-button2 {
    display: inline-block;
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    color: #ffffff;
    background: #4caf50c4;
    border: none;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    cursor: pointer;
    font-size: 15pt;
}

.stylish-button2:hover {
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

.acc_noborder {
    border: none !important;
    box-shadow: none;
}

.hidden_chat {
    transition: transform 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    top: 0;
    right: -1000px;
    width: 70%;
    height: 100%;
    background-color: white;
    z-index: 9999; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 20px 0px 0px 20px;
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
    transform: translateX(-1000px);
}

.hidden_chat_container.show {
    opacity: 1;
    z-index: 9998;
}

.hidden_config {
    transition: transform 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    bottom: 0;
    right: -1000px;
    width: 50%;
    height: 99%;
    background-color: white;
    z-index: 10002; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 20px 0px 0px 20px;
    box-shadow: rgba(0, 0, 0, 0.1) -20px 0px 20px 20px;
}

.hidden_config.show {
    transform: translateX(-1000px);
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
    z-index: 10001;
}

.hidden_preview {
    transition: transform 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    bottom: 0;
    right: -1000px;
    width: 100%;
    height: 99%;
    background-color: white;
    z-index: 9999; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 20px 0px 0px 20px;
    box-shadow: rgba(0, 0, 0, 0.1) -20px 0px 20px 20px;
    padding-right: 50px;
}

.hidden_preview.show {
    transform: translateX(-1000px);
}

.hidden_preview_container {
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

.hidden_preview_container.show {
    opacity: 1;
    z-index: 9998;
}

.hidden_background_container {
    opacity: 0;
    transition: opacity 0.5s ease-in-out; /* Smooth transition */

    position: fixed;  /* Ensures it's always on top */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.3);
    z-index: -2; /* A very high value to ensure it's on top */
}

.hidden_background_container.show {
    opacity: 1;
    z-index: 9996;    
}

.hidden_background {
    transition: transform 0.5s ease-in-out; /* Smooth transition */
    
    position: fixed;  /* Ensures it's always on top */
    bottom: 0;
    left: -1000px;
    width: 90%;
    height: 99%;
    background-color: white;
    z-index: 9997; /* A very high value to ensure it's on top */
    border: 1px solid;
    border-color: aliceblue;
    border-radius: 0px 20px 20px 0px;
    box-shadow: rgba(0, 0, 0, 0.1) 20px 0px 20px 20px;
    padding-left: 30px;
    padding-right: 30px;
    padding-top: 30px;
}

.hidden_background.show {
    transform: translateX(1000px);
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
    background: #007bff;
    cursor: pointer;     /* Indicate it's clickable */
    border-radius: 10px;    /* Add rounded corners */
    z-index: 10000;        /* Ensure it's above other content */
    border: none;
    transition: all 0.3s ease;
}

.modal_trigger:hover {
    background: #0069d9;
    width: 15px;
}

.modal_trigger:active {
    background: #0062cc;
    width: 10px;
}

.padding_20px {
    padding: 20px;
}

.md_overflow_scroll {
    overflow: scroll !important;
}

.chatbot_fullheight {
    height: 100% !important;
}

.chatbot_nolabel > div > label {
    display: none;
}

#chat_user_message {
    margin: 0px;
    padding: 0px;
    height: 100px;
}

#chat_user_message > label > span {
    display: none;
}

.weird_1p_height {
    height: 1%;
}

#writing_container > div {
    border: none;
    box-shadow: none;
}

#writing_container, #stats_container, #history_container, #background_container {
    padding: 12px;
    border: 1px;
    border-style: solid;
    border-radius: 10px;
    border-color: antiquewhite;
    box-shadow: -1px 0px 20px 2px rgb(224 224 224 / 70%);
}

#stats_container {
    row-gap: 10px;
}

.md_stat_label > div > div > span > h5 {
    color: gray;
}

#plus_btn {
    min-width: fit-content;
    font-size: 20px;
}
"""

with gr.Blocks(css=css) as demo:
    data = gr.State()

    gr.Markdown("# Exploring the Future of Writing with Recall Mate", elem_classes=["md_text_center"]) 

    # HIDDEN -----
    nav_btn = gr.Button("", elem_id="nav_btn", elem_classes=["modal_trigger"])
    nav_btn.click(None, None, None, js=show_config_js)

    with gr.Column(visible=True, elem_classes=["hidden_preview_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_preview"]):
        preview_modal_back_btn = gr.Button("🔙", elem_classes=["modal_back_btn"])
        with gr.Column(elem_classes=["padding_20px", "md_overflow_scroll"]):
            gr.Markdown("## Preview", elem_classes=["md_text_center", "md_color_white"])

            preview_md = gr.Markdown("", elem_classes=["md_color_white"])

    preview_modal_back_btn.click(None, None, None, js=hide_preview_js)

    with gr.Column(visible=True, elem_classes=["hidden_config_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_config"]):
        config_modal_back_btn = gr.Button("🔙", elem_classes=["modal_back_btn"])
        with gr.Column(elem_classes=["padding_20px"]):
            gr.Markdown("## Control GenAI Behaviour", elem_classes=["md_text_center", "md_color_white"])

            gr.Markdown("### Language Model", elem_classes=["md_color_white"])
            gr.Slider(0, 8192, step=1, value=gen_configs['max_output_tokens'], label="max output tokens", interactive=True)
            gr.Slider(0, 2.0, step=0.1, value=gen_configs['temperature'], label="temperature", interactive=True)
            gr.Slider(0, 2.0, step=0.1, value=gen_configs['top_p'], label="top p", interactive=True)
            gr.Slider(0, 100, step=1, value=gen_configs['top_k'], label="top k", interactive=True)

            # gr.Markdown("### External Knowledge", elem_classes=["md_color_white"])
            with gr.Accordion("External Knowledge", open=False, elem_classes=["acc_big_font", "acc_only_bottom_shadow"]) as url_section:
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, scale=8, elem_classes=["txt_no_label", "txt_no_border"])

            gr.Markdown("### Image Generation", elem_classes=["md_color_white"])

        config_modal_back_btn.click(None, None, None, js=hide_config_js)

    with gr.Column(visible=True, elem_classes=["hidden_chat_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_chat"]):
        chat_modal_back_btn = gr.Button("🔙", elem_classes=["modal_back_btn"])
        with gr.Column(elem_classes=["weird_1p_height", "padding_20px"]):
            gr.Markdown("## Exchange thoughts", elem_classes=["md_text_center", "md_color_white"])
            chat_topic = gr.Markdown("Based on ....", elem_classes=["md_color_white"])

            chatbot = gr.Chatbot(
                [("hello", "world"), ("how are you?", "I am fine!")], 
                avatar_images=("assets/avatar-user.png", "assets/avatar-machine.png"), 
                elem_classes=["chatbot_fullheight", "chatbot_nolabel"]
            )
            user_chat_message = gr.Textbox(lines=3, placeholder="enter your message", elem_id="chat_user_message")
            with gr.Row():
                user_chat_submit = gr.Button("Ask", elem_classes=["stylish-button"])
                gr.Button("Remove last", elem_classes=["stylish-button"])

            user_chat_submit.click(
                events.submit_user_chat,
                [chatbot, user_chat_message],
                chatbot
            )

        chat_modal_back_btn.click(None, None, None, js=hide_chat_js)

    with gr.Column(visible=False, elem_classes=["follow-cursor"]) as info_box:
        gr.Markdown("### 💡 Suggestion", elem_classes=["md_text_center"])
        markdown = gr.Markdown("", elem_classes=["md_vertical_margin"])
        gr.Button("Take Suggestion", elem_classes=["stylish-button", "narrow-stylish-botton"])
        
        with gr.Row(elem_classes=["row_nogap"]):
            gr.Button("👏🏻", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            gr.Button("🤔", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            gr.Button("?", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])
            chat_btn = gr.Button("💬", elem_classes=["btn_no_width", "stylish-button2", "narrow-stylish-botton"])

            chat_btn.click(None, None, None, js=show_chat_js)

    aaa = gr.Button("d")
    aaa.click(
        None, None, None, 
        js=show_bg_js
    )

    with gr.Column(visible=True, elem_classes=["hidden_background_container"]):
        gr.Markdown("")

    with gr.Column(visible=True, elem_classes=["hidden_background"]):
        with gr.Column(elem_classes=["padding_20px"]):
            gr.Markdown("# Setups", elem_classes=['md_text_center'])

            with gr.Row():
                gr.Textbox(placeholder="enter external knowledge (URL)", label=None, elem_classes=["txt_no_label", "txt_no_border"], scale=12)
                gr.Button("+", elem_id="plus_btn", elem_classes=["stylish-button"], interactive=True)

            bg_modal_back_btn = gr.Button("Done", elem_id="plus_btn", elem_classes=["stylish-button"], interactive=True)

    bg_modal_back_btn.click(None, None, None, js=hide_bg_js)
    # ----- HIDDEN

    with gr.Column(elem_id="stats_container"):
        with gr.Row():
            gr.Markdown("##### Read Time (min)", elem_classes=['md_text_center', 'md_stat_label'])
            gr.Markdown("##### Acceptance %", elem_classes=['md_text_center', 'md_stat_label'])
            gr.Markdown("##### Word Counts", elem_classes=['md_text_center', 'md_stat_label'])
        with gr.Row():
            ert = gr.Markdown("## 0", label="Estimated Read Time", elem_classes=['md_text_center'])
            gr.Markdown("## 0", label="Readability Score", elem_classes=['md_text_center'])
            wc = gr.Markdown("## 0", label="Word Counts", elem_classes=['md_text_center'])

    with gr.Column(elem_id="writing_container"):
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

        tb_write.change(
            None, tb_write, [ert, wc],
            js=stats_js
        )

    with gr.Row():
        analyze_btn = gr.Button("Analyze", elem_classes=["stylish-button"])
        prev_analyze_btn = gr.Button("Prev Analysis", interactive=False, elem_classes=["stylish-button"])
        preview_btn = gr.Button("Preview", elem_id="preview_btn", elem_classes=["stylish-button"])

    analyze_btn.click(
        events.analyze_click, 
        [analyze_btn, tb_write, data],
        [analyze_btn, prev_analyze_btn, tb_write, highlighted_text, data],
    ).then(
        None, None, None,
        js=update_position_js
    )

    prev_analyze_btn.click(
        lambda data: [
            gr.Button("Back to writing"), 
            gr.Button(interactive=False), 
            gr.Textbox(visible=False), 
            gr.Highlightedtext(value=data, visible=True)
        ],
        data,
        [analyze_btn, prev_analyze_btn, tb_write, highlighted_text],
    ).then(
        None, None, None,
        js=update_position_js
    )

    preview_btn.click(
        # events.preview_click,
        lambda x: x, 
        tb_write, 
        preview_md
    ).then(None, None, None, js=show_preview_js)

    highlighted_text.select(
        fn=events.on_select, 
        inputs=[highlighted_text, data, markdown], 
        outputs=[markdown, chat_topic]
    )

    with gr.Column(elem_id="history_container") as t_c:
        with gr.Accordion("History", open=False, elem_classes=["acc_big_font", "acc_noborder"]):
            gr.DataFrame(
                value=[
                    ["first one...", "2024/07/27"],
                    ["first one...", "2024/07/27"]
                ],
                headers=["Title", "Date"],
                datatype=["str", "date"],
                interactive=False,
            )

demo.launch()