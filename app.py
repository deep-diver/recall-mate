import gradio as gr
from gr_events import events
from init import css
from init import (
    update_position_js,
    show_config_js, hide_config_js,
    show_chat_js, hide_chat_js,
    show_preview_js, hide_preview_js
)
from init import gen_configs

with gr.Blocks(css=css) as demo:
    data = gr.State()

    gr.Markdown("# Exploring the Future of Writing with Recall Mate", elem_classes=["md_text_center"]) 

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
            js="""
function wc(text) {
    const wordsPerMinute = 100; 

    // Count the words using any of the methods mentioned before
    const wordCount = text.split(/\s+/).filter(word => word !== "").length;

    // Calculate read time in minutes and round up to the nearest minute
    let readTimeMinutes = Math.ceil(wordCount / wordsPerMinute);

    // Format the output
    readTimeMinutes = readTimeMinutes === 1 ? "## 1" : `## ${readTimeMinutes}`;

    return [readTimeMinutes, '## ' + wordCount];
}
"""
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