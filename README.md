# README
原作者：https://github.com/shinan6/chatgpt_cmd
做了较大改进


# before use
需要设置环境变量OPENAI_API_KEY为opanai的api key，
设置CHAT_HISTORY_DIR为保存目录。

然后就可以随意使用了。


# use
输入内容即可进行聊天。
当输入需要换行的内容时，输入/i(-i,\i均可，之后的所以/都可以使用\\、-代替)进入长文本输入模式，输入完毕请输入END。

聊天结束想要保存聊天记录可以输入/q,/exit,/quit,不想保存聊天记录输入/q!。

配合windows终端使用效果更佳.

# other commands
/save 保存当前记录为模板
/load 加载某一模板
/print 打印当前聊天记录
/reinput 修改某一段聊天记录
/turing 可以让程序执行你输入的代码
/help 打印帮助