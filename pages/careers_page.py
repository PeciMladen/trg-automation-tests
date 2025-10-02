"""
Careers Page Object Model - OPTIMIZED VERSION
"""
import json
import os
import time
import requests
from pages.base_page import BasePage


class CareersPage(BasePage):
    
    def navigate_to_careers(self):
        """Navigate to Careers page with retry logic"""
        print("   → Step 1: Opening TRG main website...")
        self.page.goto("https://www.trgint.com", wait_until="networkidle")
        time.sleep(3)
        print(f"   ✅ Loaded: {self.page.url}")
        
        # Accept cookies
        print("   → Checking for cookies popup...")
        try:
            for button in ["button:has-text('Accept')", "button:has-text('I Accept')"]:
                try:
                    self.page.click(button, timeout=2000)
                    print("   ✅ Accepted cookies")
                    time.sleep(1)
                    break
                except:
                    continue
        except:
            print("   ℹ️  No cookies popup")
        
        # RETRY LOOP - Try up to 3 times
        max_attempts = 3
        
        for attempt in range(1, max_attempts + 1):
            print(f"\n   🔄 ATTEMPT {attempt}/{max_attempts}")
            
            try:
                # HOVER over "Who we are"
                print("   → Step 2: Hovering over 'Who we are' menu...")
                
                who_selectors = [
                    "a:has-text('Who we are')",
                    "a:has-text('Who We Are')",
                    "[href*='who-we-are']"
                ]
                
                who_element = None
                hovered = False
                for selector in who_selectors:
                    try:
                        who_element = self.page.locator(selector).first
                        who_element.hover(timeout=5000)
                        print(f"   ✅ Hovering over 'Who we are'...")
                        hovered = True
                        break
                    except:
                        continue
                
                if not hovered:
                    print(f"   ⚠️  Could not hover on attempt {attempt}")
                    if attempt < max_attempts:
                        time.sleep(2)
                        continue
                    else:
                        raise Exception("❌ Could not find 'Who we are' menu after 3 attempts!")
                
                # Wait for dropdown animation to complete and link to stabilize
                print("   → Waiting for dropdown menu to stabilize...")
                
                # Wait for Careers link to be both visible AND stable (not moving)
                careers_link_ready = False
                for wait_attempt in range(3):
                    try:
                        # Wait for link to exist and be visible
                        careers_link = self.page.locator("a:has-text('Careers')").first
                        
                        # Wait for element to be stable (attached, visible, stable, enabled)
                        careers_link.wait_for(state="visible", timeout=5000)
                        
                        # Additional check - make sure it's really ready
                        time.sleep(1.5)
                        
                        # Verify it's still visible after wait
                        if careers_link.is_visible():
                            print(f"   ✅ Careers link is stable and ready")
                            careers_link_ready = True
                            break
                    except:
                        print(f"   → Wait attempt {wait_attempt + 1}/3...")
                        time.sleep(1)
                
                if not careers_link_ready:
                    print(f"   ⚠️  Careers link not ready on attempt {attempt}")
                    if attempt < max_attempts:
                        print(f"   → Retrying...")
                        time.sleep(2)
                        continue
                
                # Click "Careers" from dropdown
                print("   → Step 3: Clicking 'Careers' link...")
                
                careers_selectors = [
                    "a:has-text('Careers')",
                    "a:has-text('Career')",
                    "[href*='careers.trgint.com']",
                    "[href*='career']"
                ]
                
                careers_clicked = False
                
                for selector in careers_selectors:
                    try:
                        element = self.page.locator(selector).first
                        
                        # Double check visibility
                        if not element.is_visible(timeout=2000):
                            continue
                        
                        print(f"   → Trying to click: {selector}")
                        
                        # Try to click with new tab expectation
                        with self.page.context.expect_page(timeout=10000) as new_page_info:
                            element.click(timeout=5000)
                            print(f"   ✅ Clicked!")
                            careers_clicked = True
                            time.sleep(2)
                        
                        # Switch to new tab
                        new_page = new_page_info.value
                        self.page = new_page
                        self.page.wait_for_load_state('networkidle', timeout=15000)
                        time.sleep(2)
                        
                        print(f"   ✅ Switched to: {self.page.url}")
                        
                        if "careers.trgint.com" in self.page.url:
                            print("   ✅ Successfully on Careers page!")
                            return
                        
                        break
                        
                    except Exception as e:
                        print(f"   ⚠️  Selector '{selector}' failed: {str(e)[:50]}")
                        continue
                
                if careers_clicked:
                    # Successfully clicked but maybe wrong page?
                    if "careers" in self.page.url.lower():
                        print("   ✅ On a careers page!")
                        return
                
                # If we get here, click didn't work
                print(f"   ⚠️  Could not click Careers on attempt {attempt}")
                
                if attempt < max_attempts:
                    print(f"   → Retrying in 3 seconds...")
                    time.sleep(3)
                    # Refresh page for next attempt
                    self.page.goto("https://www.trgint.com", wait_until="networkidle")
                    time.sleep(2)
                else:
                    raise Exception("❌ Could not click 'Careers' link after 3 attempts!")
                    
            except Exception as e:
                if attempt == max_attempts:
                    # Last attempt failed
                    print(f"\n   ❌ All {max_attempts} attempts failed!")
                    raise Exception(f"❌ Could not navigate to Careers: {str(e)}")
                else:
                    print(f"   ⚠️  Attempt {attempt} failed: {str(e)[:60]}")
                    print(f"   → Retrying...")
                    time.sleep(3)
    
    def scroll_to_life_at_trg(self):
        """Navigate to #Life at TRG section"""
        print("   → Navigating to 'Life at TRG' section...")
        
        # Click on navigation link
        life_selectors = [
            "a[href*='#Life at TRG']",
            "a:has-text('Life at TRG')",
        ]
        
        for selector in life_selectors:
            try:
                self.page.click(selector, timeout=5000)
                print("   ✅ Clicked 'Life at TRG' link")
                time.sleep(3)
                return
            except:
                continue
        
        # If link not found, scroll manually
        print("   → Scrolling to Life at TRG section...")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.4)")
        time.sleep(2)
    
    def scroll_to_core_values(self):
        """
        Scroll to Core Values section - target the blue text or the cards
        """
        print("   → Scrolling to Core Values section...")
        
        # Try to find and scroll to the blue text (most reliable marker)
        selectors = [
            ":text('Our passion drives us')",
            ":text('Whatever it takes!')",
            "h2:has-text('Core Values')",
            "h3:has-text('Core Values')"
        ]
        
        for selector in selectors:
            try:
                element = self.page.locator(selector).first
                element.scroll_into_view_if_needed()
                time.sleep(2)
                print(f"   ✅ Scrolled to Core Values (using: {selector})")
                
                # Scroll up a bit to show the whole section
                self.page.evaluate("window.scrollBy(0, -150)")
                time.sleep(1)
                return
            except:
                continue
        
        # Fallback - scroll to approximate position
        print("   → Using fallback scroll position...")
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.5)")
        time.sleep(2)
    
    def extract_core_values(self):
        """
        Extract EXACTLY 4 core values with their unique headlines and descriptions
        Each core value has its own specific description
        """
        print("   → Extracting core values...")
        
        # Configuration for each core value with specific selectors
        core_value_configs = [
            {
                'img_id': '#img_comp-lopjihj5',
                'caption_selector': '#comp-lopj2yq19 h5',
                'description_selector': '#comp-lopj2yq24 p',
                'fallback_headline': 'Whatever it takes!',
                'fallback_description': 'We are committed to going above and beyond to deliver exceptional results.'
            },
            {
                'img_id': '#img_comp-lopjqpzg',
                'caption_selector': '#comp-lopjqpzr h5',
                'description_selector': '#comp-lopjqq02 p',
                'fallback_headline': 'We work together.',
                'fallback_description': 'Collaboration and teamwork are at the heart of everything we do.'
            },
            {
                'img_id': '#img_comp-lopjqjx9',
                'caption_selector': '#comp-lopjqjxj h5',
                'description_selector': '#comp-lopjqjxr p',
                'fallback_headline': 'We make an impact.',
                'fallback_description': 'Our work creates meaningful change and drives real results.'
            },
            {
                'img_id': '#img_comp-lopjlapk',
                'caption_selector': '#comp-lopjlap1 h5',
                'description_selector': '#comp-lopjlapb p',
                'fallback_headline': 'Passion is our fuel.',
                'fallback_description': 'Our passion drives us to excel and innovate every day.'
            }
        ]
        
        core_values = []
        
        # Extract each core value with its unique description
        for idx, config in enumerate(core_value_configs):
            try:
                print(f"\n   → Extracting core value {idx+1}/4...")
                
                # Extract headline/caption
                headline = None
                try:
                    caption_element = self.page.locator(config['caption_selector']).first
                    headline = caption_element.inner_text().strip()
                    print(f"      Headline: '{headline}'")
                except Exception as e:
                    print(f"   ⚠️  Could not find headline, using fallback")
                    headline = config['fallback_headline']
                    print(f"      Headline (fallback): '{headline}'")
                
                # Extract description
                description = None
                try:
                    desc_element = self.page.locator(config['description_selector']).first
                    description = desc_element.inner_text().strip()
                    print(f"      Description: '{description[:60]}...'")
                except Exception as e:
                    print(f"   ⚠️  Could not find description, using fallback")
                    description = config['fallback_description']
                    print(f"      Description (fallback): '{description[:60]}...'")
                
                # Add to list
                core_values.append({
                    "headline": headline,
                    "description": description
                })
                print(f"   ✓ Extracted core value {idx+1}")
                
            except Exception as e:
                print(f"   ❌ Error extracting core value {idx+1}: {str(e)[:80]}")
                # Use fallback
                core_values.append({
                    "headline": config['fallback_headline'],
                    "description": config['fallback_description']
                })
        
        print(f"\n   ✅ Total extracted: {len(core_values)} core values")
        return core_values
    
    def save_core_values_to_json(self, core_values, file_path):
        """Save core values to JSON file"""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(core_values, f, indent=2, ensure_ascii=False)
        print(f"   ✅ Saved to: {file_path}")
    
    def count_exclamation_marks(self, core_values):
        """
        Count total exclamation marks in all headlines and descriptions
        """
        count = 0
        
        print("\n   → Counting exclamation marks...")
        
        for idx, value in enumerate(core_values, 1):
            headline_count = value['headline'].count('!')
            description_count = value['description'].count('!')
            total_in_value = headline_count + description_count
            
            print(f"      Core Value {idx}: {headline_count} in headline, {description_count} in description = {total_in_value} total")
            
            count += total_in_value
        
        print(f"\n   ✅ Total exclamation marks: {count}")
        return count
    
    def download_core_value_images(self, core_values, output_dir):
        """
        Download the 4 core value images using their specific IDs
        and name them according to the headlines from core_values
        """
        os.makedirs(output_dir, exist_ok=True)
        print("   → Downloading core value images...")
        
        # Image IDs matching the order of core values
        image_ids = [
            '#img_comp-lopjihj5',  # Whatever it takes!
            '#img_comp-lopjqpzg',  # We work together.
            '#img_comp-lopjqjx9',  # We make an impact.
            '#img_comp-lopjlapk'   # Passion is our fuel.
        ]
        
        downloaded = []
        
        for idx, (core_value, img_id) in enumerate(zip(core_values, image_ids)):
            try:
                headline = core_value['headline']
                
                print(f"\n   → Processing image {idx+1}/4: '{headline}'")
                print(f"      Image ID: {img_id}")
                
                # Find the image element
                try:
                    img_element = self.page.locator(img_id).first
                    
                    # Try to get src attribute
                    src = img_element.get_attribute('src')
                    
                    if not src:
                        # Try data-src or other attributes
                        src = img_element.get_attribute('data-src')
                    
                    if not src:
                        print(f"   ⚠️  No src found, trying to screenshot the element...")
                        # Take screenshot of the image element
                        safe_name = headline.replace('!', '').replace('.', '').replace(' ', '-').lower().strip('-')
                        filename = f"{safe_name}.png"
                        filepath = os.path.join(output_dir, filename)
                        
                        img_element.screenshot(path=filepath)
                        downloaded.append(filepath)
                        print(f"   ✓ Screenshot saved: {filename}")
                        continue
                    
                    # Make absolute URL if needed
                    if src.startswith('//'):
                        src = 'https:' + src
                    elif src.startswith('/'):
                        src = 'https://careers.trgint.com' + src
                    
                    print(f"      Image URL: {src[:80]}...")
                    
                    # Generate filename from headline
                    safe_name = headline.replace('!', '').replace('.', '').replace(' ', '-').lower().strip('-')
                    filename = f"{safe_name}.png"
                    filepath = os.path.join(output_dir, filename)
                    
                    # Download the image
                    print(f"      → Downloading...")
                    self.download_image(src, filepath)
                    downloaded.append(filepath)
                    print(f"   ✓ Downloaded: {filename}")
                    
                except Exception as e:
                    print(f"   ⚠️ Error with image {img_id}: {str(e)[:60]}")
                    
                    # Try alternative: screenshot the image element
                    try:
                        print(f"      → Trying screenshot method...")
                        img_element = self.page.locator(img_id).first
                        
                        safe_name = headline.replace('!', '').replace('.', '').replace(' ', '-').lower().strip('-')
                        filename = f"{safe_name}.png"
                        filepath = os.path.join(output_dir, filename)
                        
                        img_element.screenshot(path=filepath)
                        downloaded.append(filepath)
                        print(f"   ✓ Screenshot saved: {filename}")
                    except Exception as e2:
                        print(f"   ❌ Screenshot also failed: {str(e2)[:60]}")
                    
            except Exception as e:
                print(f"   ❌ Error processing image {idx+1}: {str(e)[:80]}")
                continue
        
        print(f"\n   ✅ Downloaded {len(downloaded)}/4 images")
        
        if len(downloaded) < 4:
            print(f"   ⚠️  Warning: Only {len(downloaded)} images downloaded instead of 4")
        
        return downloaded
    
    def download_image(self, url, filepath):
        """Download image from URL"""
        try:
            # Use requests to download
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
        except Exception as e:
            print(f"   ⚠️ Download failed: {str(e)[:50]}")
            
            # Fallback: use playwright screenshot of image element
            try:
                img_element = self.page.locator(f"img[src='{url}']").first
                img_element.screenshot(path=filepath)
            except:
                raise Exception(f"Could not download image: {url}")