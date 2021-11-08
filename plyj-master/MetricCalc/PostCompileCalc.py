
# a file explorer in Tkinter

# import all components
# from the tkinter library
import sys
from xml.etree.ElementTree import tostring

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
        self.output = []
        self.timeStamp = 0
        self.hash = 0
        self.filesize = None
        self.filePath = ""
        self.root = xml2.Element("File")
        self.strXML =""
        self.dataSize = ""
        
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
        self.Num3Char =0
        self.Num3thru9Char =0
        self.Num10thru19Char =0
        self.Num20Char = 0
        self.PreambleFilename = ""
        self.PreambleAuthor = 0
        self.PreamblePurpose ="",
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
    ##########################################This will be moved to precompiled file###############################################    
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
            else:
                if(';' in stripLine):
                    self.numSemiColons += 1
        
        self.fullCommentLines = x
        
    def programClarity(self):

        for lineNo in range (0,self.SLOC):
            words = self.rawCodeList[lineNo].split(" ")
            for x in words:
                
                if (len(x) >= self.minCharsLong):
                     self.varsAtleastXCharsLong += 1
                elif (self.maxCharsLong >= x):
                    self.varsNoLongerThanXChars += 1
            





    def getTimeStamp(self):
        p = Path(self.actFilePath)
        stats = p.stat()
        time = stats.st_mtime
        self.timeStamp = datetime.fromtimestamp(time).strftime('%c')
        return self.timeStamp
        

##################################precompiled class######################################

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
        self.compileThisFile()
        self.createXMLString()
        #generates the output
        self.genOutput()
    ##This creates a string of the xml
    def createXMLString(self):
        tree =  ElementTree.ElementTree(self.root)
        f = open("prac.xml",'wb')
        tree.write(f)

        f.close()
        f = open("prac.xml")
        stringXml = f.read()
        self.strXML = stringXml
        print(self.strXML)
        return 0

        
        
        """ id integer PRIMARY KEY,
        0 filename text NOT NULL,
        1 timestamp text,
        2 ESLOC integer,
        3 SLOCnoComm integer,
        4 SLOCComm integer,
        5 BlankLines integer,
        6 FullCommLines integer,
        7 Semicolons integer,
        8 FunctionCalls integer,
        9 NumPassedParam integer,
        10 McCabeCyclComp integer,
        11 Halstead integer,
        12 MaxNest integer,
        ESLOCMaxNest integer,
        SwitchComp text,
        NumForLoop integer,
        NumWhileLoop integer,
        NumRepeatLoop integer,
        NumInts integer,
        NumFloat integer,
        NumChar integer,
        NumString integer,
        NumUserDef integer,
        NumStruct integer,
        NumArray integer,
        Num3Char integer,
        Num3thru9Char integer,
        Num10thru19Char integer,
        Num20Char integer,
        PreambleFilename text,
        PreambleAuthor text,
        PreamblePurpose text,
        PreambleInterface text,
        PreambleAssumptions text,
        PreambleChangeLog text,
        NoGoTo text,
        OneEntry text,
        OneExit text,
        RecursionStatus text,
        VariableNamesAtLeastXChar text,
        VariableNamesNoLongXChar text,
        DefineParamAllCAPS text,
        VarNamesNotAllCAPS text,
        McCabeLessThanX text,
        NestingLessThanX text,
        ESLOCLessThanXinFunc text,
        LocalizationOfVar text  
 """
    #this generates a list that contains all the metrics. This should be move to calc interface.
    def genOutput(self):
        self.output.append(self.filePath)
        self.output.append(self.getTimeStamp())
        self.output.append(self.dataSize)
        now = datetime.now()
        self.output.append(now.strftime("%c"))
        self.output.append(self.SLOC)
        self.output.append(self.SLOCnoComm)
        self.output.append(self.SLOCwiComm)
        self.output.append(self.blankLines)
        self.output.append(self.fullCommentLines)
        self.output.append(self.numSemiColons)
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
        self.output.append(self.numInt)
        self.output.append(self.numFloat)
        self.output.append(self.numChar)
        self.output.append(self.numString)
        self.output.append(self.numUserDefined)
        self.output.append(0)#<----------NO STRUCTS
        self.output.append(self.numArrays)
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
    
    ##Calculate metric
    def calMetric(self, sourceElement, variableElement:xml2.Element):
        
        if(type(sourceElement) is m.IfThenElse):
            self.node +=2
            self.edge += 4

            self.calMetric(sourceElement.if_true, variableElement)
            self.currNestingLevel += 1
            if sourceElement.if_false is None:
                
                self.edge-=1
            else:
                self.currNestingLevel -= 1
                if type(sourceElement.if_false is m.For):
                    self.testingVariable += 1
                self.calMetric(sourceElement.if_false, variableElement)
                
        elif type(sourceElement) is m.While:
            ## Count the while loops here
            self.currNestingLevel += 1
            self.node +=2
            self.edge +=3
            ## count the while
            self.numWhileLoops += 1
            for line in sourceElement.body:
                self.calMetric(line, variableElement)
        elif(type(sourceElement) is m.For):
            self.currNestingLevel += 1 
            self.node += 2
            self.edge +=3

            self.numForLoops += 1
           
            self.calMetric(sourceElement.body, variableElement)
            

        elif(type(sourceElement)is m.DoWhile):
            self.currNestingLevel += 1
            self.node += 2
            self.edge += 3

            self.numDoWhileLoops += 1
            self.calMetric(sourceElement.body, variableElement)
            
        elif type(sourceElement) is m.Switch:
            numSwitches = len(sourceElement.switch_cases)
            self.edge += 2* numSwitches

            for switch in sourceElement.switch_cases:
                for line in switch.body:
                    self.calMetric(line, variableElement)

        elif type(sourceElement) is m.VariableDeclaration:
            self.node += 1

                        
            if type(sourceElement.type) is str:
                type_name = sourceElement.type
            else:
                type_name = sourceElement.type.name.value
            self.variableCounter(type_name)

            variableSE = xml2.SubElement(variableElement, "")
            variableSE.text = type_name + ' ' + sourceElement.variable.name


        elif type(sourceElement) is m.Break or type(sourceElement) is m.Return:
            pass

        elif type(sourceElement) is m.Block:

            for line in sourceElement.statements:
                if(type(line) is m.For):
                    self.testingVariable +=1
                self.calMetric(line,variableElement)
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

    #This Compiles the file and calculates
    def compileThisFile(self):

        # Change label contents

        p = Parser()
        tree = p.parse_file(self.actFilePath)

        print('declared types:')
        for type_decl in tree.type_declarations:
            ### This is where I'll get the class names
            classElement = xml2.Element(type_decl.name)
            self.root.append(classElement)
            print(type_decl.name)

            if type_decl.extends is not None:
                print(' -> extending ' + type_decl.extends.name.value)
            if len(type_decl.implements) is not 0:
                print(' -> implementing ' + ', '.join([type.name.value for type in type_decl.implements]))
            print
            ## This where I'll get the fields
            print('fields:')
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



            print
            print('methods:')
            
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
                    
                    parameterSE = xml2.SubElement(parametersElement,"")
                    if type(param.type) is str:
                        param_strings.append(param.type + ' ' + param.variable.name)

                        
                        parameterSE.text = param.type + ' ' + param.variable.name
                    else:
                        param_strings.append(param.type.name.value + ' ' + param.variable.name)
                        
                        parameterSE.text = param.type.name.value + ' ' + param.variable.name

                print('    ' + method_decl.name + '(' + ', '.join(param_strings) + ')')


                if method_decl.body is not None:
                    variablesElement = xml2.Element("Variables")
                    method.append(variablesElement)
                    for statement in method_decl.body:
                        
                        
                        if type(statement) is m.VariableDeclaration:

                            variableSE = xml2.SubElement(variablesElement,"")
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
                                self.maxNestingLevel = self.currNestingLevel

if __name__ == '__main__':
        fn = "JavaTest\dev.java"
        
        """   p = Parser()
        tree = p.parse_file(fn)
        print(tree) """
        p = myParser2()
        p.actFilePath = fn
        p.compileThisFile()
        p.createXMLString()
        p.genOutput()


