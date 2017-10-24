args <- commandArgs(trailingOnly = TRUE)

res <- formatR::tidy_source(source = args[1],
                            comment = as.logical(args[3]),
                            blank = as.logical(args[4]),
                            arrow = as.logical(args[5]),
                            brace.newline = as.logical(args[6]),
                            indent = as.integer(args[7]),
                            output = FALSE,
                            text = NULL,
                            width.cutoff = as.integer(args[8]))$text.tidy

writeLines(res, args[2])
