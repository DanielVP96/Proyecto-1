from node import Node
from edge import Edge

class Graph:
    def __init__(self,id="grafo", directed=False, auto=False):
        """
        Constructor
        """
        self.id=id
        self.nodes={}
        self.edges={}
        self.directed= directed
        self.auto=auto


    def addNode(self, id):
        """
        Agrega nodo al grafo, en caso de que no exista lo crea, si existe, regresa el nodo
        encontrado en el diccionario
        """
        new_node=self.nodes.get(id)
        if new_node is None:
            new_node=Node(id)
            self.nodes[new_node.id]=new_node
        return new_node

    def addEdge(self, source, target):
        """
        Agregar una arista al grafo, los nodos deben ser agregados con anterioridad, si no,
        levanta una excepcion
        """

        #Si los nodos no se encuentran en el grafo, levantar excepcion
        if self.nodes.get(source) is None or self.nodes.get(target) is None:
            raise Exception("Nodes are not in the graph, please add them to the graph")

        #nodos en grafo
        nodeSource=self.nodes[source]
        nodeTarget=self.nodes[target]

        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)

        #Si el grafo es no dirigido, checar que no se repitan los vertices en el diccionario
        repeated=False
        autoAux=False
        if not self.directed:
            idAuxNotDirected=str(target) + ' -> ' +str(source)
            aux=self.edges.get(idAuxNotDirected)
            if not(aux is None):
                repeated=True
        
        #Si el grafo es no autociclico, checar que source y target no sean iguales
        if not self.auto:
            if source is target:
                #print(source, target)
                autoAux=True
        
        new_edge= self.edges.get(idAux)
        
        """
        chequeo para grafo no dirigido y no autociclico.
        si la arista es nueva (no se encuentra en el grafo) y los nodos no son repetidos
        agrega nueva arista
        """
        if new_edge is None and repeated is False and autoAux is False:
            new_edge= Edge(idAux, nodeSource, nodeTarget)
            self.edges[new_edge.id]=new_edge
            nodeSource.attr.get("neighbors").append(nodeTarget)
            nodeTarget.attr.get("neighbors").append(nodeSource)
            nodeSource.attr.get("edges").append(new_edge)
            nodeTarget.attr.get("edges").append(new_edge)
            
        return new_edge


    def getDegree(self, id):
        """
        Obtener el grado de nodo
        """
        node=self.nodes.get(id)
        if node is None:
            return 0
        return len(node.attr["neighbors"])
    
    def getNode(self, id):
        """
        Encontrar nodo en el grafo
        """
        return self.nodes.get(id)

    def getTotalNodes(self):
        """
        Obtener el total de nodos en el grafo
        """
        nodes=self.nodes
        if nodes is None:
            return 0
        return len(self.nodes)
    
    def getTotalEdges(self):
        """
        Obtener el total de aristas del grafo
        """
        edges=self.edges
        if edges is None:
            return 0
        return len(self.edges)

    def saveGV(self):
        """
        Crea el archivo .gv que posteriormente sera usado para la creacion de los grafos
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        
        for nodo in self.nodes:
            graph+=str(nodo)+';\n'

        for key, value in self.edges.items():
            graph+= value.id+';\n'

        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        file = open(name, "w")
        file.write(graph)
        file.close()
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')