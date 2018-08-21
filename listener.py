import snowboydecoder

def detect_callback():
   print("Yes, Master!")

detector = snowboydecoder.HotwordDetector("resources/models/Rustem.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detect_callback)
