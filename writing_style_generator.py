#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文体指示生成スクリプト
執筆時の文体、表現技法、描写の詳細度を指示

使用方法:
    python writing_style_generator.py                    # ランダムで1文体指示生成
    python writing_style_generator.py 3                  # ランダムで3文体指示生成
    python writing_style_generator.py --style 1          # 番号1の文体を指定して生成
    python writing_style_generator.py --style 2 3        # 番号2の文体を3回生成
    python writing_style_generator.py --list              # 利用可能な文体一覧を表示

利用可能な文体:
    1. 生々しいリアル系
    2. 官能的ロマンチック系
    3. エロティック詳細系
    4. 心理描写重視系
    5. 官能小説系
"""

import random
from typing import Dict, List

class WritingStyleGenerator:
    """文体指示生成クラス"""
    
    def __init__(self):
        """初期化"""
        self.writing_styles = {
            "生々しいリアル系": {
                "description": "具体的で生々しい描写を重視する文体",
                "narrative_style": "三人称限定視点",
                "detail_level": "詳細",
                "explicit_level": "高",
                "sensory_descriptions": [
                    "五感を活用した具体的な描写",
                    "身体的な反応の詳細な記述",
                    "音、匂い、触感の生々しい表現",
                    "性的な部位の具体的な名称使用"
                ],
                "dialogue_style": [
                    "生々しいセリフと感嘆詞・間投詞の多用",
                    "感情の高まりを音で表現",
                    "性的な快感を直接的に表現",
                    "身体的な反応を言葉で表現",
                    "女の子の受け側：意味のある言葉を少なめに、感嘆詞中心",
                    "高まりの度合いで感嘆詞の強度を段階的に上げる"
                ],
                "scene_descriptions": [
                    "身体の動きを詳細に描写",
                    "性的な行為の具体的な記述",
                    "快感の段階的な変化を描写",
                    "身体的な反応のリアルな表現"
                ],
                "example_expressions": [
                    "【ツンデレ】「べ、別に…でも、もっと…激しく…」",
                    "【甘え系】「ん…気持ちいい…もっと…激しく…」",
                    "【無口・クール】「……ん…もっと…」",
                    "【天然・無邪気】「えへへ…なんだか気持ちいいね…もっと…」",
                    "【ヤンデレ】「あなたは私だけのもの…もっと…激しく…」",
                    "【お姉さん】「ふふ…可愛いのね…もっと…激しく…」",
                    "【後輩・年下】「先輩…もっと…激しく…動いてください…」"
                ]
            },
            "官能的ロマンチック系": {
                "description": "官能性とロマンチックさを両立した文体",
                "narrative_style": "三人称全知視点",
                "detail_level": "中程度",
                "explicit_level": "中",
                "sensory_descriptions": [
                    "美しい比喩表現を多用",
                    "官能的な雰囲気の描写",
                    "感情と身体の反応を融合",
                    "詩的な表現で性的な行為を描写"
                ],
                "dialogue_style": [
                    "愛情深いセリフと官能的な表現",
                    "感情の高まりを美しく表現",
                    "性的な快感を詩的に表現",
                    "二人の愛情を言葉で表現"
                ],
                "scene_descriptions": [
                    "官能的な雰囲気の描写",
                    "美しい比喩で性的な行為を表現",
                    "感情と身体の反応を融合",
                    "ロマンチックな余韻の描写"
                ],
                "example_expressions": [
                    "【ツンデレ】「べ、別に…でも、愛してる…一緒に気持ちよくなりたい…」",
                    "【甘え系】「ん…愛してる…一緒に気持ちよくなりたい…」",
                    "【無口・クール】「……愛してる…一緒に気持ちよくなりたい…」",
                    "【天然・無邪気】「えへへ…愛してる…一緒に気持ちよくなりたい…」",
                    "【ヤンデレ】「あなたは私だけのもの…私だけを愛して…」",
                    "【お姉さん】「ふふ…愛してる…一緒に気持ちよくなりましょう…」",
                    "【後輩・年下】「先輩…愛してます…一緒に気持ちよくなりたいです…」"
                ]
            },
            "エロティック詳細系": {
                "description": "エロティックな要素を詳細に描写する文体",
                "narrative_style": "三人称限定視点",
                "detail_level": "非常に詳細",
                "explicit_level": "最高",
                "sensory_descriptions": [
                    "性的な行為の詳細な記述",
                    "身体的な反応の微細な描写",
                    "快感の段階的な変化を詳細に表現",
                    "性的な部位の具体的で生々しい描写"
                ],
                "dialogue_style": [
                    "性的な快感を直接的に表現",
                    "生々しい感嘆詞・間投詞とセリフ",
                    "身体的な反応を言葉で表現",
                    "性的な興奮を言葉で表現",
                    "女の子の受け側：意味のある言葉を少なめに、感嘆詞中心",
                    "高まりの度合いで感嘆詞の強度を段階的に上げる",
                    "ピーク時は途切れ途切れの断続的な喘ぎ声に変化"
                ],
                "scene_descriptions": [
                    "性的な行為の詳細な記述",
                    "身体的な反応の微細な描写",
                    "快感の段階的な変化を詳細に表現",
                    "性的な部位の具体的で生々しい描写",
                    "擬音語の効果的な使用（ビクッ、ブルンブルン、ヌチュヌチュ、ぱちゅぱちゅ等）"
                ],
                "example_expressions": [
                    "【ツンデレ】初期「べ、別に…」→中盤「ち、違うから…でも…」→ピーク「だ、だめ…でも、もっと…あっあっ！」",
                    "【甘え系】初期「ん…気持ちいい…」→中盤「あたし、気持ちよくなりたい…」→ピーク「もっと…もっと動いて…あぁあぁ！」",
                    "【無口・クール】初期「……ん…」→中盤「……気持ちいい…」→ピーク「……あ…あっ…」",
                    "【天然・無邪気】初期「えへへ…なんだか気持ちいいね…」→中盤「きゃっ…なんだかくすぐったい…」→ピーク「え？なに？なんだか…すごい…あぁあぁ！」",
                    "【ヤンデレ】初期「あなたは私だけのもの…」→中盤「私だけを見て…私だけを愛して…」→ピーク「私のもの…私のものよ…あっあっ！」",
                    "【お姉さん】初期「ふふ…なんだか可愛いのね…」→中盤「大丈夫…私がいるから…」→ピーク「私と一緒に気持ちよくなりましょう…あぁあぁ！」",
                    "【後輩・年下】初期「先輩…なんだかドキドキします…」→中盤「先輩と一緒だと…すごく気持ちいいです…」→ピーク「先輩…もっと…もっと動いてください…あっあっ！」"
                ]
            },
            "心理描写重視系": {
                "description": "心理描写と感情の変化を重視する文体",
                "narrative_style": "三人称全知視点",
                "detail_level": "中程度",
                "explicit_level": "中",
                "sensory_descriptions": [
                    "心理状態と身体的反応の関連性",
                    "感情の変化を身体的反応で表現",
                    "内面的な葛藤と快感の描写",
                    "心理的な高まりの段階的表現"
                ],
                "dialogue_style": [
                    "心理状態を反映したセリフ",
                    "感情の高まりを言葉で表現",
                    "内面的な葛藤をセリフで表現",
                    "心理的な変化を言葉で表現"
                ],
                "scene_descriptions": [
                    "心理状態と身体的反応の関連性",
                    "感情の変化を身体的反応で表現",
                    "内面的な葛藤と快感の描写",
                    "心理的な高まりの段階的表現"
                ],
                "example_expressions": [
                    "【ツンデレ】「彼女の心の中で理性と快感が激しく戦っている…でも、もっと…」",
                    "【甘え系】「彼女の心の中で優しさと快感が混じり合う…もっと…」",
                    "【無口・クール】「彼女の心の中で静かな陶酔が広がる…もっと…」",
                    "【天然・無邪気】「彼女の心の中で純粋な好奇心と快感が混じり合う…もっと…」",
                    "【ヤンデレ】「彼女の心の中で独占欲と快感が激しく燃え上がる…もっと…」",
                    "【お姉さん】「彼女の心の中で包容力と快感が優しく包み込む…もっと…」",
                    "【後輩・年下】「彼女の心の中で従順さと快感が甘く絡み合う…もっと…」"
                ]
            },
            "官能小説系": {
                "description": "官能小説特有の文体と表現技法",
                "narrative_style": "三人称限定視点",
                "detail_level": "詳細",
                "explicit_level": "高",
                "sensory_descriptions": [
                    "官能小説特有の表現技法",
                    "性的な行為の詳細な記述",
                    "快感の段階的な変化を描写",
                    "官能的な雰囲気の描写"
                ],
                "dialogue_style": [
                    "官能小説特有のセリフ表現",
                    "性的な快感を言葉で表現",
                    "身体的な反応を言葉で表現",
                    "官能的な雰囲気を言葉で表現",
                    "女の子の受け側：意味のある言葉を少なめに、感嘆詞中心",
                    "高まりの度合いで感嘆詞の強度を段階的に上げる"
                ],
                "scene_descriptions": [
                    "官能小説特有の描写技法",
                    "性的な行為の詳細な記述",
                    "快感の段階的な変化を描写",
                    "官能的な雰囲気の描写"
                ],
                "example_expressions": [
                    "【ツンデレ】「べ、別に…でも、気持ちいい…もっと…」",
                    "【甘え系】「ん…気持ちいい…もっと…」",
                    "【無口・クール】「……気持ちいい…もっと…」",
                    "【天然・無邪気】「えへへ…なんだか気持ちいいね…もっと…」",
                    "【ヤンデレ】「あなたは私だけのもの…気持ちいい…もっと…」",
                    "【お姉さん】「ふふ…可愛いのね…気持ちいい…もっと…」",
                    "【後輩・年下】「先輩…気持ちいいです…もっと…動いてください…」"
                ]
            }
        }
        
        # 番号付き文体リスト
        self.style_list = list(self.writing_styles.keys())
        
        self.detail_indicators = {
            "非常に詳細": [
                "身体の動きを微細に描写",
                "性的な部位の具体的な名称を使用",
                "快感の段階的な変化を詳細に表現",
                "五感を活用した生々しい描写"
            ],
            "詳細": [
                "身体の動きを詳細に描写",
                "性的な行為の具体的な記述",
                "快感の変化を表現",
                "感覚的な描写を重視"
            ],
            "中程度": [
                "身体の動きを適度に描写",
                "性的な行為を控えめに記述",
                "感情と身体の反応を融合",
                "雰囲気を重視した描写"
            ]
        }
        
        self.explicit_indicators = {
            "最高": [
                "性的な部位の具体的で生々しい名称を使用",
                "性的な行為の詳細で直接的な記述",
                "生々しい感嘆詞・間投詞とセリフの多用",
                "身体的な反応の微細な描写",
                "女の子の受け側：段階的な感嘆詞の強度変化",
                "ピーク時は途切れ途切れの断続的な喘ぎ声"
            ],
            "高": [
                "性的な部位の具体的な名称を使用",
                "性的な行為の具体的な記述",
                "生々しい感嘆詞・間投詞の使用",
                "身体的な反応の詳細な描写",
                "女の子の受け側：段階的な感嘆詞の強度変化"
            ],
            "中": [
                "性的な部位を控えめに表現",
                "性的な行為を比喩的に記述",
                "官能的な表現の使用",
                "感情と身体の反応を融合"
            ]
        }

    def get_style_by_number(self, style_number: int) -> str:
        """番号で文体を取得"""
        if 1 <= style_number <= len(self.style_list):
            return self.style_list[style_number - 1]
        else:
            raise ValueError(f"無効な文体番号です。1から{len(self.style_list)}の範囲で指定してください。")
    
    def list_styles(self) -> None:
        """利用可能な文体一覧を表示"""
        print("=" * 60)
        print("📝 利用可能な文体一覧")
        print("=" * 60)
        for i, style_name in enumerate(self.style_list, 1):
            style_data = self.writing_styles[style_name]
            print(f"{i}. {style_name}")
            print(f"   {style_data['description']}")
            print(f"   詳細度: {style_data['detail_level']} | 生々しさ: {style_data['explicit_level']}")
            print()

    def generate_style(self, style_type: str = None) -> Dict:
        """文体指示を生成"""
        if style_type is None:
            style_type = random.choice(list(self.writing_styles.keys()))
        
        style_data = self.writing_styles[style_type]
        
        generated_style = {
            "style_type": style_type,
            "description": style_data["description"],
            "narrative_style": style_data["narrative_style"],
            "detail_level": style_data["detail_level"],
            "explicit_level": style_data["explicit_level"],
            "sensory_descriptions": style_data["sensory_descriptions"],
            "dialogue_style": style_data["dialogue_style"],
            "scene_descriptions": style_data["scene_descriptions"],
            "example_expressions": style_data["example_expressions"]
        }
        
        # 詳細度と生々しさの指示を追加
        generated_style["detail_guidelines"] = self.detail_indicators[style_data["detail_level"]]
        generated_style["explicit_guidelines"] = self.explicit_indicators[style_data["explicit_level"]]
        
        return generated_style

    def format_style(self, style: Dict) -> str:
        """文体指示を整形して出力"""
        output = f"""
【{style['style_type']}】
{style['description']}

【基本設定】
・視点: {style['narrative_style']}
・詳細度: {style['detail_level']}
・生々しさ: {style['explicit_level']}

【描写技法】
"""
        
        for i, desc in enumerate(style["sensory_descriptions"], 1):
            output += f"  {i}. {desc}\n"
        
        output += "\n【セリフ・会話技法】\n"
        for i, desc in enumerate(style["dialogue_style"], 1):
            output += f"  {i}. {desc}\n"
        
        output += "\n【シーン描写技法】\n"
        for i, desc in enumerate(style["scene_descriptions"], 1):
            output += f"  {i}. {desc}\n"
        
        output += "\n【詳細度ガイドライン】\n"
        for i, desc in enumerate(style["detail_guidelines"], 1):
            output += f"  {i}. {desc}\n"
        
        output += "\n【生々しさガイドライン】\n"
        for i, desc in enumerate(style["explicit_guidelines"], 1):
            output += f"  {i}. {desc}\n"
        
        output += "\n【表現例】\n"
        for i, expr in enumerate(style["example_expressions"], 1):
            output += f"  {i}. {expr}\n"
        
        return output

    def generate_and_display(self) -> None:
        """文体指示を生成して表示"""
        style = self.generate_style()
        print("=" * 60)
        print("✍️ 文体指示生成結果")
        print("=" * 60)
        print(self.format_style(style))

def main():
    """メイン関数"""
    import sys
    import argparse
    
    generator = WritingStyleGenerator()
    
    # 引数パーサーの設定
    parser = argparse.ArgumentParser(description='文体指示生成スクリプト')
    parser.add_argument('count', nargs='?', type=int, default=1, help='生成する文体指示の数（デフォルト: 1）')
    parser.add_argument('--style', '-s', type=int, help='指定した番号の文体を使用（1-5）')
    parser.add_argument('--list', '-l', action='store_true', help='利用可能な文体一覧を表示')
    
    args = parser.parse_args()
    
    # 文体一覧表示
    if args.list:
        generator.list_styles()
        return
    
    # 生成数の検証
    if args.count <= 0:
        print("生成数は1以上の整数を指定してください。")
        return
    
    # 文体指定の検証
    if args.style is not None:
        try:
            style_name = generator.get_style_by_number(args.style)
        except ValueError as e:
            print(f"エラー: {e}")
            return
    else:
        style_name = None
    
    # 文体指示を生成
    for i in range(args.count):
        if args.count > 1:
            print(f"\n【文体指示 {i+1}】")
        
        if style_name:
            style = generator.generate_style(style_name)
            print("=" * 60)
            print("✍️ 文体指示生成結果")
            print("=" * 60)
            print(generator.format_style(style))
        else:
            generator.generate_and_display()
        
        if i < args.count - 1:
            print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
