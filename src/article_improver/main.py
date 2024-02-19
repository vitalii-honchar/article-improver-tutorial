import typer
from article_improver import config
from article_improver.chat_gpt import ChatGpt
from article_improver.command import config_command
from openai import AsyncOpenAI

app = typer.Typer()
cfg, loop = config.init()

if cfg is not None:
    chat_gpt = ChatGpt(AsyncOpenAI(api_key=cfg.open_ai_key))

@app.command(name="seo")
def seo_command():
    print("Seo command")

@app.command(name="configure")
def configure_command():
    config_command.handle(config.DEFAULT_CONFIG_FILE, config.DEFAULT_CONFIG_FILE_FOLDER)

if __name__ == "__main__":
    app()