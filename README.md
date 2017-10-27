# MaxMatch
句子的最大匹配算法

基于实例的机器翻译系统，预先存储⼀个语料库，其中每⼀项都是⼀个对译的双语句⼦对，通
常也完成了句⼦中词的对齐。当输⼊⼀个待翻译句⼦，翻译步骤为三步：⾸先完成待翻译句⼦的
分割，获得⼀系列已存在语料中的⽚段；然后以拷贝语料库已有译⽂的⽅式完成每个⽚段的翻译，
得到⼀系列译⽂⽚段；最后将所有译⽂⽚段组装成整个句⼦的译⽂。其中第⼀步，我们称为匹配
（match），匹配得到的单个⽚段越长，对应的译⽂越可靠，匹配得到的⽚段数量越少，组装阶段出
错的机会就越少，因此，我们希望得到尽可能长、尽可能少的⽚段，我们把这个⽚段结果称为最⼤
匹配（maxmatch）。
这个作业的⽬的就是设计和实现求解句⼦最⼤匹配的算法。例⼦如下，假设语料库为如下三个
句⼦，

    ⼩明 今年 ⼆⼗ 岁
    复旦 ⼤学 的 学⽣ 参加 了 歌唱 表演
    他 是 交通 ⼤学 的 ⽼师


下⾯是⼀些输⼊和输出情况，


    输⼊ ⼩明 是 复旦 ⼤学 的 学⽣
    输出 [⼩明] [是] [复旦 ⼤学 的 学⽣]
    输⼊ 他 今年 是 ⼤学 的 学⽣ 了
    输出 [他] [今年] [是] [⼤学 的 学⽣] [了]


