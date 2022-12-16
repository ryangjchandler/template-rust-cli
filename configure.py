import os

def ask(question, required = True, message = None):
    while True:
        value = input(question)
        if not value and required:
            red_print(message)
            continue
        return value

def red_print(text):
    print("\033[1;31m{}\033[0m".format(text))

def main():
    name = ask("Project name (kebab-case): ", message = "Project name is required")
    description = ask("Project description: ", message = "Project description is required")
    author = ask("Project author, e.g. Your Name <yourname@example.com>: ", message = "Author is required")
    
    details = """
Project name: {}
Project description: {}
Project author: {}
    """.format(name, description, author)
    print(details)

    replace = ask("Is this correct? [Y/n]: ", required = False)
    if replace == "n":
        return

    for _, _, files in os.walk(os.getcwd()):
        for file in files:
            if ".git" in file or "configure.py" in file
                continue

            with open(file, "r+") as f:
                content = f.read()
                content = content.replace("template-rust-cli", name)
                content = content.replace("My awesome Rust project.", description)
                content = content.replace("Your Name <yourname@example.com>", author)
                f.write(content)

if __name__ == "__main__":
    main()