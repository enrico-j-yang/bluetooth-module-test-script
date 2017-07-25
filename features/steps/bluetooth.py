# -*- coding: utf-8 -*-
'''
bluetooth.py is step implementation file for bluetooth.feature

'''
import logging
from time import sleep


@given(u'蓝牙模块未配对')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.send("AT#DD")  # disconnect bluetooth
    context.florenceTestInput.sysIntEvt.send("AT#DV")  # delete bluetooth pair list


@given(u'蓝牙模块的配对码为{pin_code}')
def step_impl(context, pin_code):
    context.florenceTestInput.sysIntEvt.send("AT#MN" + pin_code)


@given(u'蓝牙模块可以连接手机蓝牙')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure cellphone can connect bluetooth")


@when(u'用户使用蓝牙设备连接电动车蓝牙模块')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please use cellphone connect e-bike bluetooth")


@then(u'蓝牙模块已连接')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothCMD', 'MG3')
    context.florenceActRes.mock_value('BluetoothCMD', 'MG3')
    context.florenceActRes.get_value_from_multi_line('BluetoothCMD', context.florenceExpRes.get_value('BluetoothCMD'))
    logging.debug("context.florenceExpRes.BluetoothCMD: " + str(context.florenceExpRes.dist['BluetoothCMD']))
    logging.debug("context.florenceActRes.BluetoothCMD: " + str(context.florenceActRes.dist['BluetoothCMD']))
    assert context.florenceActRes.dist['BluetoothCMD'] == context.florenceExpRes.dist['BluetoothCMD']

    context.florenceExpRes.set_value('BluetoothCMD', 'IB')
    context.florenceActRes.mock_value('BluetoothCMD', 'IB')
    context.florenceActRes.get_value_from_multi_line('BluetoothCMD', context.florenceExpRes.get_value('BluetoothCMD'))
    logging.debug("context.florenceExpRes.BluetoothCMD: " + str(context.florenceExpRes.dist['BluetoothCMD']))
    logging.debug("context.florenceActRes.BluetoothCMD: " + str(context.florenceActRes.dist['BluetoothCMD']))
    assert context.florenceActRes.dist['BluetoothCMD'] == context.florenceExpRes.dist['BluetoothCMD']


@when(u'用户输入PIN码{pin_code}')
def step_impl(context, pin_code):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please enter pin code:" + pin_code)


@then(u'手机提示配对码不正确')
def step_impl(context):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if pin code error tips exist>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"


@when(u'用户不输入PIN码')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please don't enter pin code and cancel pairing")


@then(u'手机未连接蓝牙')
def step_impl(context):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if bluetooth not connected>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"


@then(u'面板显示蓝牙图标')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_connected()

    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('Bluetooth', 'Connected')
    context.florenceActRes.mock_value('Bluetooth', 'Connected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']


@then(u'面板不显示蓝牙图标')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_disconnected()

    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('Bluetooth', 'Disconnected')
    context.florenceActRes.mock_value('Bluetooth', 'Disconnected')
    context.florenceActRes.get_value('Bluetooth')
    logging.debug("context.florenceExpRes.Bluetooth: " + str(context.florenceExpRes.dist['Bluetooth']))
    logging.debug("context.florenceActRes.Bluetooth: " + str(context.florenceActRes.dist['Bluetooth']))
    assert context.florenceActRes.dist['Bluetooth'] == context.florenceExpRes.dist['Bluetooth']


@when(u'用户不输入配对码')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please do not enter pin code")


@given(u'蓝牙模块已有配对设备')
def step_impl(context):
    context.execute_steps(u'''
        假如    蓝牙模块未配对
        当      用户使用蓝牙设备连接电动车蓝牙模块
        那么    面板进入系统设置
        
        当      用户输入PIN码0000
        那么    面板显示蓝牙图标
        ''')


@when(u'用户启动电动车')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_launched()


@when(u'用户等待{duration}秒后')
def step_impl(context, duration):
    sleep(float(duration))


@given(u'蓝牙模块可以连接蓝牙设备')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure cellphone bluetooth available")


@given(u'蓝牙模块不可以连接蓝牙设备')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please close cellphone bluetooth")


@given(u'面板已经连接手机蓝牙')
def step_impl(context):
    context.execute_steps(u'''
        假如    蓝牙模块未连接
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接
        
        当      用户使用蓝牙设备连接电动车蓝牙模块
        那么    面板显示蓝牙正在连接

        当      用户的蓝牙设备已经连接上电动车蓝牙模块
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        ''')


@when(u'用户在手机上播放音乐')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please play music on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Music Is The Key', 'Sarah Connor')


@then(u'面板显示音乐歌曲名和歌手名')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('MusicName', 'Music Is The Key')
    context.florenceActRes.mock_value('MusicName', 'Music Is The Key')
    context.florenceActRes.get_value('MusicName')
    logging.debug("context.florenceExpRes.MusicName: " + str(context.florenceExpRes.dist['MusicName']))
    logging.debug("context.florenceActRes.MusicName: " + str(context.florenceActRes.dist['MusicName']))
    assert context.florenceActRes.dist['MusicName'] == context.florenceExpRes.dist['MusicName']

    context.florenceExpRes.set_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.mock_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.get_value('MusicAuthor')
    logging.debug("context.florenceExpRes.MusicAuthor: " + str(context.florenceExpRes.dist['MusicAuthor']))
    logging.debug("context.florenceActRes.MusicAuthor: " + str(context.florenceActRes.dist['MusicAuthor']))
    assert context.florenceActRes.dist['MusicAuthor'] == context.florenceExpRes.dist['MusicAuthor']


@when(u'用户在手机上暂停音乐')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please pause music on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_pause()


@then(u'面板不显示音乐歌曲名和歌手名')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板显示音量减少到静音')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothSerial', 'AT#VD')
    context.florenceActRes.mock_value('BluetoothSerial', 'AT#VD')
    context.florenceActRes.get_value('BluetoothSerial')
    logging.debug("context.florenceExpRes.BluetoothSerial: " + str(context.florenceExpRes.dist['BluetoothSerial']))
    logging.debug("context.florenceActRes.BluetoothSerial: " + str(context.florenceActRes.dist['BluetoothSerial']))
    assert context.florenceActRes.dist['BluetoothSerial'] == context.florenceExpRes.dist['BluetoothSerial']

    context.florenceExpRes.set_value('Volume', 0)
    context.florenceActRes.mock_value('Volume', 0)
    context.florenceActRes.get_value('Volume')
    logging.debug("context.florenceExpRes.Volume: " + str(context.florenceExpRes.dist['Volume']))
    logging.debug("context.florenceActRes.Volume: " + str(context.florenceActRes.dist['Volume']))
    assert context.florenceActRes.dist['Volume'] == context.florenceExpRes.dist['Volume']


@then(u'面板显示音量增加到最大')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothSerial', 'AT#VU')
    context.florenceActRes.mock_value('BluetoothSerial', 'AT#VU')
    context.florenceActRes.get_value('BluetoothSerial')
    logging.debug("context.florenceExpRes.BluetoothSerial: " + str(context.florenceExpRes.dist['BluetoothSerial']))
    logging.debug("context.florenceActRes.BluetoothSerial: " + str(context.florenceActRes.dist['BluetoothSerial']))
    assert context.florenceActRes.dist['BluetoothSerial'] == context.florenceExpRes.dist['BluetoothSerial']

    context.florenceExpRes.set_value('Volume', 10)
    context.florenceActRes.mock_value('Volume', 10)
    context.florenceActRes.get_value('Volume')
    logging.debug("context.florenceExpRes.Volume: " + str(context.florenceExpRes.dist['Volume']))
    logging.debug("context.florenceActRes.Volume: " + str(context.florenceActRes.dist['Volume']))
    assert context.florenceActRes.dist['Volume'] == context.florenceExpRes.dist['Volume']


@then(u'面板显示上一首歌曲名和歌手名')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothSerial', 'AT#ME')
    context.florenceActRes.mock_value('BluetoothSerial', 'AT#ME')
    context.florenceActRes.get_value('BluetoothSerial')
    logging.debug("context.florenceExpRes.BluetoothSerial: " + str(context.florenceExpRes.dist['BluetoothSerial']))
    logging.debug("context.florenceActRes.BluetoothSerial: " + str(context.florenceActRes.dist['BluetoothSerial']))
    assert context.florenceActRes.dist['BluetoothSerial'] == context.florenceExpRes.dist['BluetoothSerial']

    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('MusicName', 'Previously Music')
    context.florenceActRes.mock_value('MusicName', 'Previously Music')
    context.florenceActRes.get_value('MusicName')
    logging.debug("context.florenceExpRes.MusicName: " + str(context.florenceExpRes.dist['MusicName']))
    logging.debug("context.florenceActRes.MusicName: " + str(context.florenceActRes.dist['MusicName']))
    assert context.florenceActRes.dist['MusicName'] == context.florenceExpRes.dist['MusicName']

    context.florenceExpRes.set_value('MusicAuthor', 'Previously Author')
    context.florenceActRes.mock_value('MusicAuthor', 'Previously Author')
    context.florenceActRes.get_value('MusicAuthor')
    logging.debug("context.florenceExpRes.MusicAuthor: " + str(context.florenceExpRes.dist['MusicAuthor']))
    logging.debug("context.florenceActRes.MusicAuthor: " + str(context.florenceActRes.dist['MusicAuthor']))
    assert context.florenceActRes.dist['MusicAuthor'] == context.florenceExpRes.dist['MusicAuthor']


@then(u'蓝牙模块播放上一首歌曲')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play previously music")


@then(u'面板显示下一首歌曲歌曲名和歌手名')
def step_impl(context):
    context.florenceExpRes.set_value('BluetoothSerial', 'AT#MD')
    context.florenceActRes.mock_value('BluetoothSerial', 'AT#MD')
    context.florenceActRes.get_value('BluetoothSerial')
    logging.debug("context.florenceExpRes.BluetoothSerial: " + str(context.florenceExpRes.dist['BluetoothSerial']))
    logging.debug("context.florenceActRes.BluetoothSerial: " + str(context.florenceActRes.dist['BluetoothSerial']))
    assert context.florenceActRes.dist['BluetoothSerial'] == context.florenceExpRes.dist['BluetoothSerial']

    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('MusicName', 'Next Music')
    context.florenceActRes.mock_value('MusicName', 'Next Music')
    context.florenceActRes.get_value('MusicName')
    logging.debug("context.florenceExpRes.MusicName: " + str(context.florenceExpRes.dist['MusicName']))
    logging.debug("context.florenceActRes.MusicName: " + str(context.florenceActRes.dist['MusicName']))
    assert context.florenceActRes.dist['MusicName'] == context.florenceExpRes.dist['MusicName']

    context.florenceExpRes.set_value('MusicAuthor', 'Next Author')
    context.florenceActRes.mock_value('MusicAuthor', 'Next Author')
    context.florenceActRes.get_value('MusicAuthor')
    logging.debug("context.florenceExpRes.MusicAuthor: " + str(context.florenceExpRes.dist['MusicAuthor']))
    logging.debug("context.florenceActRes.MusicAuthor: " + str(context.florenceActRes.dist['MusicAuthor']))
    assert context.florenceActRes.dist['MusicAuthor'] == context.florenceExpRes.dist['MusicAuthor']


@then(u'蓝牙模块播放下一首歌曲')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play next music")


@when(u'用户使用另一台手机拨打已连接蓝牙模块的手机')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please another cellphone dial cellphone connected to e-bike")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_incoming_call('13888888888')


@then(u'面板显示来电图标和来电号码')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'IncomingCall')
    context.florenceActRes.mock_value('UIStatus', 'IncomingCall')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('PhoneNumber', '13888888888')
    context.florenceActRes.mock_value('PhoneNumber', '13888888888')
    context.florenceActRes.get_value('PhoneNumber')
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@when(u'用户接听电话')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please accept incoming call")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_calling('13888888888')


@then(u'面板显示通话图标和通话号码')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Calling')
    context.florenceActRes.mock_value('UIStatus', 'Calling')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('PhoneNumber', '13888888888')
    context.florenceActRes.mock_value('PhoneNumber', '13888888888')
    context.florenceActRes.get_value('PhoneNumber')
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@when(u'用户挂断电话')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please hang up call")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_hangup_call()


@then(u'面板显示挂断图标和挂断号码')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'HangUpCall')
    context.florenceActRes.mock_value('UIStatus', 'HangUpCall')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('PhoneNumber', '13888888888')
    context.florenceActRes.mock_value('PhoneNumber', '13888888888')
    context.florenceActRes.get_value('PhoneNumber')
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@when(u'用户使用已连接蓝牙模块的手机拨打另一台手机')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please cellphone connected to e-bike dialing ")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_dialing('13888888888')


@then(u'面板显示拨打图标和拨打号码')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Dialing')
    context.florenceActRes.mock_value('UIStatus', 'Dialing')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('PhoneNumber', '13888888888')
    context.florenceActRes.mock_value('PhoneNumber', '13888888888')
    context.florenceActRes.get_value('PhoneNumber')
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@given(u'蓝牙模块音乐播放中')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Music Is The Key', 'Sarah Connor')

    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('MusicName', 'Music Is The Key')
    context.florenceActRes.mock_value('MusicName', 'Music Is The Key')
    context.florenceActRes.get_value('MusicName')
    logging.debug("context.florenceExpRes.MusicName: " + str(context.florenceExpRes.dist['MusicName']))
    logging.debug("context.florenceActRes.MusicName: " + str(context.florenceActRes.dist['MusicName']))
    assert context.florenceActRes.dist['MusicName'] == context.florenceExpRes.dist['MusicName']

    context.florenceExpRes.set_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.mock_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.get_value('MusicAuthor')
    logging.debug("context.florenceExpRes.MusicAuthor: " + str(context.florenceExpRes.dist['MusicAuthor']))
    logging.debug("context.florenceActRes.MusicAuthor: " + str(context.florenceActRes.dist['MusicAuthor']))
    assert context.florenceActRes.dist['MusicAuthor'] == context.florenceExpRes.dist['MusicAuthor']


@then(u'面板暂停音乐播放')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']


@then(u'面板恢复音乐播放')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play music")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Music Is The Key', 'Sarah Connor')


@then(u'面板返回音乐播放界面')
def step_impl(context):
    context.florenceExpRes.set_value('UIStatus', 'Home')
    context.florenceActRes.mock_value('UIStatus', 'Home')
    context.florenceActRes.get_value('UIStatus')
    logging.debug("context.florenceExpRes.UIStatus: " + str(context.florenceExpRes.dist['UIStatus']))
    logging.debug("context.florenceActRes.UIStatus: " + str(context.florenceActRes.dist['UIStatus']))
    assert context.florenceActRes.dist['UIStatus'] == context.florenceExpRes.dist['UIStatus']

    context.florenceExpRes.set_value('MusicName', 'Music Is The Key')
    context.florenceActRes.mock_value('MusicName', 'Music Is The Key')
    context.florenceActRes.get_value('MusicName')
    logging.debug("context.florenceExpRes.MusicName: " + str(context.florenceExpRes.dist['MusicName']))
    logging.debug("context.florenceActRes.MusicName: " + str(context.florenceActRes.dist['MusicName']))
    assert context.florenceActRes.dist['MusicName'] == context.florenceExpRes.dist['MusicName']

    context.florenceExpRes.set_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.mock_value('MusicAuthor', 'Sarah Connor')
    context.florenceActRes.get_value('MusicAuthor')
    logging.debug("context.florenceExpRes.MusicAuthor: " + str(context.florenceExpRes.dist['MusicAuthor']))
    logging.debug("context.florenceActRes.MusicAuthor: " + str(context.florenceActRes.dist['MusicAuthor']))
    assert context.florenceActRes.dist['MusicAuthor'] == context.florenceExpRes.dist['MusicAuthor']
