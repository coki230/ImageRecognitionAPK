from torchvision.io import decode_image
from torchvision.models import  EfficientNet_B2_Weights
from torchvision import models

def parse_img(img):
    img = decode_image(img).unsqueeze(0)
    weighets = EfficientNet_B2_Weights.DEFAULT
    process = weighets.transforms()
    img = process(img)
    model = models.efficientnet_b2(weights=weighets)
    model.eval()
    result = model(img).squeeze(0).softmax(0)
    id = result.squeeze(0).argmax().item()
    category_name = weighets.meta["categories"][id]
    return str(category_name)




