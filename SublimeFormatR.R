args <- commandArgs(trailingOnly = TRUE)

in_text <- readLines(args[1])
n_indent <- as.integer(args[7])

in_text_trimmed <- stringr::str_trim(in_text)
in_text_not_blank <- in_text[stringr::str_length(in_text_trimmed) > 0]

initial_spacetabs <- stringr::str_extract(in_text_not_blank, "^[\\t\\s]+")
initial_tabs <- stringr::str_count(initial_spacetabs, "\\t")
initial_spaces <- stringr::str_count(initial_spacetabs, "\\s")
total_spaces <- initial_tabs * n_indent + initial_spaces
spaces_to_add <- min(total_spaces)

res <- formatR::tidy_source(text = in_text,
                            comment = as.logical(args[3]),
                            blank = as.logical(args[4]),
                            arrow = as.logical(args[5]),
                            brace.newline = as.logical(args[6]),
                            indent = n_indent,
                            output = FALSE,
                            width.cutoff = as.integer(args[8]))$text.tidy

res_joined <- stringr::str_c(res, collapse = "\n")
res_split <- c(stringr::str_split(res_joined, pattern = "\\n", simplify = T))
res_padded <- stringr::str_c(stringr::str_c(rep(" ", spaces_to_add), collapse = ""), res_split)

writeLines(res_padded, args[2])
