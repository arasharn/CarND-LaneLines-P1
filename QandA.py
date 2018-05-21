# Test images
for file in files:
	if file[ 0 : 6 ] != "output":
		img = mpimg.imread( "test_images/" + file )
		gray = grayscale( img )
		gray = guassian.blur( gray, 3 )
		edges = canny( gray, 50, 150 )

		# MAsking
		imshape = img.shape 							# Shape of the image
		vertices = np.array( [ [ ( .51 * imshape[ 1 ], imshape[ 0 ] * .58 ), \
			( .49 * imshape[ 1 ], imshape * .58 ), \
			( 0, imshape[ 0 ] ), \
			( imshape[ 1 ], imshape[ 0 ] ) ] ], dtype = np.int32 )
		target = region_of_intrest( edges, vertices ) 	# Masking the image

		# Hough transform
		lines = hough_line( target, 1, np.pi / 180, 35, 5, 2 )

		# blending the results with original images
		result = weighted_img( line, img, α = .8, β = 1.0 )  
		'''
		Other options:
		result = edges ->
		result = target -> Shows the cropped image
		'''

		# Results
		# Converting the CV2 results from BGR to RGB
		r, g, b = cv2.split( result )
		result = cv2.merge( ( b, g, r ) )

		cv2.imwrite( "test_images/output_" + files, result )
		#plt.imshow( result, cmap = "gray" )

# After cell 13
def process_image( image ):
	gray = grayscale( image )
	gray = guassian.blur( gray, 3 )
	edges = canny( gray, 50, 150 )

	# Masking
	imshape = img.shape 							# Shape of the image
	vertices = np.array( [ [ ( .51 * imshape[ 1 ], imshape[ 0 ] * .58 ), \
		( .49 * imshape[ 1 ], imshape * .58 ), \
		( 0, imshape[ 0 ] ), \
		( imshape[ 1 ], imshape[ 0 ] ) ] ], dtype = np.int32 )
	target = region_of_intrest( edges, vertices ) 	# Masking the image

	# Hough transform
	lines = hough_line( target, 1, np.pi / 180, 35, 5, 2 )

	# blending the results with original images
	result = weighted_img( line, image, α = .8, β = 1.0 )   

# Let's try one with solid white lane
white_output = "white.mp4"
clip1 = VideoFileClip( "SolidWhiteRight.mp4" )
white_clip = clip1.f1_image( process_image ) # NOTE: This function expects color images!!
%time white_clip.write_videofile( white_output, audio = False ) 

#%%
# For draw_line
draw_line:

rigth/left centers list
right/left slop list

rm = []
lm = []
rc = []
lc = []

'''
iterate through each line points ( x1, y1, x2, y2 )
'''

# Calculate slope and centers
slope = ( y2 - y1 ) / ( x2 - x1 )
centers = [ ( x2 + x1 ) / 2, ( y2 + y1 ) / 2 ]

'''
seperate right and left by measuring slope, throw out steep vertical slopes
'''

# Example
'''
if slope is between 0 and some small posetive number then put the slope and 
center values in the right lists

if slope is between 0 and some small negative number then put the slope and 
center values in the left lists
'''

# average over all right/ left center, slope values to get single center and slope
r_slope = np.sum( rm ) / len( rm )
l_slope = np.sum( lm ) / len( lm )

r_center = np.divide( np.sum( rc, axis = 0 ), len( rc ) )
l_center = np.divide( np.sum( lc, axis = 0 ), len( lc ) )

'''
specify line height maybe could just be half of way point of image height
'''

'''
find new ( x1, y1, x2, y2 ) from using center and slope values and fitting to
bottom of image and specified height
'''
'''
( y - y' ) = M ( x - x' ) we know ( x, y ) its he center and we know M the slope
we can find the x1, x2 values by calculating x' from plugging in y' as specified
height or image bottom
'''


