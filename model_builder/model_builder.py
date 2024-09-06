from models.DSANet import DSANet
from models.SPFNet import SPFNet
from models.SSFPN import SSFPN
from models.DABNet import DABNet
from models.CGNet import CGNet

def build_model(model_name,num_classes):
    if model_name == 'DABNet':
        return DABNet(classes=num_classes)
    elif model_name == 'DSANet':
        return DSANet(classes=num_classes)
    elif model_name == 'CGNet':
        return CGNet(classes=num_classes)
    elif model_name == 'SPFNet':
        return SPFNet("resnet18",pretrained=True,classes=num_classes)
    elif model_name == 'SSFPN':
        return SSFPN("resnet18",pretrained=True,classes=num_classes)
    else:
        raise NotImplementedError