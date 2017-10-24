import sublime, sublime_plugin
import os
import subprocess

class FormatrCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        text = self.view.substr(region)
        
        pkg_path = os.path.join(sublime.packages_path(), "SublimeFormatR")
        
        in_file = os.path.join(pkg_path, "in.R")
        out_file = os.path.join(pkg_path, "out.R")

        with open(in_file, "w") as in_file_buf:
            in_file_buf.write(text)

        format_script_path = os.path.join(pkg_path, "SublimeFormatR.R")

        settings = sublime.load_settings('SublimeFormatR.sublime-settings')
        comment =  str(settings.get("comment ", True))
        blank =  str(settings.get("blank", True))
        arrow =  str(settings.get("arrow", True))
        brace_newline =  str(settings.get("brace_newline", False))
        indent =  str(settings.get("indent", 2))
        width_cutoff =  str(settings.get("width_cutoff", 80))

        args = [in_file, out_file, comment, blank, arrow, brace_newline, indent, width_cutoff]

        cmd = ["Rscript", format_script_path] + args
        print(cmd)
        subprocess.check_call(cmd)

        with open(out_file, "r") as out_file_buf:
            out_text = out_file_buf.read()

        self.view.replace(edit, region, out_text)

        os.remove(in_file)
        os.remove(out_file)

        print('Formatted R code')
