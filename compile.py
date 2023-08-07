import markdown
md = markdown.Markdown(extensions=['mdx_math'])

file_dir = "test"

file = open(file_dir, "r")
text = file.read()
file.close()

file_dir = file_dir + '.html'
file = open(file_dir, "w")
text = md.convert(text)

template_file = open("template.html", "r")
template = template_file.read()
template_file.close()

css_dir = "style.css"

template = template.replace("{{css_dir}}", css_dir)
template = template.replace("{{main}}", text)

file.write(template)
file.close()
