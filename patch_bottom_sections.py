import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper function to center a section's contents (column, heading, paragraph, image)
def center_section_content(html_content, header_text, img_src_pattern=None):
    # Search for the heading and its containing column
    # We look for the column that contains the specific header
    # Then we modify its style to be a centered vertical flexbox
    
    # 1. Update Column style to center everything
    # We find the heading first
    heading_pattern = rf'<h2 class="wp-block-heading has-text-align-center"[^>]*><strong>{header_text}</strong></h2>'
    match = re.search(heading_pattern, html_content)
    if not match:
        print(f"Heading '{header_text}' not found.")
        return html_content
    
    # Target the specific column containing this header (upwards search)
    # The sections usually follow: <div class="wp-block-column ..."><div class="wp-block-group ..."><h2 ...>
    
    # Simplified approach: Replace specific styles for these 4 sections
    # They all share: style="flex-basis: auto; display: flex; flex-direction: column; align-items: center; text-align: center;"
    # But we want to ensure any internal elements like paragraphs and images are also large and centered.
    
    # 2. Update IMAGE scaling if present
    if img_src_pattern:
        img_pattern = rf'<figure class="wp-block-image size-large"[^>]*><img loading="lazy" src="{img_src_pattern}"[^>]*></figure>'
        new_img_html = f'<figure class="wp-block-image size-large" style="margin: 0 auto; max-width: 800px; padding-bottom: 2rem;"><img loading="lazy" src="{img_src_pattern}" alt="" style="width: 100%; height: auto; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);"/></figure>'
        html_content = re.sub(img_pattern, new_img_html, html_content)

    return html_content

# We'll do direct replacements for clarity and precision on these specific 4 sections

# 1. Concrete as a Material
old_s1_img = '<figure class="wp-block-image size-large" style="margin: 0 auto; max-width: 400px; padding-bottom: 2rem;"><img loading="lazy" src="/uploads/concrete_pouring_mixer_1773538877875.png" alt="Concrete mixing truck pouring wet concrete" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/></figure>'
new_s1_img = '<figure class="wp-block-image size-large" style="margin: 2rem auto; max-width: 800px;"><img loading="lazy" src="/uploads/concrete_pouring_mixer_1773538877875.png" alt="Concrete mixing truck pouring wet concrete" style="width: 100%; height: auto; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.2);"/></figure>'
content = content.replace(old_s1_img, new_s1_img)

# 2. Iconic Structures
old_s2_img = '<figure class="wp-block-image size-large" style="margin: 0 auto; max-width: 400px; padding-bottom: 2rem;"><img loading="lazy" src="/uploads/pantheon_rome_1773538812213.png" alt="The Pantheon in Rome, a historic unreinforced concrete dome" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/></figure>'
new_s2_img = '<figure class="wp-block-image size-large" style="margin: 2rem auto; max-width: 800px;"><img loading="lazy" src="/uploads/pantheon_rome_1773538812213.png" alt="The Pantheon in Rome, a historic unreinforced concrete dome" style="width: 100%; height: auto; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.2);"/></figure>'
content = content.replace(old_s2_img, new_s2_img)

# 3. The Plastic Problem
old_s3_img = '<figure class="wp-block-image size-large" style="margin: 0 auto; max-width: 400px; padding-bottom: 2rem;"><img loading="lazy" src="/uploads/extracted_page8_img1.jpeg" alt="Waste Polylactic Acid (PLA) produced as a byproduct of 3D printing" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"/></figure>'
new_s3_img = '<figure class="wp-block-image size-large" style="margin: 2rem auto; max-width: 800px;"><img loading="lazy" src="/uploads/extracted_page8_img1.jpeg" alt="Waste Polylactic Acid (PLA) produced as a byproduct of 3D printing" style="width: 100%; height: auto; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.2);"/></figure>'
content = content.replace(old_s3_img, new_s3_img)

# 4. What is PLA? (Ensure text is centered and maybe add some vertical breathing room)
# It's already fairly centered, but let's ensure the group it's in is centered.
# Already checked code: align-items: center; text-align: center; max-width: 800px; margin: auto;

# 5. Global cleanup for these columns to ensure no horizontal scroll and consistent max-width
# We ensure the paragraph text doesn't stretch too wide.
content = content.replace('max-width: 800px; margin-left: auto; margin-right: auto;', 'max-width: 900px; margin: 0 auto 2rem auto; font-size: 1.25rem; line-height: 1.6;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied centered formatting and image scaling to the bottom 4 sections.")
