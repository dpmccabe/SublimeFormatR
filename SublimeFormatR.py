import sublime, sublime_plugin
import os
import subprocess

class FormatrCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        text = self.view.substr(region)
        pkg_path = sublime.packages_path() + "\\SublimeFormatR"
        tmp = pkg_path  + "\\TEMP.R"
        with open(tmp, "w") as code_file:
            code_file.write(text)

        settings = sublime.load_settings('SublimeFormatR.sublime-settings')
        comment =  str(settings.get("comment ", True))
        blank =  str(settings.get("blank", True))
        arrow =  str(settings.get("arrow", True))
        brace_newline =  str(settings.get("brace_newline", False))
        indent =  str(settings.get("indent", 2))
        width_cutoff =  str(settings.get("width_cutoff", 80))
        args = [pkg_path, comment, blank, arrow, brace_newline, indent, width_cutoff]
        # \n can not be in the argument of check_output()?
        try:
            text_formated = format_r(args)
        except Exception:
            pass
        os.remove(tmp)
        error_file = pkg_path + "\\ERROR.txt"
        if os.path.isfile(error_file):
            with open(error_file, "r") as error_f:
                error_message = error_f.read()
            sublime.error_message(error_message)
            os.remove(error_file)
        self.view.replace(edit, region, text_formated)


def format_r(args):
    cmd = ["Rscript", args[0] + "\\SublimeFormatR.R"] + args
    res = subprocess.check_output(cmd, universal_newlines = True, shell = True)
    return res
