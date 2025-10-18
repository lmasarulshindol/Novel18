#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
強化版プロット生成システム
「このまま中に出していい？→中はダメ→強制中出しされながら抗議の言葉と甘えの態度が半々」
の流れを再現

使用方法:
    python enhanced_plot_generator.py                    # ランダムで1プロット生成
    python enhanced_plot_generator.py 3                  # ランダムで3プロット生成
    python enhanced_plot_generator.py --character tsundere # ツンデレ指定で生成
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class EnhancedPhaseData:
    """強化版フェーズデータクラス"""
    phase_id: int
    name: str
    intensity: Tuple[int, int]
    duration: int
    description: str
    male_dialogue: List[str]
    female_dialogue: List[str]
    emotional_state: str
    physical_reaction: str
    context: str

class EnhancedPlotGenerator:
    """強化版プロット生成クラス"""
    
    def __init__(self):
        """初期化"""
        self.phases = self._initialize_enhanced_phases()
    
    def _initialize_enhanced_phases(self) -> List[EnhancedPhaseData]:
        """強化版フェーズデータを初期化"""
        phases = [
            EnhancedPhaseData(
                phase_id=1,
                name="静（導入）",
                intensity=(0, 1),
                duration=5,
                description="残業後の二人、エレベーターで下りる",
                male_dialogue=["でも、夜遅いから…", "一緒に帰ろう"],
                female_dialogue=["べ、別に…一緒に帰るわけじゃないし…", "な、何よ…そんな顔して…"],
                emotional_state="拒絶・照れ隠し",
                physical_reaction="微細な緊張感",
                context="導入"
            ),
            EnhancedPhaseData(
                phase_id=2,
                name="揺れ（乱れ始め）",
                intensity=(1, 2),
                duration=3,
                description="路地裏に誘導、身体の距離が近づく",
                male_dialogue=["路地裏の方、通らない？", "ちょっと話があるんだ"],
                female_dialogue=["ち、違うから…勘違いしないで…", "や…っ、ちょ、近い…！"],
                emotional_state="動揺・混乱",
                physical_reaction="微細な反応開始",
                context="誘導"
            ),
            EnhancedPhaseData(
                phase_id=3,
                name="崩れ（感情解放）- 前戯開始",
                intensity=(2, 3),
                duration=5,
                description="壁に押し付けられる、キスと軽い愛撫",
                male_dialogue=["美咲…", "大丈夫…"],
                female_dialogue=["や…っ、ちょ、近い…！", "ちょっと…待っ…て、あっ…"],
                emotional_state="感情の揺らぎ",
                physical_reaction="身体的反応の明確化",
                context="前戯開始"
            ),
            EnhancedPhaseData(
                phase_id=4,
                name="崩れ（感情解放）- 前戯本格化",
                intensity=(3, 4),
                duration=7,
                description="服を脱がされる、胸やお尻を触られる",
                male_dialogue=["美咲…綺麗だ…", "気持ちいいか？"],
                female_dialogue=["だ、だめ…そんなの…", "や…やめて…"],
                emotional_state="抵抗・動揺",
                physical_reaction="身体的反応の明確化",
                context="前戯本格化"
            ),
            EnhancedPhaseData(
                phase_id=5,
                name="崩れ（感情解放）- 前戯クライマックス",
                intensity=(4, 5),
                duration=8,
                description="下着を脱がされる、指での愛撫",
                male_dialogue=["美咲…濡れてる…", "気持ちいいか？"],
                female_dialogue=["ちょっと…待っ…て、あっ…", "だ、だめ…や…ぁ…"],
                emotional_state="快感の明確化",
                physical_reaction="激しい身体的反応",
                context="前戯クライマックス"
            ),
            EnhancedPhaseData(
                phase_id=6,
                name="頂点（制御不能）- 挿入準備",
                intensity=(5, 6),
                duration=5,
                description="立ちバックの体勢に、挿入への期待",
                male_dialogue=["美咲…準備はいいか？", "大丈夫…優しくするから…"],
                female_dialogue=["ちょっと…待っ…て、あっ…", "だめ…でも…"],
                emotional_state="最後の抵抗",
                physical_reaction="挿入準備完了",
                context="挿入準備"
            ),
            EnhancedPhaseData(
                phase_id=7,
                name="頂点（制御不能）- 挿入・本番開始",
                intensity=(6, 7),
                duration=10,
                description="強制挿入、激しい動き開始",
                male_dialogue=["美咲…気持ちいいか？", "もっと…もっと動いて…"],
                female_dialogue=["もう…わかんない…っ", "あっ…あぁっ…"],
                emotional_state="挿入瞬間の反応",
                physical_reaction="激しい動き開始",
                context="挿入開始"
            ),
            EnhancedPhaseData(
                phase_id=8,
                name="頂点（制御不能）- 本番クライマックス",
                intensity=(7, 8),
                duration=15,
                description="激しいピストン、絶頂への突き進み",
                male_dialogue=["美咲…もう少しで…", "一緒に…一緒に気持ちよくなろう…"],
                female_dialogue=["あ、あぁ…ばか…♥", "や、やめて…あぁ…♥"],
                emotional_state="制御不能状態",
                physical_reaction="激しいピストン",
                context="本番クライマックス"
            ),
            EnhancedPhaseData(
                phase_id=9,
                name="頂点（制御不能）- 中出し",
                intensity=(8, 9),
                duration=5,
                description="強制中出し、射精・絶頂（抗議と甘えが半々）",
                male_dialogue=["美咲…もう限界だ…", "このまま中に出していい？", "ごめん…でも、もう止められない…", "美咲…気持ちよかった…"],
                female_dialogue=["や、やめて…あぁ…♥中は…中はダメって言ったのに…♥", "だめ…中は…中はダメ…っ♥", "あっあっあっ…ば、ばか…っ…♥中はダメって言ったのに…出てる…出てる…♥でも…気持ちいい…♥", "中はダメ…中はダメって言ったのに…♥でも…もっと…もっと出して…♥ばか…♥"],
                emotional_state="完全崩壊（抗議と甘えの葛藤）",
                physical_reaction="射精・絶頂",
                context="中出し"
            ),
            EnhancedPhaseData(
                phase_id=10,
                name="余韻（静寂）- 中出し後",
                intensity=(9, 10),
                duration=10,
                description="中出し後の余韻、静寂と複雑な感情",
                male_dialogue=["美咲…大丈夫か？", "ごめん…でも、気持ちよかった…"],
                female_dialogue=["もう…わかんない…っ♥中はダメって言ったのに…でも…気持ちいい…♥", "…ばか…", "中はダメって言ったのに…でも…気持ちよかった…♥"],
                emotional_state="複雑な感情",
                physical_reaction="静寂と余韻",
                context="中出し後"
            )
        ]
        return phases
    
    def generate_enhanced_plot(self, character_type: str = "tsundere") -> Dict:
        """強化版プロットを生成"""
        plot_data = {
            "character_type": character_type,
            "phases": []
        }
        
        for phase in self.phases:
            # 男性のセリフを選択
            male_dialogue = random.choice(phase.male_dialogue)
            
            # 女性のセリフを選択
            female_dialogue = random.choice(phase.female_dialogue)
            
            # 擬音語を生成
            sound_effects = self._generate_sound_effects(phase)
            
            # 身体的反応を詳細化
            physical_reaction = self._enhance_physical_reaction(phase)
            
            enhanced_phase = {
                "phase_id": phase.phase_id,
                "name": phase.name,
                "intensity": phase.intensity,
                "duration": phase.duration,
                "description": phase.description,
                "male_dialogue": male_dialogue,
                "female_dialogue": female_dialogue,
                "sound_effects": sound_effects,
                "physical_reaction": physical_reaction,
                "emotional_state": phase.emotional_state,
                "context": phase.context
            }
            
            plot_data["phases"].append(enhanced_phase)
        
        return plot_data
    
    def _generate_sound_effects(self, phase: EnhancedPhaseData) -> List[str]:
        """擬音語を生成"""
        intensity_level = self._get_intensity_level(phase.intensity)
        
        sound_effects = {
            "low": ["ビクッ", "んっ"],
            "medium": ["ヌチュヌチュ", "あっ", "やっ"],
            "high": ["ぱちゅぱちゅ", "あっあっ", "やっやっ"],
            "peak": ["ドクドク", "ビクビク", "あっあっあっ", "やっやっやっ"]
        }
        
        return sound_effects.get(intensity_level, [])
    
    def _get_intensity_level(self, phase_intensity: Tuple[int, int]) -> str:
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
    
    def _enhance_physical_reaction(self, phase: EnhancedPhaseData) -> str:
        """身体的反応を詳細化"""
        intensity_level = self._get_intensity_level(phase.intensity)
        
        reactions = {
            "low": "微細な緊張感、身体の微細な震え",
            "medium": "身体的反応の明確化、息遣いの変化",
            "high": "激しい身体的反応、制御不能状態",
            "peak": "完全崩壊、激しい痙攣、射精・絶頂"
        }
        
        return reactions.get(intensity_level, phase.physical_reaction)
    
    def format_enhanced_plot(self, plot_data: Dict) -> str:
        """強化版プロットを整形して出力"""
        output = f"""
# 強化版プロット生成結果 - {plot_data['character_type'].title()}

## 📋 基本設定
- **キャラクター**: {plot_data['character_type'].title()}
- **特徴**: 抗議と甘えが半々の複雑な心理描写

---

## 📖 強化版プロット（{len(plot_data['phases'])}段階）

"""
        
        for phase in plot_data["phases"]:
            output += f"""
### ⑨ {phase['name']}
**強度**: {phase['intensity'][0]}-{phase['intensity'][1]}
**時間**: {phase['duration']}分
**内容**:
- {phase['description']}
- **男性のセリフ**: 「{phase['male_dialogue']}」
- **女性のセリフ**: 「{phase['female_dialogue']}」
- **擬音語**: {', '.join(phase['sound_effects']) if phase['sound_effects'] else 'なし'}
- **身体的反応**: {phase['physical_reaction']}
- **心理状態**: {phase['emotional_state']}
- **コンテキスト**: {phase['context']}

"""
        
        return output

def main():
    """メイン関数"""
    import sys
    import argparse
    
    generator = EnhancedPlotGenerator()
    
    # 引数パーサーの設定
    parser = argparse.ArgumentParser(description='強化版プロット生成システム')
    parser.add_argument('count', nargs='?', type=int, default=1, help='生成するプロットの数（デフォルト: 1）')
    parser.add_argument('--character', '-c', choices=['tsundere'], default='tsundere', help='キャラクタータイプ')
    
    args = parser.parse_args()
    
    # 生成数の検証
    if args.count <= 0:
        print("生成数は1以上の整数を指定してください。")
        return
    
    # プロットを生成
    for i in range(args.count):
        if args.count > 1:
            print(f"\n【プロット {i+1}】")
        
        plot_data = generator.generate_enhanced_plot(args.character)
        print("=" * 60)
        print("✍️ 強化版プロット生成結果")
        print("=" * 60)
        print(generator.format_enhanced_plot(plot_data))
        
        if i < args.count - 1:
            print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
