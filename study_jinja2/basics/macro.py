from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'), trim_blocks=False)
template = env.get_template('macro.tpl')
disp_text = template.render()
print(disp_text)