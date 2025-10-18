#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
統合エロ小説執筆支援システム
キャラクター生成、プロット生成、セリフ最適化、性行為フロー、文体指示を統合

使用方法:
    python novel_writing_assistant.py character                    # キャラクター生成
    python novel_writing_assistant.py plot                        # プロット生成
    python novel_writing_assistant.py dialogue                    # セリフ最適化
    python novel_writing_assistant.py sexflow                     # 性行為フロー生成
    python novel_writing_assistant.py style                       # 文体指示生成
    python novel_writing_assistant.py complete                    # 完全な小説生成（全機能統合）
    python novel_writing_assistant.py --help                      # ヘルプ表示
"""

import random
import argparse
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class CharacterData:
    """キャラクターデータクラス"""
    name: str
    gender: str
    age: int
    height: int
    personality_type: str
    personality_description: str
    first_person: str
    second_person: str
    hobby: str
    occupation: str
    characteristic: str

@dataclass
class PhaseData:
    """フェーズデータクラス"""
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

class NovelWritingAssistant:
    """統合エロ小説執筆支援クラス"""
    
    def __init__(self):
        """初期化"""
        self._initialize_character_data()
        self._initialize_plot_data()
        self._initialize_sex_flow_data()
        self._initialize_style_data()
    
    def _initialize_character_data(self):
        """キャラクターデータを初期化"""
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
            "male": list(range(165, 185)),
            "female": list(range(145, 165))
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
    
    def _initialize_plot_data(self):
        """プロットデータを初期化"""
        self.plot_phases = [
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
            PhaseData(
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
    
    def _initialize_sex_flow_data(self):
        """性行為フローデータを初期化"""
        self.sex_flows = {
            "フェラチオ": {
                "description": "口を使った奉仕行為（女性視点）",
                "viewpoint": "女性",
                "phases": {
                    "導入": [
                        "彼の前に跪く姿勢を取る",
                        "彼の股間に向かって座る",
                        "彼の勃起したペニスの先端に軽くキスをする",
                        "先端から滲み出る透明な液体を舌で舐める"
                    ],
                    "開始": [
                        "彼の勃起したペニスを唇で包み込む",
                        "彼のペニスを手で支えながら深く含む",
                        "舌先で彼のペニスの先端を激しく舐める",
                        "口全体を上下に動かして彼のペニスを激しく刺激する"
                    ],
                    "発展": [
                        "舌で彼のペニス全体を激しく舐め回す",
                        "彼のペニスを喉の奥深くまで含み込む",
                        "舌の動きのリズムを激しく変えて刺激する",
                        "手で彼のペニスの根元を強く刺激する"
                    ],
                    "頂点": [
                        "彼の射精を促すように動きを激しくする",
                        "彼のペニスを深く含み直して射精を待つ",
                        "彼の射精を完全に受け入れる準備をする",
                        "彼の精液を口内で受け取りながら飲み込む"
                    ],
                    "余韻": [
                        "彼の精液を完全に飲み込む",
                        "彼のペニスを優しく舐めて後処理をする",
                        "彼のペニスを口から離して顔を上げる",
                        "彼を見上げながら満足そうに微笑む"
                    ]
                }
            },
            "正常位": {
                "description": "男性が上に位置する基本的な体位（男性視点）",
                "viewpoint": "男性",
                "phases": {
                    "導入": [
                        "彼女と向き合って座る",
                        "彼女の唇に優しくキスをする",
                        "彼女の身体を自分の身体に寄せ合う",
                        "彼女の体温を感じる"
                    ],
                    "開始": [
                        "彼女の身体を優しく愛撫しながら興奮を高める",
                        "彼女の身体と自分の身体を触れ合わせる",
                        "彼女の息遣いを感じながら動き始める",
                        "彼女の上に覆いかぶさり優しく動き始める"
                    ],
                    "発展": [
                        "彼女の濡れた膣内で徐々に動きを深める",
                        "彼女の反応を感じながら激しく動く",
                        "彼女とのリズムを合わせながら動きを激しくする",
                        "彼女を愛情を込めて動かしながら興奮を高める"
                    ],
                    "頂点": [
                        "彼女の膣内で激しく動いて快感を追求する",
                        "彼女を強く抱きしめながら動きを激しくする",
                        "彼女と完全に一つになりながら頂点を迎える",
                        "彼女と共に頂点を迎えて射精する"
                    ],
                    "余韻": [
                        "彼女を静かに抱きしめ合う",
                        "彼女の鼓動を感じる",
                        "彼女との愛情を確認し合う",
                        "彼女と静寂を共有する"
                    ]
                }
            },
            "立ちバック": {
                "description": "後ろからの立ちバック体位（男性視点）",
                "viewpoint": "男性",
                "phases": {
                    "導入": [
                        "彼女の後ろから抱きしめる",
                        "彼女の首筋に優しくキスをする",
                        "彼女の身体を自分の身体に寄せ合う",
                        "彼女の体温を感じる"
                    ],
                    "開始": [
                        "彼女の膣内で優しく動き始める",
                        "彼女の反応を感じる",
                        "彼女とのリズムを作る",
                        "彼女を愛情を込めて動かす"
                    ],
                    "発展": [
                        "彼女の膣内で動きを深める",
                        "彼女の反応を感じる",
                        "彼女とのリズムを合わせる",
                        "彼女の膣内で動きを激しくする"
                    ],
                    "頂点": [
                        "彼女の膣内で激しく動く",
                        "彼女を抱きしめる",
                        "彼女と完全に一つになる",
                        "彼女と共に頂点を迎える"
                    ],
                    "余韻": [
                        "彼女を静かに抱きしめ合う",
                        "彼女の鼓動を感じる",
                        "彼女との愛情を確認し合う",
                        "彼女と静寂を共有する"
                    ]
                }
            }
        }
    
    def _initialize_style_data(self):
        """文体データを初期化"""
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
                    "身体的な反応を言葉で表現"
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
                    "性的な興奮を言葉で表現"
                ]
            }
        }
    
    def generate_character(self, gender: str = None) -> CharacterData:
        """キャラクターを生成"""
        if gender is None:
            gender = random.choice(["male", "female"])
        
        personality_type = random.choice(list(self.personality_types.keys()))
        personality_data = self.personality_types[personality_type]
        
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
        
        age = random.choice(self.ages)
        hobby = random.choice(self.hobbies)
        occupation = random.choice(self.occupations)
        characteristic = random.choice(personality_data["characteristics"])
        
        return CharacterData(
            name=name,
            gender=gender,
            age=age,
            height=height,
            personality_type=personality_type,
            personality_description=personality_data["description"],
            first_person=first_person,
            second_person=second_person,
            hobby=hobby,
            occupation=occupation,
            characteristic=characteristic
        )
    
    def generate_plot(self, character_type: str = "tsundere") -> Dict:
        """プロットを生成"""
        plot_data = {
            "character_type": character_type,
            "phases": []
        }
        
        # 性格タイプのマッピング（英語→日本語）
        character_type_mapping = {
            "tsundere": "ツンデレ",
            "甘え系": "甘え系",
            "無口・クール": "無口・クール",
            "天然・無邪気": "天然・無邪気",
            "ヤンデレ": "ヤンデレ",
            "お姉さん": "お姉さん",
            "後輩・年下": "後輩・年下"
        }
        
        # 性格タイプに応じたセリフ生成
        japanese_character_type = character_type_mapping.get(character_type, "ツンデレ")
        personality_data = self.personality_types.get(japanese_character_type, self.personality_types["ツンデレ"])
        personality_data["personality_type"] = japanese_character_type
        
        for phase in self.plot_phases:
            # 性格・役割に応じたセリフを生成
            male_dialogue = self._generate_character_dialogue(phase, personality_data, "male", "立ちバック")
            female_dialogue = self._generate_character_dialogue(phase, personality_data, "female", "立ちバック")
            
            sound_effects = self._generate_sound_effects(phase.intensity)
            physical_reaction = self._enhance_physical_reaction(phase.intensity)
            
            plot_data["phases"].append({
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
            })
        
        return plot_data
    
    def _generate_character_dialogue(self, phase: PhaseData, personality_data: Dict, gender: str, play_type: str = "立ちバック") -> str:
        """性格・役割に応じたセリフを生成"""
        personality_type = personality_data.get("personality_type", "ツンデレ")
        
        # 役割を決定（性別とプレイタイプから）
        role = self._determine_role(gender, play_type)
        
        # 攻め・受けの役割別セリフパターン
        if personality_type == "無口・クール":
            if role == "attacker":  # 攻め役
                if self._get_intensity_level(phase.intensity) == "low":
                    options = ["「……大丈夫か？」", "「……準備はいいか？」", "「……気持ちいいか？」"]
                elif self._get_intensity_level(phase.intensity) == "medium":
                    options = ["「……気持ちいいか？」", "「……感じるか？」", "「……いいか？」"]
                elif self._get_intensity_level(phase.intensity) == "high":
                    options = ["「……もっと…」", "「……続けて…」", "「……まだ…」"]
                else:  # peak
                    options = ["「……あ…」", "「……ああ…」", "「……うあ…」"]
            else:  # 受け役
                if self._get_intensity_level(phase.intensity) == "low":
                    options = ["「……ん…」", "「……うん…」", "「……そう…」"]
                elif self._get_intensity_level(phase.intensity) == "medium":
                    options = ["「……気持ちいい…」", "「……いい…」", "「……感じる…」"]
                elif self._get_intensity_level(phase.intensity) == "high":
                    options = ["「……もっと…」", "「……続けて…」", "「……まだ…」"]
                else:  # peak
                    options = ["「……あ…」", "「……ああ…」", "「……うあ…」"]
        
        elif personality_type == "ツンデレ":
            if role == "attacker":  # 攻め役
                if self._get_intensity_level(phase.intensity) == "low":
                    options = ["「……一緒に帰ろう」", "「……大丈夫か？」", "「……準備はいいか？」"]
                elif self._get_intensity_level(phase.intensity) == "medium":
                    options = ["「……気持ちいいか？」", "「……感じるか？」", "「……いいか？」"]
                elif self._get_intensity_level(phase.intensity) == "high":
                    options = ["「……もっと…」", "「……続けて…」", "「……まだ…」"]
                else:  # peak
                    options = ["「……あ…」", "「……ああ…」", "「……うあ…」"]
            else:  # 受け役
                if self._get_intensity_level(phase.intensity) == "low":
                    options = ["「べ、別に…一緒に帰るわけじゃないし…」", "「ち、違うから…勘違いしないで…」", "「な、何よ…そんな顔して…」"]
                elif self._get_intensity_level(phase.intensity) == "medium":
                    options = ["「ち、違うから…でも、もっと…」", "「や、やめて…でも、気持ちいい…」", "「だ、だめ…でも、続けて…」"]
                elif self._get_intensity_level(phase.intensity) == "high":
                    options = ["「や、やめて…でも、気持ちいい…」", "「だ、だめ…でも、続けて…」", "「も、もう…やめて…でも…」"]
                else:  # peak
                    options = ["「だ、だめ…でも、続けて…」", "「も、もう…やめて…でも…」", "「あ、あぁ…ばか…」"]
        
        else:
            # デフォルトは元のセリフを使用
            if gender == "male":
                return random.choice(phase.male_dialogue)
            else:
                return random.choice(phase.female_dialogue)
        
        # セリフを選択
        return random.choice(options)
    
    def _determine_role(self, gender: str, play_type: str) -> str:
        """性別とプレイタイプから役割を決定"""
        if play_type == "立ちバック":
            return "attacker" if gender == "male" else "receiver"
        elif play_type == "フェラチオ":
            return "receiver" if gender == "male" else "attacker"
        elif play_type == "正常位":
            return "attacker" if gender == "male" else "receiver"
        else:
            # デフォルトは性別で決定
            return "attacker" if gender == "male" else "receiver"
    
    def _get_intensity_level(self, intensity: Tuple[int, int]) -> str:
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
    
    def generate_sex_flow(self, flow_type: str = None) -> Dict:
        """性行為フローを生成"""
        if flow_type is None:
            flow_type = random.choice(list(self.sex_flows.keys()))
        
        flow_data = self.sex_flows[flow_type]
        
        generated_flow = {
            "flow_type": flow_type,
            "description": flow_data["description"],
            "viewpoint": flow_data["viewpoint"],
            "phases": {}
        }
        
        for phase_name, actions in flow_data["phases"].items():
            num_actions = random.randint(2, 4)
            selected_actions = random.sample(actions, min(num_actions, len(actions)))
            generated_flow["phases"][phase_name] = selected_actions
        
        return generated_flow
    
    def generate_style(self, style_type: str = None) -> Dict:
        """文体指示を生成"""
        if style_type is None:
            style_type = random.choice(list(self.writing_styles.keys()))
        
        return self.writing_styles[style_type]
    
    def _generate_sound_effects(self, intensity: Tuple[int, int]) -> List[str]:
        """擬音語を生成"""
        avg_intensity = (intensity[0] + intensity[1]) / 2
        
        if avg_intensity <= 2:
            return ["ビクッ", "んっ"]
        elif avg_intensity <= 4:
            return ["ヌチュヌチュ", "あっ", "やっ"]
        elif avg_intensity <= 7:
            return ["ぱちゅぱちゅ", "あっあっ", "やっやっ"]
        else:
            return ["ドクドク", "ビクビク", "あっあっあっ", "やっやっやっ"]
    
    def _enhance_physical_reaction(self, intensity: Tuple[int, int]) -> str:
        """身体的反応を詳細化"""
        avg_intensity = (intensity[0] + intensity[1]) / 2
        
        if avg_intensity <= 2:
            return "微細な緊張感、身体の微細な震え"
        elif avg_intensity <= 4:
            return "身体的反応の明確化、息遣いの変化"
        elif avg_intensity <= 7:
            return "激しい身体的反応、制御不能状態"
        else:
            return "完全崩壊、激しい痙攣、射精・絶頂"
    
    def generate_complete_novel(self) -> Dict:
        """完全な小説生成（全機能統合）"""
        # キャラクター生成
        male_character = self.generate_character("male")
        female_character = self.generate_character("female")
        
        # プロット生成
        plot = self.generate_plot(female_character.personality_type)
        
        # 性行為フロー生成
        sex_flow = self.generate_sex_flow("立ちバック")
        
        # 文体指示生成
        style = self.generate_style("エロティック詳細系")
        
        return {
            "characters": {
                "male": male_character,
                "female": female_character
            },
            "plot": plot,
            "sex_flow": sex_flow,
            "style": style
        }
    
    def format_character(self, character: CharacterData) -> str:
        """キャラクターを整形して出力"""
        return f"""
【{character.name}】
性別: {character.gender}
年齢: {character.age}歳
身長: {character.height}cm
職業: {character.occupation}
趣味: {character.hobby}

性格タイプ: {character.personality_type}
性格説明: {character.personality_description}
特徴: {character.characteristic}

【呼び方設定】
一人称: {character.first_person}
二人称: {character.second_person}
"""
    
    def format_plot(self, plot_data: Dict) -> str:
        """プロットを整形して出力"""
        output = f"""
# {plot_data['character_type'].title()} エロ小説プロット

## 📋 基本設定
- **キャラクター**: {plot_data['character_type'].title()}

---

## 📖 プロット（{len(plot_data['phases'])}段階）

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
    
    def format_sex_flow(self, flow: Dict) -> str:
        """性行為フローを整形して出力"""
        output = f"""
【{flow['flow_type']} - {flow['viewpoint']}視点】
{flow['description']}

"""
        
        for phase_name, actions in flow["phases"].items():
            output += f"【{phase_name}】\n"
            for i, action in enumerate(actions, 1):
                output += f"  {i}. {action}\n"
            output += "\n"
        
        return output
    
    def format_style(self, style: Dict) -> str:
        """文体指示を整形して出力"""
        output = f"""
【{style['description']}】

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
        
        return output
    
    def format_complete_novel(self, novel_data: Dict) -> str:
        """完全な小説データを整形して出力"""
        output = """
# 完全統合エロ小説執筆支援データ

"""
        
        # キャラクター情報
        output += "## 👥 キャラクター設定\n\n"
        output += "### 👨 男性キャラクター\n"
        output += self.format_character(novel_data["characters"]["male"])
        output += "\n### 👩 女性キャラクター\n"
        output += self.format_character(novel_data["characters"]["female"])
        
        # プロット情報
        output += "\n" + "="*60 + "\n"
        output += self.format_plot(novel_data["plot"])
        
        # 性行為フロー情報
        output += "\n" + "="*60 + "\n"
        output += "## 🔥 性行為フロー\n"
        output += self.format_sex_flow(novel_data["sex_flow"])
        
        # 文体指示
        output += "\n" + "="*60 + "\n"
        output += "## ✍️ 文体指示\n"
        output += self.format_style(novel_data["style"])
        
        return output

def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='統合エロ小説執筆支援システム')
    parser.add_argument('mode', choices=['character', 'plot', 'dialogue', 'sexflow', 'style', 'complete'], 
                       help='実行モードを選択')
    parser.add_argument('--count', '-c', type=int, default=1, help='生成数（デフォルト: 1）')
    parser.add_argument('--character-type', help='キャラクタータイプ（ツンデレ、甘え系など）')
    parser.add_argument('--flow-type', help='性行為フロータイプ（フェラチオ、正常位、立ちバック）')
    parser.add_argument('--style-type', help='文体タイプ（生々しいリアル系、官能的ロマンチック系、エロティック詳細系）')
    
    args = parser.parse_args()
    
    assistant = NovelWritingAssistant()
    
    for i in range(args.count):
        if args.count > 1:
            print(f"\n【生成 {i+1}】")
        
        if args.mode == "character":
            male = assistant.generate_character("male")
            female = assistant.generate_character("female")
            print("=" * 60)
            print("🎭 キャラクター生成結果")
            print("=" * 60)
            print("\n👨 男性キャラクター")
            print(assistant.format_character(male))
            print("\n👩 女性キャラクター")
            print(assistant.format_character(female))
            
        elif args.mode == "plot":
            character_type = args.character_type or "tsundere"
            plot = assistant.generate_plot(character_type)
            print("=" * 60)
            print("✍️ プロット生成結果")
            print("=" * 60)
            print(assistant.format_plot(plot))
            
        elif args.mode == "dialogue":
            # セリフ最適化はプロット生成に含まれている
            character_type = args.character_type or "tsundere"
            plot = assistant.generate_plot(character_type)
            print("=" * 60)
            print("💬 セリフ最適化結果")
            print("=" * 60)
            print(assistant.format_plot(plot))
            
        elif args.mode == "sexflow":
            flow_type = args.flow_type
            flow = assistant.generate_sex_flow(flow_type)
            print("=" * 60)
            print("🔥 性行為フロー生成結果")
            print("=" * 60)
            print(assistant.format_sex_flow(flow))
            
        elif args.mode == "style":
            style_type = args.style_type
            style = assistant.generate_style(style_type)
            print("=" * 60)
            print("✍️ 文体指示生成結果")
            print("=" * 60)
            print(assistant.format_style(style))
            
        elif args.mode == "complete":
            novel_data = assistant.generate_complete_novel()
            print("=" * 60)
            print("📚 完全統合小説生成結果")
            print("=" * 60)
            print(assistant.format_complete_novel(novel_data))
        
        if i < args.count - 1:
            print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
