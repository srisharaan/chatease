import cv2
import torch
from torchvision.transforms import transforms
import torchvision
import numpy
from PIL import Image


def camuh():
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("cam_video.mp4", vid_cod, 20.0, (640,480))
    videoCaptureObject = cv2.VideoCapture(0)
    pred_labels = []
    while(True):
        ret,frame = videoCaptureObject.read()

        cv2.imwrite('image.png',frame)
        cv2.imshow('recognising,press q to quit',frame)
        path="modeluh.pt"
        device=torch.device('cpu')
        model = torchvision.models.vgg19_bn(pretrained=True)
        model=(torch.load(path, map_location=device))
        model.eval()
        transform = transforms.Compose([transforms.Resize(224),
                                        transforms.RandomHorizontalFlip(),
                                        transforms.ToTensor()])
    
        
        image =transform(Image.open('image.png'))
        #print(image)
        image = image.unsqueeze(0)
        outputs = model(image)
        _, predicted = torch.max(outputs.data,1 )
        a=(predicted.item())
        #print(a)
        #print(_)
        dictuh ={
          0:'a',
          1:'b',
          2:'c',
          3:'d',
          4:'e',
          5:'f',
          6:'g',
          7:'h',
          8:'i',
          9:'j',
          10:'k',
          11:'l',
          12:'m',
          13:'n',
          14:'o',
          15:'p',
          16:'q',
          17:'r',
          18:'s',
          19:'t',
          20:'u',
          21:'v',
          22:'w',
          23:'x',
          24:'y',
          25:'z',
        }

        vandru=dictuh[a]
        pred_labels.append(vandru)
        #print(pred_labels)
        output.write(frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    output.release()
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return pred_labels

'''


import cv2
#Capture video from webcam
vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640,480))
while(True):
     # Capture each frame of webcam video
     ret,frame = vid_capture.read()
     cv2.imshow("My cam video", frame)
     output.write(frame)
     # Close and break the loop after pressing "x" key
     if cv2.waitKey(1) &0XFF == ord('x'):
         break
# close the already opened camera
vid_capture.release()
# close the already opened file
output.release()
# close the window and de-allocate any associated memory usage
cv2.destroyAllWindows()

'''
