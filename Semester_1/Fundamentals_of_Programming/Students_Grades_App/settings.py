class settings:

    def __init__(self,fileName):
        self._fileName=fileName
        self._readFile()

    def _readFile(self):
        result = []
        try:
            f = open(self._fileName)
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(" ")
                result.append(line)
                line = f.readline().strip()
            f.close()
        except IOError as e:
            print("An error reading the file has occured")
        return result

    def comm(self):
        com=settings._readFile(self)
        if com[0][2]=='inmemory':
            cmd='inmemory'
            return cmd
        elif com[0][2]=='textFiles':
            cmd='textFiles'
            return cmd
        elif com[0][2]=='binary':
            cmd='binary'
            return cmd
        else:
            return 'error'