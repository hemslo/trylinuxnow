import zerorpc
import os
import shutil
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
        # backup
        self.__backup(id)
        # exec
        # validate
        # continue or restore
        return True

    def __backup(self, id):
        self.backup_dir = os.path.join(PATH, ".%s" % id)
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)
        shutil.copytree(self.working_dir, self.backup_dir)


def main():
    s = zerorpc.Server(InformationListener())
    s.bind("tcp://0.0.0.0:4242")
    s.run()


if __name__ == '__main__':
    main()
