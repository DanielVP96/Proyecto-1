import algorithms as a
import draw_graph

def main():
    try:
        
        #Grafo Malla de 50 nodos
        grafoMalla_50=a.gridGraph(10,5,directed=False)
        grafoMalla_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoMalla_50.id, open_view=False, fmt="svg")
        #Grafo Malla de 200 nodos
        grafoMalla_200=a.gridGraph(20,10,directed=False)
        grafoMalla_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoMalla_200.id, open_view=False, fmt="svg")
        #Grafo Malla de 500 nodos
        grafoMalla_500=a.gridGraph(25,20,directed=False)
        grafoMalla_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoMalla_500.id, open_view=False, fmt="svg")

        #Grafo ErdosRenyi de 50 nodos
        grafoErdos_50=a.randomErdosRenyi(50, 50, directed=False, auto=False)
        grafoErdos_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoErdos_50.id, open_view=False, fmt="svg")
        #Grafo ErdosRenyi de 200 nodos
        grafoErdos_200=a.randomErdosRenyi(200, 200, directed=False, auto=False)
        grafoErdos_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoErdos_200.id, open_view=False, fmt="svg")
        #Grafo ErdosRenyi de 500 nodos
        grafoErdos_500=a.randomErdosRenyi(500, 500, directed=False, auto=False)
        grafoErdos_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoErdos_500.id, open_view=False, fmt="svg")

        #Grafo Gilbert de 50 nodos
        grafoGilbert_50=a.randomGilbert(50, 0.4, directed=False, auto=False)
        grafoGilbert_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoGilbert_50.id, open_view=False, fmt="svg")
        #Grafo Gilbert de 200 nodos
        grafoGilbert_200=a.randomGilbert(200, 0.1, directed=False, auto=False)
        grafoGilbert_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoGilbert_200.id, open_view=False, fmt="svg")
        #Grafo Gilbert de 500 nodos
        grafoGilbert_500=a.randomGilbert(500, 0.1, directed=False, auto=False)
        grafoGilbert_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoGilbert_500.id, open_view=False, fmt="svg")

        #Grafo Geografico de 50 nodos
        grafoGeografico_50=a.randomGeografico(50, 0.2, directed=False, auto=False)
        grafoGeografico_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoGeografico_50.id, open_view=False, fmt="svg")
        #Grafo Geografico de 200 nodos
        grafoGeografico_200=a.randomGeografico(200, 0.1, directed=False, auto=False)
        grafoGeografico_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoGeografico_200.id, open_view=False, fmt="svg")
        #Grafo Geografico de 500 nodos
        grafoGeografico_500=a.randomGeografico(500, 0.1, directed=False, auto=False)
        grafoGeografico_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoGeografico_500.id, open_view=False, fmt="svg")

        #Grafo BarabasiAlbert de 50 nodos
        grafoBarabasiAlbert_50= a.randomBarabasiAlbert(50, 5, directed=False, auto=False)
        grafoBarabasiAlbert_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoBarabasiAlbert_50.id, open_view=False, fmt="svg")
        #Grafo BarabasiAlbert de 200 nodos
        grafoBarabasiAlbert_200= a.randomBarabasiAlbert(200, 3, directed=False, auto=False)
        grafoBarabasiAlbert_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoBarabasiAlbert_200.id, open_view=False, fmt="svg")
        #Grafo BarabasiAlbert de 500 nodos
        grafoBarabasiAlbert_500= a.randomBarabasiAlbert(500, 2, directed=False, auto=False)
        grafoBarabasiAlbert_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoBarabasiAlbert_500.id, open_view=False, fmt="svg")

        #Grafo DorogovtsevMendes de 50 nodos 
        grafoDorogovt_50= a.randomDorogovtsevMendes(n=50, directed=False)
        grafoDorogovt_50.saveGV()
        #draw_graph.draw_from_graph_id(grafoDorogovt_50.id, open_view=False, fmt="svg")
        #Grafo DorogovtsevMendes de 200 nodos
        grafoDorogovt_200= a.randomDorogovtsevMendes(n=200, directed=False)
        grafoDorogovt_200.saveGV()
        #draw_graph.draw_from_graph_id(grafoDorogovt_200.id, open_view=False, fmt="svg")
        #Grafo DorogovtsevMendes de 500 nodos
        grafoDorogovt_500= a.randomDorogovtsevMendes(n=500, directed=False)
        grafoDorogovt_500.saveGV()
        #draw_graph.draw_from_graph_id(grafoDorogovt_500.id, open_view=False, fmt="svg")
        
    except Exception as err:
        print("Error")

main()