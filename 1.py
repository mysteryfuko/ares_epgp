import sqlite3

dataDkp= [
  ["锤爆诸位的蛋","DRUID","654","1234"],
  ["百耶德","DRUID","642","927"],
  ["白鹿丶青崖","DRUID","79","998"],
  ["等风来追风去","HUNTER","603","1078"],
  ["你挺闹啊","HUNTER","583","1158"],
  ["污妖王猎犬","HUNTER","489","659"],
  ["Spirithunter","HUNTER","404","509"],
  ["Rz","HUNTER","270","300"],
  ["猎小白","HUNTER","214","234"],
  ["刀枪炮","HUNTER","103","103"],
  ["夜尘","HUNTER","63","63"],
  ["随宁","HUNTER","49","49"],
  ["蠢逼","HUNTER","23","23"],
  ["玩儿","HUNTER","23","23"],
  ["老虎钳","HUNTER","5","5"],
  ["宝猪","HUNTER","5","5"],
  ["小小玄女","HUNTER","0","10"],
  ["韩大爷","HUNTER","0","490"],
  ["趴下有凶器","MAGE","698","1107"],
  ["塞露修斯","MAGE","587","952"],
  ["傑尼亀","MAGE","567","1227"],
  ["小悠悠呢","MAGE","455","495"],
  ["Suedaiba","MAGE","339","1066"],
  ["白夏","MAGE","318","438"],
  ["出雲小胖","MAGE","305","1180"],
  ["暗祭暴击","MAGE","296","536"],
  ["善孝丶","MAGE","289","479"],
  ["Ryhnell","MAGE","271","536"],
  ["夜辰","MAGE","250","697"],
  ["维他命三号氵","MAGE","228","1049"],
  ["Minyuhao","MAGE","133","133"],
  ["Skywalkeer","MAGE","118","118"],
  ["名为你的诗","MAGE","20","20"],
  ["小法思","MAGE","18","18"],
  ["playerfidvcm","MAGE","12","12"],
  ["谁便搞搞","MAGE","10","15"],
  ["毛布鞋","MAGE","0","0"],
  ["其实不麻烦","PALADIN","494","576"],
  ["鲸落丶南北","PALADIN","492","1177"],
  ["猫系棉花糖","PALADIN","490","492"],
  ["野狼来了啊","PALADIN","407","512"],
  ["阿尼戈尼","PALADIN","368","413"],
  ["熊猫炒河粉","PALADIN","181","489"],
  ["那个奶德","PALADIN","132","132"],
  ["沙茶","PALADIN","118","648"],
  ["战神丶雅典娜","PALADIN","97","97"],
  ["痴情的马库斯","PALADIN","58","58"],
  ["西瓜巨人","PALADIN","22","22"],
  ["阿瑞斯卡妙","PALADIN","13","13"],
  ["秋叶","PALADIN","0","0"],
  ["脾气极差","PALADIN","0","302"],
  ["沉睡听风","PALADIN","-5","735"],
  ["爆浆南瓜饼","PRIEST","434","506"],
  ["霜写秋叶","PRIEST","318","1128"],
  ["丶粪海仙蛆丶","PRIEST","263","865"],
  ["雷先生","PRIEST","230","390"],
  ["布丁很甜","PRIEST","218","383"],
  ["奶不住人","PRIEST","191","236"],
  ["卷卷小魔女","PRIEST","163","830"],
  ["杜兰斯","PRIEST","103","103"],
  ["能彻斯特方程","PRIEST","91","96"],
  ["你放心我奶你","PRIEST","74","74"],
  ["落橙橙","PRIEST","68","68"],
  ["蓝色雨天","PRIEST","68","95"],
  ["奶水就是蒩","PRIEST","68","68"],
  ["甜心千雾","PRIEST","52","274"],
  ["星旭者","PRIEST","48","48"],
  ["荒村尸叔","PRIEST","47","866"],
  ["大米饺子","PRIEST","33","33"],
  ["小筱","PRIEST","20","20"],
  ["星河入梦","PRIEST","16","454"],
  ["島根猫","PRIEST","11","11"],
  ["笨憨","ROGUE","824","1234"],
  ["凉拖鞋","ROGUE","756","1051"],
  ["奥州鲍","ROGUE","336","481"],
  ["我隐了","ROGUE","247","497"],
  ["卷卷大魔王","ROGUE","246","386"],
  ["鬼步无痕","ROGUE","126","236"],
  ["西瓜飞人","ROGUE","118","1013"],
  ["白短短","ROGUE","98","393"],
  ["巨蟹座丶赛奇","ROGUE","95","125"],
  ["冷血杀戮","ROGUE","53","53"],
  ["人造人十八号","ROGUE","27","27"],
  ["那个奶骑","ROGUE","27","27"],
  ["魅影之纱","ROGUE","23","23"],
  ["无息","ROGUE","15","15"],
  ["戳你的屁屁","ROGUE","4","4"],
  ["熊猫会武功","ROGUE","4","4"],
  ["逍遥灵儿","WARLOCK","343","733"],
  ["Nelson","WARLOCK","211","241"],
  ["天使与恶魔","WARLOCK","205","332"],
  ["永恒的痕迹","WARLOCK","185","1200"],
  ["歐米茄","WARLOCK","172","172"],
  ["小米饺子","WARLOCK","102","707"],
  ["咻咻的仙凤","WARLOCK","0","10"],
  ["四月你的謊言","WARRIOR","674","1239"],
  ["怒米","WARRIOR","670","805"],
  ["剑锋丨所指","WARRIOR","482","497"],
  ["满目星河","WARRIOR","452","497"],
  ["湛王","WARRIOR","317","733"],
  ["無事生非","WARRIOR","257","677"],
  ["泽明","WARRIOR","241","411"],
  ["霹雳娇娘","WARRIOR","220","1212"],
  ["明明是个女孩","WARRIOR","180","1185"],
  ["不良少年今井","WARRIOR","69","84"],
  ["我是坦克哥","WARRIOR","68","1148"],
  ["红骷髅","WARRIOR","48","48"],
  ["Straight","WARRIOR","32","312"],
  ["璃小磊","WARRIOR","20","50"],
  ["天蝎座丶灭正","WARRIOR","0","0"],
  ["憨逼","WARRIOR","0","0"],
]
data = [
  ["锤爆诸位的蛋","DRUID","4738.89","104.66"],
  ["笨憨","ROGUE","4726.29","161.1"],
  ["其实不麻烦","PALADIN","3025.88","11.09"],
  ["甜心千雾","PRIEST","2816.31","29.56"],
  ["白鹿丶青崖","DRUID","3668.18","133.57"],
  ["趴下有凶器","MAGE","3875.2","185.54"],
  ["等风来追风去","HUNTER","2924.23","72.71"],
  ["永恒的痕迹","WARLOCK","3813.08","189.05"],
  ["你挺闹啊","HUNTER","4068.83","225.57"],
  ["傑尼亀","MAGE","4703.98","383.33"],
  ["Suedaiba","MAGE","4391.8","348.84"],
  ["明明是个女孩","WARRIOR","4626.65","393.83"],
  ["出雲小胖","MAGE","4550.9","437.33"],
  ["Spirithunter","HUNTER","2281.13","108.82"],
  ["霜写秋叶","PRIEST","2799.63","206.31"],
  ["塞露修斯","MAGE","3026.52","316.77"],
  ["星河入梦","PRIEST","1435.86","0"],
  ["鲸落丶南北","PALADIN","3815.52","517.86"],
  ["小悠悠呢","MAGE","1480.86","28.05"],
  ["满目星河","WARRIOR","1435.86","28.05"],
  ["四月你的謊言","WARRIOR","4604.66","804.54"],
  ["霹雳娇娘","WARRIOR","4526.59","808.26"],
  ["泽明","WARRIOR","1152.81","0"],
  ["鬼步无痕","ROGUE","1151.46","0"],
  ["熊猫炒河粉","PALADIN","1754.6","157.41"],
  ["我是坦克哥","WARRIOR","3233.7","648.51"],
  ["西瓜飞人","ROGUE","3416.09","702.5"],
  ["剑锋丨所指","WARRIOR","1480.86","159"],
  ["丶粪海仙蛆丶","PRIEST","2787.6","571.32"],
  ["小米饺子","WARLOCK","2609.5","519"],
  ["百耶德","DRUID","2550.31","516.62"],
  ["Nelson","WARLOCK","919.38","0"],
  ["爆浆南瓜饼","PRIEST","2207.48","487.81"],
  ["湛王","WARRIOR","2829.48","725.27"],
  ["凉拖鞋","ROGUE","3018.29","835.57"],
  ["猫系棉花糖","PALADIN","1480.86","281.74"],
  ["奶不住人","PRIEST","750.6","0"],
  ["我隐了","ROGUE","1480.86","312.68"],
  ["维他命三号氵","MAGE","3094.06","1100.74"],
  ["奥州鲍","ROGUE","1916.3","627.88"],
  ["阿尼戈尼","PALADIN","1152.81","294"],
  ["怒米","WARRIOR","2041.58","759.84"],
  ["白夏","MAGE","1057.86","264.25"],
  ["猎小白","HUNTER","763.2","159"],
  ["歐米茄","WARLOCK","378","0"],
  ["野狼来了啊","PALADIN","1344.46","826.32"],
  ["人造人十八号","ROGUE","297","0"],
  ["随宁","HUNTER","291.6","0"],
  ["憨逼","WARRIOR","291.6","0"],
  ["布丁很甜","PRIEST","314.64","80.03"],
  ["名为你的诗","MAGE","216","0"],
  ["老虎钳","HUNTER","45","0"],
  ["你惯的啊","MAGE","5.23","0"]
]

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
for i in data:
  c.execute("SELECT * from point_score WHERE name=?",[i[0]])
  recode_res = c.fetchone()
  if recode_res:
    c.execute('UPDATE point_score SET ep=? , gp=? WHERE name=?',(i[2],i[3],i[0]))
  else:
    c.execute('INSERT INTO point_score (dkp,ep,name,job,gp) VALUES (?,?,?,?,?) ',(0,i[2],i[0],i[1],i[3]))
  #c.execute('INSERT INTO point_score (dkp,ep,name,job,gp) VALUES (?,?,?,?,?) ',(i[2],0,i[0],i[1],0))
conn.commit()
conn.close()