# MaiHome

This guide provides a comprehensive overview of the hardware and software options available for playing the arcade rhythm game *maimai DX* at home.

> Note: Because oversea users have no easy choice other than ADX Controller,
> 
> more info are only get updated in Chinese version.

## Hardware Solutions

You can play *maimai DX* at home using either general-purpose devices or specialized, custom-built controllers that mimic the arcade experience.

### General-Purpose Devices

For a basic setup, you can use a touch-screen device you may already own.

  * Windows: A Microsoft Surface or any Windows laptop with a low-latency touchscreen is a viable option.
  * Android: A tablet with a Snapdragon 865 processor or better is recommended for smooth performance.
  * iPad: An iPad with an A10X chip or a newer model is suggested.

### Dedicated Controllers (Extra Cost)

For a more authentic arcade experience, several dedicated controllers are available for purchase. These are often produced by smaller communities or individual makers.

> Shipping & Customization Notes:
>
>   * ADX Controllers: International air freight costs approximately 4900 CNY, while sea transport is around 2700 CNY (note: only the 60Hz model is available via sea). Other models are unlikely to be shipped internationally.
>   * Wuyu Controllers: Starting from the base model with standard buttons, you can upgrade to specialized buttons:
>       * Arcade/[Shui Shen][Shui Shen] (睡神) Buttons: +200 CNY
>       * [Tu Jian][Tu Jian] (兔键) Buttons: +550 CNY
>       * PP/Copper Frame: +250 CNY

| Model               | Price (CNY) | Refresh Rate | Screen        | Notes                                                           |
| :------------------ | :---------- | :----------- | :------------ | :-------------------------------------------------------------- |
| [maipico] (DIY)     | \~700       | N/A          | User-provided | Requires self-assembly (Do-It-Yourself).                        |
| maipico (Pre-built) | \~1200      | N/A          | Unknown       | Pre-built, often found on second-hand platforms like Idle Fish. |
| Wuyu (Board Only)   | 1499        | N/A          | Not Included  | Controller board only; no buttons or frame.                     |
| Wuyu (Basic)        | 2349        | N/A          | Not Included  | Includes basic buttons and frame.                               |
| HDX Air             | 4399        | N/A          | Not Included  |                                                                 |
| HDX                 | 5888        | N/A          | Not Included  |                                                                 |
| HDX                 | 7288        | 60 Hz        | Rayneo 5S365C | Includes a 60Hz monitor.                                        |
| ADX                 | 8000        | 60 Hz        | Unknown       | Includes a 60Hz monitor.                                        |
| HDX                 | 9588        | 120 Hz       | Custom        | Includes a custom 120Hz high-refresh-rate monitor.              |
| ADX                 | 12000       | 120 Hz       | Unknown       | Includes a 120Hz high-refresh-rate monitor.                     |

-----

## Software Solutions

Several software options exist to simulate the *maimai DX* gameplay on your devices. They range from clean-room implementations to loaders that require game data.

> Performance Tip for `******DX`:
> Some users report that custom Android ROMs (or even some stock ROMs) can lead to a worse experience compared to AOSP-based ROMs (like LineageOS). For example, my OnePlus Ace 3 (Snapdragon 8 Gen 2) experiences random lag with its stock OS, while a OnePlus 8T (Snapdragon 865) running LineageOS 21 performs flawlessly.

| Application   | Android | iOS/iPadOS/macOS | Windows | Implementation         | Notes                                                    |
| ------------- | ------- | ---------------- | ------- | ---------------------- | :------------------------------------------------------- |
| [sentakki]    | ✔️       | ✔️                | ✔️       | Clean Room             | Open-source simulator.                                   |
| [AstroDX]     | ✔️       | ✔️                | ❌       | Clean Room             | Open-source simulator.                                   |
| `******DX`    | ✔️       | ✔️                | ❌       | Unofficial Mobile Port | Requires an invitation to access.                        |
| [MajdataPlay] | ❌  ️     | ❌ ️               | ✔️       | Clean Room             | Open-source chart player.                                |
| segatools     | ❌       | ❌                | ✔️       | Loader/Emulator        | Requires an unauthorized copy of the game's arcade data. |

[shui shen]: https://space.bilibili.com/895949/
[tu jian]: http://www.taobao.com/list/item/660013732031.htm
[maipico]: https://github.com/whowechina/mai_pico
[astrodx]: https://wiki.astrodx.com
[sentakki]: https://github.com/LumpBloom7/sentakki
[majdataplay]: https://github.com/LingFeng-bbben/MajdataPlay
