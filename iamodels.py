import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from diffusers.utils import load_image
import pickle
import os

def TrainModel(ruta,name_model,settings):
	pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
	    name_model, torch_dtype=torch.float16, variant=settings["variant"], use_safetensors=settings["use_safetensors"]
	)
	pipe = pipe.to("cuda")

	with open(f"{ruta}/model.pkl", "wb") as f:
		pickle.dump(pipe, f)
	
	print(f"Modelo Exportdo: {ruta}/")

def MainModel(ruta,prompt,image_path):

	with open(f"{ruta}/model.pkl", "rb") as f:
		pipe = pickle.load(f)

	if not os.path.exists(f"{ruta}/model.pkl"):
		print("Descargue primeramente el modelo")
		return

	init_image = load_image(image_path).convert("RGB")

	image = pipe(prompt, image=init_image).images

	image[0].save(f"{ruta}/output.png")

	print(f"Imagen Exportado {ruta}/")