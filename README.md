
#### 说明
* unittest 框架管理测试用例
* 使用 poco 进行元素的定位和操作
* BeautifulReport 作为测试结果的报告

#### 使用
* unittest 框架，在 test_cases 下对应模块的目录中添加用例
* 直接运行 runner.py 执行所有用例
* 报告生成在 ./report 目录下
* 用例成功的截图保存在 ./img 目录下
* 连接 iOS 相对麻烦，所以目前是在 runner.py 里面手动处理
* 目前代码只适合连接单一设备测试

#### 怎么写 case
* 可以选择通过 airtest IDE 先进行元素定位，然后移植到 python case 中
* 每个 case 的收尾工作应该是返回到首页
* 对比结果需要放在每个 case 脚本的最后

#### 闲谈
> 个人认为 iOS 自动化最难的是前两步，首先有一个开发者账号，然后连接上真机;
* 连接 iOS 见官方教程：https://github.com/AirtestProject/IOS-Tagent
* UI 自动化的另外一个难点就是怎么能够让客户端的开发规范统一

#### 未解决问题
* poco 目前不支持 toast 的处理
* poco 对于 iOS 的部分类型元素支持不好，比如 StaticText

> 注：poco 的元素定位可以通过使用 airtest IDE 进行，具体 airtest 的用法请查看官方文档