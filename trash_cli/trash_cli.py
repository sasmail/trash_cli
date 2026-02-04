import click
import storage
import config

@click.command()
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(exists=True),
)

def cli(paths):
    for file in files:
        click.echo(f"Trashing {file.name}")

    # this will be needed at some point:
    # def move_files(new_filename, info_file_name):
    #     info_file_path = Path(info).resolve()


if __name__ == "__main__":
    cli()

cli("trash.py")