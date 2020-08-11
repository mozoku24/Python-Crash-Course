import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'

wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})

wm.render_to_file(r'E:\Temp\数据可视化\na_populations.svg')