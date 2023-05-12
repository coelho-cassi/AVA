# blender --background --python C:\Users\jnchi\Documents\Current_Classes\CS-4391_(Senior_Project_II)\Workplace\runBlender.py -- C:\Users\jnchi\Documents\Current_Classes\CS-4391_(Senior_Project_II)\Workplace\template.blend C:\Users\jnchi\Documents\Current_Classes\CS-4391_(Senior_Project_II)\Workplace\test.blend C:\Users\jnchi\Documents\Current_Classes\CS-4391_(Senior_Project_II)\Workplace\sample1.mp3 C:\Users\jnchi\Documents\Current_Classes\CS-4391_(Senior_Project_II)\Workplace\vocals.wav

# How to run:
# blender --background --python [PATH TO PYTHON FILE] -- [PATH TO SRC .BLEND FILE] [PATH TO DEST .BLEND FILE] [PATH TO MAIN MP3 FILE] [PATH TO LYRIC MP3 FILE]

import os
import sys

argz = sys.argv[sys.argv.index("--") + 1:]

import bpy

def reset_blend():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
def get_context_area(context, context_dict, area_type='GRAPH_EDITOR',
                     context_screen=False):
    '''
    context : the current context
    context_dict : a context dictionary. Will update area, screen, scene, 
                   area, region
    area_type: the type of area to search for
    context_screen: Boolean. If true only search in the context screen.
    '''
    if not context_screen:  # default
        screens = bpy.data.screens
    else:
        screens = [context.screen]
    for screen in screens:
        for area_index, area in screen.areas.items():
            if area.type == area_type:
                for region in area.regions:
                    if region.type == 'WINDOW':
                        context_dict["area"] = area
                        context_dict["screen"] = screen
                        context_dict["scene"] = context.scene
                        context_dict["window"] = context.window
                        context_dict["region"] = region
                        return area
    return None

if __name__ == "__main__":
    reset_blend()
    try:
        filepath_src = argz[0]
        filepath_dst = argz[1]
        musicFP = argz[2]
        lyricsFP = argz[3]
        bpy.ops.wm.open_mainfile(filepath=os.path.abspath(filepath_src))
        
        # Do stuff here
        c = bpy.context.copy()
        
        # Bake Lyrics to Driver
        obj = bpy.data.objects["Driver"]
        obj.select_set(True)
        get_context_area(bpy.context, c)
        bpy.ops.graph.sound_bake(c, filepath=os.path.abspath(lyricsFP))
        
        # Bake Main Music to Head Rotation
        obj = bpy.data.objects["Cube"]
        obj.select_set(True)
        get_context_area(bpy.context, c)
        bpy.ops.graph.sound_bake(c,filepath=os.path.abspath(musicFP))    
        
        bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(filepath_dst), check_existing=False)
    except Exception as e:
        print("Some error occurred")
        print(e)
        pass