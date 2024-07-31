import re
import toml
import gradio as gr
from string import Template
from modules import lm

def analyze_click(title, tb_write, data, retry_num=5):
    if title == "Analyze":
        with open('prompts/analyze_prompts.toml', 'r') as f:
            prompt_tmpl = toml.load(f)

        prompt_tmpl = Template(prompt_tmpl['analyze']['prompt'])
        prompt = prompt_tmpl.substitute(original_text=tb_write)

        json_dict = None
        cur_retry = 0
		
        while json_dict is None and cur_retry < retry_num:
            try:
                response = lm.model.generate_content(prompt)
                json_dict = lm._parse_first_json_snippet(response.text)
            except Exception as e:
                json_dict = None
                cur_retry = cur_retry + 1

        # print(json_dict)
        json_dict['text'] = tb_write
		
        previous_end = 0  # Initialize a variable to track the end index of the previous match

        for feedback in json_dict["entities"]:
            entity = feedback['entity']
            match = re.search(re.escape(entity), tb_write[previous_end:])  # Search after the previous match
            
            if match:
                feedback['start'] = match.start() + previous_end  # Adjust start index based on previous_end
                feedback['end'] = match.end() + previous_end  # Adjust end index as well
                previous_end = feedback['end']  # Update previous_end for the next iteration

        return [
            gr.Button("Back to writing"),
            gr.Button(interactive=False),
            gr.Textbox(visible=False), 
            gr.Highlightedtext(value=json_dict, visible=True),
			json_dict,
        ]
    else:
        return [
            gr.Button("Analyze"),
			gr.Button(interactive=True),
            gr.Textbox(visible=True), 
            gr.Highlightedtext(visible=False),
			data
        ]

def on_select(value, data, markdown, evt: gr.SelectData):  # Event handler function
    selected_text = evt.value[0]  # Get the label of the selected entity
    selected_label = evt.value[1]

    eval = markdown
    for entity in data["entities"]:
        start = entity["start"]
        end = entity["end"]

        if entity["entity"] == selected_label and \
            data["text"][start:end] == selected_text:
            eval = entity["feedback"]

    return [
		gr.Markdown(value=eval),
		gr.Markdown(value=f"based on \"{eval}\"")
    ]

def submit_user_chat(chatbot, user_chat_message):
	messages = chatbot
	messages.append(
        (user_chat_message, "????")
    )
	return messages