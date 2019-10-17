# BlenderToUnity
This blender addon applies axis compensation to nested meshes and hierarchies for export to Unity. It's meant for static meshes, not animated objects or armatures.

![Screenshot](/Documentation/header.png)

The addon adds two buttons to the Object context menu (right click in 3D view):
* `Select Hierarchy` is the same as the one in the outliner, simply selects all children of the active object.

* `Blender to Unity` preps an object hierarchy for export. Select the parent / root object of a nested asset you want to export, right-click and choose Blender to Unity.

This operation runs the following steps:

1. Selects the entire hierarchy
2. Applies all rotations and scale
3. Starting with the root object, applies 90 degree offsets on the X axis recursively, ignoring every second child object.
4. Selects the entire hierarchy, ready for export.

Export FBX using the following settings:

![FBX Export settings](/Documentation/exportfbx.png)