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
        self.maxNesting = 0
        self.switchCompl = 0

        ##Number of variables
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
        
    def setMetricDict(self, dictin):
        self.dictOfMetric = dictin
    
    def measurementXML(self)-> xml2.Element:
        output =xml2.Element("Metrics")
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
                        pass
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
                for box in v:
                    if box == "Total Number of Variables":
                        pass
                    elif box == "Float":
                        pass
                    elif box == "Array":
                        pass
                    elif box == "Integer":
                        pass
                    elif box == "User Defined Variable":
                        pass
                    elif box == "String":
                        pass
                    elif box == "Structure":
                        pass
                    elif box == "Character":
                        pass


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
            
        

        
    def calcMetrics(self):
        self.numbParams = len(self.parameters)
    

    def XMLElement(self) -> xml2.Element:

        output = xml2.Element(self.name)
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

    def addMethod(self, newMethod:methodObject):
        newMethod.setMetricDict(self.dictOfMetric)
        newMethod.calcMetrics()
        self.methods.append(newMethod)

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


        return output

    def calcMeasurements(self):


        for method in self.methods:
            
            method:methodObject
            self.variables.extend(method.variables)
            #self.returnType = ""
            self.mcabe += method.mcabe
            self.whileLoops += method.whileLoops
            self.forLoops  += method.forLoops
            self.doWhile += method.doWhile
            self.isRecursion = self.isRecursion or method.isRecursion
            self.parameters.extend(method.parameters)
            
            ##self.halstead = 0
            ##self.maxNesting = 0
            self.switchCompl += method.switchCompl

        ##Number of variables TODO we need to add fields to these.
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
    

class fileObject(methodObject):
    def __init__(self, pathway:str) -> None:
        self.pathWay = pathway
        self.classes = []
        self.filesize = ""
        self.dictOfMetric = {}

    def setMetricDict(self, dict):
        self.dictOfMetric = dict

    def addClass(self, newClass:classObject):
        
        newClass.calcMeasurements()
        self.classes.append(newClass)



    def genXMLString(self)->str:
        ##This is the root
        
        fileElement = xml2.Element("File")
        
        classesElement = xml2.Element("Classes")
        
        fileElement.append(classesElement)
        
        for classObj in self.classes:
            #classObj = classObject(classObj)
            classesElement.append(classObj.XMLElement())

        

        return xml2.tostring(fileElement, 'unicode')
        

 
        