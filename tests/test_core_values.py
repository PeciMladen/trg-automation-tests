"""
Test suite for Core Values extraction
"""
import pytest
import os
import json
from pages.careers_page import CareersPage


class TestCoreValues:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup test"""
        self.careers_page = CareersPage(page)
    
    def test_extract_and_save_core_values(self, page):
        """
        Task 1: Extract core values, save to JSON, count exclamation marks, download images
        """
        print("\n" + "="*70)
        print("🚀 TASK 1: CORE VALUES EXTRACTION TEST")
        print("="*70)
        
        # STEP 1
        print("\n📍 STEP 1: Navigating to Careers page")
        print("-" * 70)
        self.careers_page.navigate_to_careers()
        assert "trg" in page.url.lower()
        print("✅ Successfully navigated")
        
        # STEP 2
        print("\n📍 STEP 2: Scrolling to Life At TRG")
        print("-" * 70)
        self.careers_page.scroll_to_life_at_trg()
        print("✅ Scrolled to Life At TRG")
        
        # STEP 3
        print("\n📍 STEP 3: Scrolling to Core Values")
        print("-" * 70)
        self.careers_page.scroll_to_core_values()
        print("✅ Scrolled to Core Values")
        
        # STEP 4
        print("\n📍 STEP 4: Extracting core values")
        print("-" * 70)
        core_values = self.careers_page.extract_core_values()
        assert len(core_values) > 0, "No core values extracted!"
        print(f"\n✅ Extracted {len(core_values)} core values")
        
        print("\n📋 Extracted Core Values:")
        print("-" * 70)
        for idx, value in enumerate(core_values, 1):
            print(f"\n{idx}. {value['headline']}")
            print(f"   Description: {value['description'][:100]}...")
        
        # STEP 5 & 6
        print("\n" + "="*70)
        print("📍 STEP 5 & 6: Saving to JSON and counting exclamation marks")
        print("-" * 70)
        
        json_file_path = "data/core_values.json"
        exclamation_count = self.careers_page.count_exclamation_marks(core_values)
        print(f"   → Exclamation marks: {exclamation_count}")
        
        result = {
            "core_values": core_values,
            "exclamation_marks_count": exclamation_count,
            "total_values_extracted": len(core_values)
        }
        
        self.careers_page.save_core_values_to_json(result, json_file_path)
        assert os.path.exists(json_file_path)
        print(f"✅ Saved to: {json_file_path}")
        
        # STEP 7
        print("\n" + "="*70)
        print("📍 STEP 7: Downloading images")
        print("-" * 70)
        
        images_dir = "data/images"
        downloaded_images = self.careers_page.download_core_value_images(
            core_values, 
            images_dir
        )
        
        print(f"\n✅ Downloaded {len(downloaded_images)} images")
        
        # SUMMARY
        print("\n" + "="*70)
        print("✅ TEST COMPLETED SUCCESSFULLY!")
        print("="*70)
        print(f"\n📊 Summary:")
        print(f"   • Core values: {len(core_values)}")
        print(f"   • Exclamation marks: {exclamation_count}")
        print(f"   • Images: {len(downloaded_images)}")
        print(f"   • JSON: {json_file_path}")
        print("\n" + "="*70 + "\n")