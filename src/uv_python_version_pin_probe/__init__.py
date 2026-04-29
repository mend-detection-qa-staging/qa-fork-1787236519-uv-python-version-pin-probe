import click
import requests


@click.command()
@click.option("--url", default="https://httpbin.org/get", help="URL to fetch")
def main(url: str) -> None:
    response = requests.get(url, timeout=5)
    click.echo(f"Status: {response.status_code}")


if __name__ == "__main__":
    main()