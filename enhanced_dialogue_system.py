#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
攻め・受けの役割を考慮したセリフ生成システム
"""

import random
from typing import Dict, List, Tuple

class EnhancedDialogueSystem:
    """攻め・受けの役割を考慮したセリフ生成システム"""
    
    def __init__(self):
        """初期化"""
        self.dialogue_patterns = {
            "無口・クール": {
                "attacker": {  # 攻め役
                    "low": [
                        "「……大丈夫か？」",
                        "「……準備はいいか？」",
                        "「……気持ちいいか？」"
                    ],
                    "medium": [
                        "「……気持ちいいか？」",
                        "「……感じるか？」",
                        "「……いいか？」"
                    ],
                    "high": [
                        "「……もっと…」",
                        "「……続けて…」",
                        "「……まだ…」"
                    ],
                    "peak": [
                        "「……あ…」",
                        "「……ああ…」",
                        "「……うあ…」"
                    ]
                },
                "receiver": {  # 受け役
                    "low": [
                        "「……ん…」",
                        "「……うん…」",
                        "「……そう…」"
                    ],
                    "medium": [
                        "「……気持ちいい…」",
                        "「……いい…」",
                        "「……感じる…」"
                    ],
                    "high": [
                        "「……もっと…」",
                        "「……続けて…」",
                        "「……まだ…」"
                    ],
                    "peak": [
                        "「……あ…」",
                        "「……ああ…」",
                        "「……うあ…」"
                    ]
                }
            },
            "ツンデレ": {
                "attacker": {  # 攻め役
                    "low": [
                        "「……一緒に帰ろう」",
                        "「……大丈夫か？」",
                        "「……準備はいいか？」"
                    ],
                    "medium": [
                        "「……気持ちいいか？」",
                        "「……感じるか？」",
                        "「……いいか？」"
                    ],
                    "high": [
                        "「……もっと…」",
                        "「……続けて…」",
                        "「……まだ…」"
                    ],
                    "peak": [
                        "「……あ…」",
                        "「……ああ…」",
                        "「……うあ…」"
                    ]
                },
                "receiver": {  # 受け役
                    "low": [
                        "「べ、別に…一緒に帰るわけじゃないし…」",
                        "「ち、違うから…勘違いしないで…」",
                        "「な、何よ…そんな顔して…」"
                    ],
                    "medium": [
                        "「ち、違うから…でも、もっと…」",
                        "「や、やめて…でも、気持ちいい…」",
                        "「だ、だめ…でも、続けて…」"
                    ],
                    "high": [
                        "「や、やめて…でも、気持ちいい…」",
                        "「だ、だめ…でも、続けて…」",
                        "「も、もう…やめて…でも…」"
                    ],
                    "peak": [
                        "「だ、だめ…でも、続けて…」",
                        "「も、もう…やめて…でも…」",
                        "「あ、あぁ…ばか…」"
                    ]
                }
            },
            "甘え系": {
                "attacker": {  # 攻め役
                    "low": [
                        "「……一緒に帰ろう」",
                        "「……大丈夫か？」",
                        "「……準備はいいか？」"
                    ],
                    "medium": [
                        "「……気持ちいいか？」",
                        "「……感じるか？」",
                        "「……いいか？」"
                    ],
                    "high": [
                        "「……もっと…」",
                        "「……続けて…」",
                        "「……まだ…」"
                    ],
                    "peak": [
                        "「……あ…」",
                        "「……ああ…」",
                        "「……うあ…」"
                    ]
                },
                "receiver": {  # 受け役
                    "low": [
                        "「ん…気持ちいい…」",
                        "「あたし、気持ちよくなりたい…」",
                        "「あなたと一緒だと…すごく気持ちいい…」"
                    ],
                    "medium": [
                        "「あたし、気持ちよくなりたい…」",
                        "「あなたと一緒だと…すごく気持ちいい…」",
                        "「もっと…もっと動いて…」"
                    ],
                    "high": [
                        "「あなたと一緒だと…すごく気持ちいい…」",
                        "「もっと…もっと動いて…」",
                        "「あたし、気持ちよくなりたい…」"
                    ],
                    "peak": [
                        "「もっと…もっと動いて…」",
                        "「あたし、気持ちよくなりたい…」",
                        "「あなたと一緒だと…すごく気持ちいい…」"
                    ]
                }
            },
            "ヤンデレ": {
                "attacker": {  # 攻め役
                    "low": [
                        "「……一緒に帰ろう」",
                        "「……大丈夫か？」",
                        "「……準備はいいか？」"
                    ],
                    "medium": [
                        "「……気持ちいいか？」",
                        "「……感じるか？」",
                        "「……いいか？」"
                    ],
                    "high": [
                        "「……もっと…」",
                        "「……続けて…」",
                        "「……まだ…」"
                    ],
                    "peak": [
                        "「……あ…」",
                        "「……ああ…」",
                        "「……うあ…」"
                    ]
                },
                "receiver": {  # 受け役
                    "low": [
                        "「あなたは私だけのもの…」",
                        "「私だけを見て…私だけを愛して…」",
                        "「他の女なんて考えないで…私だけを…」"
                    ],
                    "medium": [
                        "「私だけを見て…私だけを愛して…」",
                        "「他の女なんて考えないで…私だけを…」",
                        "「私のもの…私のものよ…」"
                    ],
                    "high": [
                        "「他の女なんて考えないで…私だけを…」",
                        "「私のもの…私のものよ…」",
                        "「あなたは私だけのもの…」"
                    ],
                    "peak": [
                        "「私のもの…私のものよ…」",
                        "「あなたは私だけのもの…」",
                        "「私だけを見て…私だけを愛して…」"
                    ]
                }
            }
        }
    
    def get_intensity_level(self, intensity: Tuple[int, int]) -> str:
        """強度からレベルを判定"""
        avg_intensity = (intensity[0] + intensity[1]) / 2
        if avg_intensity <= 2:
            return "low"
        elif avg_intensity <= 4:
            return "medium"
        elif avg_intensity <= 7:
            return "high"
        else:
            return "peak"
    
    def generate_dialogue(self, personality_type: str, role: str, intensity: Tuple[int, int]) -> str:
        """性格・役割・強度に応じたセリフを生成"""
        intensity_level = self.get_intensity_level(intensity)
        
        # 性格タイプが存在しない場合はデフォルトを使用
        if personality_type not in self.dialogue_patterns:
            personality_type = "無口・クール"
        
        # 役割が存在しない場合は受け役を使用
        if role not in self.dialogue_patterns[personality_type]:
            role = "receiver"
        
        # 強度レベルが存在しない場合はlowを使用
        if intensity_level not in self.dialogue_patterns[personality_type][role]:
            intensity_level = "low"
        
        options = self.dialogue_patterns[personality_type][role][intensity_level]
        return random.choice(options)
    
    def determine_role(self, gender: str, play_type: str) -> str:
        """性別とプレイタイプから役割を決定"""
        # 基本的な役割決定ロジック
        if play_type == "立ちバック":
            return "attacker" if gender == "male" else "receiver"
        elif play_type == "フェラチオ":
            return "receiver" if gender == "male" else "attacker"
        elif play_type == "正常位":
            return "attacker" if gender == "male" else "receiver"
        else:
            # デフォルトは性別で決定
            return "attacker" if gender == "male" else "receiver"

# 使用例
if __name__ == "__main__":
    system = EnhancedDialogueSystem()
    
    # 無口・クール、受け役、低強度
    dialogue1 = system.generate_dialogue("無口・クール", "receiver", (0, 1))
    print(f"無口・クール受け役低強度: {dialogue1}")
    
    # 無口・クール、攻め役、低強度
    dialogue2 = system.generate_dialogue("無口・クール", "attacker", (0, 1))
    print(f"無口・クール攻め役低強度: {dialogue2}")
    
    # ツンデレ、受け役、中強度
    dialogue3 = system.generate_dialogue("ツンデレ", "receiver", (3, 4))
    print(f"ツンデレ受け役中強度: {dialogue3}")
    
    # 役割決定の例
    role1 = system.determine_role("male", "立ちバック")
    role2 = system.determine_role("female", "フェラチオ")
    print(f"男性立ちバック役割: {role1}")
    print(f"女性フェラチオ役割: {role2}")
