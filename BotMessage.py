class BotMessage(object):

    @staticmethod
    def StartMessage():
        message = 'HellO!!!\n This bot help you use your compyter with telegram :)' \
                  '\n To check commands use /help'
        return message

    @staticmethod
    def HelpMessage():
        message = "[cd \\] to first directory\n" \
                  "[cd ..] to Parent directory\n" \
                  "[cd FULLPATH]\n" \
                  "[cd CHILDIRNAME]\n" \
                  '[ls] show all files and directories in current directory\n' \
                  "[mkdir DIRNAME] Create directory in current directory with name = DIRNAME\n" \
                  "[rmdir [full] or [dir]] full delete with all component\n"

        return message


