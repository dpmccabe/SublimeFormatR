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
        args = "settings"
        text_formated = format_r(args, pkg_path)
        self.view.replace(edit, region, text_formated)


def format_r(args, pkg_path):
    cmd = ["Rscript", pkg_path + "\\SublimeFormatR.R", pkg_path, args]
    res = subprocess.check_output(cmd, universal_newlines = True, shell = True)
    return res
