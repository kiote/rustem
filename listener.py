import snowboydecoder

callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]

detector = snowboydecoder.HotwordDetector("resources/models/Rustem.pmdl", sensitivity=0.5, audio_gain=1)
print("Say something...")
detector.start(detected_callback=callbacks)

