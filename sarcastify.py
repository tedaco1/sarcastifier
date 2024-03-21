import click

# TODO: Add different levels of sarcasm
def make_sarcastic(normal_text):
    # Make everything lowercase
    for letter in normal_text:
        letter.lower()

    # Make every other letter uppercase
    counter = 1
    sarcastic = ""
    for letter in normal_text:
        if counter % 2 == 0:
            sarcastic = sarcastic + letter.upper()
        else:
            sarcastic = sarcastic + letter.lower()
        counter = counter + 1
        # print(f"{sarcastic}")

    # Print it out with click
    click.echo(f"{sarcastic}")
    

@click.group()
def cli():
    pass

@click.command()
@click.option('--severity', default=1, help="How sarcastic to be (1-3)")
@click.option('--normal-text', prompt='Your normal text', help='Text to make sarcastic')
def sarcastify(severity, normal_text):
    """Turns your text sarcastic!"""
    make_sarcastic(normal_text)

if __name__ == '__main__':
    sarcastify()