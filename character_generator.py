#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
人物設定生成スクリプト
ランダムに選ばれた男女2名の簡易プロフィールと一人称・二人称を適切に設定

使用方法:
    python character_generator.py          # 1ペア生成（デフォルト）
    python character_generator.py 3        # 3ペア生成
    python character_generator.py 5        # 5ペア生成
"""

import random
from typing import Dict, List, Tuple

class CharacterGenerator:
    """人物設定生成クラス"""
    
    def __init__(self):
        """初期化"""
        self.male_names = [
            "翔太", "健太", "大輔", "拓也", "直樹", "慎一", "和也", "智也",
            "俊介", "雄一", "正樹", "誠", "亮", "剛", "竜", "海斗", "颯太",
            "蓮", "陽太", "悠斗", "大樹", "翼", "優斗", "陸", "蒼", "颯"
        ]
        
        self.female_names = [
            "美咲", "由美", "さくら", "あい", "みお", "ゆい", "あや", "みき",
            "なな", "あいり", "ひなた", "みく", "あん", "ゆう", "りん", "まい",
            "あいか", "みゆ", "あいみ", "ひまり", "みう", "あいな", "ゆあ", "みな"
        ]
        
        self.personality_types = {
            "ツンデレ": {
                "description": "本音と建前のギャップが激しく、強がりから崩壊への落差が大きい",
                "male_first_person": ["俺", "僕", "おれ"],
                "male_second_person": ["お前", "君", "あんた"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "あんた"],
                "characteristics": ["強がり", "照れ屋", "素直になれない", "愛情深い"],
                "explicit_expressions": [
                    "「べ、別に…気持ちよくなってくれるなら…」",
                    "「ち、違うから…でも、もっと…」",
                    "「や、やめて…でも、気持ちいい…」",
                    "「だ、だめ…でも、続けて…」"
                ]
            },
            "甘え系": {
                "description": "素直で愛情表現が豊か、柔らかくて可愛らしい",
                "male_first_person": ["僕", "ぼく", "俺"],
                "male_second_person": ["君", "きみ", "お前"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "お前"],
                "characteristics": ["素直", "愛情深い", "可愛らしい", "優しい"],
                "explicit_expressions": [
                    "「ん…気持ちいい…もっと…」",
                    "「あたし、気持ちよくなりたい…」",
                    "「あなたと一緒だと…すごく気持ちいい…」",
                    "「もっと…もっと動いて…」"
                ]
            },
            "無口・クール": {
                "description": "感情を表に出さず、静かな陶酔を好む",
                "male_first_person": ["俺", "僕", "おれ"],
                "male_second_person": ["お前", "君", "あんた"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "お前"],
                "characteristics": ["無口", "クール", "冷静", "静か"],
                "explicit_expressions": [
                    "「……ん…」",
                    "「……気持ちいい…」",
                    "「……もっと…」",
                    "「……あ…」"
                ]
            },
            "天然・無邪気": {
                "description": "純粋で素直、好奇心旺盛で明るい",
                "male_first_person": ["僕", "ぼく", "俺"],
                "male_second_person": ["君", "きみ", "お前"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "お前"],
                "characteristics": ["純粋", "無邪気", "明るい", "好奇心旺盛"],
                "explicit_expressions": [
                    "「えへへ…なんだか気持ちいいね…」",
                    "「きゃっ…なんだかくすぐったい…」",
                    "「あ…なんだか変な感じ…でも気持ちいい…」",
                    "「え？なに？なんだか…すごい…」"
                ]
            },
            "ヤンデレ": {
                "description": "独占欲が強く、感情の起伏が激しい",
                "male_first_person": ["俺", "僕", "おれ"],
                "male_second_person": ["お前", "君", "あんた"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "お前"],
                "characteristics": ["独占欲が強い", "執着深い", "感情豊か", "愛情深い"],
                "explicit_expressions": [
                    "「あなたは私だけのもの…私だけを感じて…」",
                    "「私だけを見て…私だけを愛して…」",
                    "「他の女なんて考えないで…私だけを…」",
                    "「私のもの…私のものよ…」"
                ]
            },
            "お姉さん": {
                "description": "包容力があり、相手をリードする",
                "male_first_person": ["俺", "僕", "おれ"],
                "male_second_person": ["君", "きみ", "お前"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["あなた", "君", "お前"],
                "characteristics": ["包容力がある", "リーダーシップ", "優しい", "大人っぽい"],
                "explicit_expressions": [
                    "「ふふ…なんだか可愛いのね…」",
                    "「大丈夫…私がいるから…」",
                    "「安心して…私がリードするから…」",
                    "「私と一緒に気持ちよくなりましょう…」"
                ]
            },
            "後輩・年下": {
                "description": "素直で従順、相手に依存しがち",
                "male_first_person": ["僕", "ぼく", "俺"],
                "male_second_person": ["先輩", "○○さん", "あなた"],
                "female_first_person": ["私", "あたし", "わたし"],
                "female_second_person": ["○○さん", "先輩", "あなた"],
                "characteristics": ["素直", "従順", "依存しがち", "可愛らしい"],
                "explicit_expressions": [
                    "「先輩…なんだかドキドキします…」",
                    "「先輩と一緒だと…すごく気持ちいいです…」",
                    "「先輩…もっと…もっと動いてください…」",
                    "「先輩…私、気持ちよくなりたいです…」"
                ]
            }
        }
        
        self.ages = list(range(15, 20))  
        self.heights = {
            "male": list(range(165, 185)),  # 165-184cm
            "female": list(range(145, 165))  # 150-169cm
        }
        
        self.hobbies = [
            "読書", "映画鑑賞", "音楽", "スポーツ", "料理", "ゲーム",
            "アニメ", "漫画", "写真", "旅行", "ショッピング", "カフェ巡り",
            "ダンス", "楽器演奏", "絵を描く", "手芸", "園芸", "ペット"
        ]
        
        self.occupations = [
            "大学生", "会社員", "フリーター", "専門学校生", "高校生",
            "アルバイト", "自営業", "公務員", "看護師", "教師"
        ]

    def generate_character(self, gender: str) -> Dict:
        """単一キャラクターを生成"""
        personality_type = random.choice(list(self.personality_types.keys()))
        personality_data = self.personality_types[personality_type]
        
        # 名前を選択
        if gender == "male":
            name = random.choice(self.male_names)
            first_person = random.choice(personality_data["male_first_person"])
            second_person = random.choice(personality_data["male_second_person"])
            height = random.choice(self.heights["male"])
        else:
            name = random.choice(self.female_names)
            first_person = random.choice(personality_data["female_first_person"])
            second_person = random.choice(personality_data["female_second_person"])
            height = random.choice(self.heights["female"])
        
        # その他の属性をランダム選択
        age = random.choice(self.ages)
        hobby = random.choice(self.hobbies)
        occupation = random.choice(self.occupations)
        characteristic = random.choice(personality_data["characteristics"])
        
        return {
            "name": name,
            "gender": gender,
            "age": age,
            "height": height,
            "personality_type": personality_type,
            "personality_description": personality_data["description"],
            "first_person": first_person,
            "second_person": second_person,
            "hobby": hobby,
            "occupation": occupation,
            "characteristic": characteristic
        }

    def generate_pair(self) -> Tuple[Dict, Dict]:
        """男女ペアのキャラクターを生成"""
        male_character = self.generate_character("male")
        female_character = self.generate_character("female")
        
        return male_character, female_character

    def format_character_profile(self, character: Dict) -> str:
        """キャラクタープロフィールを整形して出力"""
        profile = f"""
【{character['name']}】
性別: {character['gender']}
年齢: {character['age']}歳
身長: {character['height']}cm
職業: {character['occupation']}
趣味: {character['hobby']}

性格タイプ: {character['personality_type']}
性格説明: {character['personality_description']}
特徴: {character['characteristic']}

【呼び方設定】
一人称: {character['first_person']}
二人称: {character['second_person']}
"""
        return profile

    def generate_and_display(self) -> None:
        """キャラクターペアを生成して表示"""
        male, female = self.generate_pair()
        
        print("=" * 50)
        print("🎭 ランダム人物設定生成結果")
        print("=" * 50)
        
        print("\n👨 男性キャラクター")
        print(self.format_character_profile(male))
        
        print("\n👩 女性キャラクター")
        print(self.format_character_profile(female))
        
        print("\n💕 ペア設定")
        print(f"男性: {male['name']} ({male['age']}歳, {male['personality_type']})")
        print(f"女性: {female['name']} ({female['age']}歳, {female['personality_type']})")
        print(f"\n【呼び方関係】")
        print(f"・{male['name']}は自分を「{male['first_person']}」と呼び、{female['name']}を「{male['second_person']}」と呼ぶ")
        print(f"・{female['name']}は自分を「{female['first_person']}」と呼び、{male['name']}を「{female['second_person']}」と呼ぶ")
        print(f"\n【執筆時の注意】")
        print(f"・{male['name']}のセリフ: 一人称「{male['first_person']}」、二人称「{male['second_person']}」")
        print(f"・{female['name']}のセリフ: 一人称「{female['first_person']}」、二人称「{female['second_person']}」")

def main():
    """メイン関数"""
    import sys
    
    generator = CharacterGenerator()
    
    # 引数の処理
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
            if count <= 0:
                print("生成数は1以上の整数を指定してください。")
                return
        except ValueError:
            print("生成数は整数で指定してください。")
            return
    else:
        count = 1  # デフォルトは1ペア
    
    print("=" * 50)
    print("🎭 人物設定生成スクリプト")
    print("=" * 50)
    
    for i in range(count):
        if count > 1:
            print(f"\n【ペア {i+1}】")
        generator.generate_and_display()
        if i < count - 1:
            print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
