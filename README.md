# Este repositorio contiene un algoritmo de Python para generar modificar una imagen a partir de un texto dado

*Descripción del algoritmo*

El algoritmo se utiliza para editar una imagen basado en el texto proporcionado.

## Pre-requisitos

• Python 3.7 o superior
• Librerías de Python:
    • Transformers
    • diffusers
    • torch

## Instalación

bash```
pip install -r requirements.txt
```

## Configuración (config.json)

El archivo config.json contiene la configuración del proceso de generación de video. Se pueden modificar los parámetros de la configuración de acuerdo a las necesidades del usuario.

Parámetros:

• name_model: Nombre del modelo de refinamiento de imagen.
• settings: Lista de configuraciones para el refinamiento.
    • variant: Variante del modelo, "fp16" o "fp32".
    • use_safetensors: Indica si se deben usar archivos SafeTensors para el modelo.
• prompt: Texto que describe los cambios a realizar en la imagen.
• image_path: Ruta al archivo de imagen que se va a refinar.

## Ejecución

1. Asegúrate de que el archivo config.json esté configurado correctamente.
2. Ejecuta el train.py para que se realice el entrenamiento
3. Ejecute el main.py para generar el video

Notas

• El rendimiento del modelo y la calidad del video generado dependen de la configuración del proceso de generación.
• Se recomienda ajustar los parámetros de la configuración para obtener el mejor resultado.
• La generación de videos requiere una gran cantidad de recursos computacionales.
Licencia