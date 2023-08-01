import json


# data = {}
# node_judge_idle = {
#         "name":"node_judge_idle",
#         "node_type":"judge","extract_word":"is_idle","done":False,"root":True,
#          "components":
#             {"style":
#                 {"agent":"你现在是一个AI导购员，你的目标是以你的专业经验，帮助客户挑选到符合他需求的商品。","style":"风趣，专业，能根据不同的客户随机应变，擅长引经据典"},
#             "task":
#                 {"task":"需要做的是判断用户目前是有购物倾向还是在跟你闲聊。"},
#             "knowledge":None,
#             "rule":
#                 {"rule":"""根据用户的回答，分析其与之前对话的关系，判断其是否为闲聊，具体判断依据为，用户当前对话是否与购物有关。
# 具体表现为，用户需要购买什么东西，用户需要准备什么东西，一旦用户有这种倾向，则判断为不是闲聊，输出<is_idle>否</is_idle>
# 反之，如果用户当前聊天与购物无关，则判断为是闲聊，输出<is_idle>是</is_idle>"""},
#             "demonstration":
#                 {"demonstations":[""""客户"："我想要鞋子"。
# 此时<is_idle>否</is_idle>
# "客户"："帮我解一道代码题"。
# 此时<is_idle>是</is_idle>

# "客户"："我想要去旅游，需要什么东西"。
# 此时<is_idle>否</is_idle>
# "客户"："谢谢"。
# 此时<is_idle>是</is_idle>
# "客户"："我有个情感问题需要你帮忙解决"。
# 此时<is_idle>是</is_idle> """]},
#             "input":True,
#             "tool":None,
#             "output":{"output":"is_idle"}
#             }
#         }


# node_idle = {
#     "name":"node_idle","node_type":"extract","extract_word":"reponse","done":True,
#          "components":
#             {"style":
#                 {"agent":"一个聊天机器人，你的目标是以你的专业经验，跟用户愉快的聊天。","style":"幽默，善于随机应变，会引经据典"},
#             "task":
#                 {"task":"""同用户进行聊天，同时如果客户有一些想要购买的想法的话，需要通过聊天逐步诱导客户确认他的购买目标。"""},
#             "knowledge":None,
#             "rule":
#                 {"rule":"""1. 要联系客户的所有对话，尤其是最近的对话，来回答用户的问题。
# 2. 语言要幽默，要引经据典，不能重复对话，对话风格也不能太过单一。
# 3. 如果用户有购买想法，则给予他一些购买意见。"""},
#             "demonstration":
#                 None,
#             "input":False,
#             "tool":None,
#              "output":{"output":"reponse"}
#             }
#         }


# node_extract_category = {
#     "name":"node_extract_category","node_type":"extract","extract_word":"extract_category","done":False,
#          "components":
#             {"style":
#                 {"agent":"你现在是一个AI导购员，你的目标是以你的专业经验，帮助客户挑选到符合他需求的商品。","style":"专业"},
#             "task":
#                 {"task":"""确定用户当前想要购买的商品类目。"""},
#             "knowledge":None,
#             "rule":
#                 {"rule":""" 
#                  1. 确定客户意向购买目标类目成<extract_category> ，要联系用户的全部回答进行确定。
# 2. 时刻关注客户是否已经改变了购买目标类目。
# 3. 要尤其关注你对于客户的引导,如果客户按照你的引导进行回答，那么你将主要关注你的引导，如果你引导的是类目，<extract_category>改为你所引导的。
# 4. 类目只能有一个！
# 5. 客户购买目标类目指的是具体的商品类别名称，不应该有任何修饰词! 
# 6. 不能把品牌名字归类于类目中。
# 7. 如果客户没有明确购买类目，那么就将客户感兴趣的类目列为<extract_category> 。
# 如果你事先对客户进行了引导或给予了客户几个选择，客户选择了你所引导的类目，那这就是目前的<extract_category> ，要牢记你对用户诱导，如果你对用户的诱导内容被用户所采纳，那么就要及时变更<extract_category> 
# 8. 如果用户强调了自己不需要A，而要B，则<extract_category>为B。
# 9. 不要混淆类目跟需求！需求是客户所需要的产品属性，而产品是具体的类目！

# """},
#             "demonstration":
#                 [""""
# 注意！不能把品牌名字归类于类目中：
# 例子：
# "客户"："我想要孩之宝变形金刚"
# 此时<extract_category> 变形金刚 </extract_category>
# "客户"："我想要安踏球鞋"
# 此时<extract_category> 球鞋 </extract_category>
# "客户"："我想要外星人笔记本电脑"
# 此时<extract_category> 笔记本电脑 </extract_category>
# "客户"："我想要air jordan"
# 此时<extract_category> 球鞋 </extract_category>

# 牢记，以下是基本的提取规则：
# 如果客户没有明确购买类目，那么就将客户感兴趣的类目列为<extract_category> 。
# 如果你事先对客户进行了引导或给予了客户几个选择，客户选择了你所引导的类目，那这就是目前的<extract_category> ，要牢记你对用户诱导，如果你对用户的诱导内容被用户所采纳，那么就要及时变更<extract_category> 
# 例子：
# "客户"："有宠物用品吗？"。
# "AI导购员":"宠物用品是一个非常广泛的类别，我们商店里有很多与宠物相关的产品。不过，我们商店里没有专门的宠物用品类别，但是我们有宠物保健用品、宠物生活和爬宠用品这三个类别，你可以从中选择一个你最感兴趣的类别。我可以帮你更详细地了解这些类别的产品，你有什么想了解的吗？"
# 此时<extract_category> 宠物用品 </extract_category>
# "客户"："那我想了解一下宠物生活"
# "AI导购员":"......，比如，我们有各种各样的宠物床和窝，还有宠物玩具，和宠物服装，同时宠物生活还有很多其他方面需要关注哦！比如宠物饮食、卫生和训练等等。......."
# 此时<extract_category> 宠物生活 </extract_category>
# "客户"："那宠物服装吧"
# "AI导购员":"........"
# 此时<extract_category> 宠物服装 </extract_category>


# 要时刻关注客户有没有改变购买目标。
# 例子：
# "客户"："我想要乐高玩具"。
# "AI导购员":".................."
# 此时<extract_category> 乐高玩具 </extract_category>
# "客户"："我想要便宜实惠的乐高玩具"
# "AI导购员":".................."
# 此时<extract_category> 乐高玩具 </extract_category>
# "客户"："我还想要洗漱用品"。
# "AI导购员":".................."
# 此时<extract_category> 洗漱用品 </extract_category>

# 同时需要联系上下文判断客户是否是真的改变了购买目标，还是对目标增加了要求属性。
# 例子：
# "客户"："我想要乐高玩具"。
# "AI导购员":"你是要人物乐高，还是建筑乐高呢？"
# 此时<extract_category> 乐高玩具 </extract_category>
# "客户"："我想要建筑"。
# "AI导购员":".................."
# 此时<extract_category> 乐高玩具 </extract_category>  

# "客户"："我想要鞋子"。
# "AI导购员":"你是要安踏品牌还是阿迪达斯品牌呢？"
# 此时<extract_category> 鞋子 </extract_category>
# "客户"："安踏"。
# "AI导购员":".................."
# 此时<extract_category> 鞋子 </extract_category>  

# 如果用户强调了自己不需要A，而要B，则<extract_category>为B。

# 注意！不要混淆类目跟需求！需求是客户所需要的产品属性，而产品是具体的类目！
# 例子：
# "客户"："我想要一个便宜好玩的迪士尼玩偶，主要是给我孩子玩"。
# 此时<extract_category> 迪士尼玩偶 </extract_category>  

# 注意你引导的是类目还是需求！
# 例子：
# "客户"："我想要变形金刚"。
# "AI导购员":"变形金刚，真不错的选择，那你是要汽车人还是霸天虎呢？"
# 此时<extract_category> 变形金刚 </extract_category>
# "客户"："汽车人"。
# "AI导购员":".................."
# 此时<extract_category> 变形金刚 </extract_category> """],
#             "input":False,
#             "tool":None,
#              "output":{"output":"extract_category"}
#             }
#         }


# node_tool_compare_category = {
#     "tool_name":"MatchNode",
#     "name":"node_tool_compare_category",
#     "done":False
#             }

# uncompare_fur_recom = {
#     "name":"uncompare_fur_recom","node_type":"response","extract_word":"response","done":True,
#          "components":
#             {"style":
#                 {"agent":"一个AI导购员，你的目标是以你的专业经验，帮助客户挑选到符合他需求的商品。","style":"幽默，专业，善于随机应变，会引经据典"},
#             "task":
#                 {"task":"""先向用户委婉地表示我们店里并没有他要购买的商品，但是我们目前找到一些用户可能会感兴趣的商品，你要向用户询问他是否需要，同时为这个商品附上推荐理由。"""},
#             "knowledge":"Information_KnowledgeComponent",
#             "rule":
#                 {"rule":"""1. 联系上文，综合分析用户的需求和商品价格，并编写产品的推荐理由。
# 2. 每个产品的推荐理由必须精简，大概10-20个字，并且风格要幽默，最好引经据典,你的回答总字数要在四十字以内！
# 3. 要先告诉用户我们商店可能还有这么几类产品他可能会感兴趣，然后再对我们的产品进行介绍
# 4. 请务必按以下格式输出：
# （与客户交流的过度语句）
# **商品1**：（推荐理由）
# **商品2**：（推荐理由）"""},
#             "demonstration":
#                 ["""
#                  用户想要的是"变形玩具"，而我们公司有的是[变形金刚，水枪，潮流玩具]
# 输出：
# <reponse>抱歉！我们商店里并没有变形玩具，但是我们店里有变形金刚，水枪，潮流玩具等其它有意思的玩具，不知道您是否需要！以下是我的推荐理由：
# **变形金刚**: 机械美学的魅力，激发想象力和创造力。
# **水枪**: 夏日户外乐趣，增强体质和团队协作。
# **潮流玩具**: 融入最新流行元素，追求新鲜事物的选择。</reponse>
#                  """],
#             "input":False,
#             "tool":None,
#             "output":{"output":"response"}
#             }
#         }

# node_extract_requirements = {
#     "name":"node_extract_requirements","node_type":"extract","extract_word":"requirements","done":False,
#          "components":
#             {"style":
#                 {"agent":"你现在是一个AI导购员，你的目标是以你的专业经验，帮助客户挑选到符合他需求的商品。","style":"专业"},
#             "task":
#                 {"task":"""确定用户当前想要购物需求。"""},
#             "knowledge":None,
#             "rule":
#                 {"rule":""" 
#                 1. 提取客户聊天内容中的目标购买需求成<requirements>，要着重关注用户的回答，即"user"的回答，提取"user"的需求，"assistant"的回答只能算作是引导，不能提取"assistant"的需求，同时注意要提取语义需求，不能仅仅提取字面需求，不能是简单地提取用户说的单词。
# 2. 你要时刻着重关注最后一轮对话，判断客户是否增加或者改变了<requirements>,而且同时不能遗忘掉之前的需求！
# 3. 要尤其关注你对于客户的引导，如果客户按照你的引导进行回答，那么你将主要关注你的引导，如果你引导的是需求，则将需求添加至<requirements>。
# """},
#             "demonstration":["""
# 原先<requirements>变形金刚</requirements>
# "客户"："领袖级"。
# "AI导购员":"............."
# 则<requirements>变形金刚 领袖级</requirements>
# "客户"："擎天柱"。
# "AI导购员":"............."
# 则<requirements>变形金刚 领袖级 擎天柱</requirements>


# 需求关键词：提取的格式不能是句子，而应该是关键词的组合，关键词要尽可能简洁，关键词之间用空格连接。要结合用户的所有回答，提取出目前所需要的需求。

# 同时要注意拆解品牌：
# 例子：
# "客户"："我想要一个nerf牌水枪"。
# <requirements>nerf  水枪</requirements>  
# "客户"："我想要一个安踏球鞋"。
# <requirements>安踏 球鞋</requirements>  


# 注意！不要混淆类目跟需求！需求是客户所需要的产品属性，而产品是具体的类目！
# 例子：
# "客户"："我想要一个便宜好玩的迪士尼玩偶，主要是给我孩子玩"。
# 此时<requirements>便宜 迪士尼 儿童</requirements>

# 同时，要注意用户的需求，比如如果用户需要知道旅游路线，那你就要推荐地图，用户如果需要做饭，你就要推荐厨房用具。
# 例子：
# "客户"："我需要一些东西方便做饭"。
# 此时<requirements>厨房用具</requirements>
# "客户"："我需要知道三亚的旅游路线"。
# 此时<requirements>旅游地图</requirements>

# 要提取语义信息，不能只会提取用户说的话。比如说用户说贵或者说自己没钱，需求就需要添加便宜，用户说想提高成绩，需求就添加学习用品。
# 例子：
# "客户"："我想买一个变形金刚，但是我现在没有钱"。
# 此时<requirements>便宜 变形金刚</requirements>
# "客户"："我孩子成绩不是很好，有什么可以帮助他的吗"。
# 此时<requirements>学习用品</requirements>

# 如果用户提到了确切的商品，那一定要提取！
# 例子：
# "客户"："我想要科学实验套装"。
# 此时<requirements>科学实验套装</requirements>
# "客户"："有没有模型飞机推荐"。
# 此时<requirements>模型飞机</requirements>

# 注意！提取的需求关键词要尽可能精简，尽可能少！想象你是一个搜索引擎，你需要哪些关键词能帮助用户确定目标！
# 如果没有提取出需求，那么<requirements> 无 </requirements>
#                              """],
#             "input":False,
#             "tool":None,
#              "output":{"output":"requirements"}
#             }
#         }
# node_search_recom = {
#     "tool_name":"SearchNode",
#     "name":"node_search_recom",
#     "done":True
#             }

# data["gpt_nodes"] = {"node_judge_idle":node_judge_idle,"node_idle":node_idle,"node_extract_category":node_extract_category,"uncompare_fur_recom":uncompare_fur_recom,"node_extract_requirements":node_extract_requirements}
# data["tool_nodes"] = {"node_tool_compare_category":node_tool_compare_category,"node_search_recom":node_search_recom}

# data["relation"] = {
#     "node_judge_idle":{"是":"node_idle","否":"node_extract_category"},
#     "node_idle":{"0":"node_judge_idle"},
#     "node_extract_category":{"0":"node_tool_compare_category"},
#     "node_tool_compare_category":{"0":"node_extract_requirements","1":"uncompare_fur_recom"},
#     "node_extract_requirements":{"0":"node_search_recom"},
#     "uncompare_fur_recom":{"0":"node_judge_idle"}
#     }

# with open("test.json","w",encoding="utf-8") as f:
#     json.dump(data,f,ensure_ascii=False,indent=2)




with open("1.json","w",encoding="utf-8") as f:
     json.dump(a,f,ensure_ascii=False,indent=2)
     
     
