from models.DABNet import DABNet
from models.DSANet import DSANet
from models.EDANet import EDANet
from models.SPFNet import SPFNet
from models.SSFPN import SSFPN
from models.CGNet import CGNet
from models.ContextNet import ContextNet

def build_model(model_name,num_classes):
    if model_name == 'DABNet':
        return DABNet(classes=num_classes)
    elif model_name == 'DSANet':
        return DSANet(classes=num_classes)
    elif model_name == 'CGNet':
        return CGNet(classes=num_classes)
    elif model_name == 'ContextNet':
        return ContextNet(classes=num_classes)
    elif model_name == 'EDANet':
        return EDANet(classes=num_classes)
    elif model_name == 'SPFNet':
        return SPFNet("resnet18",pretrained=True,classes=num_classes)
    elif model_name == 'SSFPN':
        return SSFPN("resnet18",pretrained=True,classes=num_classes)
    else:
        raise NotImplementedError