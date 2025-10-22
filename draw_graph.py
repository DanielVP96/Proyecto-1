import os
import graphviz

def draw_gv_file(gv_path: str, open_view: bool = True, fmt: str = "png") -> str:
    """
    Renderiza un archivo .gv (Graphviz DOT) a imagen (SVG o PNG).
    - gv_path: ruta del archivo .gv
    - open_view: abre la imagen automáticamente si es True
    - fmt: 'svg' o 'png'
    """
    if not os.path.exists(gv_path):
        raise FileNotFoundError(f"No existe el archivo: {gv_path}")

    base_name = os.path.splitext(os.path.basename(gv_path))[0]

    # Cargar el archivo DOT
    src = graphviz.Source.from_file(gv_path)

    # Renderizar a imagen
    outpath = src.render(filename=base_name, format=fmt, cleanup=True, view=open_view)
    return outpath + '/imagenes'


def draw_from_graph_id(graph_id: str, open_view: bool = True, fmt: str = "png") -> str:
    """
    Renderiza una imagen a partir del nombre base del grafo (sin extensión .gv).
    Ejemplo: draw_from_graph_id("Grid_columns_50_rows_49", fmt="svg")
    """
    gv_path = f"{graph_id}.gv"
    return draw_gv_file(gv_path, open_view=open_view, fmt=fmt)

if __name__ == "__main__":
    print("🧩 Generador de imágenes Graphviz independiente")
    print("==============================================")
    print("Convierte todos los archivos .gv de la carpeta actual en imágenes.\n")

    # Elegir formato de salida
    fmt = input("Formato de salida (svg/png) [svg]: ").strip().lower() or "svg"
    open_view_input = input("¿Abrir cada imagen al generarla? (s/n) [n]: ").strip().lower()
    open_view = open_view_input == "s"

    # Buscar todos los archivos .gv
    gv_files = [f for f in os.listdir(".") if f.endswith(".gv")]

    if not gv_files:
        print("⚠️ No se encontraron archivos .gv en la carpeta actual.")
    else:
        print(f"🔍 Se encontraron {len(gv_files)} archivos .gv.\n")
        for i, file in enumerate(gv_files, start=1):
            try:
                print(f"[{i}/{len(gv_files)}] Renderizando {file} ...")
                outpath = draw_gv_file(file, open_view=open_view, fmt=fmt)
                print(f"   ✅ Imagen creada: {outpath}\n")
            except Exception as e:
                print(f"   ❌ Error con {file}: {e}\n")

        print("🏁 Proceso completado. Todas las imágenes se guardaron en esta carpeta.")
