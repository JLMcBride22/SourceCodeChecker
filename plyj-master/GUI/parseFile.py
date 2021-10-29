# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import sys
sys.path.append(".")

import PLYJ.model as m
from PLYJ.parser import Parser


# Function for opening the
# file explorer window


## To save time change initialdir to a directory with a java file.
class myParser2():
    def __init__(self) -> None:
        self.node:int = 2
        self.edge:int = 0
    
    def calcMcCabe(self):
        out = self.edge - self.node  + 2

        return out
    
    def calMetric(self, sourceElement):
        print()
        if(type(sourceElement) is m.IfThenElse):
            self.node +=2
            self.edge += 4
            print (sourceElement.if_true)
            self.calMetric(sourceElement.if_true)
            print()
            if sourceElement.if_false is None:
                self.edge-=1
            
            else:
                self.calMetric(sourceElement.if_false)
        elif type(sourceElement) is m.While:
            self.node +=2
            self.node +=3
        elif type(sourceElement) is m.VariableDeclaration:
            self.node += 1

            



    def parseThisFile(self, filename: str):

        # Change label contents

        p = Parser()
        tree = p.parse_file(filename)

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
                                    type_name = statement.type.name
                                else:
                                    ##This is where it's an array type
                                    dim = statement.type.dimensions
                                    brackets= "[]"
                                    type_name = statement.type.name
                                    for i in range(0,dim):
                                        type_name = type_name + brackets
                                    
                                    
                                print('        ' + type_name + ' ' + var_decl.variable.name)

                        else:
                            self.calMetric(statement)

if __name__ == '__main__':
        fn ="JavaTest\\dev.java"
        
        """   p = Parser()
        tree = p.parse_file(fn)
        print(tree) """
        mp = myParser2()
        mp.parseThisFile(fn)
        out = mp.calcMcCabe()
        print(out)
        


