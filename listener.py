import snowboydecoder

callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]

detector = snowboydecoder.HotwordDetector("resources/models/jarvis.pmdl", sensitivity=0.42, audio_gain=1)
print("Say something...")
detector.start(detected_callback=callbacks)

