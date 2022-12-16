# template-rust-cli

This template repository contains a skeleton for command-line Rust projects.

## Dependencies

It uses the following dependencies:
* [cmder](https://github.com/ndaba1/cmder)
* [colored](https://github.com/mackwic/colored)

`cmder` is used for argument parsing and `colored` provides a nice API for colorizing console output.

## Layout

There are 2 crates in the skeleton.
1. `template-rust-cli` is the main crate that contains your console application.
2. `template-rust-cli-lib` is the crate that contains your application logic.

### `template-rust-cli`

* Commands are written inside of the `src/cmd` directory.
* Each command has it's own file, exporting a function named after the command.
* Add the command file inside of `src/cmd/mod.rs` and re-export the function from that crate.
* Register the subcommand inside of `src/main.rs`.
* Only do the minimum amount of work inside of your commands.

An example `inspire` command is provided for reference.

### `template-rust-cli-lib`

* Expose your business logic via the `prelude` module.
* Only expose the things that you need.

## Configuration

If you have Python installed, you can configure your repository faster with the [`configure.py`](/configure.py) script:

```sh
python3 ./configure.py
```

This will ask for your project's name, description and author and replace the default values with your own.