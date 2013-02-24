#----------------------------------------------
# Pythonscript voor de animatie van vogels die
# een bepaald object volgen en hindernissen
# ontwijken.
#
# Wouter Pinnoo en Eveline Hoogstoel
#----------------------------------------------

import bpy
import random

# Maken van hindernissen op willekeurige plaatsen
for i in range(20):
	bpy.ops.mesh.primitive_cylinder_add(radius = 1, depth = 100,  location=(random.random()*100, random.random()*100, 0))
	bpy.ops.object.modifier_add(type='COLLISION')

# Camera
layers = 20*[False]
layers[0] = True
cam = Camera.New('ortho')
cam.location = (76.48082733154297, -48.86098861694336, 20.241960525512695)
cam.scale = (24.341266632080078, 24.341266632080078, 24.341266632080078)
scn = Scene.GetCurrent()
ob = scn.objects.new(cam)
scn.setCurrentCamera(ob)

# Import van een vogel-object
bpy.ops.wm.link_append(link=False,instance_groups=False, filename="Bird.blend")
bird = bpy.context.object

# Leeg object dat fungeert als doel dat de vogels zullen volgen
bpy.ops.object.add()
target = bpy.context.object

# De plain met de particles
bpy.ops.mesh.primitive_plane_add(view_align=False, enter_editmode=False);
bpy.context.scene.objects.active = emitter
bpy.ops.object.particle_system_add()    
particleSystem = emitter.particle_systems[-1]
particleSystem.name = 'BirdsPartSystem'
particleSettings = particleSystem.settings
particleSystem.name = 'BirdsPartSettings'

particleSettings.count = 77
particleSettings.frame_start = 1
particleSettings.frame_end = 1
particleSettings.lifetime = 300000.000
particleSettings.emit_from = 'FACE'
particleSettings.use_render_emitter = True
particleSettings.physics_type = 'BOIDS'
particleSettings.particle_size = 0.859
particleSettings.draw_percentage = 1
particleSettings.draw_method = 'RENDER'
particleSettings.dupli_object = cube
particleSettings.material = 1
particleSettings.render_type = 'OBJECT'

bpy.ops.boid.rule_add(type='GOAL')
particleSettings.active_boid_rule.object="target"
goal.object = target
