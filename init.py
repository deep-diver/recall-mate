import yaml

with open("styles/styles.css", "r") as f:
    css = f.read()

with open("js/stats.js", "r") as f:
    stats_js = f.read()

with open("js/update_position.js", "r") as f:
    update_position_js = f.read()

with open("js/anima_show_config.js", "r") as f:
    show_config_js = f.read()

with open("js/anima_hide_config.js", "r") as f:
    hide_config_js = f.read()

with open("js/anima_show_chat.js", "r") as f:
    show_chat_js = f.read()

with open("js/anima_hide_chat.js", "r") as f:
    hide_chat_js = f.read()

with open("js/anima_show_preview.js", "r") as f:
    show_preview_js = f.read()

with open("js/anima_hide_preview.js", "r") as f:
    hide_preview_js = f.read()

with open("js/anima_show_bg.js", "r") as f:
    show_bg_js = f.read()

with open("js/anima_hide_bg.js", "r") as f:
    hide_bg_js = f.read()

with open("configs/generation_configs.yaml") as f:
    gen_configs = yaml.safe_load(f)