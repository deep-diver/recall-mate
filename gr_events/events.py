import os
import re
import json
import toml
import gradio as gr
from string import Template
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def _find_json_snippet(raw_snippet):
	"""
	_find_json_snippet tries to find JSON snippets in a given raw_snippet string
	"""
	json_parsed_string = None

	json_start_index = raw_snippet.find('{')
	json_end_index = raw_snippet.rfind('}')

	if json_start_index >= 0 and json_end_index >= 0:
		json_snippet = raw_snippet[json_start_index:json_end_index+1]
		try:
			json_parsed_string = json.loads(json_snippet, strict=False)
		except:
			raise ValueError('......failed to parse string into JSON format')
	else:
		raise ValueError('......No JSON code snippet found in string.')

	return json_parsed_string

def _parse_first_json_snippet(snippet):
	"""
	_parse_first_json_snippet tries to find JSON snippet and parse into json object
	"""
	json_parsed_string = None

	if isinstance(snippet, list):
		for snippet_piece in snippet:
			try:
				json_parsed_string = _find_json_snippet(snippet_piece)
				return json_parsed_string
			except:
				pass
	else:
		try:
			json_parsed_string = _find_json_snippet(snippet)
		except Exception as e:
			raise ValueError(str(e))

	return json_parsed_string

def test_click(title, tb_write, retry_num=5):
    if title == "Analyze":
        with open('prompts/analyze_prompts.toml', 'r') as f:
            prompt_tmpl = toml.load(f)

        prompt_tmpl = Template(prompt_tmpl['analyze']['prompt'])
        prompt = prompt_tmpl.substitute(original_text=tb_write)

        json_dict = None
        cur_retry = 0
		
        while json_dict is None and cur_retry < retry_num:
            try:
                response = model.generate_content(prompt)
                json_dict = _parse_first_json_snippet(response.text)
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
            gr.Textbox(visible=False), 
            gr.Highlightedtext(value=json_dict, visible=True),
			json_dict,
        ]
    else:
        return [
            gr.Button("Analyze"),
            gr.Textbox(visible=True), 
            gr.Highlightedtext(visible=False),
			None
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

    return gr.Markdown(value=eval)