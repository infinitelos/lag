#!/usr/bin/env python3

from rich.console import Console
from rich.markdown import Markdown
from string import Template
from langchain_openai import ChatOpenAI
import sys
import click


### Define llm, any langchain llm should work
llm = ChatOpenAI()

### Define prompt template
PROMPT_TEMPLATE = """Consider the following INPUT in context of the DATA. Respond in markdown format.

DATA:
$context

INPUT:
$input_prompt
"""


def prompt_with_context(context, input_prompt):
    t = Template(PROMPT_TEMPLATE)
    prompt = t.substitute(context=context, input_prompt=input_prompt)
    resp = llm.invoke(prompt)
    return resp.content


@click.command()
@click.option("-p", "--prompt", help="Prompt relating to file")
@click.option(
    "-f",
    "--file",
    help="Context file to work with. Defaults to STDIN.",
    type=click.File("r"),
    default=sys.stdin,
)
def main(prompt, file):
    """Local Augmented Generation"""
    context = ""
    if file is sys.stdin:
        context = sys.stdin.read()
    else:
        with open(file.name, "r") as f:
            context = f.read()

    response = prompt_with_context(context, prompt)
    console = Console()
    md = Markdown(response)
    console.print(md)


if __name__ == "__main__":
    main()
