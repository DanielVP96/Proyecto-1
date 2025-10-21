# draw_graph.py
import os
import graphviz

def draw_gv_file(gv_path: str, open_view: bool = True, fmt: str = "png") -> str:
    
    if not os.path.exists(gv_path):
        raise FileNotFoundError(f"No existe el archivo: {gv_path}")

    base_name = os.path.splitext(os.path.basename(gv_path))[0]
    # Cargar el DOT
    src = graphviz.Source.from_file(gv_path)
    outpath = src.render(filename=base_name, format=fmt, cleanup=True, view=open_view)
    return outpath

def draw_from_graph_id(graph_id: str, open_view: bool = True, fmt: str = "png") -> str:
    
    gv_path = f"{graph_id}.gv"
    return draw_gv_file(gv_path, open_view=open_view, fmt=fmt)
