use cmder::ParserMatches;
use colored::Colorize;

pub fn inspire(matches: ParserMatches) {
    println!("{}", "Genius is one percent inspiration and ninety-nine percent perspiration. - Thomas Edison".green().underline());
}