# Local (file) Augmented Generation

This Python script allows you to provide a prompt and a context file, and it will generate a response in markdown format using the OpenAI ChatGPT language model. You  also can easily modify the llm object at the top of the script to another langchain llm instance.

## Prerequisites
- Python 3.x
- `rich` library (`pip install rich`)
- `langchain` library (`pip install langchain`)
- `click` library (`pip install click`)
- OpenAI API key (set as an environment variable `OPENAI_API_KEY`)
```
pip install -r requirements.txt
```

## Usage

```
python lag.py --prompt "Your prompt here" --file path/to/context/file.txt
```

- `--prompt`: The prompt you want to provide related to the context file.
- `--file`: The path to the context file you want to use. If not provided, the script will read from stdin.

### Example

```
python lag.py --prompt "Summarize the key points from this document." --file document.txt
```

This will read the content of `document.txt`, send it along with the prompt to the OpenAI ChatGPT model, and print the generated markdown response to the console.

### Stdin

If you don't provide a file, the script will read the context from stdin. You can pipe the content to the script like this:

```
cat document.txt | python lag.py --prompt "Summarize the key points from this document."
```

## How it Works

1. The script defines an OpenAI ChatGPT language model instance using `langchain_openai.ChatOpenAI`.
2. It constructs a prompt template that includes the context and the user-provided prompt.
3. The `prompt_with_context` function substitutes the template with the provided context and prompt, and invokes the language model to generate a response.
4. The `main` function parses the command-line arguments using `click`, reads the context from the specified file or stdin, calls `prompt_with_context`, and prints the generated markdown response to the console using `rich.Markdown`.

## License

This project is licensed under the [MIT License](LICENSE).
