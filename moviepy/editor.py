"""
This file is meant to make it easy to load the main features of MoviePy
by simply typing:

>>> from moviepy.editor import *

In particular it will load many effects from the video.fx and audio.fx
folders and turn them into VideoClip methods, so that instead of
>>> clip.fx( vfx.resize, 2 ) # or equivalently vfx.resize(clip, 2)
we can write
>>> clip.resize(2)
"""

# Note that these imports could have been performed in the __init__.py
# file, but this would make the loading of moviepy slower.

# Clips

from .video.io.VideoFileClip import VideoFileClip
from .video.VideoClip import VideoClip, ImageClip, ColorClip, TextClip
from .video.compositing.CompositeVideoClip import CompositeVideoClip
from .video.compositing.concatenate import concatenate

<<<<<<< HEAD

from moviepy.audio.AudioClip import AudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.MultiCam import MultiCam ###############
=======
from .audio.AudioClip import AudioClip
from .audio.io.AudioFileClip import AudioFileClip
>>>>>>> dd296029c192b8ac894b3ace4cf23d1468a59504

# FX

import moviepy.video.fx as vfx
import moviepy.audio.fx as afx
import moviepy.video.compositing.transitions as transfx

# Tools

import moviepy.video.tools as videotools
import moviepy.video.io.ffmpeg_tools as ffmpeg_tools
from .tools import cvsecs

try:
    from .video.io.sliders import sliders
except ImportError:
    pass

# The next loop transforms many effects into VideoClip methods so that
# they can be walled with myclip.resize(width=500) instead of 
# myclip.fx( vfx.resize, width= 500)
for method in ["vfx.crop",
               "vfx.resize",
               "vfx.margin",
               "vfx.fadein",
               "vfx.fadeout",
               "vfx.speedx",
               "afx.volumex",
               "afx.audio_fadein",
               "afx.audio_fadeout",
               "transfx.crossfadein",
               "transfx.crossfadeout"]:
    exec("VideoClip.%s = %s"%( method.split('.')[1], method))


for method in ["afx.audio_fadein",
               "afx.audio_fadeout"]:
    exec("AudioClip.%s = %s"%( method.split('.')[1], method))

