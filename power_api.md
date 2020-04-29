<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module power_api</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>power_api</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:/home/pi/sixfab_dev/sixfab-power-python-api/power_api/power_api.py">/home/pi/sixfab_dev/sixfab-power-python-api/power_api/power_api.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="datetime.html">datetime</a><br>
</td><td width="25%" valign=top><a href="os.html">os</a><br>
</td><td width="25%" valign=top><a href="time.html">time</a><br>
</td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="power_api.html#SixfabPower">SixfabPower</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="SixfabPower">class <strong>SixfabPower</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr bgcolor="#ffc8d8"><td rowspan=2><tt>&nbsp;&nbsp;&nbsp;</tt></td>
<td colspan=2><tt>Sixfab&nbsp;Power&nbsp;Class.<br>&nbsp;</tt></td></tr>
<tr><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="SixfabPower-__del__"><strong>__del__</strong></a>(self)</dt></dl>

<dl><dt><a name="SixfabPower-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</tt></dd></dl>

<dl><dt><a name="SixfabPower-ask_watchdog_alarm"><strong>ask_watchdog_alarm</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;asking&nbsp;watchdog&nbsp;alarm&nbsp;is&nbsp;exist<br>
&nbsp;&nbsp;&nbsp;&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;EXIST,&nbsp;"2"&nbsp;for&nbsp;NOT_EXIST</tt></dd></dl>

<dl><dt><a name="SixfabPower-clear_program_storage"><strong>clear_program_storage</strong></a>(self, timeout=500)</dt><dd><tt>Function&nbsp;for&nbsp;clearing&nbsp;firmware&nbsp;storage<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SUCCESS,&nbsp;"2"&nbsp;for&nbsp;FAIL</tt></dd></dl>

<dl><dt><a name="SixfabPower-create_scheduled_event"><strong>create_scheduled_event</strong></a>(self, event_id, schedule_type, repeat, time_or_interval, interval_type, repeat_period, action, timeout=200)</dt><dd><tt>Function&nbsp;for&nbsp;creating&nbsp;scheduling&nbsp;event<br>
&nbsp;<br>
Parameters<br>
-----------<br>
event_id&nbsp;:&nbsp;int&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;to&nbsp;describe&nbsp;events&nbsp;indivudially<br>
&nbsp;<br>
schedule_type&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.NO_EVENT<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.EVENT_TIME<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.EVENT_INTERVAL<br>
&nbsp;<br>
repeat&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.EVENT_ONE_SHOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.EVENT_REPEATED<br>
&nbsp;<br>
time_or_interval&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;daily_epoch_time&nbsp;in&nbsp;seconds&nbsp;or&nbsp;interval&nbsp;(Checkout&nbsp;*Notes&nbsp;for&nbsp;daily_exact_time)<br>
&nbsp;<br>
interval_type&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.INTERVAL_TYPE_SEC<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.INTERVAL_TYPE_MIN<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.INTERVAL_TYPE_HOUR&nbsp;<br>
&nbsp;<br>
repeat_period&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;day_factor&nbsp;(Checkout&nbsp;*Notes)<br>
&nbsp;<br>
action&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;"1"&nbsp;for&nbsp;START<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;"2"&nbsp;for&nbsp;HARD&nbsp;SHUTDOWN<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;"3"&nbsp;for&nbsp;SOFT&nbsp;SHUTDOWN<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;"4"&nbsp;for&nbsp;HARD&nbsp;REBOOT<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;"5"&nbsp;for&nbsp;SOFT&nbsp;REBOOT<br>
&nbsp;<br>
&nbsp;timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Notes<br>
-----<br>
1)&nbsp;Calculation&nbsp;of&nbsp;daily_exact_time&nbsp;:<br>
daily&nbsp;exact_time&nbsp;formula:&nbsp;epoch_time_local&nbsp;%&nbsp;(24*60*60)<br>
&nbsp;<br>
daily&nbsp;exact&nbsp;time&nbsp;example:&nbsp;<br>
--&gt;&nbsp;Friday,&nbsp;March&nbsp;27,&nbsp;2020&nbsp;11:19:00&nbsp;PM&nbsp;GMT+03:00<br>
--&gt;&nbsp;epoch_local&nbsp;=&nbsp;1585340340&nbsp;(In&nbsp;this&nbsp;case&nbsp;local&nbsp;:&nbsp;GMT+3)<br>
--&gt;&nbsp;daily&nbsp;exact_time&nbsp;=&nbsp;1585340340&nbsp;%&nbsp;86400&nbsp;=&nbsp;73140<br>
&nbsp;<br>
2)&nbsp;Calculation&nbsp;of&nbsp;day_factor&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
[monday]&nbsp;-&nbsp;[tuesday]&nbsp;-&nbsp;[wednesday]&nbsp;-&nbsp;[thursday]&nbsp;-&nbsp;[friday]&nbsp;-&nbsp;[saturday]&nbsp;-&nbsp;[sunday]&nbsp;-&nbsp;[RESERVED&nbsp;as&nbsp;Zero]<br>
Bit&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bit&nbsp;7<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
Example&nbsp;Calculation&nbsp;for&nbsp;every&nbsp;day&nbsp;:&nbsp;<br>
day_factor&nbsp;=&nbsp;0b01111111&nbsp;=&nbsp;127<br>
&nbsp;<br>
Example&nbsp;Calculation&nbsp;for&nbsp;(sunday&nbsp;+&nbsp;monday&nbsp;+&nbsp;tuesday)&nbsp;:<br>
day_factor&nbsp;=&nbsp;0b01000011&nbsp;=&nbsp;67<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-create_scheduled_event_with_event"><strong>create_scheduled_event_with_event</strong></a>(self, event, timeout=200)</dt><dd><tt>Function&nbsp;for&nbsp;creating&nbsp;scheduling&nbsp;event<br>
&nbsp;<br>
Parameters<br>
-----------<br>
event&nbsp;:&nbsp;Event&nbsp;Class&nbsp;Object<br>
&nbsp;&nbsp;&nbsp;&nbsp;instance&nbsp;of&nbsp;Event&nbsp;class<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_current"><strong>get_battery_current</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;current<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
current&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;current&nbsp;[Ampere]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_design_capacity"><strong>get_battery_design_capacity</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;design&nbsp;capacity<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
capacity&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;design&nbsp;capacity&nbsp;in&nbsp;[mAh]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_health"><strong>get_battery_health</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;health<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
health&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;health&nbsp;as&nbsp;percentage&nbsp;[%]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_level"><strong>get_battery_level</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;level<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
level&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;charge&nbsp;of&nbsp;state&nbsp;as&nbsp;percentage&nbsp;[%]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_max_charge_level"><strong>get_battery_max_charge_level</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;max&nbsp;charge&nbsp;level<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
level&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;max&nbsp;charge&nbsp;level&nbsp;in&nbsp;percentage&nbsp;[%]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_power"><strong>get_battery_power</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;power<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
power&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;power&nbsp;[Watt]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_temp"><strong>get_battery_temp</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;temperature<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
temperature&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;temperature&nbsp;[Celcius]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_battery_voltage"><strong>get_battery_voltage</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;battery&nbsp;voltage<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
voltage&nbsp;:&nbsp;float&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;voltage&nbsp;[Volt]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_button1_status"><strong>get_button1_status</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;button&nbsp;1<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
status&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SHORT_PRESS,&nbsp;"2"&nbsp;for&nbsp;LONG_PRESS,&nbsp;"3"&nbsp;for&nbsp;RELEASED</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_button2_status"><strong>get_button2_status</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;button&nbsp;2<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
status&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SHORT_PRESS,&nbsp;"2"&nbsp;for&nbsp;LONG_PRESS,&nbsp;"3"&nbsp;for&nbsp;RELEASED</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_fan_automation"><strong>get_fan_automation</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;fan&nbsp;automation<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
automation&nbsp;:&nbsp;byteArray(2)&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;[slow_threshold,&nbsp;fast_threshold]&nbsp;[Celcius]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_fan_health"><strong>get_fan_health</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;fan&nbsp;health<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
health&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;HEALTHY,&nbsp;"2"&nbsp;for&nbsp;BROKEN</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_fan_speed"><strong>get_fan_speed</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;fan&nbsp;speed<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
speed&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;fan&nbsp;speed&nbsp;[RPM]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_firmware_ver"><strong>get_firmware_ver</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;firmware&nbsp;version&nbsp;on&nbsp;mcu<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
version&nbsp;:&nbsp;char[8]&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;ver&nbsp;[Ex.&nbsp;v1.00.00]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_input_current"><strong>get_input_current</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;input&nbsp;current<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
current&nbsp;:&nbsp;float&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;input&nbsp;current&nbsp;[Ampere]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_input_power"><strong>get_input_power</strong></a>(self, timeout=50)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;input&nbsp;power<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
power&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;input&nbsp;power&nbsp;[Watt]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_input_temp"><strong>get_input_temp</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;input&nbsp;temperature<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
temperature&nbsp;:&nbsp;float&nbsp;<br>
PCB&nbsp;temperature&nbsp;of&nbsp;Sixfab&nbsp;Power&nbsp;Management&nbsp;and&nbsp;UPS&nbsp;HAT&nbsp;[Celcius]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_input_voltage"><strong>get_input_voltage</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;input&nbsp;voltage<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
voltage&nbsp;:&nbsp;float&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;input&nbsp;voltage&nbsp;[Volt]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_rgb_animation"><strong>get_rgb_animation</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;RGB&nbsp;animation<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
animation&nbsp;:&nbsp;byteArray(3)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[anim_type,&nbsp;color,&nbsp;speed]<br>
&nbsp;<br>
Notes<br>
-----<br>
anim_type&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.RGB_DISABLED<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.RGB_HEARTBEAT<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.RGB_TEMP_MAP<br>
&nbsp;<br>
color&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.RED<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.GREEN<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.BLUE<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.YELLOW<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.CYAN<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.MAGENTA<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.WHITE<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.BLACK<br>
&nbsp;<br>
speed&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.SLOW<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.NORMAL<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.FAST</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_rtc_time"><strong>get_rtc_time</strong></a>(self, format=0, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;time&nbsp;of&nbsp;RTC&nbsp;in&nbsp;MCU<br>
&nbsp;<br>
Parameters<br>
-----------<br>
format&nbsp;:&nbsp;Definition&nbsp;Object&nbsp;Property<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.TIME_FORMAT_EPOCH<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.TIME_FORMAT_DATE_AND_TIME<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.TIME_FORMAT_DATE<br>
&nbsp;&nbsp;&nbsp;&nbsp;--&gt;&nbsp;Definition.TIME_FORMAT_TIME<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
timestamp&nbsp;:&nbsp;int/str<br>
&nbsp;&nbsp;&nbsp;&nbsp;time&nbsp;in&nbsp;chosen&nbsp;format</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_safe_shutdown_battery_level"><strong>get_safe_shutdown_battery_level</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;safe&nbsp;shutdown&nbsp;battery&nbsp;level<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
level&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;safe&nbsp;shutdown&nbsp;level&nbsp;in&nbsp;percentage&nbsp;[%]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_safe_shutdown_battery_status"><strong>get_safe_shutdown_battery_status</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;safe&nbsp;shutdown&nbsp;status<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
status&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;ENABLEDi&nbsp;"2"&nbsp;for&nbsp;DISABLED</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_scheduled_event_ids"><strong>get_scheduled_event_ids</strong></a>(self, timeout=50)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;scheduled&nbsp;event&nbsp;ids<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
ids&nbsp;:&nbsp;byteArray(10)<br>
&nbsp;&nbsp;&nbsp;&nbsp;active&nbsp;ids&nbsp;of&nbsp;scheduled&nbsp;events</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_system_current"><strong>get_system_current</strong></a>(self, timeout=50)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;system&nbsp;current<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
current&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;current&nbsp;that&nbsp;supplies&nbsp;raspberry&nbsp;pi&nbsp;and&nbsp;other&nbsp;peripherals&nbsp;[Ampere]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_system_power"><strong>get_system_power</strong></a>(self, timeout=50)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;system&nbsp;power<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
power&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;power&nbsp;that&nbsp;supplies&nbsp;raspberry&nbsp;pi&nbsp;and&nbsp;other&nbsp;peripherals&nbsp;[Ampere]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_system_temp"><strong>get_system_temp</strong></a>(self)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;raspberry&nbsp;pi&nbsp;core&nbsp;temperature<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
None<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
temperature&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;raspberry&nbsp;pi&nbsp;core&nbsp;temperature&nbsp;[Celcius]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_system_voltage"><strong>get_system_voltage</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;system&nbsp;voltage<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
voltage&nbsp;:&nbsp;float<br>
&nbsp;&nbsp;&nbsp;&nbsp;voltage&nbsp;source&nbsp;that&nbsp;supplies&nbsp;raspberry&nbsp;pi&nbsp;and&nbsp;other&nbsp;peripherals&nbsp;[Volt]</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_watchdog_status"><strong>get_watchdog_status</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;watchdog&nbsp;status<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
status&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;WATCHDOG&nbsp;ENABLED,&nbsp;"2"&nbsp;for&nbsp;WATCHDOG&nbsp;DISABLED</tt></dd></dl>

<dl><dt><a name="SixfabPower-get_working_mode"><strong>get_working_mode</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;working&nbsp;mode<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
working_mode&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;CHARGING,&nbsp;"2"&nbsp;for&nbsp;FULLY_CHARGED,&nbsp;"3"&nbsp;for&nbsp;BATTERY&nbsp;POWERED</tt></dd></dl>

<dl><dt><a name="SixfabPower-hard_power_off"><strong>hard_power_off</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;raspberry&nbsp;pi&nbsp;hard&nbsp;powering&nbsp;off<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-hard_reboot"><strong>hard_reboot</strong></a>(self, timeout=100)</dt><dd><tt>Function&nbsp;for&nbsp;hard&nbsp;rebooting<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-remove_all_scheduled_events"><strong>remove_all_scheduled_events</strong></a>(self, timeout=200)</dt><dd><tt>Function&nbsp;for&nbsp;removing&nbsp;all&nbsp;scheduling&nbsp;events<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-remove_scheduled_event"><strong>remove_scheduled_event</strong></a>(self, event_id, timeout=200)</dt><dd><tt>Function&nbsp;for&nbsp;removing&nbsp;scheduling&nbsp;event&nbsp;with&nbsp;event&nbsp;id<br>
&nbsp;<br>
Parameters<br>
-----------<br>
event_id&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;event&nbsp;id&nbsp;that&nbsp;is&nbsp;required&nbsp;to&nbsp;remove<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-reset_for_boot_update"><strong>reset_for_boot_update</strong></a>(self)</dt><dd><tt>Function&nbsp;for&nbsp;resetting&nbsp;MCU&nbsp;and&nbsp;go&nbsp;to&nbsp;boot&nbsp;mode<br>
&nbsp;<br>
Parameters<br>
-----------<br>
None<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
None</tt></dd></dl>

<dl><dt><a name="SixfabPower-reset_mcu"><strong>reset_mcu</strong></a>(self)</dt><dd><tt>Function&nbsp;for&nbsp;resetting&nbsp;MCU<br>
&nbsp;<br>
Parameters<br>
-----------<br>
None<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
None</tt></dd></dl>

<dl><dt><a name="SixfabPower-send_system_temp"><strong>send_system_temp</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;sending&nbsp;raspberry&nbsp;pi&nbsp;core&nbsp;temperature&nbsp;to&nbsp;mcu<br>
&nbsp;<br>
Parameters<br>
-----------&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SUCCESS,&nbsp;"2"&nbsp;for&nbsp;FAIL</tt></dd></dl>

<dl><dt><a name="SixfabPower-setFanSpeed"><strong>setFanSpeed</strong></a>(self, status, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;fan&nbsp;speed<br>
&nbsp;<br>
Parameters<br>
-----------<br>
status&nbsp;:&nbsp;"1"&nbsp;for&nbsp;START&nbsp;FAN,&nbsp;"2"&nbsp;for&nbsp;STOP&nbsp;FAN<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_battery_design_capacity"><strong>set_battery_design_capacity</strong></a>(self, capacity, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;battery&nbsp;design&nbsp;capacity<br>
&nbsp;<br>
Parameters<br>
-----------<br>
capacity&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;design&nbsp;capacity&nbsp;in&nbsp;[mAh]<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_battery_max_charge_level"><strong>set_battery_max_charge_level</strong></a>(self, level, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;battery&nbsp;max&nbsp;charge&nbsp;level<br>
&nbsp;<br>
Parameters<br>
-----------<br>
level&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;battery&nbsp;is&nbsp;charged&nbsp;up&nbsp;to&nbsp;this&nbsp;level&nbsp;in&nbsp;percentage&nbsp;[%]<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_fan_automation"><strong>set_fan_automation</strong></a>(self, slow_threshold, fast_threshold=100, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;fan&nbsp;automation<br>
&nbsp;<br>
Parameters<br>
-----------<br>
slow_threshold&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;temperature&nbsp;threshold&nbsp;to&nbsp;decide&nbsp;fan&nbsp;working&nbsp;status<br>
fast_threshold&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;temperature&nbsp;threshold&nbsp;to&nbsp;decide&nbsp;fan&nbsp;working&nbsp;status&nbsp;(default&nbsp;is&nbsp;100)<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_rgb_animation"><strong>set_rgb_animation</strong></a>(self, anim_type, color, speed, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;RGB&nbsp;animation<br>
&nbsp;<br>
Parameters<br>
-----------<br>
anim_type&nbsp;:&nbsp;[DISABLED,&nbsp;HEARTBEAT,&nbsp;TEMP_MAP]<br>
color&nbsp;:&nbsp;[GREEN,&nbsp;BLUE,&nbsp;RED,&nbsp;YELLOW,&nbsp;CYAN,&nbsp;MAGENTA,&nbsp;WHITE]<br>
speed&nbsp;:&nbsp;[SLOW,&nbsp;NORMAL,&nbsp;FAST]&nbsp;<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_rtc_time"><strong>set_rtc_time</strong></a>(self, timestamp, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;time&nbsp;of&nbsp;RTC&nbsp;in&nbsp;MCU<br>
&nbsp;<br>
Parameters<br>
-----------<br>
time&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;epoch&nbsp;time<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET_OK,&nbsp;"2"&nbsp;for&nbsp;SET_FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_safe_shutdown_battery_level"><strong>set_safe_shutdown_battery_level</strong></a>(self, level, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;safe&nbsp;shutdown&nbsp;battery&nbsp;level<br>
&nbsp;<br>
Parameters<br>
-----------<br>
level&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;raspberry&nbsp;pi&nbsp;is&nbsp;turned&nbsp;off&nbsp;if&nbsp;battery&nbsp;falls&nbsp;to&nbsp;this&nbsp;level<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_safe_shutdown_battery_status"><strong>set_safe_shutdown_battery_status</strong></a>(self, status, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;safe&nbsp;shutdown&nbsp;status<br>
&nbsp;<br>
Parameters<br>
-----------<br>
status&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;ENABLED,&nbsp;"2"&nbsp;for&nbsp;DISABLED<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-set_watchdog_status"><strong>set_watchdog_status</strong></a>(self, status, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;setting&nbsp;watchdog&nbsp;status<br>
&nbsp;<br>
Parameters<br>
-----------<br>
status&nbsp;:&nbsp;"1"&nbsp;for&nbsp;WATCHDOG&nbsp;ENABLED,&nbsp;"2"&nbsp;for&nbsp;WATCHDOG&nbsp;DISABLED<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SET&nbsp;OK,&nbsp;"2"&nbsp;for&nbsp;SET&nbsp;FAILED</tt></dd></dl>

<dl><dt><a name="SixfabPower-soft_power_off"><strong>soft_power_off</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;checking&nbsp;any&nbsp;soft&nbsp;power&nbsp;off&nbsp;request&nbsp;is&nbsp;exist.&nbsp;If&nbsp;any<br>
request&nbsp;exist,&nbsp;raspberry&nbsp;pi&nbsp;turns&nbsp;off&nbsp;by&nbsp;using&nbsp;"sudo&nbsp;shutdown"&nbsp;terminal<br>
command&nbsp;in&nbsp;5&nbsp;seconds.<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;EXIST,&nbsp;"2"&nbsp;for&nbsp;NOT_EXIST</tt></dd></dl>

<dl><dt><a name="SixfabPower-soft_reboot"><strong>soft_reboot</strong></a>(self, timeout=10)</dt><dd><tt>Function&nbsp;for&nbsp;checking&nbsp;any&nbsp;soft&nbsp;reboot&nbsp;request&nbsp;is&nbsp;exist.&nbsp;If&nbsp;any<br>
request&nbsp;exist,&nbsp;raspberry&nbsp;pi&nbsp;reboots&nbsp;by&nbsp;using&nbsp;"sudo&nbsp;reboot"&nbsp;terminal<br>
command&nbsp;in&nbsp;5&nbsp;seconds.<br>
&nbsp;<br>
Parameters<br>
-----------<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;EXIST,&nbsp;"2"&nbsp;for&nbsp;NOT_EXIST</tt></dd></dl>

<dl><dt><a name="SixfabPower-update_firmware"><strong>update_firmware</strong></a>(self, firmware_file, update_method=0, timeout=25)</dt><dd><tt>Function&nbsp;for&nbsp;updating&nbsp;mcu&nbsp;firmware.&nbsp;Do&nbsp;not&nbsp;make&nbsp;any&nbsp;other&nbsp;api&nbsp;call&nbsp;while&nbsp;update&nbsp;call&nbsp;is&nbsp;running.<br>
&nbsp;<br>
Parameters<br>
-----------<br>
firmware_file&nbsp;:&nbsp;str<br>
&nbsp;&nbsp;&nbsp;&nbsp;.bin&nbsp;file&nbsp;path<br>
update_method&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;"0"&nbsp;for&nbsp;boot_mode_update,&nbsp;"1"&nbsp;for&nbsp;firmware_mode_update&nbsp;(default&nbsp;is&nbsp;0)<br>
timeout&nbsp;:&nbsp;int&nbsp;(optional)<br>
&nbsp;&nbsp;&nbsp;&nbsp;timeout&nbsp;while&nbsp;receiving&nbsp;the&nbsp;response&nbsp;(default&nbsp;is&nbsp;RESPONSE_DELAY)<br>
&nbsp;<br>
Yields<br>
------<br>
process&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;Process&nbsp;[%]&nbsp;on&nbsp;every&nbsp;step<br>
&nbsp;<br>
Returns<br>
-------&nbsp;<br>
result&nbsp;:&nbsp;int<br>
&nbsp;&nbsp;&nbsp;&nbsp;"1"&nbsp;for&nbsp;SUCCESS,&nbsp;"2"&nbsp;for&nbsp;FAIL</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>board</strong> = 'Sixfab Raspberry Pi UPS HAT'</dl>

</td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#eeaa77">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Functions</strong></big></font></td></tr>
    
<tr><td bgcolor="#eeaa77"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl><dt><a name="-debug_print"><strong>debug_print</strong></a>(message)</dt><dd><tt>Function&nbsp;for&nbsp;printing&nbsp;debug&nbsp;message.</tt></dd></dl>
 <dl><dt><a name="-delay_ms"><strong>delay_ms</strong></a>(ms)</dt><dd><tt>Function&nbsp;for&nbsp;delay&nbsp;as&nbsp;miliseconds.</tt></dd></dl>
 <dl><dt><a name="-millis"><strong>millis</strong></a>()</dt><dd><tt>Function&nbsp;for&nbsp;getting&nbsp;time&nbsp;as&nbsp;miliseconds.</tt></dd></dl>
</td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#55aa55">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Data</strong></big></font></td></tr>
    
<tr><td bgcolor="#55aa55"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><strong>COMMAND_SIZE_FOR_DOUBLE</strong> = 13<br>
<strong>COMMAND_SIZE_FOR_FLOAT</strong> = 11<br>
<strong>COMMAND_SIZE_FOR_INT16</strong> = 9<br>
<strong>COMMAND_SIZE_FOR_INT32</strong> = 11<br>
<strong>COMMAND_SIZE_FOR_INT64</strong> = 15<br>
<strong>COMMAND_SIZE_FOR_UINT8</strong> = 8<br>
<strong>COMMAND_TYPE_REQUEST</strong> = 1<br>
<strong>COMMAND_TYPE_RESPONSE</strong> = 2<br>
<strong>DEVICE_ADDRESS</strong> = 65<br>
<strong>PROTOCOL_FRAME_SIZE</strong> = 7<br>
<strong>PROTOCOL_HEADER_SIZE</strong> = 5<br>
<strong>RESPONSE_DELAY</strong> = 10<br>
<strong>START_BYTE_RECIEVED</strong> = 220<br>
<strong>START_BYTE_SENT</strong> = 205<br>
<strong>buffer_receive</strong> = []<br>
<strong>buffer_recieve_index</strong> = 0<br>
<strong>buffer_send</strong> = []<br>
<strong>command</strong> = &lt;power_api.command.Command object&gt;</td></tr></table>
</body></html>