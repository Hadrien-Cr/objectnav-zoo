# [Mod-IIN](https://arxiv.org/pdf/2304.01192)

$\texttt{Mod-IIN}$ (https://arxiv.org/pdf/2304.01192) is a modular architecture for image instance navigation, which leverages a vision model "SuperGLUE" for matching the current observation with the goal image. The exploration is handled by FBE, and the method does not require extra fine tuning
<figure>
    <img src="assets/mod_IIN.png" width="800">
    <figcaption>From the article.</figcaption>
</figure>

Perception Modules:
- 2D Obstacle Mapping using Ground-Truth Depth Observation
- From Target Image I_goal:
    - Decompose into (background + object mask) using Detic
    - Each observed frame I_t has K keypoints in common with I_goal computed with SuperGLUE
    - If enough keypoints are in the object mask with high enough confidence threshold, this is a detection, keypoints are backprojected to goal 2D map.