# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import sys

sys.path.append(".")
import pathlib
#parsar stuff
import PLYJ.model as m
from PLYJ.parser import Parser





## To save time change initialdir to a directory with a java file.
class myParser2():
    def __init__(self) -> None:
        self.output = []
        self.timeStamp = 0
        self.hash = 0
        self.filesize = None
        self.filePath = ""
        
        
        
        #function calls
        self.functionCalls = 0
        
        self.blankLines = 0
        #sloc =source lines of code
        self.SLOC = 0
        self.SLOCnoComm = 0
        self.SLOCwiComm = 0
        self.fullCommentLines = 0
        self.NumSemiColons = 0
        self.actualFilePath = ""
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
        self.currNestingLevel = 0
        self.ESLOCatMaxLevel = 0
        self.SwitchComplexity = 0

        ##
        self.localizationDict = {}

        ##Count loops:
        self.numForLoops = 0
        self.numWhileLoops = 0
        self.numDoWhileLoops = 0

        #count Variables
        self.numInt = 0
        self.numFloat = 0
        self.numChar = 0
        self.numString = 0
        self.numUserDefined = 0
        self.numArrays = 0

        self.testingVariable = 0
    # Check if there is a commented line (SLOC Metric)
    def checkNumOfComments(self):
        self.SLOC = len(self.rawCodeList)
        j = 0
        x = 0
        for lineno in range(0,self.SLOC):
            stripLine = self.rawCodeList[lineno].strip()
            if(stripLine.startswith('/*')):
                if(not stripLine.endswith('*/')):
                    while( not stripLine.endswith('*/')):
                        x += 1
                        lineno += 1
                        stripLine = self.rawCodeList[lineno].strip()
                x += 1
            elif(stripLine.startswith('//')):
                x = x + 1 
            elif len(stripLine) is 0:
                self.blankLines += 1 
        
        self.fullCommentLines = x
        




    def getData(self):
        return self.output

    
    ## This function should be used when starting the
    def findMetrics(self, filepath: str):
        self.actFilePath = filepath
        print(filepath)
        filepathL = filepath.split('/')
        numDir=len(filepathL)
        self.filePath= '.../'+ filepathL[numDir-2] +'/'+ filepathL[numDir-1]
        
        ##creates the rawsource code
        self.createCodeStringList(filepath)
        self.checkNumOfComments()
        self.parseThisFile()
        #generates the output
        self.genOutput()
    #this generates a list that contains all the metrics
    def genOutput(self):
        self.output.append(self.filePath)
        self.output.append(self.timeStamp)
        self.output.append(self.SLOC)
        self.output.append(self.SLOCnoComm)
        self.output.append(self.SLOCwiComm)
        self.output.append(self.blankLines)
        self.output.append(self.fullCommentLines)
        self.output.append(self.NumSemiColons)
        self.output.append(self.functionCalls)
        self.output.append(self.numPassParams)
        self.output.append(self.calcMcCabe())
        self.output.append(self.halstead)
        self.output.append(self.maxNestingLevel)
        self.output.append(self.ESLOCatMaxLevel)
        self.output.append(self.SwitchComplexity)
        self.output.append(self.numForLoops)
        self.output.append(self.numWhileLoops)
        self.output.append(self.numDoWhileLoops)
        return 0
        



    ## Creates the raw source code in list format.
    def createCodeStringList(self, filePath)->bool:
            
            file = open(filePath, 'r')
            self.rawCodeList = file.readlines()
            
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
            self.currNestingLevel += 1
            if sourceElement.if_false is None:
                
                self.edge-=1
            else:
                self.currNestingLevel -= 1
                if type(sourceElement.if_false is m.For):
                    self.testingVariable += 1
                self.calMetric(sourceElement.if_false)
                
        elif type(sourceElement) is m.While:
            ## Count the while loops here
            self.currNestingLevel += 1
            self.node +=2
            self.edge +=3
            ## count the while
            self.numWhileLoops += 1
            for line in sourceElement.body:
                self.calMetric(line)
        elif(type(sourceElement) is m.For):
            self.currNestingLevel += 1 
            self.node += 2
            self.edge +=3

            self.numForLoops += 1
           
            self.calMetric(sourceElement.body)
            

        elif(type(sourceElement)is m.DoWhile):
            self.currNestingLevel += 1
            self.node += 2
            self.edge += 3

            self.numDoWhileLoops += 1
            self.calMetric(sourceElement.body)
            
        elif type(sourceElement) is m.Switch:
            numSwitches = len(sourceElement.switch_cases)
            self.edge += 2* numSwitches

            for switch in sourceElement.switch_cases:
                for line in switch.body:
                    self.calMetric(line)

        elif type(sourceElement) is m.VariableDeclaration:
            self.node += 1
            ##Get the names of the variables that are within if, for while or switch statements
            
            for var_decl in sourceElement.variable_declarators:
                    if type(sourceElement.type) is str:
                        type_name = sourceElement.type
                    else:
                        type_name = sourceElement.type.name.value
                    self.variableCounter(type_name)
        elif type(sourceElement) is m.Break or type(sourceElement) is m.Return:
            pass

        elif type(sourceElement) is m.Block:

            for line in sourceElement.statements:
                if(type(line) is m.For):
                    self.testingVariable +=1
                self.calMetric(line)
###############################################################
    #counts the variables 
    def variableCounter(self,type):
        if(type =='String'):
            self.numString += 1
        elif(type == 'int'):
            self.numInt += 1
        elif(type == "char"):
            self.numChar +=1
        elif(type =="Array"):
            self.numArrays += 1
        else:
            self.numUserDefined +=1

        return


    def parseThisFile(self):

        # Change label contents

        p = Parser()
        tree = p.parse_file(self.actFilePath)

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
                    #count the params
                    self.numPassParams +=1
                    if type(param.type) is str:
                        param_strings.append(param.type + ' ' + param.variable.name)
                    else:
                        param_strings.append(param.type.name.value + ' ' + param.variable.name)
                print('    ' + method_decl.name + '(' + ', '.join(param_strings) + ')')

                if method_decl.body is not None:
                    for statement in method_decl.body:
                        if type(statement) is m.VariableDeclaration:
                            for var_decl in statement.variable_declarators:

                                
                                if type(statement.type) is str:
                                    type_name = statement.type
                                else:
                                    ##This is where it's an array type
                                    dim = statement.type.dimensions
                                    
                                    type_name = str(statement.type.name)
                                    if(dim > 0):
                                        type_name = "Array"
                                    
                                self.variableCounter(type_name)
                                print('        ' + type_name + ' ' + var_decl.variable.name)
                        #TODO Must add a elif statement for function statement.. very important for counting functions
                        else:
                            self.currNestingLevel = 0
                            self.calMetric(statement)
                            if self.currNestingLevel > self.maxNestingLevel:
                                self.maxNestingLevel = self.currNestingLevel

if __name__ == '__main__':
        fn = "C:\\Users\\Jonathan Lewis\\Documents\\GitHub\\SourceCodeChecker\\plyj-master\\JavaTest\\Personal_Income_Tax.java"
        
        """   p = Parser()
        tree = p.parse_file(fn)
        print(tree) """
        mp = myParser2()
        mp.findMetrics(fn)
        
        print(mp.numForLoops)
        


