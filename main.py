import json
import iamodels


def fuctions_execute(config_json_path: str):
    # Leer el archivo de configuración
    with open(config_json_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    #Ruta del proyecto
    ruta = config["proyect"]
    with open(f"{ruta}/{config_json_path}", 'r', encoding='utf-8') as file:
        config = json.load(file)

    # Usar los valores del archivo JSON
    prompt = config["prompt"]
    image_path = f"{ruta}/{config['image_path']}"

    # Llamar al modelo y mostrar los resultados
    iamodels.MainModel(ruta,prompt,image_path)

def main():

    config_json_path = "config.json"

    result = fuctions_execute(config_json_path)

if __name__ == "__main__":
    main()