#!/usr/bin/python3
from KeystrokeML import KeystrokeML
import warnings

warnings.filterwarnings('ignore')
pathData = "./output/Keystrokes_dataset_consolidado.csv"
pathPredict = "./01_KeystrokeDynamics/output/HardcodeUser_timings.csv"
keyML = KeystrokeML()


#keyML.setDataset(pathData)
#keyML.trainModel()

keyML.predictFromFile(pathPredict)