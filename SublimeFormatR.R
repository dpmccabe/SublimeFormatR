args <- commandArgs(trailingOnly = TRUE)
pkg_path <- args[1]
comment <- as.logical(args[2])
blank <- as.logical(args[3])
arrow <- as.logical(args[4])
brace.newline <- as.logical(args[5])
indent <- as.integer(args[6])
width.cutoff <- as.integer(args[7])
tryCatch(
  res <- formatR::tidy_source(
    paste0(pkg_path, "\\TEMP.R"), comment = comment, blank = blank, arrow = arrow, 
    brace.newline = brace.newline, indent = indent, width.cutoff = width.cutoff, output = FALSE )$text.tidy,
  error = function(e) cat(e$message, file = paste0(pkg_path, "\\ERROR.txt"))
)
cat(res)
