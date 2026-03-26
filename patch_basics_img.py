import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Enlarge the foreground image (concreteblocks.jpg)
# Previous style was width:848px;height:auto
old_img_tag = '<img loading="lazy" width="2000" height="1125" src="https://changingconcrete.org/uploads/concreteblocks.jpg" alt="" class="wp-image-14" style="width:848px;height:auto" />'
new_img_tag = '<img loading="lazy" width="2000" height="1125" src="https://changingconcrete.org/uploads/concreteblocks.jpg" alt="" class="wp-image-14" style="width:100%; max-width:1100px; height:auto; border-radius:12px; box-shadow: 0 15px 45px rgba(0,0,0,0.3);" />'
content = content.replace(old_img_tag, new_img_tag)

# 2. Shrink the background image (concrete-wall.jpg) to fit
# We change data-object-fit="cover" to "contain" and add an inline style to override object-fit
old_bg_tag = '<img loading="lazy" width="1200" height="675" class="wp-block-cover__image-background background-opacity wp-image-27" alt="" src="https://changingconcrete.org/uploads/concrete-wall.jpg" data-object-fit="cover" />'
new_bg_tag = '<img loading="lazy" width="1200" height="675" class="wp-block-cover__image-background background-opacity wp-image-27" alt="" src="https://changingconcrete.org/uploads/concrete-wall.jpg" data-object-fit="contain" style="object-fit: contain !important; opacity: 0.2 !important;" />'
content = content.replace(old_bg_tag, new_bg_tag)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated Basics section: enlarged foreground image and contained background image.')
