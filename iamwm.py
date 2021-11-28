#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://rgozi.com/]iamwm", guide_style="bold cyan")
language_tree = tree.add("🐵 programing language")
language_tree.add("proficient in python")
language_tree.add("competent in go")
language_tree.add("competent in javascript")
framework_tree = tree.add("🏭 framework")
framework_tree.add("proficient in [link=https://www.tornadoweb.org/en/stable/]tornado")
framework_tree.add("competent in [link=https://flask.palletsprojects.com/en/2.0.x/]flask")
framework_tree.add("knowledge and experience in [link=https://fastapi.tiangolo.com/]fastapi")
framework_tree.add("knowledge and experience in [link=https://echo.labstack.com/]echo")
framework_tree.add("experience in [link=https://vuejs.org/index.html]vue")
database_tree = tree.add("🎁 database && middleware")
database_tree.add("proficient [link=https://www.mongodb.com/]mongodb")
database_tree.add("competent in [link=https://redis.io//]redis")
database_tree.add("competent in [link=https://www.rabbitmq.com/]rabbitmq")

about = """\
I'm a software developer, living in [link=https://ditu.amap.com/search?query=%E6%AD%A6%E6%B1%89&city=420000&geoobj=113.248277%7C30.047641%7C115.949036%7C31.166271&zoom=9.55]Wuhan[/], China. I'm now working for an industrial IoT company. I'm interest in distributed systems.Other than software development, my passion would be [link=https://500px.com/p/vcg-wangmengcn?view=photos/]landscape photography[/]."""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)


if __name__ == '__main__':
    console.print(Columns([panel, tree]))

    CONSOLE_HTML_FORMAT = """\
    <pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
    """

    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
