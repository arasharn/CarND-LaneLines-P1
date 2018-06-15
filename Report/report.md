<div style="text-align: justify">   
# **Finding Lane Lines on the Road**    
### Arash Nouri

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:

* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

[//]: # (Image References)

[Fig1]: ./solidWhiteRight.jpg "Raw image"
[Fig2]: ./gray_solidWhiteRight.jpg "Grayscale"
[Fig3]: ./edges_solidWhiteRight.jpg "Edges"
[Fig4]: ./target_solidWhiteRight.jpg "Masking"
[Fig5]: ./masked_region.png "Masked region"
[Fig6]: ./output_solidWhiteCurve.jpg "Output"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

#### An overview on the pipeline

The pipeline consists of 5 steps that each step was addressed by using image in [Figure 1][Fig1]  
![Figure 1][Fig1]

 1. First the image converted to grayscale by using `cv2.cvtColor`. Also, a gaussian noise kernel was applied to the image to reduce the noise of the images and helps to detect the edges better ([Figure 2][Fig2]).   
![Figure 2][Fig2]
 2.  In the next step, an edge detectio analysis was done by using the Canny algorithm (`cv2.Canny`) on the [Figure 2][Fig2]. The result is shown in [Figure 3][Fig3].
![Figure 3][Fig3]
 3. To improved the results and prune unwanted edges, a mask was define. It should be noted that for defining the mask it was assumed that camera location is constatnt and `cv2.fillPoly` was used for defining the masked area. [Figure 4][Fig4] shows the results after the mask.   
![Figure 4][Fig4]  
It should be mentioned, for definng the mask easier the mask was also plotted on the image ([Figure 5][Fig5]). This plot helps alot for defining a suitable windows for images.    
![Figure 5][Fig5]
 4. In the $4^{th}$ step, Hough line transform was used to draw line that pass through all the hough line. `cv2.HoughLinesP` was used for this task. 
 5. Finally in the last step, the results of hough transform lines was blended with the orginal image ([Figure 6][Fig6]) by using `cv2.addWeighted` function.     
![Figure 6][Fig6]

#### Improve `draw_lines` function
This function works base don the outout of the out out of the Hough transofrom. For making this function better to give a overall line in noth right nd left sides: 
 
 1. first starting and finishing coordinates of each lines were extracted
 2. Then  the slope and the center of each lines were calculated
 3. The points, their slopes, and their centers were grouped based on the values of their slope to right and left side ccordinates. In fact, if the value of the slope is negative and small the line was in the left side and whenever the slope values are posetive and small the line belongs to the right hand side fo the road. A threshhold was defined here for bothe negative and posetive slopes to rempve the vertical, orizental, or any line with large slope from the line. This threshhold helps the algorythm to have cleanear and more robust outputs
 4. Next, maximum and minimum $y$s from each side were extracted and by using the average slopes and averaged center coordinates of each side their $x$ values were calculated.
 5. Finally two lines will be drawn in each side of the road by using the caluculated maximum and minimum  coordinates from previous step 

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when there is a curve in the video. In the current version the maximum height was chosen carefully to avoid this problem. But for more advanced version a curve drawing function can be defined to avoid this problem. 

As mentioned previously, another shortcoming is the fact that the maximum height in masking function was chosen carefully but it might cause problem for more complicated road or vehicle with higher velocities


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to define a function to draw curve line instead of the straight line for the more curvy roads.

Another potential improvement could be to tune the edge detector and hough transfor line functions. Thus, the maxmimum height of the mask can be increased to cover the roads completely to its end.
