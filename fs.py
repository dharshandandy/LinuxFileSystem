class FSNode():
    def __init__(self, name):
        self.name = name

class FileNode(FSNode):
    def __init__(self,name, mode = 'rw', content=''):
        super().__init__(name)
        self.mode = mode
        if('w' in self.mode):
            self.content = content
        else:
            self.content = None

    def changeMode(self, newmode):
        self.mode = newmode

    def changeContent(self, newContent):
        if 'w' in self.mode:
            self.content = newContent
        else:
            print("This File has only Read Permission")

    def getContentOfFile(self):
        return self.content;
    def renameFile(self, newname):
        self.name = newname

class FolderNode(FSNode):
    def __init__(self, name):
        super().__init__(name)
        self.childs = {}

    def __str__(self):
        return f'{self.name}'
    
    def getDirName(self):
        return self.name


    def isNameExists(self, newname):
        if newname in self.childs:
            return True
        return False
    def addFile(self, filename):
        if self.isNameExists(filename+'f'):
            print(f"Sorry '{filename}' Name is Already Exists")
        else:
            self.childs[filename+'f'] = FileNode(filename)

    def addFolder(self, foldername):
        if self.isNameExists(foldername+'d'):
            print("Sorry '{filename}' Name is Already Exists")
        else:
            self.childs[foldername+'d'] = FolderNode(foldername)

    def removeFile(self, filename):
        if self.isNameExists(filename+'f'):
            self.childs.pop(filename+'f')
            print(f'{filename} File Removed.')
        else:
            print(f"No '{filename}' Exists in current Folder")

    def removeFolder(self, foldername):
        if self.isNameExists(foldername+'d'):
            self.childs.pop(foldername+'d')
            print(f'{foldername} Folder Removed.')
        else:
            print(f"No '{foldername}' Exists in current Folder")

    def renameFile(self, oldfilename, newfilename):
        if self.isNameExists(oldfilename+'d'):
            self.childs[newfilename+'f'] = self.childs.pop(oldfilename+'f')
            print(f'{oldfilename} File Renamed => {newfilename}.')
        else:
            print(f"No '{oldfilename}' File Exists in current Folder")

    def renameFolder(self, oldfoldername, newfoldername):
        if self.isNameExists(oldfoldername+'d'):
            self.childs[newfoldername+'d'] = self.childs.pop(oldfoldername+'d')
            print(f'{oldfoldername} Folder Renamed => {newfoldername}.')
        else:
            print(f"No '{oldfoldername}' Folder Exists in current Folder")

    def listChilds(self):
        return self.childs.keys()

    def getChild(self,childName):
        if self.isNameExists(childName):
            return self.childs[childName]
        else: 
            print('Sorry Internal File System Error')


class FileSystem():
    def __init__(self):
        self.root = FolderNode('/')
        self.currentDir = [self.root]

    def getCurrentDirName(self):
        return self.currentDir[-1].name

    def createFile(self, filename):
        if self.currentDir[-1].isNameExists(filename+'f'):
            print('Sorry Not Available')
        else:
            self.currentDir[-1].addFile(filename)

    def mkdir(self,foldername):
        # print(self.getWay(self.currentDir, foldername)[1][-1])
        tempStackDir = self.currentDir
        if '/' == foldername[0]:
            tempStackDir = [tempStackDir[0]]
            foldername = foldername[1:]
        dirslist = foldername.split('/')
        isAlreadyExists = 0
        for item in dirslist:
            isThere = self.getWay(tempStackDir, item)
            if isThere[0]:
                tempStackDir = isThere[1]
            else:
                isAlreadyExists = 1
                tempStackDir = isThere[1]
                tempStackDir[-1].addFolder(item)
                tempStackDir.append(tempStackDir[-1].getChild(item+'d'))

        if not isAlreadyExists:
            print(f'mkdir: cannot create directory ‘{foldername}’: File exists')


    def getWay(self, sourcePath, pathway):
        copyDirStack = sourcePath.copy()
        pathtoDir = pathway.split('/')
        if '/' == pathway[0]:
            pathtoDir.pop(0)
            copyDirStack = [copyDirStack[0]]
        
        for dirs in pathtoDir:
                if dirs == '..':
                    if len(copyDirStack) != 1:
                        copyDirStack.pop()
                    continue 
                if copyDirStack[-1].isNameExists(dirs+'d'):
                    copyDirStack.append(copyDirStack[-1].getChild(dirs+'d'))
                else:
                    return (False,copyDirStack)
        return (True, copyDirStack)

    

    def cd(self,dirway):
        path = self.getWay(self.currentDir,dirway)
        if path[0]:
            self.currentDir = path[1]
        else:
            print(f"cd: {dirway}: No such directory")


    def ls(self):
        for item in self.currentDir[-1].listChilds():
            if item[-1] == 'f':
                print (item[:-1], end='  ')
            else:
                print (item[:-1]+'/', end = '  ')
        print()
    
    def rm(self, filename):
        if self.currentDir[-1].isNameExists(filename+'f'):
           self.currentDir[-1].removeFile(filename) 
        else:
            print(f"rm: {filename}: No such file")

    def rmdir(self, foldername):
        if self.currentDir[-1].isNameExists(foldername+'d'):
            self.currentDir[-1].removeFolder(foldername)
        else:
            print(f"rmdir: {foldername}: No such directory")
    
    def pwd(self):
        for item in self.currentDir:
            if item.getDirName() == '/':
                print('/',end='')
            else:
                print(item.getDirName(), end='/')
        print()

    def modifyContent(self, filename):
        if self.currentDir[-1].isNameExists(filename+'f'):
            file = self.currentDir[-1].getChild(filename+'f')
            try:
                content = input("");
                file.changeContent(content);
            except KeyboardInterrupt as Cancel:
                pass
            del file
        else:
            print(f'{filename}: No such file.')
    def cat(self,filename):
        if self.currentDir[-1].isNameExists(filename+'f'):
            file = self.currentDir[-1].getChild(filename+'f')
            print(file.getContentOfFile())
            del file
        else:
            print(f'{filename}: No such file.')


fs = FileSystem()

def option():
    print(' vi -> write Content \n cat -> view Content \n ls -> list content \n touch -> create file \n rm -> remove file \n mkdir -> create folder \n rmdir -> remove folder \n cd -> change directory \n help -> see available option \n pwd -> present working Directory \n Enter Your Choice: ')

option()

while(1):
    choice = input(f'[{fs.getCurrentDirName()}] $ ').split()
    if len(choice) == 0:
        continue
    if choice[0] == 'ls':
        fs.ls()
    elif choice[0] == 'help':
        option()
    elif choice[0] == 'pwd':
        fs.pwd()
    elif len(choice) > 1:
        if choice[0] == 'touch':
            fs.createFile(choice[1])
        elif choice[0] == 'mkdir':
            fs.mkdir(choice[1])
        elif choice[0] == 'cd':
	        fs.cd(choice[1])
        elif choice[0] == 'rm':
            fs.rm(choice[1])
        elif choice[0] == 'rmdir':
            fs.rmdir(choice[1])
        elif choice[0] == 'vi':
            fs.modifyContent(choice[1])
        elif choice[0] == 'cat':
            fs.cat(choice[1])

    elif choice[0] in ['ls','touch','mkdir','cd','cat','vi','rm','rmdir']:
        print(f'{choice[0]}: missing operand..')
    else:
        print(f"{choice[0]}: command not found..")


