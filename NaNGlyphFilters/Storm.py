# MenuTitle: Storm
# -*- coding: utf-8 -*-
__doc__ = """
Storm
"""

from NaNFilter import NaNFilter
from NaNGFGraphikshared import ClearPaths, CreateShapeComponent, operateOnBlackAtInterval
from NaNGFNoise import noiseMap
from NaNGlyphsEnvironment import GSComponent
from noise import snoise2


class Storm(NaNFilter):
	gridsize = 30
	minsize, maxsize = 30, 80

	def setup(self):
		self.stormcomponent = CreateShapeComponent(self.font, self.maxsize, self.maxsize, "rectangle", "StormShape")

	def drawStorm(self, x, y, layer):
		freq = 0.005
		noiz = snoise2(x * freq, y * freq, 3)
		size = noiseMap(noiz, self.minsize, self.maxsize)
		if size <= 4:
			return
		stormcomp = GSComponent(self.stormcomponent)
		scale = (float(1) / self.maxsize) * size
		stormcomp.scale = (scale, scale)
		stormcomp.position = (x, y)
		layer.components.append(stormcomp)

	def processLayer(self, thislayer, params):
		operateOnBlackAtInterval(thislayer, self.drawStorm, self.gridsize)
		ClearPaths(thislayer)


Storm()
