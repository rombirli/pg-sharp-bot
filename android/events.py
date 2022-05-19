from dataclasses import dataclass


@dataclass
class Event:
    keycode: int

unknown = Event(0)
soft_left = Event(1)
soft_right = Event(2)
home = Event(3)
back = Event(4)
call = Event(5)
endcall = Event(6)
key_0 = Event(7)
key_1 = Event(8)
key_2 = Event(9)
key_3 = Event(10)
key_4 = Event(11)
key_5 = Event(12)
key_6 = Event(13)
key_7 = Event(14)
key_8 = Event(15)
key_9 = Event(16)
star = Event(17)
pound = Event(18)
dpad_up = Event(19)
dpad_down = Event(20)
dpad_left = Event(21)
dpad_right = Event(22)
dpad_center = Event(23)
volume_up = Event(24)
volume_down = Event(25)
power = Event(26)
camera = Event(27)
clear = Event(28)
a = Event(29)
b = Event(30)
c = Event(31)
d = Event(32)
e = Event(33)
f = Event(34)
g = Event(35)
h = Event(36)
i = Event(37)
j = Event(38)
k = Event(39)
l = Event(40)
m = Event(41)
n = Event(42)
o = Event(43)
p = Event(44)
q = Event(45)
r = Event(46)
s = Event(47)
t = Event(48)
u = Event(49)
v = Event(50)
w = Event(51)
x = Event(52)
y = Event(53)
z = Event(54)
comma = Event(55)
period = Event(56)
alt_left = Event(57)
alt_right = Event(58)
shift_left = Event(59)
shift_right = Event(60)
tab = Event(61)
space = Event(62)
sym = Event(63)
explorer = Event(64)
envelope = Event(65)
enter = Event(66)
key_del = Event(67)
grave = Event(68)
minus = Event(69)
equals = Event(70)
left_bracket = Event(71)
right_bracket = Event(72)
backslash = Event(73)
semicolon = Event(74)
apostrophe = Event(75)
slash = Event(76)
at = Event(77)
num = Event(78)
headsethook = Event(79)
focus = Event(80)
plus = Event(81)
menu = Event(82)
notification = Event(83)
search = Event(84)
media_play_pause = Event(85)
media_stop = Event(86)
media_next = Event(87)
media_previous = Event(88)
media_rewind = Event(89)
media_fast_forward = Event(90)
mute = Event(91)
page_up = Event(92)
page_down = Event(93)
pictsymbols = Event(94)
switch_charset = Event(95)
button_a = Event(96)
button_b = Event(97)
button_c = Event(98)
button_x = Event(99)
button_y = Event(100)
button_z = Event(101)
button_l1 = Event(102)
button_r1 = Event(103)
button_l2 = Event(104)
button_r2 = Event(105)
button_thumbl = Event(106)
button_thumbr = Event(107)
button_start = Event(108)
button_select = Event(109)
button_mode = Event(110)
escape = Event(111)
forward_del = Event(112)
ctrl_left = Event(113)
ctrl_right = Event(114)
caps_lock = Event(115)
scroll_lock = Event(116)
meta_left = Event(117)
meta_right = Event(118)
function = Event(119)
sysrq = Event(120)
key_break = Event(121)
move_home = Event(122)
move_end = Event(123)
insert = Event(124)
forward = Event(125)
media_play = Event(126)
media_pause = Event(127)
media_close = Event(128)
media_eject = Event(129)
media_record = Event(130)
f1 = Event(131)
f2 = Event(132)
f3 = Event(133)
f4 = Event(134)
f5 = Event(135)
f6 = Event(136)
f7 = Event(137)
f8 = Event(138)
f9 = Event(139)
f10 = Event(140)
f11 = Event(141)
f12 = Event(142)
num_lock = Event(143)
numpad_0 = Event(144)
numpad_1 = Event(145)
numpad_2 = Event(146)
numpad_3 = Event(147)
numpad_4 = Event(148)
numpad_5 = Event(149)
numpad_6 = Event(150)
numpad_7 = Event(151)
numpad_8 = Event(152)
numpad_9 = Event(153)
numpad_divide = Event(154)
numpad_multiply = Event(155)
numpad_subtract = Event(156)
numpad_add = Event(157)
numpad_dot = Event(158)
numpad_comma = Event(159)
numpad_enter = Event(160)
numpad_equals = Event(161)
numpad_left_paren = Event(162)
numpad_right_paren = Event(163)
volume_mute = Event(164)
info = Event(165)
channel_up = Event(166)
channel_down = Event(167)
zoom_in = Event(168)
zoom_out = Event(169)
tv = Event(170)
window = Event(171)
guide = Event(172)
dvr = Event(173)
bookmark = Event(174)
captions = Event(175)
settings = Event(176)
tv_power = Event(177)
tv_input = Event(178)
stb_power = Event(179)
stb_input = Event(180)
avr_power = Event(181)
avr_input = Event(182)
prog_red = Event(183)
prog_green = Event(184)
prog_yellow = Event(185)
prog_blue = Event(186)
app_switch = Event(187)
button_1 = Event(188)
button_2 = Event(189)
button_3 = Event(190)
button_4 = Event(191)
button_5 = Event(192)
button_6 = Event(193)
button_7 = Event(194)
button_8 = Event(195)
button_9 = Event(196)
button_10 = Event(197)
button_11 = Event(198)
button_12 = Event(199)
button_13 = Event(200)
button_14 = Event(201)
button_15 = Event(202)
button_16 = Event(203)
language_switch = Event(204)
manner_mode = Event(205)
key_3d_mode = Event(206)
contacts = Event(207)
calendar = Event(208)
music = Event(209)
calculator = Event(210)
zenkaku_hankaku = Event(211)
eisu = Event(212)
muhenkan = Event(213)
henkan = Event(214)
katakana_hiragana = Event(215)
yen = Event(216)
ro = Event(217)
kana = Event(218)
assist = Event(219)
brightness_down = Event(220)
brightness_up = Event(221)
media_audio_track = Event(222)
sleep = Event(223)
wakeup = Event(224)
pairing = Event(225)
media_top_menu = Event(226)
key_11 = Event(227)
key_12 = Event(228)
last_channel = Event(229)
tv_data_service = Event(230)
voice_assist = Event(231)
tv_radio_service = Event(232)
tv_teletext = Event(233)
tv_number_entry = Event(234)
tv_terrestrial_analog = Event(235)
tv_terrestrial_digital = Event(236)
tv_satellite = Event(237)
tv_satellite_bs = Event(238)
tv_satellite_cs = Event(239)
tv_satellite_service = Event(240)
tv_network = Event(241)
tv_antenna_cable = Event(242)
tv_input_hdmi_1 = Event(243)
tv_input_hdmi_2 = Event(244)
tv_input_hdmi_3 = Event(245)
tv_input_hdmi_4 = Event(246)
tv_input_composite_1 = Event(247)
tv_input_composite_2 = Event(248)
tv_input_component_1 = Event(249)
tv_input_component_2 = Event(250)
tv_input_vga_1 = Event(251)
tv_audio_description = Event(252)
tv_audio_description_mix_up = Event(253)
tv_audio_description_mix_down = Event(254)
tv_zoom_mode = Event(255)
tv_contents_menu = Event(256)
tv_media_context_menu = Event(257)
tv_timer_programming = Event(258)
help = Event(259)
navigate_previous = Event(260)
navigate_next = Event(261)
navigate_in = Event(262)
navigate_out = Event(263)
stem_primary = Event(264)
stem_1 = Event(265)
stem_2 = Event(266)
stem_3 = Event(267)
dpad_up_left = Event(268)
dpad_down_left = Event(269)
dpad_up_right = Event(270)
dpad_down_right = Event(271)
media_skip_forward = Event(272)
media_skip_backward = Event(273)
media_step_forward = Event(274)
media_step_backward = Event(275)
soft_sleep = Event(276)
cut = Event(277)
copy = Event(278)
paste = Event(279)
system_navigation_up = Event(280)
system_navigation_down = Event(281)
system_navigation_left = Event(282)
system_navigation_right = Event(283)
all_apps = Event(284)
refresh = Event(285)

