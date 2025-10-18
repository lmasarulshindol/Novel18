#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人物設定生成スクリプトのテスト用サンプル実行
"""

from character_generator import CharacterGenerator

def test_character_generation():
    """テスト用のサンプル実行"""
    generator = CharacterGenerator()
    
    print("=" * 60)
    print("🎭 人物設定生成スクリプト - テスト実行")
    print("=" * 60)
    
    # 3つのペアを生成してテスト
    for i in range(3):
        print(f"\n【サンプル {i+1}】")
        print("-" * 40)
        
        male, female = generator.generate_pair()
        
        print(f"👨 男性: {male['name']} ({male['age']}歳, {male['personality_type']})")
        print(f"   一人称: {male['first_person']}, 二人称: {male['second_person']}")
        print(f"   特徴: {male['characteristic']}")
        
        print(f"👩 女性: {female['name']} ({female['age']}歳, {female['personality_type']})")
        print(f"   一人称: {female['first_person']}, 二人称: {female['second_person']}")
        print(f"   特徴: {female['characteristic']}")
        
        print(f"💕 呼び方: {male['name']} → {female['name']}を「{male['second_person']}」")
        print(f"💕 呼び方: {female['name']} → {male['name']}を「{female['second_person']}」")

if __name__ == "__main__":
    test_character_generation()
