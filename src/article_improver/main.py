import typer
from article_improver import config
from article_improver.command import config_command

cfg, loop = config.init()
app = typer.Typer()

@app.command(name="seo")
def seo_command():
    print("Seo command")

@app.command(name="configure")
def configure_command():
    config_command.handle(config.DEFAULT_CONFIG_FILE, config.DEFAULT_CONFIG_FILE_FOLDER)

if __name__ == "__main__":
    app()