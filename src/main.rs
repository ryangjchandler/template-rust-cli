use template_rust_cli_lib::prelude::*;
use cmder::Program;

mod cmd;

fn main() {
    let mut program = Program::new();

    program
        .description("My awesome Rust project.")
        .version(env!("CARGO_PKG_VERSION"))
        .author("Your Name <yourname@example.com>");

    program
        .subcommand("inspire")
        .description("Get inspired.")
        .action(cmd::inspire);

    program.parse();
}
