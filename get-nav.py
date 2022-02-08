def get_nav_content():
    MKDOCS_YML_CONTENT = ""

    with open("./oi-wiki/mkdocs.yml") as f:
        MKDOCS_YML_CONTENT = f.read().split("\n")

    NAV_CONTENT = []

    start = False
    for line in MKDOCS_YML_CONTENT:
        if start or line == "nav:":
            if line == "":
                break
            NAV_CONTENT.append(line)
            start = True

    return "\n".join(NAV_CONTENT)


def get_mkdocs_template_content():
    with open("./mkdocs.template.yml") as f:
        return f.read()


with open("./mkdocs.yml", "w", encoding="utf-8") as f:
    f.write(get_mkdocs_template_content() + "\n" + get_nav_content())
