#This file will create the objects like for storing the information for classes, methods, fields,variables, etc
import xml.etree.ElementTree as xml2


class variableObject():
    def __init__(self) -> None:
        self.variableName =""
        self.typeVar = ""
        self.isArray = False

class methodObject():
    def __init__(self, classObject) -> None:
        self.methodName = ""
        self.variables = []
        self.returnType = ""
        self.mcabe = 0
        self.whileLoops = 0
        self.forLoops = 0
        self.isRecursion = False
        self.parameters = []

    def methodXMLElement(self) -> xml2.Element:

        output = xml2.Element(self.methodName)
        variablesElement  = xml2.Element("variables")
        for variable in self.variables:
            #cast the variable
            variable = variableObject(variable)
            variableElement = xml2.Element("variable")
            variableElement.text = variable.typeVar + " " + variable.variableName

##
class classObject():
    def __init__(self) -> None:
        self.fields = []
        self.className = ""
        self.methods = []

    def addMethod(self, newMethod:methodObject):

        self.methods.append(newMethod)

    def classXMLElement(self)->xml2.Element:
        output = xml2.Element(self.className)
        fieldsElement = xml2.Element("Fields")
        output.append(fieldsElement)
        for field in self.fields:
            fieldElement = xml2.Element("field")
            field = variableObject(field)
            fieldElement.text = field.typeVar + " " + field.variableName
            fieldsElement.append(fieldElement)
        methodsElement = xml2.Element("Methods")
        output.append(methodsElement)
        for method in self.methods:
            method = methodObject(method)
            methodsElement.append(method.methodXMLElement())


        return output



class fileObject():
    def __init__(self, pathway:str) -> None:
        self.pathWay = pathway
        self.classes = []
        self.filesize = ""

    def addClass(self, newClass:classObject):
        self.classes.append(newClass)

    def genXMLString(self)->str:
        ##This is the root
        fileElement = xml2.Element("File")
        classesElement = xml2.Element("Classes")
        fileElement.append(classesElement)
        for classObj in self.classes:
            classObj = classObject(classObj)
            classesElement.append(classObj.classXMLElement())
        