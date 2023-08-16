# CPSE-Summer-Program-Trash-Genie

Trash Genie is a smart waste-bin that uses a YOLOv5 image recognition model to detect different types of wastes and sort them into their respective compartments.

To run, either execute "SmallModel.py" or "GeneralizedModel.py" with the proper model weights included in the same directory as the python script, or change path to weights in the progam.  Make sure "servo.py" is in the same directory as the python script being executed. Must execute from Raspberry Pi connected to tilting platform using servo motors and webcam.

Link to weights and datasets: https://drive.google.com/drive/folders/1ZDrL4JGhMWdp8c1CO-mRPRgROMeZdq7h?usp=sharing

Notes: Keep a white background behind the camera's field of view. "Servo.py" contains functions for controlling the servo motors to dump the items into the proper compartments. Brown Vertical servo motor (white wire) must be connected to GPIO 18 and horizontal servo motor (light-green wire) must be connected top GPIO 17. Weights for trained models in "weights" folder. "SmallModel.pt" was trained on a very small dataset and used for demonstration perposes on Demo Day; it is only capable of differentiating crumbled plastic bottles, metal coke cans, and crumbled paper with a high confidence. The model classes include: "plastic," "paper," and "metal." "GeneralizedModel.pt" was traiend with a much larger dataset, but often mislabels objects and generally has a lower confidence value. The model classes include: "PLASTIC," "GLASS," "PAPER," "CARDBOARD," "METAL," "BIODEGRADABLE," and "CLOTH." The datasets used are included in this repository under "datasets" and can be used to train YOLOv5 models if desired. 

Wire Connections:
Brown Wires to GRD
Blue Wires to 5V Power
Light-Green to GPIO 17
White to GPIO 18


