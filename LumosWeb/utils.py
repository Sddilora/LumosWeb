import os
import markdown

def render_markdown(template):
    converted_html = markdown.markdown(template, extensions=['fenced_code', 'codehilite', 'tables'])
    css_path = os.path.join(os.path.dirname(__file__), 'static/styles.css')
    with open(css_path, encoding="utf16") as css_file:
        css_content = css_file.read()
    rendered_template = f"<style>{css_content}</style>{converted_html}"
    return rendered_template

def get_previous_link(post_list, current_post):
    index = post_list.index(current_post)
    if index > 0:
        previous_post = post_list[index - 1]
        return f"/posts/{previous_post['slug']}"
    else:
        return None

def get_next_link(post_list, current_post):
    index = post_list.index(current_post)
    if index < len(post_list) - 1:
        next_post = post_list[index + 1]
        return f"/posts/{next_post['slug']}"
    else:
        return None
