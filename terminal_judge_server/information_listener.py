import zerorpc
import os
import shutil
import subprocess
import shlex
from config import PATH


class InformationListener(object):
    """Information Listener"""
    def __init__(self):
        if not os.path.exists(PATH):
            os.mkdir(PATH)

    def judge(self, id, cmd, expection):
        return self.__judge(id, cmd, expection)

    def __judge(self, id, cmd, expection):
        self.working_dir = os.path.join(PATH, id)
        if not os.path.exists(self.working_dir):
            os.mkdir(self.working_dir)
        self.__backup(id)

        # exec
        self.user_input = cmd
        self.user_result = self.__exec(cmd)

        # self.__get_structure()

        code = compile(expection, '<string>', 'exec')
        exec(code, {'user_result': self.user_result,
                    'user_input': self.user_input})
        return {'success': True,
                'output': self.user_result
                }

    def __backup(self, id):
        self.backup_dir = os.path.join(PATH, ".%s" % id)
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)
        shutil.copytree(self.working_dir, self.backup_dir)

    def __exec(self, command):
        return subprocess.check_output(shlex.split(command),
                                       cwd=self.working_dir)

    def __restore(self):
        shutil.rmtree(self.working_dir)
        shutil.copytree(self.backup_dir, self.working_dir)
        shutil.rmtree(self.backup_dir)

    def __get_structure(self):
        structure = {}
        for root, dirs, files in os.walk(self.working_dir):
            structure[root] = {}
            structure[root]['files'] = [os.path.join(root, name) for name in files]
            structure[root]['dirs'] = [os.path.join(root, name) for name in dirs]
        print structure


def main():
    s = zerorpc.Server(InformationListener())
    s.bind("tcp://0.0.0.0:4242")
    s.run()


if __name__ == '__main__':
    main()
