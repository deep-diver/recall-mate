import yaml

with open("styles/styles.css", "r") as f:
    css = f.read()

with open("js/update_position.js", "r") as f:
    update_position_js = f.read()

with open("configs/generation_configs.yaml") as f:
    gen_configs = yaml.safe_load(f)