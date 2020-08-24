# method 1 use ffmpeg in a wrapper
# ffmpeg -i yosemiteA.mp4 -f image2 -vf "select='eq(pict_type,PICT_TYPE_I)'" -vsync vfr yi%03d.png

# method 2 use video-kf
import videokf as vf
vf.extract_keyframes("My_video.mp4", method="iframes")