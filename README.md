# Description

The objective of this project was to implement a simple augmented reality application that utilizes AprilTags to recover the camera poses and place virtual objects in a real-world video. AprilTags, which are commonly used in robotics for determining the pose of the camera, were provided in each frame of the video with the 4 corners coordinates (in pixels) and the size of the tags.

Two different approaches were used to recover the camera poses: 1) solving the Perspective-N-Point (PnP) problem with coplanar assumption and 2) solving the Persepective-three-point (P3P) and the Procrustes problem.

The PnP algorithm was implemented by assuming that the AprilTags were coplanar and that the camera was calibrated. The algorithm used the 4 corner coordinates of the AprilTag in the image to compute the extrinsic parameters of the camera.

The P3P algorithm was implemented by assuming that the AprilTag was a planar object and that the camera was calibrated. The algorithm used the 3 non-colinear points of the AprilTag in the image to compute the extrinsic parameters of the camera. The Procrustes problem was then solved to obtain the scale, translation and rotation of the object.

After retrieving the 3D relationship between the camera and world, an arbitrary object was placed in the scene using the computed extrinsic parameters.

The final product was a video that contains several virtual object models as if they existed in the real world. Additionally, the user was able to specify pixel positions to place an arbitrary object.



![vis](https://user-images.githubusercontent.com/89912646/215112938-085c7af6-54d3-4d47-b9a6-2b8244e2b0b1.png)
![VR_res](https://user-images.githubusercontent.com/89912646/215115371-73025e9d-916c-4640-8fbe-e9d2263f3355.gif)
