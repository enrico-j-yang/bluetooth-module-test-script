# -*- coding: utf-8 -*-
# language: zh-CN

功能: 蓝牙
============================================
    蓝牙连接、蓝牙音乐、蓝牙电话
    
    @BluetoothConnection, @wip
    场景:   蓝牙模块初次配对连接
        假如    蓝牙模块未配对
        假如    蓝牙模块的配对码为4444
        假如    蓝牙模块可以连接手机蓝牙

        当      用户使用蓝牙设备连接电动车蓝牙模块
        而且    用户输入PIN码4444
        那么    蓝牙模块已连接

    @BluetoothConnection
    场景:   蓝牙初次配对PIN码错误，配对失败
        假如    蓝牙模块未配对
        假如    蓝牙模块的配对码为4444
        假如    蓝牙模块可以连接手机蓝牙

        当      用户使用蓝牙设备连接电动车蓝牙模块
        而且    用户输入PIN码9999
        那么    手机提示配对码不正确
    
    @BluetoothConnection
    场景:   蓝牙初次配对不输入配对码，配对失败
        假如    蓝牙模块未配对
        假如    蓝牙模块的配对码为4444
        假如    蓝牙模块可以连接手机蓝牙

        当      用户使用蓝牙设备连接电动车蓝牙模块
        而且    用户不输入PIN码
        那么    手机未连接蓝牙

    @BluetoothConnection
    场景:   蓝牙已有配对设备，蓝牙模块自动连接已配对的蓝牙设备
        假如    蓝牙模块已有配对设备
        当      用户启动蓝牙模块
        那么    手机未连接蓝牙

        假如    蓝牙模块可以连接蓝牙设备
        当      用户等待7秒后
        那么    蓝牙模块正在连接

        当      用户等待5秒后
        那么    蓝牙模块已连接
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备面板自动连接已配对的蓝牙设备失败，15秒后重连成功
        假如    蓝牙模块已有配对设备
        当      用户启动电动车
        那么    手机未连接蓝牙

        假如    蓝牙模块不可以连接蓝牙设备
        当      用户等待7秒后
        那么    蓝牙模块正在连接

        当      用户等待5秒后
        那么    手机未连接蓝牙
        
        当      用户等待15秒后
        那么    蓝牙模块正在连接
        
        假如    蓝牙模块可以连接蓝牙设备
        那么    蓝牙模块已连接

    
    @BluetoothConnection
    场景:   蓝牙已有配对设备面板自动连接已配对的蓝牙设备失败，15秒后重连也失败
        假如    蓝牙模块已有配对设备
        当      用户启动电动车
        那么    手机未连接蓝牙

        假如    蓝牙模块不可以连接蓝牙设备
        当      用户等待7秒后
        那么    蓝牙模块正在连接

        当      用户等待5秒后
        那么    手机未连接蓝牙

        假如    蓝牙模块不可以连接蓝牙设备
        当      用户等待15秒后
        那么    蓝牙模块正在连接

        当      用户等待5秒后
        那么    手机未连接蓝牙
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备，重新配对
        假如    蓝牙模块已有配对设备
        当      用户启动电动车
        那么    手机未连接蓝牙
        
        当      用户等待7秒后
        那么    蓝牙模块正在连接
        
        当      用户短按+键
        那么    手机未连接蓝牙
        
        当      用户使用蓝牙设备连接电动车蓝牙模块
        那么    蓝牙模块正在连接
        
        假如    蓝牙模块可以连接蓝牙设备
        当      用户输入PIN码0000
        那么    蓝牙模块已连接
    
    @BluetoothMusic
    场景:   蓝牙音乐信息显示
        假如    蓝牙模块已经连接手机蓝牙
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
    
    @BluetoothMusic
    场景:   蓝牙音乐播放与暂停
        假如    蓝牙模块已经连接手机蓝牙
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
        
        当      用户在手机上暂停音乐
        那么    蓝牙模块收到暂停音乐播放MA指令

        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
    
    @BluetoothMusic
    场景:   蓝牙音乐音量调节
        假如    蓝牙模块已经连接手机蓝牙
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
        
        当      用户减少蓝牙模块音量
        那么    蓝牙音乐音量减少
        
        当      用户增加蓝牙模块音量
        那么    蓝牙音乐音量增加

    @BluetoothMusic
    场景:   蓝牙音乐音量调节到具体音量值
        假如    蓝牙模块已经连接手机蓝牙
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran

        当      用户减少蓝牙模块音量到0
        那么    蓝牙音乐音量减少到0

        当      用户增加蓝牙模块音量到15
        那么    蓝牙音乐音量增加到15

        当      用户增加蓝牙模块音量到30
        那么    蓝牙音乐音量增加到30

        当      用户减少蓝牙模块音量到15
        那么    蓝牙音乐音量减少到15
    
    @BluetoothMusic
    场景:   蓝牙音乐上一首下一首
        假如    蓝牙模块已经连接手机蓝牙
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
        
        当      用户在手机上切换音乐到上一首歌(Ed Sheeran - Galway Girl)
        那么    蓝牙模块收到上一首歌曲名Galway Girl和歌手名Ed Sheeran
        而且    蓝牙模块播放上一首歌曲
        
        当      用户在手机上切换音乐到下一首歌(Ed Sheeran - Shape of You)
        那么    蓝牙模块收到下一首歌曲名Shape of You和歌手名Ed Sheeran
        而且    蓝牙模块播放下一首歌曲
    
    @BluetoothCall
    场景:   蓝牙电话来电
        假如    蓝牙模块已经连接手机蓝牙
        当      用户使用另一台手机拨打已连接蓝牙模块的手机
        那么    蓝牙模块收到来电指令和来电号码13148923264
        
        当      用户接听电话
        那么    蓝牙模块收到通话中的指令和通话号码13148923264
        
        当      用户挂断电话
        那么    蓝牙模块收到挂断指令和挂断号码
    
    @BluetoothCall
    场景:   蓝牙电话拨打
        假如    蓝牙模块已经连接手机蓝牙
        当      用户使用已连接蓝牙模块的手机拨打另一台手机
        那么    蓝牙模块收到拨打指令和拨打号码13148923264
        
        当      用户接听电话
        那么    蓝牙模块收到通话中的指令和通话号码13148923264
        
        当      用户挂断电话
        那么    蓝牙模块收到挂断指令和挂断号码
    
    @BluetoothCall
    场景:   蓝牙音乐播放中电话来电
        假如    蓝牙模块已经连接手机蓝牙
        假如    蓝牙模块音乐(Ed Sheeran - Shape of You)播放中
        当      用户使用另一台手机拨打已连接蓝牙模块的手机
        那么    蓝牙模块收到暂停音乐播放MA指令
        那么    蓝牙模块收到来电指令和来电号码13148923264
        
        当      用户接听电话
        那么    蓝牙模块收到通话中的指令和通话号码13148923264
        
        当      用户挂断电话
        那么    蓝牙模块收到挂断指令和挂断号码
        那么    蓝牙模块恢复音乐播放
        而且    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
    
    @BluetoothCall
    场景:   蓝牙音乐播放中电话拨打
        假如    蓝牙模块已经连接手机蓝牙
        假如    蓝牙模块音乐(Ed Sheeran - Shape of You)播放中
        当      用户使用已连接蓝牙模块的手机拨打另一台手机
        那么    蓝牙模块收到暂停音乐播放MA指令
        那么    蓝牙模块收到拨打指令和拨打号码13148923264
        
        当      用户接听电话
        那么    蓝牙模块收到通话中的指令和通话号码13148923264
        
        当      用户挂断电话
        那么    蓝牙模块收到挂断指令和挂断号码
        那么    蓝牙模块恢复音乐播放
        而且    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
        
        
        
        
        
    
    
        
    