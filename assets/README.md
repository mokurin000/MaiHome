## 资源相关

游戏中有不同的资源。其中:

[MaichartConverter]: https://github.com/Neskol/MaichartConverter
[CriTools]: https://github.com/kohos/CriTools
[WannaCRI]: https://github.com/donmai-me/WannaCRI
[AssetStudio]: https://github.com/Perfare/AssetStudio

|Name | Tool|Note |
|:-----|:----- | :----- |
|AssetBundleImages| |破事最多的，负责各类图像资产|
|AssetBundleImages/jacket| [AssetStudio] | 曲绘 |
|music | [MaichartConverter] |谱面文件 <br>工具需要自己编译，Release过于老旧|
|MovieData| [WannaCRI] |背景视频，CRiWare 加密<br>需要额外依赖 `python-json-logger`|
|SoundData| [CriTools] |曲目音乐，CRiWare 加密|

一些用于并发处理的脚本放在本项目的 `/utils` 中。
