import requests
import json
import mysql.connector

# url = "https://gate.nicednb.com/nice/bizinfo/v1.0/sentinel/target/company?cmpCd=1407283"
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization':'Bearer 5cfb8674-49a8-4911-b6cd-b3023a0c8e5f',
# }
# data = {
#     "cmpCd": "1407283",
# }

# response = requests.post(url, headers=headers, data=json.dumps(data))
# response_json = response.json()

# conn = mysql.connector.connect(
#     host="116.124.133.159",  # 데이터베이스 서버 주소
#     user="search",  # 데이터베이스 사용자 이름
#     password="rldjqwjdqh",  # 데이터베이스 비밀번호
#     database="searchcom"  # 사용할 데이터베이스 이름
# )

# # 커서를 생성
# cursor = conn.cursor()

# # JSON 응답에서 데이터를 추출
# cmp_info = response_json['dataBody']['cmpInfo']
# mgr_info = response_json['dataBody']['mgrInfo']
# stkr_info = response_json['dataBody']['stkrInfo']

# # mgr_info와 stkr_info를 JSON 문자열로 변환
# mgr_info_json = json.dumps(mgr_info)
# stkr_info_json = json.dumps(stkr_info)

# # SQL 쿼리를 작성
# query = """
#     INSERT INTO searchcom.cmp_info (cmpCd, cmpNm, cmpEnm, bizNo, cmpTypEnm, estbDate, indCd, empCnt, telNo, faxTelNo, enAdr, 
#     mnBizCont,pstnCdNm1,mgrNm1,edu1,crr1,pstnCdNm2,mgrNm2,edu2,crr2,pstnCdNm3,mgrNm3,edu3,crr3,pstnCdNm4,mgrNm4,edu4,crr4,
#     pstnCdNm5,mgrNm5,edu5,crr5,pstnCdNm6,mgrNm6,edu6,crr6,pstnCdNm7,mgrNm7,edu7,crr7,pstnCdNm8,mgrNm8,edu8,crr8,pstnCdNm9,mgrNm9,edu9,crr9,pstnCdNm10,mgrNm10,edu10,crr10,
#     pstnCdNm11,mgrNm11,edu11,crr11,pstnCdNm12,mgrNm12,edu12,crr12,pstnCdNm13,mgrNm13,edu13,crr13,pstnCdNm14,mgrNm14,edu14,crr14,pstnCdNm15,mgrNm15,edu15,crr15
#     ,pstnCdNm16,mgrNm16,edu16,crr16,pstnCdNm17,mgrNm17,edu17,crr17,pstnCdNm18,mgrNm18,edu18,crr18,pstnCdNm19,mgrNm19,edu19,crr19,pstnCdNm20,mgrNm20,edu20,crr20,
#     stkrNm1,note1,ownRate1,stkrNm2,note2,ownRate2,stkrNm3,note3,ownRate3,stkrNm4,note4,ownRate4,stkrNm5,note5,ownRate5)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?,?,?,
#     ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?,?, ?);
# """

# mgr_info_values = []
# for i in range(20):
#     if i < len(mgr_info):
#         mgr = mgr_info[i]
#         mgr_info_values.extend([mgr['pstnCdNm'], mgr['mgrNm'], mgr['edu'], mgr['crr']])
#     else:
#         # 매니저 정보가 없는 경우 None 또는 적절한 기본값을 사용
#         mgr_info_values.extend([None, None, None, None])

# stkr_info_values = []
# for i in range(5): # stkr_info 항목이 5개라고 가정했습니다.
#     if i < len(stkr_info):
#         stkr = stkr_info[i]
#         stkr_info_values.extend([stkr['stkrNm'], stkr['note'], stkr['ownRate']])
#     else:
#         # stkr 정보가 없는 경우 None 또는 적절한 기본값을 사용
#         stkr_info_values.extend([None, None, None])

# # cmp_info와 mgr_info_values를 결합
# values = (cmp_info['cmpCd'], cmp_info['cmpNm'], cmp_info['cmpEnm'], cmp_info['bizNo'], cmp_info['cmpTypEnm'], cmp_info['estbDate'], cmp_info['indCd'], cmp_info['empCnt'], cmp_info['telNo'], cmp_info['faxTelNo'], cmp_info['enAdr'], cmp_info['mnBizCont']) + tuple(mgr_info_values) + tuple(stkr_info_values)
# print(len(values))
# # 쿼리 실행
# cursor.execute(query, values)

# # 변경사항을 커밋
# conn.commit()

# # 데이터베이스 연결을 종료
# conn.close()


url = "https://gate.nicednb.com/nice/bizinfo/v1.0/sentinel/target/company?cmpCd={data}"
headers = {
    'Content-Type': 'application/json',
    'Authorization':'Bearer c404b1da-b7bb-492b-a5a9-c654194ec5a9',
}



cmpCds = ["1486388", "1926700", "1932455", "1862244", "6705433", "8394118", "1991646", "3172071", "3221375", "1650657", "1221199", "1136966", "1653358", "1103348", "4050132", "1123212", "1929694", "1128549", "2980996", "8896719", "5973180", "5857409", "4033890", "3348348", "2791441", "2611178", "2210236", "1894168", "1786035", "1673849", "1670324", "1598125", "1465866", "1355102", "1241159", "1127016", "1208099", "8645891", "1954567", "9244471", "11053816", "11163656", "11175379", "10872121", "10946398", "11059940", "10806527", "10689536", "9610536", "9610849", "9610317", "8897244", "9470474", "1565439", "2223784", "2181668", "1884589", "4202368", "4121594", "9692292", "6721007", "9285880", "9295846", "8768121", "3689500", "3833881", "6731810", "9330416", "9329229", "5942832", "8532730", "9468964", "9306554", "10610679", "6798757", "9298428", "6686084", "9243535", "5897417", "10772600", "3856869", "4012921", "2113883", "8351651", "8230319", "12046824", "4087343", "6691213", "2941664", "3620723", "3667145", "2111442", "3703861", "9613779", "10613411", "1789796", "8769748", "6695355", "6806696", "8535053", "8771930", "9677797", "9453251", "6550350", "2276198", "6531405", "8155064", "4072143", "1210210", "7051273", "9557681", "11171792", "9331452", "8984685", "9448351", "8152896", "9543982", "9295408", "9258739", "8476560", "8156920", "10687830", "10614919", "9554291", "9548499", "9054393", "6422212", "6402324", "8998573", "3653545", "9552909", 
"3717557", "9150233", "10803906", "10725936", "10725278", "8992781", "8767716", "4009401", "4348030", "6635885", "3685105", "3836555", "5974489", "5966600", "8401691", "4167183", "6686507", "6721226", "4188111", "4192772", "4067224", "2987684", "4151451", "4074341", "2910628", "8962673", "3654821", "8947060", "8785753", "3695012", "1167525", "3220603", "2884288", "2950022", "3689696", "8659419", "8992587", "2976182", "8773083", "9686510", "1328231", "8809168", "1912510", "3740269", "10682885", "6726711", "10719491", "3717023", "9689857", "10963731", "8165459", "6802107", "8659678", "9302844", "4308516", "3697863", "9545224", "5862208", "6524802", "4118307", "4191799", "8992233", "4171678", "8078443", "9465665", "4344751", "3220234", "5852902", "6690974"]
for cmpCd in cmpCds:
    data = { "cmpCd": cmpCd }
    response = requests.post(url.format(data=cmpCd), headers=headers, data=json.dumps(data))
    # print(response.status_code)
    # print(response.text)
    response_data = response.json()

    conn = mysql.connector.connect(
        host="116.124.133.159",  # 데이터베이스 서버 주소
        user="search",  # 데이터베이스 사용자 이름
        password="rldjqwjdqh",  # 데이터베이스 비밀번호
        database="searchcom"  # 사용할 데이터베이스 이름
    )

    # 커서를 생성
    cursor = conn.cursor()
    # SQL 쿼리를 작성
    query = """
        INSERT INTO searchcom.cmp_info (cmpCd, cmpNm, cmpEnm, bizNo, cmpTypEnm, estbDate, indCd, empCnt, telNo, faxTelNo, enAdr, mnBizCont, pstnCdNm1,
        mgrNm1, edu1, crr1, pstnCdNm2, mgrNm2, edu2, crr2, pstnCdNm3, mgrNm3, edu3, crr3, pstnCdNm4, mgrNm4, edu4, crr4, pstnCdNm5, mgrNm5, edu5, crr5,
        pstnCdNm6, mgrNm6, edu6, crr6, pstnCdNm7, mgrNm7, edu7, crr7, pstnCdNm8, mgrNm8, edu8, crr8, pstnCdNm9, mgrNm9, edu9, crr9, pstnCdNm10, mgrNm10,
        edu10, crr10, pstnCdNm11, mgrNm11, edu11, crr11, pstnCdNm12, mgrNm12, edu12, crr12, pstnCdNm13, mgrNm13, edu13, crr13, pstnCdNm14, mgrNm14, edu14,
        crr14, pstnCdNm15, mgrNm15, edu15, crr15, pstnCdNm16, mgrNm16, edu16, crr16, pstnCdNm17, mgrNm17, edu17, crr17, pstnCdNm18, mgrNm18, edu18, crr18,
        pstnCdNm19, mgrNm19, edu19, crr19, pstnCdNm20, mgrNm20, edu20, crr20, stkrNm1, note1, ownRate1, stkrNm2, note2, ownRate2, stkrNm3, note3, ownRate3,
        stkrNm4, note4, ownRate4, stkrNm5, note5, ownRate5)
        VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,
        %s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s,
        %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s);
    """
    print(response_data['dataBody'])

    values = (
            response_data['dataBody']['cmpInfo'].get('cmpCd'),
            response_data['dataBody']['cmpInfo'].get('cmpNm'),
            response_data['dataBody']['cmpInfo'].get('cmpEnm'),
            response_data['dataBody']['cmpInfo'].get('bizNo'),
            response_data['dataBody']['cmpInfo'].get('cmpTypEnm'),
            response_data['dataBody']['cmpInfo'].get('estbDate'),
            response_data['dataBody']['cmpInfo'].get('indCd'),
            response_data['dataBody']['cmpInfo'].get('empCnt'),
            response_data['dataBody']['cmpInfo'].get('telNo'),
            response_data['dataBody']['cmpInfo'].get('faxTelNo'),
            response_data['dataBody']['cmpInfo'].get('enAdr'),
            response_data['dataBody']['cmpInfo'].get('mnBizCont'),
            response_data['dataBody']['mgrInfo'][0]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 0 else 'N/A',
            response_data['dataBody']['mgrInfo'][0]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 0 else 'N/A',
            response_data['dataBody']['mgrInfo'][0]['edu'] if len(response_data['dataBody']['mgrInfo']) > 0 else 'N/A',
            response_data['dataBody']['mgrInfo'][0]['crr'] if len(response_data['dataBody']['mgrInfo']) > 0 else 'N/A',
            response_data['dataBody']['mgrInfo'][1]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 1 else 'N/A',
            #response_data['dataBody']['mgrInfo'][1].get('pstnCdNm2', 'N/A') if len(response_data['dataBody']['mgrInfo']) > 1 else 'N/A',
            response_data['dataBody']['mgrInfo'][1]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 1 else 'N/A',
            response_data['dataBody']['mgrInfo'][1]['edu'] if len(response_data['dataBody']['mgrInfo']) > 1 else 'N/A',
            response_data['dataBody']['mgrInfo'][1]['crr'] if len(response_data['dataBody']['mgrInfo']) > 1 else 'N/A',
            response_data['dataBody']['mgrInfo'][2]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 2 else 'N/A',
            response_data['dataBody']['mgrInfo'][2]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 2 else 'N/A',
            response_data['dataBody']['mgrInfo'][2]['edu'] if len(response_data['dataBody']['mgrInfo']) > 2 else 'N/A',
            response_data['dataBody']['mgrInfo'][2]['crr'] if len(response_data['dataBody']['mgrInfo']) > 2 else 'N/A',
            response_data['dataBody']['mgrInfo'][3]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 3 else 'N/A',
            response_data['dataBody']['mgrInfo'][3]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 3 else 'N/A',
            response_data['dataBody']['mgrInfo'][3]['edu'] if len(response_data['dataBody']['mgrInfo']) > 3 else 'N/A',
            response_data['dataBody']['mgrInfo'][3]['crr'] if len(response_data['dataBody']['mgrInfo']) > 3 else 'N/A',
            response_data['dataBody']['mgrInfo'][4]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 4 else 'N/A',
            response_data['dataBody']['mgrInfo'][4]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 4 else 'N/A',
            response_data['dataBody']['mgrInfo'][4]['edu'] if len(response_data['dataBody']['mgrInfo']) > 4 else 'N/A',
            response_data['dataBody']['mgrInfo'][4]['crr'] if len(response_data['dataBody']['mgrInfo']) > 4 else 'N/A',
            response_data['dataBody']['mgrInfo'][5]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 5 else 'N/A',
            response_data['dataBody']['mgrInfo'][5]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 5 else 'N/A',
            response_data['dataBody']['mgrInfo'][5]['edu'] if len(response_data['dataBody']['mgrInfo']) > 5 else 'N/A',
            response_data['dataBody']['mgrInfo'][5]['crr'] if len(response_data['dataBody']['mgrInfo']) > 5 else 'N/A',
            response_data['dataBody']['mgrInfo'][6]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 6 else 'N/A',
            response_data['dataBody']['mgrInfo'][6]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 6 else 'N/A',
            response_data['dataBody']['mgrInfo'][6]['edu'] if len(response_data['dataBody']['mgrInfo']) > 6 else 'N/A',
            response_data['dataBody']['mgrInfo'][6]['crr'] if len(response_data['dataBody']['mgrInfo']) > 6 else 'N/A',
            response_data['dataBody']['mgrInfo'][7]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 7 else 'N/A',
            response_data['dataBody']['mgrInfo'][7]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 7 else 'N/A',
            response_data['dataBody']['mgrInfo'][7]['edu'] if len(response_data['dataBody']['mgrInfo']) > 7 else 'N/A',
            response_data['dataBody']['mgrInfo'][7]['crr'] if len(response_data['dataBody']['mgrInfo']) > 7 else 'N/A',
            response_data['dataBody']['mgrInfo'][8]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 8 else 'N/A',
            response_data['dataBody']['mgrInfo'][8]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 8 else 'N/A',
            response_data['dataBody']['mgrInfo'][8]['edu'] if len(response_data['dataBody']['mgrInfo']) > 8 else 'N/A',
            response_data['dataBody']['mgrInfo'][8]['crr'] if len(response_data['dataBody']['mgrInfo']) > 8 else 'N/A',
            response_data['dataBody']['mgrInfo'][9]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 9 else 'N/A',
            response_data['dataBody']['mgrInfo'][9]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 9 else 'N/A',
            response_data['dataBody']['mgrInfo'][9]['edu'] if len(response_data['dataBody']['mgrInfo']) > 9 else 'N/A',
            response_data['dataBody']['mgrInfo'][9]['crr'] if len(response_data['dataBody']['mgrInfo']) > 9 else 'N/A',
            response_data['dataBody']['mgrInfo'][10]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 10 else 'N/A',
            response_data['dataBody']['mgrInfo'][10]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 10 else 'N/A',
            response_data['dataBody']['mgrInfo'][10]['edu'] if len(response_data['dataBody']['mgrInfo']) > 10 else 'N/A',
            response_data['dataBody']['mgrInfo'][10]['crr'] if len(response_data['dataBody']['mgrInfo']) > 10 else 'N/A',
            response_data['dataBody']['mgrInfo'][11]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 11 else 'N/A',
            response_data['dataBody']['mgrInfo'][11]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 11 else 'N/A',
            response_data['dataBody']['mgrInfo'][11]['edu'] if len(response_data['dataBody']['mgrInfo']) > 11 else 'N/A',
            response_data['dataBody']['mgrInfo'][11]['crr'] if len(response_data['dataBody']['mgrInfo']) > 11 else 'N/A',
            response_data['dataBody']['mgrInfo'][12]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 12 else 'N/A',
            response_data['dataBody']['mgrInfo'][12]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 12 else 'N/A',
            response_data['dataBody']['mgrInfo'][12]['edu'] if len(response_data['dataBody']['mgrInfo']) > 12 else 'N/A',
            response_data['dataBody']['mgrInfo'][12]['crr'] if len(response_data['dataBody']['mgrInfo']) > 12 else 'N/A',
            response_data['dataBody']['mgrInfo'][13]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 13 else 'N/A',
            response_data['dataBody']['mgrInfo'][13]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 13 else 'N/A',
            response_data['dataBody']['mgrInfo'][13]['edu'] if len(response_data['dataBody']['mgrInfo']) > 13 else 'N/A',
            response_data['dataBody']['mgrInfo'][13]['crr'] if len(response_data['dataBody']['mgrInfo']) > 13 else 'N/A',
            response_data['dataBody']['mgrInfo'][14]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 14 else 'N/A',
            response_data['dataBody']['mgrInfo'][14]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 14 else 'N/A',
            response_data['dataBody']['mgrInfo'][14]['edu'] if len(response_data['dataBody']['mgrInfo']) > 14 else 'N/A',
            response_data['dataBody']['mgrInfo'][14]['crr'] if len(response_data['dataBody']['mgrInfo']) > 14 else 'N/A',
            response_data['dataBody']['mgrInfo'][15]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 15 else 'N/A',
            response_data['dataBody']['mgrInfo'][15]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 15 else 'N/A',
            response_data['dataBody']['mgrInfo'][15]['edu'] if len(response_data['dataBody']['mgrInfo']) > 15 else 'N/A',
            response_data['dataBody']['mgrInfo'][15]['crr'] if len(response_data['dataBody']['mgrInfo']) > 15 else 'N/A',
            response_data['dataBody']['mgrInfo'][16]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 16 else 'N/A',
            response_data['dataBody']['mgrInfo'][16]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 16 else 'N/A',
            response_data['dataBody']['mgrInfo'][16]['edu'] if len(response_data['dataBody']['mgrInfo']) > 16 else 'N/A',
            response_data['dataBody']['mgrInfo'][16]['crr'] if len(response_data['dataBody']['mgrInfo']) > 16 else 'N/A',
            response_data['dataBody']['mgrInfo'][17]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 17 else 'N/A',
            response_data['dataBody']['mgrInfo'][17]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 17 else 'N/A',
            response_data['dataBody']['mgrInfo'][17]['edu'] if len(response_data['dataBody']['mgrInfo']) > 17 else 'N/A',
            response_data['dataBody']['mgrInfo'][17]['crr'] if len(response_data['dataBody']['mgrInfo']) > 17 else 'N/A',
            response_data['dataBody']['mgrInfo'][18]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 18 else 'N/A',
            response_data['dataBody']['mgrInfo'][18]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 18 else 'N/A',
            response_data['dataBody']['mgrInfo'][18]['edu'] if len(response_data['dataBody']['mgrInfo']) > 18 else 'N/A',
            response_data['dataBody']['mgrInfo'][18]['crr'] if len(response_data['dataBody']['mgrInfo']) > 18 else 'N/A',
            response_data['dataBody']['mgrInfo'][19]['pstnCdNm'] if len(response_data['dataBody']['mgrInfo']) > 19 else 'N/A',
            response_data['dataBody']['mgrInfo'][19]['mgrNm'] if len(response_data['dataBody']['mgrInfo']) > 19 else 'N/A',
            response_data['dataBody']['mgrInfo'][19]['edu'] if len(response_data['dataBody']['mgrInfo']) > 19 else 'N/A',
            response_data['dataBody']['mgrInfo'][19]['crr'] if len(response_data['dataBody']['mgrInfo']) > 19 else 'N/A',
            response_data['dataBody']['stkrInfo'][0]['stkrNm'] if len(response_data['dataBody']['stkrInfo']) > 0 else 'N/A',
            response_data['dataBody']['stkrInfo'][0]['note'] if len(response_data['dataBody']['stkrInfo']) > 0 else 'N/A',
            response_data['dataBody']['stkrInfo'][0]['ownRate'] if len(response_data['dataBody']['stkrInfo']) > 0 else 'N/A',
            response_data['dataBody']['stkrInfo'][1]['stkrNm'] if len(response_data['dataBody']['stkrInfo']) > 1 else 'N/A',
            response_data['dataBody']['stkrInfo'][1]['note'] if len(response_data['dataBody']['stkrInfo']) > 1 else 'N/A',
            response_data['dataBody']['stkrInfo'][1]['ownRate'] if len(response_data['dataBody']['stkrInfo']) > 1 else 'N/A',
            response_data['dataBody']['stkrInfo'][2]['stkrNm'] if len(response_data['dataBody']['stkrInfo']) > 2 else 'N/A',
            response_data['dataBody']['stkrInfo'][2]['note'] if len(response_data['dataBody']['stkrInfo']) > 2 else 'N/A',
            response_data['dataBody']['stkrInfo'][2]['ownRate'] if len(response_data['dataBody']['stkrInfo']) > 2 else 'N/A',
            response_data['dataBody']['stkrInfo'][3]['stkrNm'] if len(response_data['dataBody']['stkrInfo']) > 3 else 'N/A',
            response_data['dataBody']['stkrInfo'][3]['note'] if len(response_data['dataBody']['stkrInfo']) > 3 else 'N/A',
            response_data['dataBody']['stkrInfo'][3]['ownRate'] if len(response_data['dataBody']['stkrInfo']) > 3 else 'N/A',
            response_data['dataBody']['stkrInfo'][4]['stkrNm'] if len(response_data['dataBody']['stkrInfo']) > 4 else 'N/A',
            response_data['dataBody']['stkrInfo'][4]['note'] if len(response_data['dataBody']['stkrInfo']) > 4 else 'N/A',
            response_data['dataBody']['stkrInfo'][4]['ownRate'] if len(response_data['dataBody']['stkrInfo']) > 4 else 'N/A',
        )
    # 쿼리 실행
    cursor.execute(query, values)

# 변경사2을 커밋
conn.commit()

# 데이터베이스 연결을 종료
conn.close()


# url = "https://gate.nicednb.com/nice/bizinfo/v1.0/sentinel/target/company?cmpCd=1407283"
# header4 = {
#     'Content-Type': 'application/json',
#     'Authorization':'Bearer 5cfb8674-49a8-4911-b6cd-b3023a0c8e5f',
# }
# data =5{
#     "cmpCd": "1407283",
# }

# respon6e = requests.post(url, headers=headers, data=json.dumps(data))

# response_json = response.json()

# #회사명
# cmpNm = response_json['dataBody']['cmpInfo']['cmpNm']
# print(f"cmpNm: {cmpNm}")

# print(f"cmpCd: {cmpCd}")
# cmpEnm = response_json['dataBody']['cmpInfo']['cmpEnm']
# print(f"cmpEnm: {cmpEnm}")

# print(f"bizNo: {bizNo}")
# try:
#     cmpTypEnm = response_json['dataBody']['cmpInfo']['cmpTypEnm']20     print(f"cmpTypEnm: {cmpTypEnm}")
# except:
#     print(f"cmpTypEnm: null")
# try:
#     estbDate = response_json['dataBody']['cmpInfo']['estbDate']
#     print(f"estbDate: {estbDate}")
# except:
#     print(f"estbDate: null")
# try:
#     indCd = response_json['dataBody']['cmpInfo']['indCd']
#     print(f"indCd: {indCd}")
# except:
#     print(f"indCd: null")
# try:
#     telNo = response_json['dataBody']['cmpInfo']['telNo']
#     print(f"telNo: {telNo}")
# except:
#     print(f"telNo: null")
# try:
#     faxTelNo = response_json['dataBody']['cmpInfo']['faxTelNo']
#     print(f"faxTelNo: {faxTelNo}")
# except:
#     print(f"faxTelNo: null")
# try:
#     enAdr = response_json['dataBody']['cmpInfo']['enAdr']
#     print(f"enAdr: {enAdr}")
# except:
#     print(f"enAdr: null")
# try:
#     mnBizCont = response_json['dataBody']['cmpInfo']['mnBizCont']
#     print(f"mnBizCont: {mnBizCont}")
# except:
#     print(f"mnBizCont: null")
# #----------------------mgrInfo
# try:
#     pstnCdNm1 = response_json['dataBody']['mgrInfo']['pstnCdNm1']
#     print(f"pstnCdNm1: {pstnCdNm1}")
# except:
#     print(f"pstnCdNm1: null")
# try:
#     mgrNm1 = response_json['dataBody']['mgrInfo']['mgrNm1']
#     print(f"mgrNm1: {mgrNm1}")
# except:
#     print(f"mgrNm1: null")
# try:
#     edu1 = response_json['dataBody']['mgrInfo']['edu1']
#     print(f"edu1: {edu1}")
# except:
#     print(f"edu1: null")
# try:
#     crr1 = response_json['dataBody']['mgrInfo']['crr1']
#     print(f"crr1: {crr1}")
# except:
#     print(f"crr1: null")

# try:
#     pstnCdNm2 = response_json['dataBody']['mgrInfo']['pstnCdNm2']
#     print(f"pstnCdNm2: {pstnCdNm2}")
# except:
#     print(f"pstnCdNm2: null")
# try:
#     mgrNm2 = response_json['dataBody']['mgrInfo']['mgrNm2']
#     print(f"mgrNm2: {mgrNm2}")
# except:
#     print(f"mgrNm2: null")
# try:
#     edu2 = response_json['dataBody']['mgrInfo']['edu2']
#     print(f"edu2: {edu2}")
# except:
#     print(f"edu2: null")
# try:
#     crr2 = response_json['dataBody']['mgrInfo']['crr2']
#     print(f"crr2: {crr2}")
# except:
#     print(f"crr2: null")

# try:
#     pstnCdNm3 = response_json['dataBody']['mgrInfo']['pstnCdNm3']
#     print(f"pstnCdNm3: {pstnCdNm3}")
# except:
#     print(f"pstnCdNm3: null")
# try:
#     mgrNm3 = response_json['dataBody']['mgrInfo']['mgrNm3']
#     print(f"mgrNm3: {mgrNm3}")
# except:
#     print(f"mgrNm3: null")
# try:
#     edu4 = response_json['dataBody']['mgrInfo']['edu4']
#     print(f"edu4: {edu4}")
# except:
#     print(f"edu4: null")
# try:
#     crr4 = response_json['dataBody']['mgrInfo']['crr4']
#     print(f"crr4: {crr4}")
# except:
#     print(f"crr4: null")

# try:
#     pstnCdNm5 = response_json['dataBody']['mgrInfo']['pstnCdNm5']
#     print(f"pstnCdNm5: {pstnCdNm5}")
# except:
#     print(f"pstnCdNm5: null")
# try:
#     mgrNm6 = response_json['dataBody']['mgrInfo']['mgrNm6']
#     print(f"mgrNm6: {mgrNm6}")
# except:
#     print(f"mgrNm6: null")
# try:
#     edu6 = response_json['dataBody']['mgrInfo']['edu6']
#     print(f"edu6: {edu6}")
# except:
#     print(f"edu6: null")
# try:
#     crr6 = response_json['dataBody']['mgrInfo']['crr6']
#     print(f"crr6: {crr6}")
# except:
#     print(f"crr6: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm8 = response_json['dataBody']['mgrInfo']['pstnCdNm8']
#     print(f"pstnCdNm8: {pstnCdNm8}")
# except:
#     print(f"pstnCdNm8: null")
# try:
#     mgrNm8 = response_json['dataBody']['mgrInfo']['mgrNm8']
#     print(f"mgrNm8: {mgrNm8}")
# except:
#     print(f"mgrNm8: null")
# try:
#     edu8 = response_json['dataBody']['mgrInfo']['edu8']
#     print(f"edu8: {edu8}")
# except:
#     print(f"edu8: null")
# try:
#     crr8 = response_json['dataBody']['mgrInfo']['crr8']
#     print(f"crr8: {crr8}")
# except:
#     print(f"crr8: null")

# try:
#     pstnCdNm9 = response_json['dataBody']['mgrInfo']['pstnCdNm9']
#     print(f"pstnCdNm9: {pstnCdNm9}")
# except:
#     print(f"pstnCdNm9: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")

# try:
#     pstnCdNm7 = response_json['dataBody']['mgrInfo']['pstnCdNm7']
#     print(f"pstnCdNm7: {pstnCdNm7}")
# except:
#     print(f"pstnCdNm7: null")
# try:
#     mgrNm7 = response_json['dataBody']['mgrInfo']['mgrNm7']
#     print(f"mgrNm7: {mgrNm7}")
# except:
#     print(f"mgrNm7: null")
# try:
#     edu7 = response_json['dataBody']['mgrInfo']['edu7']
#     print(f"edu7: {edu7}")
# except:
#     print(f"edu7: null")
# try:
#     crr7 = response_json['dataBody']['mgrInfo']['crr7']
#     print(f"crr7: {crr7}")
# except:
#     print(f"crr7: null")


# #경영진 이름
# stkrNm = response_json['dataBody']['stkrInfo'][0]['stkrNm']
# print(f"stkrNm: {stkrNm}")
# try:
#     stkrNm1 = response_json['dataBody']['stkrInfo'][1]['stkrNm']
#     print(f"stkrNm1: {stkrNm1}")
# except:
#     print(f"stkrNm1: null")    
# try:
#     stkrNm2 = response_json['dataBody']['stkrInfo'][2]['stkrNm']
#     print(f"stkrNm2: {stkrNm2}")
# except:
#     print(f"stkrNm2: null")
# try:
#     stkrNm3 = response_json['dataBody']['stkrInfo'][3]['stkrNm']
#     print(f"stkrNm3: {stkrNm3}")
# except:
#     print(f"stkrNm3: null")
# try:    
#     stkrNm4 = response_json['dataBody']['stkrInfo'][4]['stkrNm']
#     print(f"stkrNm4: {stkrNm4}")
# except:
#     print(f"stkrNm4: null")
# try:    
#     stkrNm5 = response_json['dataBody']['stkrInfo'][5]['stkrNm']
#     print(f"stkrNm5: {stkrNm5}")
# except:
#     print(f"stkrNm5: null")


# conn = mysql.connector.connect(
#     host="116.124.133.159",  # 데이터베이스 서버 주소
#     user="search",  # 데이터베이스 사용자 이름
#     password="rldjqwjdqh",  # 데이터베이스 비밀번호
#     database="searchcom"  # 사용할 데이터베이스 이름
# )

# # 커서를 생성
# cursor = conn.cursor()
# # SQL 쿼리를 작성
# query = """
#     INSERT INTO searchcom.cmp_info (cmpNm, stkrNm1, stkrNm2, stkrNm3, stkrNm4, stkrNm5)
#     VALUES (%s, %s, %s, %s, %s,%s);
# """

# # 경영진 정보 추출 및 NULL 처리
# stkr_info = response_json['dataBody']['stkrInfo']
# stkr_values = [None] * 5  # stkrNm1 ~ stkrNm5이므로 총 5명의 경영진에 대한 정보를 처리
# for i in range(5):  
#     try:
#         stkr_values[i] = stkr_info[i + 1]['stkrNm']  # stkr_info[0]은 stkrNm에 해당하므로, stkrNm1부터 시작
#     except IndexError:  
#         break

# # values 튜플 생성
# values = (cmpNm, *stkr_values)

# # 쿼리 실행
# cursor.execute(query, values)

# # 변경사항을 커밋
# conn.commit()

# # 데이터베이스 연결을 종료
# conn.close()