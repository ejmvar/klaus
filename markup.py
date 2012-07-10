import os


def get_renderer(filename):
    _, ext = os.path.splitext(filename)

    for extensions, renderer in LANGUAGES:
        if ext in extensions:
            return renderer


def can_render(filename):
    return get_renderer(filename) is not None


def render(filename, content=None):
    if content is None:
        content = open(filename).read()

    return get_renderer(filename)(content)


LANGUAGES = []

try:
    import markdown
    LANGUAGES.append((['.md'], markdown.markdown))
except ImportError:
    pass

try:
    from docutils.core import publish_parts
    from docutils.writers.html4css1 import Writer

    def render_rest(content):
        return publish_parts(content, writer=Writer()).get('html_body')

    LANGUAGES.append((['.rst'], render_rest))
except ImportError:
    pass