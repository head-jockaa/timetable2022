# coding:utf-8
from datetime import datetime, timedelta
import util

cellHeight = 3
yesterday = ""
tomorrow = ""

def checkContent(html, year, month, day, area):
	global yesterday, tomorrow, cellHeight
	if not str((int)(month)) + "月 " + str((int)(day)) + "日" in html:
		print(year + "_" + month + "_" + day + "_" + area + ".htmlの内容が間違っています")

	splited1 = html.split("cellHeight=")
	if len(splited1) > 1:
		splited2 = splited1[1].split("&")
		cellHeight = (int)(splited2[0])
	else:
		cellHeight = 3

	today = year + month + day
	yesterday = (datetime.strptime(today,"%Y%m%d") - timedelta(1)).strftime("%Y%m%d")
	tomorrow = (datetime.strptime(today,"%Y%m%d") + timedelta(days=1)).strftime("%Y%m%d")

def splitByStation(html):
	splited = html.split("class=\"cell-station cell-top\"")
	splited.pop(0)
	return splited

# splitByStationで切り分けたhtmlを与える
def extractStationName(html):
	splited1 = html.split("title=\"")
	splited2 = splited1[1].split("\"")
	return splited2[0]

# splitByStationで切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("<div class=\"cell-schedule")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html):
	splited1 = html.split("system-cell-schedule-head-")
	if len(splited1) == 1:
		return "", False

	splited2 = splited1[1].split("\"")
	start_minute = splited2[0][-2:]
	start_hour = splited2[0][-4:-2]
	date_string = splited2[0][-12:-4]

	if date_string == tomorrow:
		start_hour = str((int)(start_hour)+24)

	return start_hour+start_minute, date_string == yesterday

# splitByItemで切り分けたhtmlを与える
def extractCategoryCode(html):
	splited1 = html.split("cell-genre-")
	return splited1[1][:6]

# splitByItemで切り分けたhtmlを与える
def extractTitleWithIcons(html):
	splited1 = html.split("<span class=\"schedule-title\">")
	if len(splited1) == 1:
		splited1 = html.split("<span class=\"schedule-titleC\">")
	if len(splited1) == 1:
		return ""
	splited2 = splited1[1].split("</span>")
	return util.sanitize(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractDescriptionsWithIcons(html):
	splited1 = html.split("<span class=\"schedule-summary\">")
	if len(splited1) == 1:
		splited1 = html.split("<span class=\"schedule-summaryC\">")
	splited2 = splited1[1].split("</span>")
	return util.sanitize(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractInterval(html):
	splited1 = html.split("height: ")
	splited2 = splited1[1].split("px;")
	px = (int)(splited2[0])
	return (int)((px+3) / cellHeight)

# extractTitleWithIconsまたはextractDescriptionsWithIconsの返した文字列を与える
def extractIconsFromTitle(title_string):
	types = []
	if "🈟" in title_string:
		types.append(util.append_type_name("新"))
		title_string = title_string.replace("🈟","")
	if "[新]" in title_string:
		types.append(util.append_type_name("新"))
		title_string = title_string.replace("[新]","")
	if "［新］" in title_string:
		types.append(util.append_type_name("新"))
		title_string = title_string.replace("［新］","")
	if "🈞" in title_string:
		types.append(util.append_type_name("再"))
		title_string = title_string.replace("🈞","")
	if "[再]" in title_string:
		types.append(util.append_type_name("再"))
		title_string = title_string.replace("[再]","")
	if "(再)" in title_string:
		types.append(util.append_type_name("再"))
		title_string = title_string.replace("(再)","")
	if "【再】" in title_string:
		types.append(util.append_type_name("再"))
		title_string = title_string.replace("【再】","")
	if "🈡" in title_string:
		types.append(util.append_type_name("終"))
		title_string = title_string.replace("🈡","")
	if "[終]" in title_string:
		types.append(util.append_type_name("終"))
		title_string = title_string.replace("[終]","")
	if "［終］" in title_string:
		types.append(util.append_type_name("終"))
		title_string = title_string.replace("［終］","")
	if "🈐" in title_string:
		types.append(util.append_type_name("手"))
		title_string = title_string.replace("🈐","")
	if "[手]" in title_string:
		types.append(util.append_type_name("手"))
		title_string = title_string.replace("[手]","")
	if "🈑" in title_string:
		types.append(util.append_type_name("字"))
		title_string = title_string.replace("🈑","")
	if "[字]" in title_string:
		types.append(util.append_type_name("字"))
		title_string = title_string.replace("[字]","")
	if "🈒" in title_string:
		types.append(util.append_type_name("双"))
		title_string = title_string.replace("🈒","")
	if "[双]" in title_string:
		types.append(util.append_type_name("双"))
		title_string = title_string.replace("[双]","")
	if "🈓" in title_string:
		types.append(util.append_type_name("デ"))
		title_string = title_string.replace("🈓","")
	if "[デ]" in title_string:
		types.append(util.append_type_name("デ"))
		title_string = title_string.replace("[デ]","")
	if "🅂" in title_string:
		types.append(util.append_type_name("S"))
		title_string = title_string.replace("🅂","")
	if "[S]" in title_string:
		types.append(util.append_type_name("S"))
		title_string = title_string.replace("[S]","")
	if "🈔" in title_string:
		types.append(util.append_type_name("二"))
		title_string = title_string.replace("🈔","")
	if "[二]" in title_string:
		types.append(util.append_type_name("二"))
		title_string = title_string.replace("[二]","")
	if "🈕" in title_string:
		types.append(util.append_type_name("多"))
		title_string = title_string.replace("🈕","")
	if "[多]" in title_string:
		types.append(util.append_type_name("多"))
		title_string = title_string.replace("[多]","")
	if "🈖" in title_string:
		types.append(util.append_type_name("解"))
		title_string = title_string.replace("🈖","")
	if "[解]" in title_string:
		types.append(util.append_type_name("解"))
		title_string = title_string.replace("[解]","")
	if "🅍" in title_string:
		types.append(util.append_type_name("SS"))
		title_string = title_string.replace("🅍","")
	if "[SS]" in title_string:
		types.append(util.append_type_name("SS"))
		title_string = title_string.replace("[SS]","")
	if "🄱" in title_string:
		types.append(util.append_type_name("B"))
		title_string = title_string.replace("🄱","")
	if "[B]" in title_string:
		types.append(util.append_type_name("B"))
		title_string = title_string.replace("[B]","")
	if "🄽" in title_string:
		types.append(util.append_type_name("N"))
		title_string = title_string.replace("🄽","")
	if "[N]" in title_string:
		types.append(util.append_type_name("N"))
		title_string = title_string.replace("[N]","")
	if "🈗" in title_string:
		types.append(util.append_type_name("天"))
		title_string = title_string.replace("🈗","")
	if "[天]" in title_string:
		types.append(util.append_type_name("天"))
		title_string = title_string.replace("[天]","")
	if "🈘" in title_string:
		types.append(util.append_type_name("交"))
		title_string = title_string.replace("🈘","")
	if "[交]" in title_string:
		types.append(util.append_type_name("交"))
		title_string = title_string.replace("[交]","")
	if "🈙" in title_string:
		types.append(util.append_type_name("映"))
		title_string = title_string.replace("🈙","")
	if "[映]" in title_string:
		types.append(util.append_type_name("映"))
		title_string = title_string.replace("[映]","")
	if "🈛" in title_string:
		types.append(util.append_type_name("料"))
		title_string = title_string.replace("🈛","")
	if "[料]" in title_string:
		types.append(util.append_type_name("料"))
		title_string = title_string.replace("[料]","")
	if "🈜" in title_string:
		types.append(util.append_type_name("前"))
		title_string = title_string.replace("🈜","")
	if "[前]" in title_string:
		types.append(util.append_type_name("前"))
		title_string = title_string.replace("[前]","")
	if "🈝" in title_string:
		types.append(util.append_type_name("後"))
		title_string = title_string.replace("🈝","")
	if "[後]" in title_string:
		types.append(util.append_type_name("後"))
		title_string = title_string.replace("[後]","")
	if "🈠" in title_string:
		types.append(util.append_type_name("初"))
		title_string = title_string.replace("🈠","")
	if "[初]" in title_string:
		types.append(util.append_type_name("初"))
		title_string = title_string.replace("[初]","")
	if "🈢" in title_string:
		types.append(util.append_type_name("生"))
		title_string = title_string.replace("🈢","")
	if "[生]" in title_string:
		types.append(util.append_type_name("生"))
		title_string = title_string.replace("[生]","")
	if "［生］" in title_string:
		types.append(util.append_type_name("生"))
		title_string = title_string.replace("［生］","")
	if "🅊" in title_string:
		types.append(util.append_type_name("HV"))
		title_string = title_string.replace("🅊","")
	if "[HV]" in title_string:
		types.append(util.append_type_name("HV"))
		title_string = title_string.replace("[HV]","")
	if "🅎" in title_string:
		types.append(util.append_type_name("PV"))
		title_string = title_string.replace("🅎","")
	if "[PV]" in title_string:
		types.append(util.append_type_name("PV"))
		title_string = title_string.replace("[PV]","")
	if "【PPS】" in title_string:
		types.append(util.append_type_name("PS"))
		title_string = title_string.replace("【PPS】","")
	if "【契】" in title_string:
		types.append(util.append_type_name("契"))
		title_string = title_string.replace("【契】","")
	if "(字幕版)" in title_string:
		types.append(util.append_type_name("幕"))
		title_string = title_string.replace("(字幕版)","")
	if "(字幕)" in title_string:
		types.append(util.append_type_name("幕"))
		title_string = title_string.replace("(字幕)","")
	if "🈥" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("🈥","")
	if "[吹]" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("[吹]","")
	if "[吹替版]" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("[吹替版]","")
	if "(吹替版)" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("(吹替版)","")
	if "【吹替】" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("【吹替】","")
	if "(吹)" in title_string:
		types.append(util.append_type_name("吹"))
		title_string = title_string.replace("(吹)","")
	if "[PG12]" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("[PG12]","")
	if "[PG-12]" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("[PG-12]","")
	if "＜PG-12＞" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("＜PG-12＞","")
	if "[PG12指定]" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("[PG12指定]","")
	if "[PG-12指定]" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("[PG-12指定]","")
	if "[PG12相当]" in title_string:
		types.append(util.append_type_name("PG12"))
		title_string = title_string.replace("[PG12相当]","")
	if "[R15]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R15]","")
	if "[R-15]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R-15]","")
	if "[R15+]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R15+]","")
	if "＜R-15＞" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("＜R-15＞","")
	if "[R-15指定]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R-15指定]","")
	if "[R15+指定]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R15+指定]","")
	if "[R15相当]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R15相当]","")
	if "[R15+指定相当]" in title_string:
		types.append(util.append_type_name("R15"))
		title_string = title_string.replace("[R15+指定相当]","")
	if "🈚" in title_string:
		types.append(util.append_type_name("無"))
		title_string = title_string.replace("🈚","")
	if "[無]" in title_string:
		types.append(util.append_type_name("無"))
		title_string = title_string.replace("[無]","")
	if "[無料]" in title_string:
		types.append(util.append_type_name("無"))
		title_string = title_string.replace("[無料]","")
	if "(無料)" in title_string:
		types.append(util.append_type_name("無"))
		title_string = title_string.replace("(無料)","")
	if "【無料】" in title_string:
		types.append(util.append_type_name("無"))
		title_string = title_string.replace("【無料】","")
	if "🆞" in title_string:
		types.append(util.append_type_name("4K"))
		title_string = title_string.replace("🆞","")
	if "[4K]" in title_string:
		types.append(util.append_type_name("4K"))
		title_string = title_string.replace("[4K]","")
	if "🆟" in title_string:
		types.append(util.append_type_name("8K"))
		title_string = title_string.replace("🆟","")
	if "[8K]" in title_string:
		types.append(util.append_type_name("8K"))
		title_string = title_string.replace("[8K]","")
	if "🆢" in title_string:
		types.append(util.append_type_name("22.2ch"))
		title_string = title_string.replace("🆢","")
	if "[22.2]" in title_string:
		types.append(util.append_type_name("22.2ch"))
		title_string = title_string.replace("[22.2]","")
	if "🆠" in title_string:
		types.append(util.append_type_name("5.1ch"))
		title_string = title_string.replace("🆠","")
	if "[5.1]" in title_string:
		types.append(util.append_type_name("5.1ch"))
		title_string = title_string.replace("[5.1]","")
	if "🆧" in title_string:
		types.append(util.append_type_name("HDR"))
		title_string = title_string.replace("🆧","")
	if "[HDR]" in title_string:
		types.append(util.append_type_name("HDR"))
		title_string = title_string.replace("[HDR]","")

	return types, title_string.replace("  "," ").strip()
