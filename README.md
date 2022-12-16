# template-rust-cli

This template repository contains a skeleton for command-line Rust projects.

It uses the following dependencies:
* [cmder](https://github.com/ndaba1/cmder)
* [colored](https://github.com/mackwic/colored)

There are 2 crates in the skeleton.
1. `template-rust-cli` is the main crate that contains your console application.
2. `template-rust-cli-lib` is the crate that contains your application logic.

If you have Python installed, you can configure your repository faster with the [`configure.py`](/configure.py) script:

```sh
python3 ./configure.py
```

This will ask for your project's name, description and author and replace the default values with your own.