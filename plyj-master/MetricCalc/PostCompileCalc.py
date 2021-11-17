
# a file explorer in Tkinter

# import all components
# from the tkinter library
import sys
from xml.etree.ElementTree import SubElement, tostring

sys.path.append(".")
import os
from pathlib import Path
import datetime
#parsar stuff
import PLYJ.model as m
from PLYJ.parser import Parser
from datetime import datetime
import xml.etree.ElementTree as xml2
from xml.etree import ElementTree







## To save time change initialdir to a directory with a java file.
class myParser2():
    
    def __init__(self) -> None:
        self.listOfMetrics = []
        self.output = []
        self.timeStamp = 0
        self.hash = 0
        self.filesize = None
        self.filePath = ""
        self.root = xml2.Element("File")
        self.strXML =""
        self.dataSize = ""
        self.currMethodName = ""
        
        #function calls
        self.functionCalls = 0
        
        self.blankLines = 0
        #sloc =source lines of code
        self.SLOC = 0
        self.SLOCnoComm = 0
        self.SLOCwiComm = 0
        self.fullCommentLines = 0
        self.numSemiColons = 0
        self.actualFilePath = ""
        #CodeComplexity
        self.numPassParams = 0
        self.mccabe =0
        ##The following is used for mcCabe Calc
        self.node = 0
        self.edge = 0
        self.P = 0
        self.methodMcCabe = 0
        self.classMcCabe = 0
        ################################
        self.halstead = 0
        self.maxNestingLevel = 0
        self.currNestingLevel = 0
        self.ESLOCatMaxLevel = 0
        self.SwitchComplexity = 0
        self.MethodVarList = []

        

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
        self.Num3Char =0
        self.Num3thru9Char =0
        self.Num10thru19Char =0
        self.Num20Char = 0
        self.PreambleFilename = ""
        self.PreambleAuthor = ""
        self.PreamblePurpose = ""
        self.PreambleInterface = ""
        self.PreambleAssumptions = ""
        self.PreambleChangeLog = ""
        self.NoGoTo = ""
        self.OneEntry = ""
        self.OneExit = ""
        self.RecursionStatus = ""
        self.VariableNamesAtLeastXChar =""
        self.VariableNamesNoLongXChar = ""
        self.DefineParamAllCAPS =""
        self.VarNamesNotAllCAPS = ""
        self.McCabeLessThanX =""
        self.NestingLessThanX =""
        self.ESLOCLessThanXinFunc = ""
        self.LocalizationOfVar = "" 
      
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
                        try:
                            stripLine = self.rawCodeList[lineno].strip()
                        except IndexError:
                            print(self.actFilePath)
                            break
                x += 1
            elif(stripLine.startswith('//')):
                x = x + 1 
            elif len(stripLine) is 0:
                self.blankLines += 1
            else:
                if(';' in stripLine):
                    self.numSemiColons += 1
        
        self.fullCommentLines = x
        
            
            



    #Calc the stats of the file like timestamp and filesize in KB
    def calcFileStats(self):
        p = Path(self.actFilePath)
        stats = p.stat()
        time = stats.st_mtime
        self.timeStamp = datetime.fromtimestamp(time).strftime('%c')
        self.dataSize = str(float(stats.st_size)/1000) + " kB"
        
        

##################################precompiled class######################################

    def getData(self):
        return self.output

    
    ## This function should be used when starting the calculation process.
    def findMetrics(self, filepath: str, listOfMetrics:list):
        self.listOfMetrics = listOfMetrics
        self.actFilePath = filepath
        print(filepath)
        filepathL = filepath.split('/')
        numDir=len(filepathL)
        self.filePath= '.../'+ filepathL[numDir-2] +'/'+ filepathL[numDir-1]
        
        ##creates the rawsource code
        self.createCodeStringList(filepath)
        self.checkNumOfComments()
        self.compileThisFile()
        self.createXMLString()
        #generates the output
        self.calcFileStats()
        self.genOutput()
    ##Creates the xml string.
    def createXMLString(self):
        self.strXML = xml2.tostring(self.root, 'unicode')
        return 0


 
    #this generates a list that contains all the metrics. This should be move to calc interface.
    def genOutput(self):
        self.output.append(self.filePath)#1
        self.output.append(self.timeStamp)
        self.output.append(self.dataSize)
        now = datetime.now()
        self.output.append(now.strftime("%c"))#5
        self.output.append(self.SLOC)
        self.output.append(self.SLOCnoComm)
        self.output.append(self.SLOCwiComm)
        self.output.append(self.blankLines)
        self.output.append(self.fullCommentLines)#10
        self.output.append(self.numSemiColons)
        self.output.append(self.functionCalls)
        self.output.append(self.numPassParams)
        self.output.append(self.calcMcCabe())
        self.output.append(self.halstead)#15
        self.output.append(self.maxNestingLevel)
        self.output.append(self.ESLOCatMaxLevel)
        self.output.append(self.SwitchComplexity)
        self.output.append(self.numForLoops)
        self.output.append(self.numWhileLoops)#20
        self.output.append(self.numDoWhileLoops)
        self.output.append(self.numInt)
        self.output.append(self.numFloat)
        self.output.append(self.numChar)
        self.output.append(self.numString)#25
        self.output.append(self.numUserDefined)
        self.output.append(0)#<----------NO STRUCTS
        self.output.append(self.numArrays)
        self.output.append(self.Num3Char)
        self.output.append(self.Num3thru9Char)#30
        self.output.append(self.Num10thru19Char)
        self.output.append(self.Num20Char)
        self.output.append(self.PreambleFilename)
        self.output.append(self.PreambleAuthor)
        self.output.append(self.PreamblePurpose)#35
        self.output.append(self.PreambleInterface)
        self.output.append(self.PreambleAssumptions)
        self.output.append(self.PreambleChangeLog)
        self.output.append(self.NoGoTo)
        self.output.append(self.OneEntry)#40
        self.output.append(self.OneExit)
        self.output.append(self.RecursionStatus)
        self.output.append(self.VariableNamesAtLeastXChar)
        self.output.append(self.VariableNamesNoLongXChar)
        self.output.append(self.DefineParamAllCAPS)#45
        self.output.append(self.VarNamesNotAllCAPS)
        self.output.append(self.McCabeLessThanX)
        self.output.append(self.NestingLessThanX)
        self.output.append(self.ESLOCLessThanXinFunc)
        self.output.append(self.strXML)#50

        
        return 0  
        



    ## Creates the raw source code in list format.
    def createCodeStringList(self, filePath)->bool:
            
            file = open(filePath, 'r')
            self.rawCodeList = file.readlines()
            file.close()

            return True
    
    def calcMcCabe(self):
        out = self.edge - self.node  + 2*self.P

        return out
    
    ##Calculate metric
    def calMetric(self, sourceElement):
        
        if(type(sourceElement) is m.IfThenElse):

            self.methodMcCabe += 1
            self.calMetric(sourceElement.if_true)
            
            
            if(sourceElement.if_false is not None):
               self.calMetric(sourceElement.if_false)
                
        elif type(sourceElement) is m.While:
            ## Count the while loops here
            
            self.methodMcCabe += 1
            ## count the while
            self.numWhileLoops += 1
            self.calMetric(sourceElement.body)
        elif(type(sourceElement) is m.For):
            
            self.methodMcCabe +=1       

            self.numForLoops += 1
           
            self.calMetric(sourceElement.body)
            

        elif(type(sourceElement)is m.DoWhile):
            
            self.methodMcCabe +=1

            self.numDoWhileLoops += 1
            self.calMetric(sourceElement.body)
            
        elif type(sourceElement) is m.Switch:
            self.methodMcCabe += len(sourceElement.switch_cases)
            

            for switch in sourceElement.switch_cases:
                for line in switch.body:
                    self.calMetric(line)

        elif type(sourceElement) is m.VariableDeclaration:

                        
            for var_decl in sourceElement.variable_declarators:

                    
                if type(sourceElement.type) is str:
                    type_name = sourceElement.type
                    self.variableCounter(type_name)
                else:
                    
                    dim = sourceElement.type.dimensions
                    
                    
                    ##IF ITs an array.
                    if(dim > 0):
                        type_name = "Array"
                        self.variableCounter(type_name)
                        try:
                            type_name = str(sourceElement.type.name.value)
                        except AttributeError:
                            type_name = str(sourceElement.type.name)

                        for b in range(0,dim):
                            type_name = type_name + '[]'

                    else:
                        type_name = sourceElement.type.name.value
                        self.variableCounter(type_name)
                        
            
                self.MethodVarList.append (type_name + ' ' + var_decl.variable.name)
            
        elif type(sourceElement) is m.ExpressionStatement:
            if type(sourceElement.expression) is m.MethodInvocation:
                # Count Function.
                self.functionCalls += 1
                if(self.currMethodName == sourceElement.expression.name):
                    sourceElement.expression.arguments





        elif type(sourceElement) is m.Break or type(sourceElement) is m.Return:
            pass

        elif type(sourceElement) is m.Block:

            for line in sourceElement.statements:
                self.calMetric(line)

        elif type(sourceElement) is list:

            for block in sourceElement:
                self.calMetric(block)

        elif sourceElement._fields.__contains__("body"):
            self.calMetric(sourceElement.body)

        elif sourceElement._fields.__contains__("block"):
            self.calMetric(sourceElement.block)

    #This creates a xmlElement for method measurements.
    def createsMethodXMLElement(self):
        output = xml2.Element("Measurements")
        for metric in self.listOfMetrics:
            measurement = xml2.Element("Measurement")
            measurement.text = metric
            if metric == "Source Lines of Code with Comments":
                pass
            elif metric == "Number of Semicolons":
                pass
            elif metric == "Source Lines of Code without Comments":
                pass
            elif metric == "Number of Function Calls":
                pass
            elif metric == "Blank Lines":
                pass
            elif metric == "Full Comment Lines":
                pass
            elif metric == "Number of Passed Parameters":
                pass
            elif metric == "Switch Complexity":
                pass
            elif metric == "McCabe's Cyclomatic Complexity":
                measurement.text = metric + "   "+ str(self.methodMcCabe)
            elif metric == "Maximum Nesting Level":
                pass
            elif metric == "ESLOC at Max Nesting Level":
                pass
            elif metric == "Halstead's Software Science Primitives":
                pass
            elif metric == "Number of For Loops":
                pass
            elif metric == "Number of While Loops":
                pass
            elif metric == "Number of Do-While Loops":
                pass
            elif metric == "User Defined Variable":
                pass
            elif metric == "Total Number of Variables":
                pass
            elif metric == "Float":
                pass
            elif metric == "Array":
                pass
            elif metric == "Integer":
                pass
            elif metric == "String":
                pass
            elif metric == "Character":
                pass
            elif metric == "Structure":
                pass
            elif metric == "Names Less Than 3 Characters":
                pass
            elif metric == "Names 20 or More Characters":
                pass
            elif metric == "Names More Than 3 but Less Than 10 Characters":
                pass
            elif metric == "Names 10 or More but Less than 20 Characters":
                pass
            elif metric == "Assumptions":
                pass
            elif metric == "Purpose":
                pass
            elif metric == "Filename":
                pass
            elif metric == "Change Log":
                pass
            elif metric == "Interface":
                pass
            elif metric == "Author":
                pass
            elif metric == "Presence of GoTo's":
                pass
            elif metric == "Singular Entry Point":
                pass
            elif metric == "Singular Exit Point":
                pass
            elif metric == "Presence of Recursion":
                pass
            elif metric == "All Variable Names at Least X Characters Long":
                pass
            elif metric == "All Variable Names Not Longer than X Characters":
                pass
            elif metric == "All #define Parameters in All Capitals":
                pass
            elif metric == "No Variable Names in All Capitals":
                pass
            elif metric == "McCabe's Cyclomatic Complexity Less Than X":
                pass
            elif metric == "Maximum Nesting Level Less Than X":
                pass
            elif metric == "Localization of Variables":
                pass
            elif metric == "ESLOC Less Than X Within Functions":
                pass
            output.append(measurement)
        return output
    #resets the method stats
    def resetMethodVariables(self):
        self.methodMcCabe = 0
        self.MethodVarList = []
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
        elif(type =="float"):
            self.numFloat += 1
        elif type == "byte" or type == "double" or type == "boolean" or type == "short" or type == "long":
            return
    
        else:
            self.numUserDefined +=1

        return

    #This Compiles the file and calculates metrics like McCabe
    def compileThisFile(self):

        # Change label contents

        p = Parser()
        
        
        
        
        
        tree = p.parse_file(self.actFilePath)
        


        classesElement = xml2.Element("Classes")
        self.root.append(classesElement)
        for type_decl in tree.type_declarations:
            ### This is where I'll get the class names
            classElement = xml2.Element(type_decl.name)
            
            
            classesElement.append(classElement)
            


            fieldElement = xml2.Element("Field")
            classElement.append(fieldElement)
            for field_decl in [decl for decl in type_decl.body if type(decl) is m.FieldDeclaration]:
                for var_decl in field_decl.variable_declarators:

                    if type(field_decl.type) is str:
                        type_name = field_decl.type
                    else:
                        type_name = field_decl.type.name.value
                    field = xml2.SubElement(fieldElement, "field")
                    field.text = type_name + ' ' + var_decl.variable.name




            
            methodsElement = xml2.Element("Methods")
            classElement.append(methodsElement)
            
            for method_decl in [decl for decl in type_decl.body if type(decl) is m.MethodDeclaration]:
                method = xml2.Element(method_decl.name)
                methodsElement.append(method)
                param_strings = []
                parametersElement = xml2.Element("Parameters")
                method.append(parametersElement)
                for param in method_decl.parameters:
                    #count the params
                    self.numPassParams +=1
                    
                    parameterSE = xml2.SubElement(parametersElement,"parameter")
                    #TODO test arrays work as parameters
                    if type(param.type) is str:
                        param_strings.append(param.type + ' ' + param.variable.name)

                        
                        parameterSE.text = param.type + ' ' + param.variable.name
                    else:
                        param_strings.append(param.type.name.value + ' ' + param.variable.name)
                        
                        parameterSE.text = param.type.name.value + ' ' + param.variable.name
                        

                print('    ' + method_decl.name + '(' + ', '.join(param_strings) + ')')

                
                if method_decl.body is not None:
                    variablesElement = xml2.Element("Variables")
                    self.MethodVarList = []
                    print(type(method_decl.body))


                    ##Reset the node and edge variable for McCabe
                    self.edge = 0
                    self.node = 0
                    self.P = 0
                    self.calMetric(method_decl.body)
                    for var in self.MethodVarList:
                        variableSub = xml2.Element("Variable")
                        variableSub.text = var
                        variablesElement.append(variableSub)
                        
                    method.append(variablesElement)
                    method.append(self.createsMethodXMLElement())

"""     def method(self):
        
        
        for statement in method_decl.body:
            
            
            if type(statement) is m.VariableDeclaration:

                variableSE = xml2.SubElement(variablesElement,"Variable")
                for var_decl in statement.variable_declarators:

                    
                    if type(statement.type) is str:
                        type_name = statement.type
                    else:
                        ##This is where it's an array type
                        dim = statement.type.dimensions
                        
                        type_name = str(statement.type.name)
                        if(dim > 0):
                            type_name = "Array"
                        else:
                            type_name = statement.type.name.value
                        
                    self.variableCounter(type_name)
                    variableSE.text = type_name + ' ' + var_decl.variable.name
            
            else:
                self.currNestingLevel = 0
                self.calMetric(statement, variablesElement)
                if self.currNestingLevel > self.maxNestingLevel:
                    self.maxNestingLevel = self.currNestingLevel """

if __name__ == '__main__':
        fn = "JavaTest\dev.java"
        
        """   p = Parser()
        tree = p.parse_file(fn)
        print(tree) """
        p = myParser2()
        p.actFilePath = fn
        p.calcFileStats()
        #p.genOutput()


