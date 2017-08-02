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


@when(u'用户不输入配对码')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please do not enter pin code")


@given(u'蓝牙模块已有配对设备')
def step_impl(context):
    context.execute_steps(u'''
        假如    蓝牙模块未配对
        假如    蓝牙模块的配对码为4444
        假如    蓝牙模块可以连接手机蓝牙

        当      用户使用蓝牙设备连接电动车蓝牙模块
        而且    用户输入PIN码4444
        那么    蓝牙模块已连接
        ''')


@when(u'用户启动蓝牙模块')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure startup bluetooth success")


@then(u'蓝牙模块未连接')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_disconnected()
    key = 'BluetoothCMD'
    value = 'IA'
    context.florenceExpRes.set_value(key, value)
    context.florenceActRes.mock_value(key, value)
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value(key, 'MG1')
    context.florenceActRes.mock_value(key, 'MG1')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]


@then(u'蓝牙模块正在连接')
def step_impl(context):
    context.florenceTestInput.sysIntEvt.mock_bluetooth_connecting()


@when(u'用户等待{duration}秒后')
def step_impl(context, duration):
    sleep(float(duration))


@given(u'蓝牙模块可以连接蓝牙设备')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure cellphone bluetooth available")


@given(u'蓝牙模块不可以连接蓝牙设备')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please close cellphone bluetooth")


@given(u'蓝牙模块已经连接手机蓝牙')
def step_impl(context):
    context.execute_steps(u'''
       假如    蓝牙模块未配对
        假如    蓝牙模块的配对码为4444
        假如    蓝牙模块可以连接手机蓝牙

        当      用户使用蓝牙设备连接电动车蓝牙模块
        而且    用户输入PIN码4444
        那么    蓝牙模块已连接
        ''')


@when(u'用户在手机上播放音乐({author_name} - {song_name})')
def step_impl(context, song_name, author_name):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please play music({"+author_name+"} - {"+song_name+"}) on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Shape of You', 'Ed Sheeran')


@then(u'蓝牙模块收到音乐{song_name}和歌手名{author_name}')
def step_impl(context, song_name, author_name):
    key = 'MusicPlaying'
    context.florenceExpRes.set_value(key, 'MB')
    context.florenceActRes.mock_value(key, 'MB')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value('SongName', song_name)
    context.florenceActRes.mock_value('SongName', song_name)
    context.florenceActRes.get_value_from_mi('SongName', 'AuthorName', song_name, author_name)
    logging.debug("context.florenceExpRes." + 'SongName' + ": " + str(context.florenceExpRes.dist['SongName']))
    logging.debug("context.florenceActRes." + 'SongName' + ": " + str(context.florenceActRes.dist['SongName']))
    assert context.florenceActRes.dist['SongName'] == context.florenceExpRes.dist['SongName']

    context.florenceExpRes.set_value('AuthorName', author_name)
    context.florenceActRes.mock_value('AuthorName', author_name)
    logging.debug("context.florenceExpRes." + 'AuthorName' + ": " + str(context.florenceExpRes.dist['AuthorName']))
    logging.debug("context.florenceActRes." + 'AuthorName' + ": " + str(context.florenceActRes.dist['AuthorName']))
    assert context.florenceActRes.dist['AuthorName'] == context.florenceExpRes.dist['AuthorName']


@when(u'用户在手机上暂停音乐')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please pause music on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_pause()


@then(u'蓝牙模块收到暂停音乐播放MA指令')
def step_impl(context):
    key = 'MusicPause'
    context.florenceExpRes.set_value(key, 'MA')
    context.florenceActRes.mock_value(key, 'MA')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]


@when(u'用户减少蓝牙模块音量')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure decrease music volume")
    context.florenceTestInput.sysIntEvt.send("AT#VD")  # decrease music volume
    context.florenceTestInput.sysIntEvt.send("AT#VD")  # decrease music volume
    context.florenceTestInput.sysIntEvt.send("AT#VD")  # decrease music volume
    context.florenceTestInput.sysIntEvt.send("AT#VD")  # decrease music volume


@then(u'蓝牙音乐音量减少')
def step_impl(context):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if music volume decrease>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"


@when(u'用户增加蓝牙模块音量')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure increase music volume")
    context.florenceTestInput.sysIntEvt.send("AT#VU")  # increase music volume
    context.florenceTestInput.sysIntEvt.send("AT#VU")  # increase music volume
    context.florenceTestInput.sysIntEvt.send("AT#VU")  # increase music volume
    context.florenceTestInput.sysIntEvt.send("AT#VU")  # increase music volume


@then(u'蓝牙音乐音量增加')
def step_impl(context):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if music volume increase>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"


@when(u'用户减少蓝牙模块音量到{volume}')
def step_impl(context, volume):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure decrease music volume")
    context.florenceTestInput.sysIntEvt.send("AT#MK" + volume)  # decrease music volume 0


@when(u'用户增加蓝牙模块音量到{volume}')
def step_impl(context, volume):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please make sure increase music volume")
    context.florenceTestInput.sysIntEvt.send("AT#MK" + volume)  # increase music volume 30


@then(u'蓝牙音乐音量减少到{volume}')
def step_impl(context, volume):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if music volume decrease>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"

    context.florenceExpRes.set_value('Volume', 'MK' + volume)
    context.florenceActRes.mock_value('Volume', 'MK ' + volume)
    context.florenceActRes.get_value_from_multi_line('Volume', context.florenceExpRes.get_value('Volume'))
    logging.debug("context.florenceExpRes.Volume: " + str(context.florenceExpRes.dist['Volume']))
    logging.debug("context.florenceActRes.Volume: " + str(context.florenceActRes.dist['Volume']))
    assert context.florenceActRes.dist['Volume'] == context.florenceExpRes.dist['Volume']


@then(u'蓝牙音乐音量增加到{volume}')
def step_impl(context, volume):
    input_string = context.florenceTestInput.sysHIEvt.mock_prompt("Please enter OK if music volume increase>>")
    logging.debug("input_string: " + input_string)
    assert input_string == "OK"

    context.florenceExpRes.set_value('Volume', 'MK' + volume)
    context.florenceActRes.mock_value('Volume', 'MK' + volume)
    context.florenceActRes.get_value_from_multi_line('Volume', context.florenceExpRes.get_value('Volume'))
    logging.debug("context.florenceExpRes.Volume: " + str(context.florenceExpRes.dist['Volume']))
    logging.debug("context.florenceActRes.Volume: " + str(context.florenceActRes.dist['Volume']))
    assert context.florenceActRes.dist['Volume'] == context.florenceExpRes.dist['Volume']


@when(u'用户在手机上切换音乐到上一首歌({author_name} - {song_name})')
def step_impl(context, author_name, song_name):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please play previously music("+author_name+" - "+song_name+") on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Galway Girl', 'Ed Sheeran')


@then(u'蓝牙模块收到上一首歌曲名{song_name}和歌手名{author_name}')
def step_impl(context, song_name, author_name):
    context.florenceExpRes.set_value('SongName', song_name)
    context.florenceActRes.mock_value('SongName', song_name)
    context.florenceActRes.get_value_from_mi('SongName', 'AuthorName', song_name, author_name)
    logging.debug("context.florenceExpRes." + 'SongName' + ": " + str(context.florenceExpRes.dist['SongName']))
    logging.debug("context.florenceActRes." + 'SongName' + ": " + str(context.florenceActRes.dist['SongName']))
    assert context.florenceActRes.dist['SongName'] == context.florenceExpRes.dist['SongName']

    context.florenceExpRes.set_value('AuthorName', author_name)
    context.florenceActRes.mock_value('AuthorName', author_name)
    logging.debug("context.florenceExpRes." + 'AuthorName' + ": " + str(context.florenceExpRes.dist['AuthorName']))
    logging.debug("context.florenceActRes." + 'AuthorName' + ": " + str(context.florenceActRes.dist['AuthorName']))
    assert context.florenceActRes.dist['AuthorName'] == context.florenceExpRes.dist['AuthorName']


@when(u'用户在手机上切换音乐到下一首歌({author_name} - {song_name})')
def step_impl(context, author_name, song_name):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please play next music("+author_name+" - "+song_name+") on cellphone bluetooth")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Galway Girl', 'Ed Sheeran')


@then(u'蓝牙模块收到下一首歌曲名{song_name}和歌手名{author_name}')
def step_impl(context, song_name, author_name):
    context.florenceExpRes.set_value('SongName', song_name)
    context.florenceActRes.mock_value('SongName', song_name)
    context.florenceActRes.get_value_from_mi('SongName', 'AuthorName', song_name, author_name)
    logging.debug("context.florenceExpRes." + 'SongName' + ": " + str(context.florenceExpRes.dist['SongName']))
    logging.debug("context.florenceActRes." + 'SongName' + ": " + str(context.florenceActRes.dist['SongName']))
    assert context.florenceActRes.dist['SongName'] == context.florenceExpRes.dist['SongName']

    context.florenceExpRes.set_value('AuthorName', author_name)
    context.florenceActRes.mock_value('AuthorName', author_name)
    logging.debug("context.florenceExpRes." + 'AuthorName' + ": " + str(context.florenceExpRes.dist['AuthorName']))
    logging.debug("context.florenceActRes." + 'AuthorName' + ": " + str(context.florenceActRes.dist['AuthorName']))
    assert context.florenceActRes.dist['AuthorName'] == context.florenceExpRes.dist['AuthorName']


@then(u'蓝牙模块播放上一首歌曲')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play previously music")


@then(u'蓝牙模块播放下一首歌曲')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play next music")


@when(u'用户使用另一台手机拨打已连接蓝牙模块的手机')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please another cellphone dial cellphone connected to e-bike")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_incoming_call('13888888888')


@then(u'蓝牙模块收到来电指令和来电号码{phone_number}')
def step_impl(context, phone_number):
    key = 'IncomingCall'
    context.florenceExpRes.set_value(key, 'MG5')
    context.florenceActRes.mock_value(key, 'MG5')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value('PhoneNumber', 'ID' + phone_number)
    context.florenceActRes.mock_value('PhoneNumber', 'ID' + phone_number)
    context.florenceActRes.get_value_from_multi_line('PhoneNumber', context.florenceExpRes.get_value('PhoneNumber'))
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@then(u'蓝牙模块收到通话中的指令和通话号码{phone_number}')
def step_impl(context, phone_number):
    key = 'Calling'
    context.florenceExpRes.set_value(key, 'MG6')
    context.florenceActRes.mock_value(key, 'MG6')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value('PhoneNumber', 'IR' + phone_number)
    context.florenceActRes.mock_value('PhoneNumber', 'IR' + phone_number)
    context.florenceActRes.get_value_from_multi_line('PhoneNumber', context.florenceExpRes.get_value('PhoneNumber'))
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@then(u'蓝牙模块收到挂断指令和挂断号码')
def step_impl(context):
    key = 'HangUpCall'
    context.florenceExpRes.set_value(key, 'MG3')
    context.florenceActRes.mock_value(key, 'MG3')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value('PhoneNumber', 'IF')
    context.florenceActRes.mock_value('PhoneNumber', 'IF')
    context.florenceActRes.get_value_from_multi_line('PhoneNumber', context.florenceExpRes.get_value('PhoneNumber'))
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@when(u'用户接听电话')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please accept incoming call")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_calling('13888888888')


@when(u'用户挂断电话')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please hang up call")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_hangup_call()


@when(u'用户使用已连接蓝牙模块的手机拨打另一台手机')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please cellphone connected to e-bike dialing ")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_dialing('13888888888')


@then(u'蓝牙模块收到拨打指令和拨打号码{phone_number}')
def step_impl(context, phone_number):
    key = 'Calling'
    context.florenceExpRes.set_value(key, 'MG4')
    context.florenceActRes.mock_value(key, 'MG4')
    context.florenceActRes.get_value_from_multi_line(key, context.florenceExpRes.get_value(key))
    logging.debug("context.florenceExpRes." + key + ": " + str(context.florenceExpRes.dist[key]))
    logging.debug("context.florenceActRes." + key + ": " + str(context.florenceActRes.dist[key]))
    assert context.florenceActRes.dist[key] == context.florenceExpRes.dist[key]

    context.florenceExpRes.set_value('PhoneNumber', 'IC' + phone_number)
    context.florenceActRes.mock_value('PhoneNumber', 'IC' + phone_number)
    context.florenceActRes.get_value_from_multi_line('PhoneNumber', context.florenceExpRes.get_value('PhoneNumber'))
    logging.debug("context.florenceExpRes.PhoneNumber: " + str(context.florenceExpRes.dist['PhoneNumber']))
    logging.debug("context.florenceActRes.PhoneNumber: " + str(context.florenceActRes.dist['PhoneNumber']))
    assert context.florenceActRes.dist['PhoneNumber'] == context.florenceExpRes.dist['PhoneNumber']


@given(u'蓝牙模块音乐(Ed Sheeran - Shape of You)播放中')
def step_impl(context):
    context.execute_steps(u'''
        当      用户在手机上播放音乐(Ed Sheeran - Shape Of You)
        那么    蓝牙模块收到音乐Shape of You和歌手名Ed Sheeran
        ''')


@then(u'蓝牙模块恢复音乐播放')
def step_impl(context):
    context.florenceTestInput.sysHIEvt.mock_prompt("Please press enter if play music")
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_playing()
    context.florenceTestInput.sysIntEvt.mock_bluetooth_music_information('Music Is The Key', 'Sarah Connor')

