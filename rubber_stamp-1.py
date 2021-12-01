#!/usr/bin/env python

# rubber_stamp.py Release 7
# Created by Tin Tran http://gimplearn.net
#
# License: GPLv3
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# To view a copy of the GNU General Public License
# visit: http://www.gnu.org/licenses/gpl.html
#
#
# ------------
#| Change Log |
# ------------
# Rel 1: Initial release.
# Rel 2: Leave on transparent layer (requested by Issabella)
# Rel 3: Added Invert Stamp option and merge option
# Rel 4: Leave mask unapplied option.
# Rel 5: decode('utf-8') text inputs (specified by MareroQ on GC)
# Rel 6: Load png or jpg or gif
# Rel 7: Loads distress files even if extension are different than lowercase() (contributed by Madlbsy)
from gimpfu import *
import math
#from array import array
#import sys
def python_tt_rubber_stamp(image, layer, distress_file, font, top_text, middle_text, bottom_text, invert, merge, leave_mask):
	#pdb.gimp_image_undo_group_start(image)
	pdb.gimp_context_push()
	#core code goes here/below
	top_text = top_text.decode("utf-8")
	middle_text = middle_text.decode("utf-8")
	bottom_text = bottom_text.decode("utf-8")
	width, height = 1000, 1000
	midx, midy = width/2, height/2
	new_img = pdb.gimp_image_new(width,height,RGB)
	new_display = pdb.gimp_display_new(new_img)

	#create a white background
	white_background = pdb.gimp_layer_new(new_img,width,height,RGBA_IMAGE,"White background",100,LAYER_MODE_NORMAL)
	pdb.gimp_image_insert_layer(new_img,white_background,None,0)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_edit_fill(white_background,FILL_FOREGROUND)

	#create a working layer
	work_layer = pdb.gimp_layer_new(new_img,width,height,RGBA_IMAGE,"Work layer",100,LAYER_MODE_NORMAL)
	pdb.gimp_image_insert_layer(new_img,work_layer,None,0)
	pdb.gimp_context_set_foreground((0,0,0))

	mid_bar_height = 194
	line_width = 14
	#draw middle bar
	pdb.gimp_image_select_rectangle(new_img,CHANNEL_OP_REPLACE,100,midy-(mid_bar_height/2),800,mid_bar_height)
	pdb.gimp_image_select_rectangle(new_img,CHANNEL_OP_SUBTRACT,100,midy-(mid_bar_height/2)+line_width,800,mid_bar_height-(line_width*2))
	pdb.gimp_edit_fill(work_layer,FILL_FOREGROUND)

	#draw outer dotted circle
	pdb.gimp_context_set_brush("2. Hardness 100")
	pdb.gimp_context_set_brush_size(line_width)
	pdb.gimp_context_set_brush_spacing(2.0)
	pdb.gimp_context_set_brush_hardness(1.0)
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_REPLACE,0,0,width,height)
	pdb.gimp_selection_shrink(new_img,line_width/2)
	pdb.plug_in_sel2path(new_img,work_layer)
	circle_path = pdb.gimp_image_get_active_vectors(new_img)
	pdb.gimp_selection_none(new_img)
	pdb.gimp_drawable_edit_stroke_item(work_layer,circle_path)

	#draw large solid outer circle
	large_circle_width = width - (18*2)
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_REPLACE,\
		midx-large_circle_width/2,midy-large_circle_width/2,\
		large_circle_width,large_circle_width)
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_SUBTRACT,\
		midx-large_circle_width/2+line_width,midy-large_circle_width/2+line_width,\
		large_circle_width-line_width*2,large_circle_width-line_width*2)
	pdb.gimp_edit_fill(work_layer,FILL_FOREGROUND)

	#clear circular white space where text will be written
	small_circle_width = width - (148*2)
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_REPLACE,\
		midx-large_circle_width/2+line_width,midy-large_circle_width/2+line_width,\
		large_circle_width-line_width*2,large_circle_width-line_width*2)
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_SUBTRACT,\
		midx-small_circle_width/2,midy-small_circle_width/2,\
		small_circle_width,small_circle_width)
	pdb.gimp_edit_clear(work_layer)

	#draw inner circle
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_REPLACE,\
		midx-small_circle_width/2,midy-small_circle_width/2,\
		small_circle_width,small_circle_width)		
	pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_SUBTRACT,\
		midx-small_circle_width/2+line_width,midy-small_circle_width/2+line_width,\
		small_circle_width-line_width*2,small_circle_width-line_width*2)
	pdb.gimp_edit_fill(work_layer,FILL_FOREGROUND)
	
	font_target_height = 115
	circle_text = top_text + bottom_text #just get height of all the circular text
	pdb.gimp_progress_init("Searching for font size of circular text",None)
	font_size = 1
	while True: #maximize height exit when we get a larger height
		t_width,t_height,t_ascent,t_descent = pdb.gimp_text_get_extents_fontname(circle_text,font_size,0,font)
		if t_height <= font_target_height: #this is the best one so far
			circle_font_size = font_size  #save it
			pdb.gimp_progress_update(t_height*1.0/font_target_height)
		else: #larger than target height exit loop
			break
		font_size+=1 #increment font size for next time through loop

	
	radius = ((large_circle_width + small_circle_width)/2.0 - line_width)/2.0
	#get a total width	
	t_width,t_height,t_ascent,t_descent = pdb.gimp_text_get_extents_fontname(top_text,circle_font_size,0,font)
	total_width = t_width
	#put each letter in it's place for top text
	top_span_degrees = 120
	start_angle = 270 - (top_span_degrees/2.0)
	for i in range(0,len(top_text)):
		_width,_height,_ascent,_descent = pdb.gimp_text_get_extents_fontname(top_text[0:i+1],circle_font_size,0,font)
		c_width,c_height,c_ascent,c_descent = pdb.gimp_text_get_extents_fontname(top_text[i:i+1],circle_font_size,0,font)
		rel_x_location = _width - c_width/2.0 #center of letter on string
		x_fraction = rel_x_location*1.0/total_width
		x_angle = math.radians(start_angle + (x_fraction * top_span_degrees))
		x = midx + math.cos(x_angle) * radius
		y = midy + math.sin(x_angle) * radius
		t_layer = pdb.gimp_text_fontname(new_img,None,0,0,top_text[i:i+1],0,TRUE,circle_font_size,0,font)
		pdb.gimp_layer_set_offsets(t_layer,x-c_width/2.0,y-c_height/2.0)
		rotate_angle = x_angle - math.radians(270)
		rotated_item = pdb.gimp_item_transform_rotate(t_layer,rotate_angle,FALSE,x,y)
		work_layer = pdb.gimp_image_merge_down(new_img,rotated_item,EXPAND_AS_NECESSARY)

	#get a total width	
	t_width,t_height,t_ascent,t_descent = pdb.gimp_text_get_extents_fontname(bottom_text,circle_font_size,0,font)
	total_width = t_width	
	#put each letter in it's place for bottom text
	bottom_span_degrees = 120
	start_angle = 90 + (bottom_span_degrees/2.0)
	for i in range(0,len(bottom_text)):
		_width,_height,_ascent,_descent = pdb.gimp_text_get_extents_fontname(bottom_text[0:i+1],circle_font_size,0,font)
		c_width,c_height,c_ascent,c_descent = pdb.gimp_text_get_extents_fontname(bottom_text[i:i+1],circle_font_size,0,font)
		rel_x_location = _width - c_width/2.0 #center of letter on string
		x_fraction = rel_x_location*1.0/total_width
		x_angle = math.radians(start_angle - (x_fraction * bottom_span_degrees))
		x = midx + math.cos(x_angle) * radius
		y = midy + math.sin(x_angle) * radius
		t_layer = pdb.gimp_text_fontname(new_img,None,0,0,bottom_text[i:i+1],0,TRUE,circle_font_size,0,font)
		pdb.gimp_layer_set_offsets(t_layer,x-c_width/2.0,y-c_height/2.0)
		rotate_angle = x_angle - math.radians(90)
		rotated_item = pdb.gimp_item_transform_rotate(t_layer,rotate_angle,FALSE,x,y)
		work_layer = pdb.gimp_image_merge_down(new_img,rotated_item,EXPAND_AS_NECESSARY)
	

	font_target_height = 166
	pdb.gimp_progress_init("Searching for font size of middle text",None)
	font_size = 1
	while True: #maximize height exit when we get a larger height
		t_width,t_height,t_ascent,t_descent = pdb.gimp_text_get_extents_fontname(middle_text,font_size,0,font)
		if t_height <= font_target_height: #this is the best one so far
			middle_font_size = font_size  #save it
			pdb.gimp_progress_update(t_height*1.0/font_target_height)
		else: #larger than target height exit loop
			break
		font_size+=1 #increment font size for next time through loop

	#get a total width	
	t_width,t_height,t_ascent,t_descent = pdb.gimp_text_get_extents_fontname(middle_text,middle_font_size,0,font)
	total_width = t_width
	#put each letter in it's place for middle text
	middle_span_width = (midx - 205)*2.0
	start_x = midx - (middle_span_width/2.0)
	for i in range(0,len(middle_text)):
		_width,_height,_ascent,_descent = pdb.gimp_text_get_extents_fontname(middle_text[0:i+1],middle_font_size,0,font)
		c_width,c_height,c_ascent,c_descent = pdb.gimp_text_get_extents_fontname(middle_text[i:i+1],middle_font_size,0,font)
		rel_x_location = _width - c_width/2.0 #center of letter on string
		x_fraction = rel_x_location*1.0/total_width
		x = start_x + (x_fraction * middle_span_width)
		y = midy
		t_layer = pdb.gimp_text_fontname(new_img,None,0,0,middle_text[i:i+1],0,TRUE,middle_font_size,0,font)
		pdb.gimp_layer_set_offsets(t_layer,x-c_width/2.0,y-c_height/2.0)
		work_layer = pdb.gimp_image_merge_down(new_img,t_layer,EXPAND_AS_NECESSARY)
	



	#loads distress image .jpg or .png and copy it
	loaders = {
		'jpg': pdb.file_jpeg_load,
		'jpeg': pdb.file_jpeg_load,
		'png': pdb.file_png_load,
		'gif': pdb.file_gif_load,
	}
	extension = distress_file.rsplit('.', 1)[1].lower()
	distress_img = loaders[extension](distress_file,distress_file)
	distress_layer = pdb.gimp_image_get_active_layer(distress_img)
	pdb.gimp_selection_all(distress_img)
	pdb.gimp_edit_copy(distress_layer)

	#if invert, put it on white background circle, merge, invert it, color-to-alpha white
	if invert == 1:
		white_circle_layer = pdb.gimp_layer_new(new_img,width,height,RGBA_IMAGE,"White circle layer",100,LAYER_MODE_NORMAL)
		pdb.gimp_image_insert_layer(new_img,white_circle_layer,None,1)
		pdb.gimp_context_set_foreground((255,255,255))
		pdb.gimp_image_select_ellipse(new_img,CHANNEL_OP_REPLACE,\
			0,0,\
			width,height)
		pdb.gimp_edit_fill(white_circle_layer,FILL_FOREGROUND)
		pdb.gimp_selection_none(new_img)
		work_layer = pdb.gimp_image_merge_down(new_img,work_layer,EXPAND_AS_NECESSARY)
		pdb.gimp_drawable_invert(work_layer,FALSE)
		pdb.plug_in_colortoalpha(new_img,work_layer,(255,255,255))

	#add as a mask and apply it
	mask = pdb.gimp_layer_create_mask(work_layer,ADD_MASK_WHITE)
	pdb.gimp_layer_add_mask(work_layer,mask)
	floating_sel = pdb.gimp_edit_paste(mask,TRUE)
	pdb.gimp_floating_sel_anchor(floating_sel)
	if leave_mask == 0:
		pdb.gimp_layer_remove_mask(work_layer,MASK_APPLY)
	if merge == 1:
		work_layer = pdb.gimp_image_merge_down(new_img,work_layer,EXPAND_AS_NECESSARY)

	#remove distress iamge
	pdb.gimp_image_delete(distress_img)

	
	#UNCOMMENT BELOW WHEN DONE
	pdb.gimp_context_pop()
	#pdb.gimp_image_undo_group_end(image)
	pdb.gimp_displays_flush()
    #return

register(
	"python_fu_tt_rubber_stamp",                           
	"Create Rubber Stamp",
	"Create Rubber Stamp",
	"Tin Tran",
	"Tin Tran",
	"March 2019",
	"<Image>/Python-Fu/Create New/Rubber Stamp...",             #Menu path
	"RGB*, GRAY*", 
	[
	(PF_FILE, "distress_file", "distress .png/.jpg/.jpeg/.gif file:", 0),
	(PF_FONT, "font", "Font:", "Sans"),
	(PF_STRING, "top_text", "Top-Arc Text:", "PAID IN FULL"),
	(PF_STRING, "middle_text", "Middle-Line Text:", "5:15 PM"),
	(PF_STRING, "bottom_text", "Bottom-Arc Text:", "THANK-YOU"),
	(PF_TOGGLE, "invert", "Invert Stamp (Solid fill with transparent text):", 0),
	(PF_TOGGLE, "merge", "Merge down (useful for copying to use Clipboard Mask brush):", 0),
	(PF_TOGGLE, "leave_mask", "Leave Mask unapplied:", 0),
	],
	[],
	python_tt_rubber_stamp)

main()
