import bpy

# Set render engine to Eevee for better performance
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Optimize viewport performance
bpy.context.scene.eevee.taa_render_samples = 16
bpy.context.scene.eevee.taa_samples = 8
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720

# Disable heavy effects
bpy.context.scene.eevee.use_bloom = False
bpy.context.scene.eevee.use_ssr = False
bpy.context.scene.eevee.use_volumetric_lights = False
bpy.context.scene.eevee.use_volumetric_shadows = False

# Reduce texture resolution
for image in bpy.data.images:
    if image.size[0] > 1024 or image.size[1] > 1024:
        image.scale(1024, 1024)

# Enable fast mode in viewport
bpy.context.scene.render.use_simplify = True
bpy.context.scene.render.simplify_subdivision = 1
bpy.context.scene.render.simplify_shadow_samples = 4
bpy.context.scene.render.simplify_child_particles = 1.0

# Save the optimized startup file
bpy.ops.wm.save_as_mainfile(filepath=b"C:/Users/YourUser/AppData/Roaming/Blender Foundation/Blender/4.0/config/startup.blend")

print("Blender optimized startup file saved successfully!")
