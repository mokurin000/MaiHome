## 注意

本文只涉及在已获取到相关 .app 文件后，经授权需要进行解包、运行游戏的场景，不涉及相关的版权文件和脱壳程序。

## 前言

请确保你的 .app 并非由 uns***REBORN 提取了 contents 。

它会导致大量的文本日文编码出错，引入大量难以溯源的启动问题。

你需要手动附加 `internal_0.vhd` 以复制出相关文件。

## 基本指向

segatools.ini 会提供一些按键映射，和aquamai.toml定义的会同时生效。

AquaMai 负责 patch 游戏的基本启动，并提供可视化（MaiChartManager）、更易用的配置方式。

segatools.ini 的 [patch] 会由于引入 MelonLoader 而失效

请勿尝试升级 MelonLoader 到 0.6.5 以上

## 切换到其他私服

如需连接到其他私服，需要联系私服进行以下文件的配置：
> 需填写 [KeyChip] 中 ID 键
- AMDaemon/segatools.ini
> 内容即为aime号码
- AMDaemon/DEVICE/aime.txt


## Melon Loader 相关文件

```text
Package/version.dll
Package/dobby.dll
Package/MelonLoader
```

## AquaMai 相关文件

```text
Package/Mods/AquaMai.dll
Package/AquaMai.toml
```

## 相关已脱壳程序

```text
AMDaemon/amdaemon.exe
Package/Sinmai_Data/Managed/Assembly-CSharp.dll
Package/Sinmai_Data/Managed/AMDaemon.NET.dll
Package/Sinmai_Data/Plugins/amdaemon_api.dll
Package/Sinmai_Data/Plugins/Cake.dll
Package/Sinmai.exe
```

<!-- https://t.me/sasakure/60546 -->
