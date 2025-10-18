#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
プロット出力ロジック統合システム
自然なセリフ生成とプロット最適化

使用方法:
    python plot_dialogue_optimizer.py                    # ランダムで1プロット生成
    python plot_dialogue_optimizer.py 3                  # ランダムで3プロット生成
    python plot_dialogue_optimizer.py --character tsundere # ツンデレ指定で生成
    python plot_dialogue_optimizer.py --plot standing_back # 立ちバック指定で生成
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class PhaseData:
    """フェーズデータクラス"""
    phase_id: int
    name: str
    intensity: Tuple[int, int]
    duration: int
    description: str
    base_dialogue: List[str]
    emotional_state: str
    physical_reaction: str

class TsundereDialogueGenerator:
    """ツンデレセリフ生成クラス"""
    
    def __init__(self):
        """初期化"""
        self.character_traits = {
            "tsundere": {
                "rejection_words": ["だめ", "やめて", "違う", "べ、別に", "ち、違う"],
                "confusion_words": ["ちょっと", "や", "あ", "ん"],
                "breakdown_words": ["もう", "わかんない", "ばか"],
                "love_words": ["ばか", "♥"],
                "intensity_modifiers": ["っ", "あ", "や", "ん"]
            }
        }
        
        self.intensity_patterns = {
            "low": {
                "rejection": ["べ、別に", "ち、違う", "な、何よ"],
                "confusion": ["ちょっと", "や", "あ"],
                "breakdown": ["もう", "わかんない"]
            },
            "medium": {
                "rejection": ["だめ", "やめて", "違う"],
                "confusion": ["ちょっと", "や", "あ", "ん"],
                "breakdown": ["もう", "わかんない", "ばか"]
            },
            "high": {
                "rejection": ["だめ", "やめて", "違う", "中はダメ"],
                "confusion": ["や", "あ", "ん", "あぁ"],
                "breakdown": ["もう", "わかんない", "ばか", "♥"]
            },
            "peak": {
                "rejection": ["だめ", "やめて", "中はダメ"],
                "confusion": ["あっ", "やっ", "んっ", "あぁっ"],
                "breakdown": ["ばか", "♥", "出てる", "気持ちいい"]
            }
        }
        
        # より自然なセリフパターン
        self.natural_dialogue_patterns = {
            "low": [
                "べ、別に…一緒に帰るわけじゃないし…",
                "な、何よ…そんな顔して…",
                "ち、違うから…勘違いしないで…"
            ],
            "medium": [
                "や…っ、ちょ、近い…！",
                "ちょっと…待って…あ、や…",
                "だ、だめ…そんなの…"
            ],
            "high": [
                "ちょっと…待っ…て、あっ…",
                "もう…わかんない…っ",
                "だ、だめ…や…ぁ…"
            ],
            "peak": [
                "あ、あぁっ…もう、や…ぁ…",
                "ば、ばか…っ…♥",
                "や、やめて…あぁ…♥",
                "もう…わかんない…っ♥",
                "あ、あぁ…ばか…♥"
            ]
        }
    
    def get_intensity_level(self, phase_intensity: Tuple[int, int]) -> str:
        """強度からレベルを判定"""
        avg_intensity = (phase_intensity[0] + phase_intensity[1]) / 2
        if avg_intensity <= 2:
            return "low"
        elif avg_intensity <= 4:
            return "medium"
        elif avg_intensity <= 7:
            return "high"
        else:
            return "peak"
    
    def generate_dialogue(self, phase: PhaseData, context: str = "") -> str:
        """セリフを生成"""
        intensity_level = self.get_intensity_level(phase.intensity)
        
        # 自然なセリフパターンから選択
        if intensity_level in self.natural_dialogue_patterns:
            natural_patterns = self.natural_dialogue_patterns[intensity_level]
            base_dialogue = random.choice(natural_patterns)
        else:
            # フォールバック: 従来の方法
            patterns = self.intensity_patterns[intensity_level]
            if "拒絶" in phase.emotional_state or "抵抗" in phase.emotional_state:
                base_words = patterns["rejection"]
            elif "動揺" in phase.emotional_state or "混乱" in phase.emotional_state:
                base_words = patterns["confusion"]
            else:
                base_words = patterns["breakdown"]
            
            base_dialogue = random.choice(base_words)
        
        # 特殊な状況の処理
        if "中出し" in context or "射精" in context:
            if intensity_level == "peak":
                # 中出し時の特別なセリフ（抗議と甘えが半々）
                special_dialogues = [
                    "あっあっあっ…ば、ばか…っ…♥中はダメって言ったのに…出てる…出てる…♥でも…気持ちいい…♥",
                    "や、やめて…あぁ…♥中は…中はダメって言ったのに…♥もっと…もっと出して…♥",
                    "もう…わかんない…っ♥中はダメって言ったのに…でも…気持ちいい…♥出てる…♥",
                    "だめ…中はダメって言ったのに…♥でも…もっと…もっと出して…♥ばか…♥",
                    "中はダメ…中はダメって言ったのに…♥でも…気持ちいい…♥出てる…出てる…♥"
                ]
                return random.choice(special_dialogues)
            elif intensity_level == "high":
                # 中出し前の抵抗
                resistance_dialogues = [
                    "だめ…中は…中はダメ…っ♥",
                    "やめて…中はダメって言ったのに…",
                    "中は…中はダメ…でも…"
                ]
                return random.choice(resistance_dialogues)
        
        return base_dialogue

class PlotDialogueOptimizer:
    """プロット・セリフ最適化クラス"""
    
    def __init__(self):
        """初期化"""
        self.dialogue_generator = TsundereDialogueGenerator()
        self.phases = self._initialize_phases()
    
    def _initialize_phases(self) -> List[PhaseData]:
        """フェーズデータを初期化"""
        phases = [
            PhaseData(
                phase_id=1,
                name="静（導入）",
                intensity=(0, 1),
                duration=5,
                description="残業後の二人、エレベーターで下りる",
                base_dialogue=["べ、別に…一緒に帰るわけじゃないし…", "な、何よ…そんな顔して…"],
                emotional_state="拒絶・照れ隠し",
                physical_reaction="微細な緊張感"
            ),
            PhaseData(
                phase_id=2,
                name="揺れ（乱れ始め）",
                intensity=(1, 2),
                duration=3,
                description="路地裏に誘導、身体の距離が近づく",
                base_dialogue=["や…っ、ちょ、近い…！", "ちょっと…待って…あ、や…"],
                emotional_state="動揺・混乱",
                physical_reaction="微細な反応開始"
            ),
            PhaseData(
                phase_id=3,
                name="崩れ（感情解放）- 前戯開始",
                intensity=(2, 3),
                duration=5,
                description="壁に押し付けられる、キスと軽い愛撫",
                base_dialogue=["ちょっと…待っ…て、あっ…", "もう…わかんない…っ"],
                emotional_state="感情の揺らぎ",
                physical_reaction="身体的反応の明確化"
            ),
            PhaseData(
                phase_id=4,
                name="崩れ（感情解放）- 前戯本格化",
                intensity=(3, 4),
                duration=7,
                description="服を脱がされる、胸やお尻を触られる",
                base_dialogue=["だ、だめ…そんなの…", "も、もう…やめて…っ"],
                emotional_state="抵抗・動揺",
                physical_reaction="身体的反応の明確化"
            ),
            PhaseData(
                phase_id=5,
                name="崩れ（感情解放）- 前戯クライマックス",
                intensity=(4, 5),
                duration=8,
                description="下着を脱がされる、指での愛撫",
                base_dialogue=["も、もう…やめて…っ", "だめ…そんなの…"],
                emotional_state="快感の明確化",
                physical_reaction="身体的反応の激化"
            ),
            PhaseData(
                phase_id=6,
                name="頂点（制御不能）- 挿入準備",
                intensity=(5, 6),
                duration=5,
                description="立ちバックの体勢に、挿入への期待",
                base_dialogue=["あ、あぁっ…もう、や…ぁ…", "だめ…でも…"],
                emotional_state="最後の抵抗",
                physical_reaction="挿入準備完了"
            ),
            PhaseData(
                phase_id=7,
                name="頂点（制御不能）- 挿入・本番開始",
                intensity=(6, 7),
                duration=10,
                description="強制挿入、激しい動き開始",
                base_dialogue=["ば、ばか…っ…♥", "や、やめて…あぁ…♥"],
                emotional_state="挿入瞬間の反応",
                physical_reaction="激しい動き開始"
            ),
            PhaseData(
                phase_id=8,
                name="頂点（制御不能）- 本番クライマックス",
                intensity=(7, 8),
                duration=15,
                description="激しいピストン、絶頂への突き進み",
                base_dialogue=["や、やめて…あぁ…♥", "もう…わかんない…っ♥"],
                emotional_state="制御不能状態",
                physical_reaction="激しいピストン"
            ),
            PhaseData(
                phase_id=9,
                name="頂点（制御不能）- 中出し",
                intensity=(8, 9),
                duration=5,
                description="強制中出し、射精・絶頂（抗議と甘えが半々）",
                base_dialogue=["あっあっあっ…ば、ばか…っ…♥中はダメって言ったのに…出てる…出てる…♥でも…気持ちいい…♥", "や、やめて…あぁ…♥中は…中はダメって言ったのに…♥もっと…もっと出して…♥"],
                emotional_state="完全崩壊（抗議と甘えの葛藤）",
                physical_reaction="射精・絶頂"
            ),
            PhaseData(
                phase_id=10,
                name="余韻（静寂）- 中出し後",
                intensity=(9, 10),
                duration=10,
                description="中出し後の余韻、静寂と複雑な感情",
                base_dialogue=["…ばか…っ…", "だめ…中はダメって言ったのに…でも…気持ちいい…♥"],
                emotional_state="複雑な感情",
                physical_reaction="静寂と余韻"
            )
        ]
        return phases
    
    def generate_optimized_plot(self, character_type: str = "tsundere", plot_type: str = "standing_back") -> Dict:
        """最適化されたプロットを生成"""
        plot_data = {
            "character_type": character_type,
            "plot_type": plot_type,
            "phases": []
        }
        
        for phase in self.phases:
            # セリフを生成
            dialogue = self.dialogue_generator.generate_dialogue(phase, phase.description)
            
            # 擬音語を生成
            sound_effects = self._generate_sound_effects(phase)
            
            # 身体的反応を詳細化
            physical_reaction = self._enhance_physical_reaction(phase)
            
            optimized_phase = {
                "phase_id": phase.phase_id,
                "name": phase.name,
                "intensity": phase.intensity,
                "duration": phase.duration,
                "description": phase.description,
                "dialogue": dialogue,
                "sound_effects": sound_effects,
                "physical_reaction": physical_reaction,
                "emotional_state": phase.emotional_state
            }
            
            plot_data["phases"].append(optimized_phase)
        
        return plot_data
    
    def _generate_sound_effects(self, phase: PhaseData) -> List[str]:
        """擬音語を生成"""
        intensity_level = self.dialogue_generator.get_intensity_level(phase.intensity)
        
        sound_effects = {
            "low": ["ビクッ", "んっ"],
            "medium": ["ヌチュヌチュ", "あっ", "やっ"],
            "high": ["ぱちゅぱちゅ", "あっあっ", "やっやっ"],
            "peak": ["ドクドク", "ビクビク", "あっあっあっ", "やっやっやっ"]
        }
        
        return sound_effects.get(intensity_level, [])
    
    def _enhance_physical_reaction(self, phase: PhaseData) -> str:
        """身体的反応を詳細化"""
        intensity_level = self.dialogue_generator.get_intensity_level(phase.intensity)
        
        reactions = {
            "low": "微細な緊張感、身体の微細な震え",
            "medium": "身体的反応の明確化、息遣いの変化",
            "high": "激しい身体的反応、制御不能状態",
            "peak": "完全崩壊、激しい痙攣、射精・絶頂"
        }
        
        return reactions.get(intensity_level, phase.physical_reaction)
    
    def format_plot(self, plot_data: Dict) -> str:
        """プロットを整形して出力"""
        output = f"""
# {plot_data['plot_type'].replace('_', ' ').title()} - {plot_data['character_type'].title()} エロ小説

## 📋 基本設定
- **キャラクター**: {plot_data['character_type'].title()}
- **プロットタイプ**: {plot_data['plot_type'].replace('_', ' ').title()}

---

## 📖 最適化プロット（{len(plot_data['phases'])}段階）

"""
        
        for phase in plot_data["phases"]:
            output += f"""
### ⑨ {phase['name']}
**強度**: {phase['intensity'][0]}-{phase['intensity'][1]}
**時間**: {phase['duration']}分
**内容**:
- {phase['description']}
- **セリフ**: 「{phase['dialogue']}」
- **擬音語**: {', '.join(phase['sound_effects']) if phase['sound_effects'] else 'なし'}
- **身体的反応**: {phase['physical_reaction']}
- **心理状態**: {phase['emotional_state']}

"""
        
        return output

def main():
    """メイン関数"""
    import sys
    import argparse
    
    optimizer = PlotDialogueOptimizer()
    
    # 引数パーサーの設定
    parser = argparse.ArgumentParser(description='プロット・セリフ最適化システム')
    parser.add_argument('count', nargs='?', type=int, default=1, help='生成するプロットの数（デフォルト: 1）')
    parser.add_argument('--character', '-c', choices=['tsundere'], default='tsundere', help='キャラクタータイプ')
    parser.add_argument('--plot', '-p', choices=['standing_back'], default='standing_back', help='プロットタイプ')
    
    args = parser.parse_args()
    
    # 生成数の検証
    if args.count <= 0:
        print("生成数は1以上の整数を指定してください。")
        return
    
    # プロットを生成
    for i in range(args.count):
        if args.count > 1:
            print(f"\n【プロット {i+1}】")
        
        plot_data = optimizer.generate_optimized_plot(args.character, args.plot)
        print("=" * 60)
        print("✍️ 最適化プロット生成結果")
        print("=" * 60)
        print(optimizer.format_plot(plot_data))
        
        if i < args.count - 1:
            print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
