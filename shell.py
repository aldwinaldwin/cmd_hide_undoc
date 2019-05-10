import cmd
import signal

signal.signal(signal.SIGTERM, signal.SIG_DFL)                                   #ctrl-D enabled
signal.signal(signal.SIGINT, signal.SIG_DFL)

class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class shell(cmd.Cmd):

    """ Testing to hide the undocumented commands """
    hide_undoc = 1

    """ Personalize shell """
    intro = bcolors.BOLD+bcolors.HEADER+"MyShell CLI ... (type help for available commands)"+bcolors.ENDC
    prompt = '$ '
    doc_header = bcolors.BOLD+'Available Commands (type help <topic>):'+bcolors.ENDC
    ruler = bcolors.BOLD+'*'+bcolors.ENDC

    """ documented commands """
    def do_quit(self, line): return True
    def help_quit(self): print(bcolors.BOLD+"\n".join(['quit','* Exit'])+bcolors.ENDC)
    def help_help(self): print(bcolors.BOLD+"\n".join(['help','* Available commands with "help" or detailed help with "help <topic>".'])+bcolors.ENDC)

    """ undocumented commands: don't show when hide_undoc = 1 """
    def do_exit(self, line): return True
    def do_EOF(self, line): return True

    ##OVERWRITES##
    def postloop(self): print(bcolors.HEADER+'\n\nThank you and goodbye ...'+bcolors.ENDC)

if __name__ == '__main__':
    shell().cmdloop()
