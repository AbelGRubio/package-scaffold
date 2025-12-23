import typer 

app = typer.Typer(
    help=" {{ cookiecutter.project_slug }} unified CLI",
    add_completion=True
)


@app.command()
def hello():
    """run the hello app"""
    print("Hello from {{ cookiecutter.project_slug }}")


@app.command()
def goodbye():
    """run the goodbye app"""
    print("Goodbye from {{ cookiecutter.project_slug }}")

    
def main():
    app()

if __name__ == "__main__":
    main()
