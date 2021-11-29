#This file will create the objects like for storing the information for classes, methods, fields,variables, etc
import xml.etree.ElementTree as xml2



class variableObject():
    def __init__(self) -> None:
        self.name =""
        self.typeVar = ""
        self.isArray = False
        self.dims = 0

class methodObject():
    def __init__(self, inMethodName) -> None:
        self.name = inMethodName
        
        self.variables = []
        self.returnType = ""
        self.mcabe = 0
        self.whileLoops = 0
        self.forLoops = 0
        self.doWhile = 0
        self.isRecursion = False
        self.parameters = []
        self.numbParams = 0
        self.halstead = 0
        self.currNestingLevel = 0
        self.maxNesting = 0
        self.switchCompl = 0
        self.noFunctionCalls = 0
        

        ##Number of variables
        self.totalVar = 0
        self.noInt = 0
        self.noFloat = 0
        self.noChar = 0
        self.noString = 0
        self.userDefined = 0
        self.noStruct = 0
        self.noArrays = 0

        #nameLengh LT= less than and MT = more than
        self.LT3char = 0
        self.MT3butLT10char = 0
        self.MT10butLT20 = 0
        self.MT20 = 0
        self.dictOfMetric = {}
        self.noSemicolons = 0
        
        
    def setMetricDict(self, dictin):
        self.dictOfMetric = dictin

    #This function helps with finding the max nested level.
    #Should be called after getting done with a block in the postCompileCalc file
    def nestingLevelMaxFinder(self):
        if(self.currNestingLevel > self.maxNesting):
            self.maxNesting = self.currNestingLevel
    #counts the variables by type
    def variableTypeCounter(self, var:variableObject):
        self.totalVar += 1
        if(var.dims > 0):
            self.noArrays += 1
            return
        varType = var.typeVar
        if(varType =='String'):
            self.noString += 1
        elif(varType == 'int'):
            self.noInt += 1
        elif(varType == "char"):
            self.noChar += 1
        elif(varType =="float"):
            self.noFloat += 1
        elif varType == "byte" or type == "double" or type == "boolean" or type == "short" or type == "long":
            return
        else:
            self.userDefined +=1
    
    
    ##The next two functions counts the variable by type(for now) and adds them to their respective list.
    def addParameter(self, par: variableObject):
        self.variableTypeCounter(par)
        self.parameters.append(par)
        self.numbParams += 1
        return

    def addVariable(self, var:variableObject):
        self.variableTypeCounter(var)
        self.variables.append(var)
        return
    
    def measurementXML(self)-> xml2.Element:
        output =xml2.Element("Measurements")
        for k,v in self.dictOfMetric.items():
            """ if k == "SizeTab":
                for box in v:
                    if box == "Full Comment Lines":
                        pass
                    elif box == "Number of Function Calls":
                        pass
                    elif box == "Blank Lines":
                        pass
                    elif box == "Number of Semicolons":
                        pass
                    elif box == "Source Lines of Code with Comments":
                        pass
                    elif box == "Source Lines of Code without Comments":
                        pass """
            if k == "ComplexityTab":#1
                element = xml2.Element("Complexity")
                output.append(element)
                for box in v:
                    subEle = xml2.Element("Complexity")
                    subEleText = ""
                    if box == "Number of Passed Parameters":
                        subEleText = box +" = "+ str(self.numbParams)
                    elif box == "Switch Complexity":
                        pass
                    elif box == "McCabe's Cyclomatic Complexity":
                        subEleText = box +" = "+ str(self.mcabe)
                    elif box == "Maximum Nesting Level":
                        subEleText = box +" = " + str(self.maxNesting)
                    elif box == "ESLOC at Max Nesting Level":
                        pass
                    elif box == "Halstead's Software Science Primitives":
                        pass
                    if subEleText is not "":
                        subEle.text = subEleText
                        element.append(subEle)

            elif k == "LoopTab":
                element = xml2.Element("Loops")
                output.append(element)
                for box in v:
                    subEle = xml2.Element("Complexity")
                    subEleText = ""
                    if box == "Number of For Loops":
                        subEleText = box +" = "+ str(self.forLoops)
                    elif box == "Number of While Loops":
                        subEleText = box +" = "+ str(self.whileLoops)
                    elif box == "Number of Do-While Loops":
                        subEleText = box + " = " + str(self.doWhile)
                    if subEleText is not "":
                        subEle.text = subEleText
                        element.append(subEle)
            elif k == "VariableTab":
                element = xml2.Element("VariableTypes")
                output.append(element)
                for box in v:
                    subEle = xml2.Element("variableCount")
                    subEleText = ""
                    if box == "Total Number of Variables":
                        subEleText = box + " = "+ str(self.totalVar)
                    elif box == "Float":
                        subEleText = box + " = "+ str(self.noFloat)
                    elif box == "Array":
                        subEleText = box + " = "+ str(self.noArrays)
                    elif box == "Integer":
                        subEleText = box + " = "+ str(self.noInt)
                    elif box == "User Defined Variable":
                        subEleText = box + " = "+ str(self.userDefined)
                    elif box == "String":
                        subEleText = box + " = "+ str(self.noString)
                    elif box == "Character":
                        subEleText = box + " = "+ str(self.noChar)
                    
                    if subEleText is not "":
                        subEle.text = subEleText
                        element.append(subEle)

            elif k == "NameLengthTab":
                for box in v:
                    if box == "Names Less Than 3 Characters":
                        pass
                    elif box == "Names 20 or More Characters":
                        pass
                    elif box == "Names More Than 3 but Less Than 10 Characters":
                        pass
                    elif box == "Names 10 or More but Less than 20 Characters":
                        pass

        
                """   elif k == "PreambleTab":
                for box in v:
                    if box == "Assumptions":
                        pass
                    elif box == "Purpose":
                        pass
                    elif box == "Filename":
                        pass
                    elif box == "Change Log":
                        pass
                    elif box == "Interface":
                        pass
                    elif box == "Author":
                        pass """

                """ elif k == "FlowControlTab":
                for box in v:
                    if box == "Presence of GoTo's":
                        pass
                    elif box == "Singular Entry Point":
                        pass
                    elif box == "Singular Exit Point":
                        pass
                    elif box == "Presence of Recursion":
                        pass """
            elif k == "ClarityTab":
                for box in v:
                    if box == "All Variable Names at Least X Characters Long":
                        pass
                    elif box == "All Variable Names Not Longer than X Characters":
                        pass
                    elif box == "All #define Parameters in All Capitals":
                        pass
                    elif box == "No Variable Names in All Capitals":
                        pass
            elif k == "ComplexityStandardTab":
                for box in v:
                    if box == "McCabe's Cyclomatic Complexity Less Than X":
                        pass
                    elif box == "Maximum Nesting Level Less Than X":
                        pass
                    elif box == "Localization of Variables":
                        pass
                    elif box == "ESLOC Less Than X Within Functions":
                        pass
        return output
            
    #this function returns the method with all its parameters in parathesises.    
    def methodNameWithParams(self)->str:

        param_strings = []
        for param in self.parameters:
            param:variableObject
            param_strings.append(param.typeVar + " " +param.name)
           
        return self.returnType+ " "+ self.name + '(' + ', '.join(param_strings) + ')'
        
        
        
    def calcMetrics(self):
        self.numbParams = len(self.parameters)
    

    def XMLElement(self) -> xml2.Element:

        output = xml2.Element(self.name)
        output.text = self.methodNameWithParams()
        variablesElement  = xml2.Element("variables")
        output.append(variablesElement)
        for variable in self.variables:
            #cast the variable
            
            variableElement = xml2.Element("variable")
            variableElement.text = variable.typeVar + " " + variable.name
            variablesElement.append(variableElement)
        paramsElement = xml2.Element("Parameters")
        output.append(paramsElement)

        for param in self.parameters:
            paramElement = xml2.Element("parameter")
            paramElement.text = param.typeVar + " " + param.name
            paramsElement.append(paramElement)

        output.append(self.measurementXML())





        return output
        

##
class classObject(methodObject):
    def __init__(self, inName) -> None:
        super().__init__(inName)
        self.fields = []
        
        self.methods = []
    #this functions add the method and add the method's stats to the class stats.
    def addMethod(self, newMethod:methodObject):
        newMethod.setMetricDict(self.dictOfMetric)
        self.addObjectIn(newMethod)
        self.methods.append(newMethod)
    #creates an xml element
    def XMLElement(self)->xml2.Element:
        output = xml2.Element(self.name)
        fieldsElement = xml2.Element("Fields")
        
        output.append(fieldsElement)

        for field in self.fields:
            fieldElement = xml2.Element("field")
            
            fieldElement.text = field.typeVar + " " + field.name
            fieldsElement.append(fieldElement)
        methodsElement = xml2.Element("Methods")
        output.append(methodsElement)
        for method in self.methods:
            #method = methodObject(method)
            methodsElement.append(method.XMLElement())
        output.append(self.measurementXML())


        return output

    #def calcMeasurements(self):
        #for method in self.methods:
            #self.addObjectIn(method)
            
    
    def addObjectIn(self,method:methodObject):
        
        self.variables.extend(method.variables)
        #self.returnType = ""
        self.mcabe += method.mcabe
        self.numbParams += method.numbParams
        self.whileLoops += method.whileLoops
        self.forLoops  += method.forLoops
        self.doWhile += method.doWhile
        self.isRecursion = self.isRecursion or method.isRecursion
        self.parameters.extend(method.parameters)
        self.noFunctionCalls += method.noFunctionCalls
        self.noSemicolons += method.noSemicolons

        
        ##self.halstead = 0
        if self.maxNesting < method.maxNesting:
            self.maxNesting = method.maxNesting
        self.switchCompl += method.switchCompl

    ##Number of variables TODO we need to add fields to these.
        self.totalVar += method.totalVar
        self.noInt += method.noInt
        self.noFloat += method.noFloat
        self.noChar  += method.noChar
        self.noString = method.noString
        self.userDefined += method.userDefined
        #self.noStruct += method.noStruct
        self.noArrays += method.noArrays

    #nameLengh LT= less than and MT = more than
        self.LT3char = 0
        self.MT3butLT10char = 0
        self.MT10butLT20 = 0
        self.MT20 = 0
        
class fileObject(classObject):
    def __init__(self, pathway:str) -> None:
        super().__init__(pathway)
        self.pathWay = pathway
        self.noFullCommentLines = 0
        # Calclated in checkNumOfComments method in parser.py
        self.noLinesOfCode = 0
        self.noSourceWComment = 0
        self.noSourceWOutComment = 0
        self.noBlankLines = 0

        self.classes = []
        self.filesize = ""
        self.dictOfMetric = {}

    def setMetricDict(self, dict):
        self.dictOfMetric = dict

    def addClass(self, newClass:classObject):
        
        self.addObjectIn(newClass)
        self.classes.append(newClass)




    def genXMLString(self)->str:
        ##This is the root
        
        fileElement = xml2.Element("File")
        
        classesElement = xml2.Element("Classes")
        
        fileElement.append(classesElement)
        
        for classObj in self.classes:
            #classObj = classObject(classObj)
            classesElement.append(classObj.XMLElement())

        fileElement.append(self.measurementXML())

        return xml2.tostring(fileElement, 'unicode')
        

 
        