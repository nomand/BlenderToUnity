# Blender To Unity
This blender addon applies axis compensation to nested meshes and hierarchies for export to Unity, resulting in clean gameobject transform.rotation properties. 

Download the zip from [releases](../releases/latest), install using addon manager as usual. 

![Screenshot](/Documentation/header.png)

The addon adds two buttons to the Object context menu (right click in 3D view):
* `Select Hierarchy` is the same as the one in the outliner, allows you to use it in the 3D View.

* `Blender to Unity` preps an object hierarchy for export. Select the parent / root object of a nested asset you want to export, right-click and choose Blender to Unity.

> Make sure to only select the root object of the hierarchy you want to export.

This operation runs the following steps:

1. Selects the entire hierarchy
2. Applies all rotations and scale
3. Starting with the root object, applies 90 degree offsets on the X axis recursively, ignoring every second child object.
4. Selects the entire hierarchy, ready for export.

Export FBX using the following settings:

![FBX Export settings](/Documentation/exportfbx.png)

> This was not tested nor intended for armatures or animated objects.

Pull requests welcome.