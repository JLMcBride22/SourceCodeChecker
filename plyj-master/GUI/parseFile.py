# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import sys

sys.path.append(".")
import os
import PLYJ.model as m
from PLYJ.parser import Parser
from PyQt5.QtSql import QSqlRecord, QSqlTableModel


#this holds the metrics of the file
# Such metrics include the list of classes, imports 
class ARIfile():
    def __init__(self) -> None:
        self.numLines = 0 
    
    def setNumLines(self, numLines: int):
        self.numLines = numLines

## To save time change initialdir to a directory with a java file.
class myParser2():
    def __init__(self) -> None:
        self.output = []
        self.date = 0
        self.hash = 0
        self.filesize = None
        self.filePath = ""
        self.record = QSqlRecord()
        self.record.setGenerated('tableid', False)
        self.dbModel = QSqlTableModel()
        
        self.blankLines = 0
        #sloc =source lines of code
        self.SLOC = 0
        self.SLOCnoComm = 0
        self.SLOCwiComm = 0
        self.fullCommentLines = 0
        self.NumSemiColons = 0
        
        #CodeComplexity
        self.numPassParams = 0
        self.mccabe =0
        ##The following is used for mcCabe Calc
        self.node = 2
        self.edge = 0
        self.P = 2
        ################################
        self.halstead = 0
        self.maxNestingLevel = 0
        self.ESLOCatMaxLevel = 0
        self.SwitchComplexity = 0

        ##
        self.localizationDict = {}

        ##Count loops:
        self.numForLoops = 0
        self.numWhileLoops = 0
        self.numDoWhileLoops = 0

    def getData(self):
        return self.output

    
    ## This function should be used when starting the
    def findMetrics(self, filepath: str):
        filepathL = filepath.split('/')
        numDir=len(filepathL)
        self.filePath = './'+ filepathL[numDir-2] +'/'+ filepathL[numDir-1]
        self.output.append(self.filePath)
        self.record.setValue(1,filepath)

        self.createCodeStringList(filepath)
        self.parseThisFile()

        ##self.dbModel.insertRecord(-1,self.record)

    def getRecord(self)->QSqlRecord:
        return self.record

    ## Creates the raw source code in list format.
    def createCodeStringList(self, filePath)->bool:
            
            file = open(filePath, 'r')
            self.rawCodeList = file.read()
            file.close()
            return True
    
    def calcMcCabe(self):
        out = self.edge - self.node  + 2

        return out
    
    def calMetric(self, sourceElement):
        
        if(type(sourceElement) is m.IfThenElse):
            self.node +=2
            self.edge += 4
            
            self.calMetric(sourceElement.if_true)
            
            if sourceElement.if_false is None:
                self.edge-=1
            
            else:
                self.calMetric(sourceElement.if_false)
        elif type(sourceElement) is m.While:
            ## Count the while loops here
            self.node +=2
            self.edge +=3
            ## count the while
            for line in sourceElement.body:
                self.calMetric(line)
        elif(type(sourceElement) is m.For):
            ## count the for loops 
            self.node += 2
            self.edge +=3
            
        elif type(sourceElement) is m.Switch:
            numSwitches = len(sourceElement.switch_cases)
            self.edge += 2* numSwitches

            for switch in sourceElement.switch_cases:
                for line in switch.body:
                    self.calMetric(line)

        elif type(sourceElement) is m.VariableDeclaration:
            self.node += 1
            ##Get the names of the variables that are within if, for while or switch statements
        elif type(sourceElement) is m.Break or type(sourceElement) is m.Return:
            pass

        else:
            self.node+=1

            



    def parseThisFile(self):

        # Change label contents

        p = Parser()
        tree = p.parse_string(self.rawCodeList)

        print('declared types:')
        for type_decl in tree.type_declarations:
            print(type_decl.name)
            if type_decl.extends is not None:
                print(' -> extending ' + type_decl.extends.name.value)
            if len(type_decl.implements) is not 0:
                print(' -> implementing ' + ', '.join([type.name.value for type in type_decl.implements]))
            print

            print('fields:')
            for field_decl in [decl for decl in type_decl.body if type(decl) is m.FieldDeclaration]:
                for var_decl in field_decl.variable_declarators:
                    if type(field_decl.type) is str:
                        type_name = field_decl.type
                    else:
                        type_name = field_decl.type.name.value
                    print('    ' + type_name + ' ' + var_decl.variable.name)

            print
            print('methods:')
            for method_decl in [decl for decl in type_decl.body if type(decl) is m.MethodDeclaration]:
                param_strings = []
                for param in method_decl.parameters:
                    if type(param.type) is str:
                        param_strings.append(param.type + ' ' + param.variable.name)
                    else:
                        param_strings.append(param.type.name.value + ' ' + param.variable.name)
                print('    ' + method_decl.name + '(' + ', '.join(param_strings) + ')')

                if method_decl.body is not None:
                    for statement in method_decl.body:
                        # note that this misses variables in inner blocks such as for loops
                        # see symbols_visitor.py for a better way of handling this
                        if type(statement) is m.VariableDeclaration:
                            for var_decl in statement.variable_declarators:

                                
                                if type(statement.type) is str:
                                    type_name = statement.type
                                else:
                                    ##This is where it's an array type
                                    dim = statement.type.dimensions
                                    brackets= "[]"
                                    
                                    type_name = str(statement.type.name)
                                    for i in range(0,dim):
                                        type_name = type_name + brackets
                                    
                                    
                                print('        ' + type_name + ' ' + var_decl.variable.name)

                        else:
                            self.calMetric(statement)

if __name__ == '__main__':
        fn ="JavaTest\\Personal_Income_Tax.java"
        
        """   p = Parser()
        tree = p.parse_file(fn)
        print(tree) """
        mp = myParser2()
        mp.parseThisFile(fn)
        out = mp.calcMcCabe()
        print(out)
        


