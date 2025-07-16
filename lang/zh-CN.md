# 舞萌DX家用指南

本指南全面介绍在家游玩街机音游《舞萌DX》的硬件配置与软件解决方案。

## 硬件方案

您可选择通用设备或仿街机定制控制器来实现家用游玩。

### 通用设备方案

基础配置可直接使用现有触屏设备：
* Windows系统：推荐微软Surface或低延迟触控笔记本电脑
* 安卓设备：建议搭载骁龙865及以上芯片的平板
* iPad设备：A10X芯片及以上型号为佳

### 专业控制器（需额外支出）

追求街机体验的玩家可选择以下定制控制器（多为小众社群或个人工作室制作）

> 运输与定制说明：
> 
> * ADX控制器：国际空运约4900元，海运约2700元（注：仅60Hz版本支持海运）
> * 雾雨控制器：基础版可升级按键：
>     * 街机/[睡神]按键：+200元
>     * [兔键]按键：+550元
>     * PP/铜制框架：+250元

| 型号             | 价格(元) | 刷新率 | 屏幕配置   | 工艺              | 备注               | 图片 |
| :--------------- | :------- | :----- | :--------- | :---------------- | :----------------- | :---- |
| [maipico]\(DIY版) | 约700    | -      | 需自备     | 蚀刻+ito膜        | 需自行组装         |
| maipico(成品)    | 约1000   | -      | 不详       | 不详              | 二手平台常见       | [<img width="200px" src="https://github.com/user-attachments/assets/99047a28-2e40-4839-a64f-f5b2f8295b54" />](https://www.goofish.com/item?id=891098479283) |
| 雾雨(内屏版)     | 1499     | -      | 不含       | 蚀刻              | 无外键支持         | [<img src="https://github.com/user-attachments/assets/17e2ca22-326d-4fe5-bbe7-a7910cc3f4f3" width=200px />](https://www.goofish.com/item?id=865663465655) |
| 雾雨(基础版)     | 2349     | -      | 不含       | 蚀刻              | 含基础按键与框架   | |
| 晶台             | 2299     | -      | 不含      | 蚀刻+ito           | 闲鱼: 吃个桃桃   | [<img src="https://github.com/user-attachments/assets/92ed71e3-9973-4d2d-ad71-f63e897bcd86" width=200px />](https://www.goofish.com/item?id=800676155187) |
| 纸片台           | 5999     | 60Hz   | 京东方面板 | 无痕蚀刻+自研触控 | 闲鱼：纸片片片片片 | [<img width="200px" src="https://github.com/user-attachments/assets/5197b7ee-af35-4f33-94cd-1a10f08f714c" />](https://www.goofish.com/item?id=922999290368) |
| HDX青春版          | 4399     | -      | 不含       | 无痕蚀刻          |                    | [<img width="200px" src="https://github.com/user-attachments/assets/c383b6c3-4d27-41de-94e4-1a2c10d2a660" />](https://item.taobao.com/item.htm?id=821589059415&skuId=5822246444323) |
| HDX              | 5888     | -      | 不含       | 无痕蚀刻          |                    | [<img src="https://github.com/user-attachments/assets/3a9eb950-b99b-4d28-bdf7-336a9425d8aa" width=200px />](https://item.taobao.com/item.htm?id=821589059415) |
| HDX              | 7288     | 60Hz   | 雷鸟鹏6se  | 无痕蚀刻          | 含60Hz显示器       | <img width="200px" src="https://github.com/user-attachments/assets/f0abfd9d-dc96-40b5-934b-6160a6508dce" /> |
| HDX              | 9588     | 120Hz  | 定制屏幕   | 无痕蚀刻          | 配备120Hz高刷屏    | |
| ADX LITE+        | 4998     | -      | 不含       | 无痕蚀刻          |                    | [<img width="200px" src="https://github.com/user-attachments/assets/c331bccf-2df2-4f1f-87e7-5cadfd058a80" />](https://item.taobao.com/item.htm?id=936311370897) |
| ADX 3            | 8000     | 60Hz   | 不详       | 无痕蚀刻          | 含60Hz显示器       | |
| ADX 3            | 12000    | 120Hz  | 不详       | 无痕蚀刻          | 配备120Hz高刷屏    | |




-----

## 软件方案

现有多种软件可模拟《舞萌DX》游玩体验，包括净室实现[^1]与需游戏数据的加载器。

> `******DX` 性能提示：
> 部分安卓定制ROM（包括某些官方系统）可能表现逊于AOSP系ROM（如LineageOS）。例如一加Ace3（骁龙8Gen2）在官方系统下偶发卡顿，而刷入LineageOS 21的骁龙865设备一加8T则运行流畅。

| 应用名称      | 安卓 | iOS/iPad/macOS | Windows | 实现方式         | 备注             |
| :------------ | :--- | :------------- | :------ | :--------------- | :--------------- |
| [Sentakki]    | ✔️    | ✔️              | ✔️       | 净室实现         | 见Discord群置顶  |
| [AstroDX]     | ✔️    | ✔️              | ❌       | 净室实现         | 开源模拟器       |
| `******DX`    | ✔️    | ✔️              | ❌       | 非官方移动端移植 | 需邀请制访问     |
| [MajdataPlay] | ❌    | ❌              | ✔️       | 净室实现         | 开源谱面播放工具 |
| segatools     | ❌    | ❌              | ✔️       | 加载器/模拟器    | 需非授权游戏数据 |
| Sinmai        | ❌    | ❌              | ✔️       | 官方实现         | NB2HI4DTHIXS64DFOJTG64TNMFUS4ZLWNFWGYZLBNNSXELTDN5WS63LBNZ2WC3BP |

[睡神]: https://space.bilibili.com/895949/
[兔键]: http://www.taobao.com/list/item/660013732031.htm
[maipico]: https://github.com/whowechina/mai_pico
[astrodx]: https://wiki.astrodx.com
[sentakki]: https://github.com/LumpBloom7/sentakki
[MajdataPlay]: https://github.com/LingFeng-bbben/MajdataPlay

[^1]: 净室实现：指开发团队在未接触原始代码的情况下，通过逆向工程和重新设计实现的软件，避免版权纠纷的开发方法。
