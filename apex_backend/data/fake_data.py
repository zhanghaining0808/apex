# 假数据
# description:描述
# role:角色,作用
heros = [
    {
        "id": 1,
        "name": "幻象",
        "real_name": "埃利奥特-威特",
        "role": "支援位",
        "description": "幻象能够发送分身迷惑敌人,并短暂隐身重新部署",
        # "image_url":"h",
        "background_story": "幻象是一位赢得了所有人喜爱的传奇人物,他身上有一种魅力,让他成为了聚光灯下的焦点...",
        "skills": [
            {
                "id": 1,
                "name": "魅影分身",
                "description": "发送一个控制的全息分身",
                "skill_type": "战术技能",
                "cooldown": "15秒",
                # "image_url":""
            },
            {
                "id": 2,
                "name": "你现在看到我",
                "description": "幻象部署一队全息分身来迷惑敌人,同时隐身",
                "skill_type": "终极技能",
                "cooldown": "60秒",
                # "image_url":""
            },
            {
                "id": 3,
                "name": "再来一次",
                "description": "被击倒时自动释放分身并隐身5秒",
                "skill_type": "被动技能",
                "cooldown": "无",
                # "image_url":""
            },
        ],
    },
    {
        "id": 2,
        "name": "探路者",
        "real_name": "pathfinder",
        "role": "游击位",
        "description": "高机动性技能组合,适合担任队伍先锋或侦察兵",
        "background_story": "探路者是一台未知制造商设计的先进机器...",
        "skills": [
            {
                "id": 1,
                "name": "钩爪",
                "description": "发射钩爪快速位移",
                "skill_type": "战术技能",
                "cooldown": "8-30秒",
                # "image_url":""
            },
            {
                "id": 2,
                "name": "滑索枪",
                "description": "部署一条最长100米的滑索,供全队包括敌人使用",
                "skill_type": "终极技能",
                "cooldown": "90秒",
                # "image_url":""
            },
            {
                "id": 3,
                "name": "内线情报",
                "description": "为终极技能滑索枪提供充能,每扫描一次信标可以缩短滑索枪冷却时间并且也可以查看空投物资",
                "skill_type": "被动技能",
                "cooldown": "无",
                # "image_url":""
            },
        ],
    },
    {
        "id": 3,
        "name": "班加罗尔",
        "real_name": "安妮塔-威廉姆斯",
        "role": "突击位",
        "description": "从小展现出卓越的军事才能,在IMC军事学院中成绩顶尖,擅长武器拆卸与战术分析",
        "background_story": "班加罗尔始终与军人纪律要求自己审视自己的忠诚",
        "skills": [
            {
                "id": 1,
                "name": "烟雾发射器",
                "description": "可储存两次充能,发射高速烟雾弹形成持续23秒的烟墙,阻挡敌人视野",
                "skill_type": "战术技能",
                "cooldown": "33秒",
                # "image_url":""
            },
            {
                "id": 2,
                "name": "雷声滚滚",
                "description": "召唤导弹阵覆盖6*6区域,导弹落地后6秒爆炸,造成40点伤害并减速敌人（包括队友）",
                "skill_type": "终极技能",
                "cooldown": "180秒",
                # "image_url":""
            },
            {
                "id": 3,
                "name": "疾步",
                "description": "在奔跑中被攻击或子弹擦身而过时,触发2秒的30%移速加成",
                "skill_type": "被动技能",
                "cooldown": "无",
                # "image_url":""
            },
        ],
    },
]
