args <- commandArgs(trailingOnly = TRUE)
pkg_path <- args[1]
settings <- args[2]
# res <- paste(args, collapse = " ")

comment <- TRUE
blank <- TRUE
arrow <- TRUE
brace.newline <- FALSE
indent <- 2
width.cutoff <- 80

# res <- formatR::tidy_source(
#   "TEMP.R", comment = comment, blank = blank, arrow = arrow, 
#   brace.newline = brace.newline, indent = indent, width.cutoff = width.cutoff )$text.tidy



res <- formatR::tidy_source(
  paste0(pkg_path, "\\TEMP.R"), comment = comment, blank = blank, arrow = arrow, 
  brace.newline = brace.newline, indent = indent, width.cutoff = width.cutoff, output = FALSE )$text.tidy
cat(res, file = paste0(pkg_path, "\\test.txt"))
cat(res)
