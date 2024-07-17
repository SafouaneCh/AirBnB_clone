#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line input."""
        pass

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help <cmd>'."""
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            cmds = [name[3:] for name in names if name[:3] == 'do_']
            self.stdout.write("Documented commands (type help <topic>):\n")
            self.print_topics(self.doc_leader, cmds, 15, 80)
