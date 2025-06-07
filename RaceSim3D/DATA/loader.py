import os
import pyray as pr
#-------------> 3D
def load_3d_obj(path):
    if not os.path.isfile(path):
        print(f"File not found: {path}")
        return None

    model = pr.load_model(path)
    if model.meshCount == 0:
        print("Error loading model or model is empty")
        return None

    print(f"Model successfully loaded: {path}")
    return model
#-------------> 2D
def load_2d_img(path):
    try:
        texture = pr.load_texture(path)
        return texture
    except Exception as e:
        print(f"Error loading texture from {path}: {e}")
        return None