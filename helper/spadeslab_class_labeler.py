import numpy as np
import pandas as pd


def to_activity_spadeslab(labels):
    label = labels.lower().strip()
    if "sitting" in label and 'writing' in label:
        return 'Sitting and writing'
    elif 'stand' in label and 'writ' in label:
        return 'Standing and writing at a table'
    elif 'sit' in label and 'story' in label:
        return "Sitting and talking"
    elif "reclin" in label and 'story' in label:
        return 'Reclining and talking'
    elif 'reclin' in label and ('text' in label or 'web' in label):
        return 'Reclining and using phone'
    elif 'sit' in label and ('web' in label or 'typ' in label):
        return 'Sitting and typing on a keyboard'
    elif "stand" in label and ('web' in label or 'typ' in label):
        return "Standing and typing on a keyboard"
    elif 'bik' in label and ('stationary' in label or '300' in label):
        return "Stationary cycle ergometry"
    elif 'treadmill' in label and '1' in label:
        return "Level treadmill walking at 1 mph with arms on desk"
    elif 'treadmill' in label and '2' in label:
        return "Level treadmill walking at 2 mph with arms on desk"
    elif 'treadmill' in label and 'phone' in label and 'arms' not in label:
        return "Level treadmill walking at 3-3.5 mph while holding a phone with dominant arm to the ear and talking"
    elif 'treadmill' in label and 'bag' in label and 'arms' not in label:
        return "Level treadmill walking at 3-3.5 mph and carrying a bag"
    elif 'treadmill' in label and 'story' in label and 'arms' not in label:
        return "Level treadmill walking at 3-3.5 mph while talking"
    elif 'treadmill' in label and 'drink' in label and 'arms' not in label:
        return 'Level treadmill walking at 3-3.5 mph and carrying a drink'
    elif ('treadmill' in label or 'walk' in label) and ('3.5' in label or '3' in label) and 'arms' not in label:
        return 'Level treadmill walking at 3-3.5 mph'
    elif 'treadmill' in label and '5.5' in label:
        return 'Treadmill running at 5.5 mph & 5% grade'
    elif 'laundry' in label:
        return 'Standing and folding towels'
    elif 'sweep' in label:
        return 'Standing and sweeping'
    elif 'shelf' in label and 'load' in label:
        return 'Standing loading/unloading shelf'
    elif 'lying' in label:
        return "Lying on the back"
    elif label == 'sitting' or ('sit' in label and 'still' in label):
        return "Sitting still"
    elif label == "still" or 'standing' == label:
        return "Self-selected free standing"
    else:
        return 'Unknown'
