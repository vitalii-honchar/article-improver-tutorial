import typer

app = typer.Typer()

@app.command(name="seo")
def seo_command():
    print("Seo command")

if __name__ == "__main__":
    app()