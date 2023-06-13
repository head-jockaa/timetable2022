# coding:utf-8
import os
import re
import math
import radiolist

htmldata = None
splitter_data = {}

year = "2023"
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

nhk_areas = ["130","010","011","012","013","014","015","016","020","030","040","050","060","070","080","090","100","110","120","140","150","160","170","180","190","200","210","220","230","240","250","260","270","280","290","300","310","320","330","340","350","360","370","380","390","400","401","410","420","430","440","450","460","470"]

stations = ["FMT","HBC","STV","AIRG","NORTHWAVE","RAB","AFB","IBC","FMI","TBC","DATEFM","ABS","AFM","YBC","RFM","RFC","FMF","TBS","QRR","LFR","INT","FMJ","JORF","BAYFM78","NACK5","YFM","IBS","CRT","RADIOBERRY","FMGUNMA","BSN","FMNIIGATA","KNB","FMTOYAMA","MRO","HELLOFIVE","FBC","FMFUKUI","YBS","FMFUJI","SBC","FMN","CBC","TOKAIRADIO","GBS","ZIPFM","FMAICHI","FMGIFU","SBS","KMIX","FMMIE","ABC","MBS","OBC","CCL","802","FMO","KISSFMKOBE","CRK","ERADIO","KBS","ALPHASTATION","WBS","BSS","FMSANIN","RSK","FMOKAYAMA","RCC","HFM","KRY","FMY","JRT","FM807","RNC","FMKAGAWA","RNB","JOEUFM","RKC","HISIX","RKB","KBC","LOVEFM","CROSSFM","FMFUKUOKA","FMS","NBC","FMNAGASAKI","RKK","FMK","OBS","FMOITA","MRT","JOYFM","MBC","MYUFM","RBC","ROK","FMOKINAWA","RN1","RN2","HOUSOUDAIGAKU"]

radiko_url_list = ["FMT","HBC","STV","AIR-G","NORTHWAVE","RAB","AFB","IBC","FMI","TBC","DATEFM","ABS","AFM","YBC","RFM","RFC","FMF","TBS","QRR","LFR","INT","FMJ","JORF","BAYFM78","NACK5","YFM","IBS","CRT","RADIOBERRY","FMGUNMA","BSN","FMNIIGATA","KNB","FMTOYAMA","MRO","HELLOFIVE","FBC","FMFUKUI","YBS","FM-FUJI","SBC","FMN","CBC","TOKAIRADIO","GBS","ZIP-FM","FMAICHI","FMGIFU","SBS","K-MIX","FMMIE","ABC","MBS","OBC","CCL","802","FMO","KISSFMKOBE","CRK","E-RADIO","KBS","ALPHA-STATION","WBS","BSS","FM-SANIN","RSK","FM-OKAYAMA","RCC","HFM","KRY","FMY","JRT","FM807","RNC","FMKAGAWA","RNB","JOEU-FM","RKC","HI-SIX","RKB","KBC","LOVEFM","CROSSFM","FMFUKUOKA","FMS","NBC","FMNAGASAKI","RKK","FMK","OBS","FM_OITA","MRT","JOYFM","MBC","MYUFM","RBC","ROK","FM_OKINAWA","RN1","RN2","HOUSOU-DAIGAKU"]

abc_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
trans_table = str.maketrans({
"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9",
"Ａ":"A","Ｂ":"B","Ｃ":"C","Ｄ":"D","Ｅ":"E","Ｆ":"F","Ｇ":"G","Ｈ":"H","Ｉ":"I","Ｊ":"J","Ｋ":"K","Ｌ":"L","Ｍ":"M","Ｎ":"N","Ｏ":"O","Ｐ":"P","Ｑ":"Q","Ｒ":"R","Ｓ":"S","Ｔ":"T","Ｕ":"U","Ｖ":"V","Ｗ":"W","Ｘ":"X","Ｙ":"Y","Ｚ":"Z",
"ａ":"a","ｂ":"b","ｃ":"c","ｄ":"d","ｅ":"e","ｆ":"f","ｇ":"g","ｈ":"h","ｉ":"i","ｊ":"j","ｋ":"k","ｌ":"l","ｍ":"m","ｎ":"n","ｏ":"o","ｐ":"p","ｑ":"q","ｒ":"r","ｓ":"s","ｔ":"t","ｕ":"u","ｖ":"v","ｗ":"w","ｘ":"x","ｙ":"y","ｚ":"z",
"！":"!","？":"?","＆":"&","＃":"#","＋":"+","，":",","：":":","（":"(","）":")","／":"/","％":"%","♯":"#","．":".","～":"〜"
})

nhk1_standards_desc = set({})
nhkfm_standards_desc = set({})
tokyofm_standards_desc = set({})
nhk1_standards = set({})
nhkfm_standards = set({})
tokyofm_standards = set({})

def reset_temporary_data():
	global nhk1_standards_desc, nhkfm_standards_desc, tokyofm_standards_desc, nhk1_standards, nhkfm_standards, tokyofm_standards
	nhk1_standards_desc = set([])
	nhkfm_standards_desc = set([])
	tokyofm_standards_desc = set([])
	nhk1_standards = set([])
	nhkfm_standards = set([])
	tokyofm_standards = set([])

def sanitize(s):
	sanitized = s.replace("<wbr/>","").replace("<br>","\\n").replace("\"","\\\"").replace("　"," ").replace("\n","\\n").replace("\u3000", " ").replace("&amp;amp;","&").replace("&amp;","&").replace("&quot;","”").replace("&lt;","＜").replace("&gt;","＞").replace("&#39;","’").replace("‼","!!").replace("⁉","!?").replace("🈀","ほか").strip().translate(trans_table)
	return " ".join(sanitized.split())

def to_base50(n,fix):
	# fix=Trueの時は2桁固定
	if n < 50:
		if fix:
			return "A" + abc_list[n]
		else:
			return abc_list[n]
	elif n < 2500:
		return abc_list[math.floor(n/50)] + abc_list[n%50]
	else:
		#print("OVERFLOW")
		return ""

def get_target_html(year,month,day,area):
	global htmldata

	if area in stations:
		url = radiko_url_list[stations.index(area)]
	else:
		url = area

	path = "./radio"+year+"/"+month+"/"+day+"/"+year+"_"+month+"_"+day+"_"+url+".html"
	if os.path.exists(path):
		f = open(path, 'r')
		htmldata = f.read()
		f.close()
		return area

	return 0

def time_base60(time):
	hour = base60[(int)(time[:2])]
	minute = base60[(int)(time[2:])]
	return hour + minute

def time_decode_base60(string):
	hour = base60.index(string[0])
	minute = base60.index(string[1])
	if hour < 10:
		hour_string = "0" + str(hour)
	else:
		hour_string = str(hour)
	if minute < 10:
		minute_string = "0" + str(minute)
	else:
		minute_string = str(minute)
	return hour_string + minute_string

def get_my_standard_programs(station_tag):
	my_standards = set({})
	if station_tag in radiolist.NHK1_NET:
		my_standards = sorted(nhk1_standards)
	elif station_tag in radiolist.NHKFM_NET:
		my_standards = sorted(nhkfm_standards)
	elif station_tag in radiolist.FM_NET:
		my_standards = sorted(tokyofm_standards)
	return my_standards

def create_program_chunk(start_date, types, name_id, chapter_id, splited_by_space, desc_id = None):
	chunk = time_base60(start_date)
	chunk += types
	chunk += str(name_id)
	if chapter_id != None:
		chunk += to_base50(chapter_id,False)
	if desc_id != None:
		if chapter_id == None:
			chunk += "_"
		chunk += str(desc_id)
	if splited_by_space == True:
		chunk += ","
	else:
		chunk += "."

	return chunk

def create_diff(st, start_date, types, name_id, chapter_id, splited_by_space, desc_id):
	program = create_program_chunk(start_date, types, name_id, chapter_id, splited_by_space, desc_id)
	no_desc = create_program_chunk(start_date, types, name_id, chapter_id, splited_by_space)

	if st == "NHK1_130":
		nhk1_standards_desc.add(program)
		nhk1_standards.add(no_desc)
		return program, False, False
	elif st == "NHKFM_130":
		nhkfm_standards_desc.add(program)
		nhkfm_standards.add(no_desc)
		return program, False, False
	elif st == "FMT":
		tokyofm_standards_desc.add(program)
		tokyofm_standards.add(no_desc)
		return program, False, False
	elif st in radiolist.NHK1_NET:
		if program in nhk1_standards_desc:
			return time_base60(start_date), True, True
		elif no_desc in nhk1_standards:
			return time_base60(start_date) + "*" + str(desc_id) + ".", True, False
	elif st in radiolist.NHKFM_NET:
		if program in nhkfm_standards_desc:
			return time_base60(start_date), True, True
		elif no_desc in nhkfm_standards:
			return time_base60(start_date) + "*" + str(desc_id) + ".", True, False
	elif st in radiolist.FM_NET:
		if program in tokyofm_standards_desc:
			return time_base60(start_date), True, True
		elif no_desc in tokyofm_standards:
			return time_base60(start_date) + "*" + str(desc_id) + ".", True, False

	return program, True, True

def get_interval(start_time, end_time):
	start_hour = (int)(start_time[:2])
	start_minute = (int)(start_time[2:])
	end_hour = (int)(end_time[:2])
	end_minute = (int)(end_time[2:])
	result = 0
	if start_hour < end_hour:
		result = 60 - start_minute
		start_minute = 0
		start_hour += 1
		result += 60 * (end_hour - start_hour)
	return result + end_minute - start_minute

def get_splitter_data(year, month):
	global splitter_data

	lines = []
	if os.path.exists("./radio_splitter.txt"):
		f = open("./radio_splitter.txt", 'r')
		a = f.read()
		lines = a.split("\n")
		f.close()

	splitter_data = {}
	stations = []
	for line in lines:
		if line.startswith(">"):
			stations = line.split(" ")[1:]
		elif line.startswith("#"):
			continue
		elif "-" in line:
			splited1 = line.split(" ")
			splited2 = splited1[0].split("-")
			from_year = splited2[0][:4]
			from_month = splited2[0][4:]
			to_year = splited2[1][:4]
			to_month = splited2[1][4:]
			for station in stations:
				if from_year < year or (from_year == year and from_month <= month) and year < to_year or (year == from_year and month <= to_month):
					if station not in splitter_data:
						splitter_data[station] = ""
					if splitter_data[station] != "":
						splitter_data[station] += "|"
					splitter_data[station] += " ".join(splited1[1:])

def split_title_chapter(title_string, station_tag, year, month):
	chapterPointer = 0
	bracePointer = 0
	trianglePointer = 0
	splitPointer = 0

	# 決め打ち
	hitPattern = False
	if station_tag in splitter_data:
		matchObj = re.search(splitter_data[station_tag], title_string)
		if matchObj:
			hitPattern = True
			if matchObj.end() < len(title_string):
				splitPointer = matchObj.end()

	if not hitPattern:
		if splitPointer == 0:
			matchObj = re.search(r'#[0-9]+', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'(①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩|⑪|⑫|⑬|⑭|⑮|⑯|⑰|⑱|⑲|⑳)$', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0 and station_tag == "RNB":
				matchObj = re.search(r'(①|②|③|④)\s*(〜|「)', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'(Hour\.|Part|part|パート)[0-9]+$', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'第[0-9]+(日|回|話|戦|節)', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'[0-9]+時〜[0-9]+時$', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'[0-9]+(時|時台)$', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'\(PART\s*[0-9]+\)$', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0:
				matchObj = re.search(r'\([0-9:・－〜時台]+\)', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			if chapterPointer == 0 and station_tag == "QRR":
				matchObj = re.search(r'[0-9]+時〜[0-9]+時', title_string)
				if matchObj:
					chapterPointer = matchObj.start()

			matchObj = re.search(r'「.+」', title_string)
			if matchObj:
				bracePointer = matchObj.start()

			if bracePointer == 0:
				matchObj = re.search(r'【.+】', title_string)
				if matchObj:
					bracePointer = matchObj.start()

			if bracePointer == 0:
				matchObj = re.search(r'『.+』', title_string)
				if matchObj:
					bracePointer = matchObj.start()

			matchObj = re.search(r'▽|▼', title_string)
			if matchObj:
				trianglePointer = matchObj.start()

			if chapterPointer !=0 and bracePointer != 0:
				splitPointer = min(chapterPointer, bracePointer)
			elif trianglePointer !=0 and bracePointer != 0:
				splitPointer = min(trianglePointer, bracePointer)
			elif chapterPointer !=0:
				splitPointer = chapterPointer
			elif bracePointer !=0:
				splitPointer = bracePointer
			elif trianglePointer !=0:
				splitPointer = trianglePointer

	splited_by_space = False
	if splitPointer == 0:
		title_part = title_string
		chapter_part = None
	else:
		title_part = title_string[:splitPointer]
		chapter_part = title_string[splitPointer:]
		if title_part[-1] == " ":
			title_part = title_part[:-1]
			splited_by_space = True
		if chapter_part[0] == " ":
			chapter_part = chapter_part[1:]
			splited_by_space = True

	return title_part, chapter_part, splited_by_space
