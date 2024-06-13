# import json
# import os
# from typing import Iterable
# from scrapy.http import Response
# import requests
# import scrapy
# import scrapy.resolver
# import sys
# sys.path.append('../../../../')
# from datetime import datetime
# from tools.save_json.save import save_json
# import copy


# class SpiderSpider(scrapy.Spider):
#     name = "main"

#     headers = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/125.0.0.0 Safari/537.36",
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive',
#         'Referer': 'https://www.lpse.kemenkeu.go.id/',
#         'X-Requested-With': 'XMLHttpRequest'
#     }

#     cookies = {
#         '_gid': 'GA1.3.875731840.1717572748',
#         '_ga_4P3N4EF554': 'GS1.3.1717644744.10.1.1717645010.0.0.0',
#         '_ga_91P6C1LWGZ': 'GS1.1.1717643425.5.1.1717645011.0.0.0',
#         '_ga': 'GA1.1.786936201.1716261060'
#     }

#     def start_requests(self):
#         yield scrapy.Request(url='https://www.google.com/', callback=self.get_api)

#     def get_server_time(self):
#         server_time_url = 'https://www.lpse.kemenkeu.go.id/eproc4/json/getservertime'
#         server_time_response = requests.get(server_time_url)
#         print("Server Time Response:", server_time_response.status_code, server_time_response.text)

#     def get_server_time_and_access_target_page(self, target_url):
#         headers = {
#             'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/125.0.0.0 Safari/537.36",
#             'Accept': 'application/json, text/javascript, */*; q=0.01',
#             'Accept-Language': 'en-US,en;q=0.9',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Connection': 'keep-alive',
#             'Referer': 'https://www.lpse.kemenkeu.go.id/',
#             'X-Requested-With': 'XMLHttpRequest'
#         }

#         cookies = {
#             '_gid': 'GA1.3.875731840.1717572748',
#             '_ga_4P3N4EF554': 'GS1.3.1717644744.10.1.1717645010.0.0.0',
#             '_ga_91P6C1LWGZ': 'GS1.1.1717643425.5.1.1717645011.0.0.0',
#             '_ga': 'GA1.1.786936201.1716261060'
#         }

#         server_time_response = requests.get('https://www.lpse.kemenkeu.go.id/eproc4/json/getservertime', headers=headers, cookies=cookies)
#         print("Server Time Response:", server_time_response.status_code, server_time_response.text)

#         response = requests.get(target_url, headers=headers, cookies=cookies)
#         print("Target Page Response:", response.status_code)
#         print(response.text) 


#     def get_api(self, response):
#         cookies = {
#             'SPSE_SESSION': 'b0436b164c8fea5c732040825b23072a51f95517-___AT=ab03fbf1850dab187d29385fd9303aec7d884924&___TS=1717756702523&___ID=b99050c2-8a8a-42f3-ac9b-8eb6ca32da0b',
#         }

#         headers = {
#             'accept': 'application/json, text/javascript, */*; q=0.01',
#             'accept-language': 'en-US,en;q=0.9,id;q=0.8',
#             'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#             # 'cookie': 'SPSE_SESSION=b0436b164c8fea5c732040825b23072a51f95517-___AT=ab03fbf1850dab187d29385fd9303aec7d884924&___TS=1717756702523&___ID=b99050c2-8a8a-42f3-ac9b-8eb6ca32da0b',
#             'origin': 'https://www.lpse.kemenkeu.go.id',
#             'priority': 'u=1, i',
#             'referer': 'https://www.lpse.kemenkeu.go.id/eproc4/lelang?kategoriId=&tahun=&instansiId=L32&rekanan=&kontrak_status=&kontrak_tipe=',
#             'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#             'x-requested-with': 'XMLHttpRequest',
#         }

#         params = {
#             'rekanan': '',
#             'instansiId': 'L32',
#         }

#         data = {
#             'draw': '2',
#             'columns[0][data]': '0',
#             'columns[0][name]': '',
#             'columns[0][searchable]': 'true',
#             'columns[0][orderable]': 'true',
#             'columns[0][search][value]': '',
#             'columns[0][search][regex]': 'false',
#             'columns[1][data]': '1',
#             'columns[1][name]': '',
#             'columns[1][searchable]': 'true',
#             'columns[1][orderable]': 'true',
#             'columns[1][search][value]': '',
#             'columns[1][search][regex]': 'false',
#             'columns[2][data]': '2',
#             'columns[2][name]': '',
#             'columns[2][searchable]': 'true',
#             'columns[2][orderable]': 'true',
#             'columns[2][search][value]': '',
#             'columns[2][search][regex]': 'false',
#             'columns[3][data]': '3',
#             'columns[3][name]': '',
#             'columns[3][searchable]': 'false',
#             'columns[3][orderable]': 'false',
#             'columns[3][search][value]': '',
#             'columns[3][search][regex]': 'false',
#             'columns[4][data]': '4',
#             'columns[4][name]': '',
#             'columns[4][searchable]': 'true',
#             'columns[4][orderable]': 'true',
#             'columns[4][search][value]': '',
#             'columns[4][search][regex]': 'false',
#             'columns[5][data]': '5',
#             'columns[5][name]': '',
#             'columns[5][searchable]': 'true',
#             'columns[5][orderable]': 'true',
#             'columns[5][search][value]': '',
#             'columns[5][search][regex]': 'false',
#             'order[0][column]': '5',
#             'order[0][dir]': 'desc',
#             'start': '0',
#             'length': '-1',
#             'search[value]': '',
#             'search[regex]': 'false',
#             'authenticityToken': 'ab03fbf1850dab187d29385fd9303aec7d884924',
#         }

#         response = requests.post(
#             'https://www.lpse.kemenkeu.go.id/eproc4/dt/lelang',
#             params=params,
#             cookies=cookies,
#             headers=headers,
#             data=data,
#         )


#         print(response.status_code)
#         datas = response.json()
#         value_raw = datas['data']
#         for item in value_raw:
#             kode = item[0]
#             nama_paket = [
#                 item[5],
#                 item[6],
#                 item[7],
#                 item[8],
#             ]
#             k_l_p_d_instansi_lainnya= item[2]
#             tahapan = item[3]
#             hps = item[4]   
            
#             spse_raw = item[9]
#             if spse_raw == '1':
#                 spse = '3'
#             elif spse_raw == '2':
#                 spse = '4'
#             elif spse_raw == '3':
#                 spse = '4.3'
#             elif spse_raw == '4':
#                 spse = '4.4'
#             elif spse_raw == '5':
#                 spse = '4.5'

#             nilai_kontrak = item[10]

#             tahapan_url = f'https://www.lpse.kemenkeu.go.id/eproc4/lelang/{kode}/pengumumanlelang'


#             self.collected_data = {
#                     'link' : 'https://www.lpse.kemenkeu.go.id/eproc4/lelang?kategoriId=&tahun=&instansiId=L32&rekanan=&kontrak_status=&kontrak_tipe=',
#                     'domain' : 'lpse.kemenkeu.go.id',
#                     'crawling_time' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                     'crawling_time_epoch' : int(datetime.now().timestamp()),
#                     # 'path_data_raw' : path_s3,
#                     'path_data_clean' : None,
#                     'kode':int(kode),
#                     'nama_paket': nama_paket,
#                     'klpd_dan_instansi_lainnya': k_l_p_d_instansi_lainnya,
#                     'tahapan': tahapan,
#                     'hps': hps,
#                     'spse': spse,
#                     'nilai_kontrak': nilai_kontrak,
#                 }
#             if tahapan_url:
#                 yield scrapy.Request(
#                 tahapan_url,
#                 callback=self.tender_pengumuman,
#                 headers=self.headers,
#                 cookies=self.cookies,
#                 meta={'collected_data': self.collected_data.copy(), 'kode_api':kode }, 
#                 )


#     def tender_pengumuman(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
#         kode = response.css('#main > div > table > tr:nth-child(1) > td > strong::text').get()
        


#         # collected_data['pengumuman']={
            
#         # }

#         url = response.url.replace('pengumumanlelang', 'peserta')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_peserta, headers=self.headers, cookies=self.cookies, 
#                                     meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )


#     def tender_peserta(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
#         rows = response.css('#main > div > table > tbody > tr')
#         peserta=[]
#         for row in rows:
#             no = row.css('td:nth-child(1)::text').get()
#             nama_peserta = row.css('td:nth-child(2)::text').get().strip()
#             npwp = row.css('td:nth-child(3)::text').get()
#             harga_penawaran = row.css('td:nth-child(4)::text').get()
#             harga_terkoreksi = row.css('td:nth-child(5)::text').get()

#             peserta.append({
#                 'no': no,
#                 'nama_peserta': nama_peserta,
#                 'npwp': npwp,
#                 'harga_penawaran': harga_penawaran,
#                 'harga_terkoreksi': harga_terkoreksi
#             })

#         collected_data['peserta']=peserta
            


#         url = response.url.replace('peserta', 'hasil').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_hasil, headers=self.headers, cookies=self.cookies,meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )

#     def tender_hasil(self, response):
#         ee = response.css('#main > div > table > tbody > tr:nth-child(1) > td:nth-child(2)::text').get()
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']

#         tender_hasil = []
#         rows = response.css('#main > div > table')
#         for row in rows:
#             headers = row.css('thead > tr > th::text, thead > tr > th > span::text, thead > tr > th > span.badge.badge-info::text').getall()
            

#             for tbody_row in row.css('tbody > tr'):
#                 values = tbody_row.css('td::text, td > i::attr(class), td > img::attr(src)').getall()
#                 values = [value.strip() for value in values]
#                 values = [value for value in values if value]
#                 if not values:
#                     continue
#                 if headers and values:
#                 # if len(headers) == len(values):
#                 #     row_data = dict(zip(headers, values))
#                 #     tender_hasil.append(row_data)
#                 # else:
#                     row_data = {}
#                     for header, value in zip(headers, values):
#                         if header == "A":
#                             row_data['evaluasi_administrasi'] = value
#                         elif header == "T":
#                             row_data['evaluasi_teknis'] = value
#                         elif header == "ST":
#                             row_data['skor_teknis'] = value
#                         elif header == "P":
#                             row_data['penawaran'] = value
#                         elif header == "PT":
#                             row_data['penawaran_terkoreksi'] = value
#                         elif header == "HN":
#                             row_data['hasil_negosiasi'] = value
#                         elif header == "SH":
#                             row_data['skor_harga'] = value
#                         elif header == "SA":
#                             row_data['skor_akhir'] = value
#                         elif header == "K":
#                             row_data['evaluasi_kualifikasi'] = value
#                         elif header == "SK":
#                             row_data['skor_kualifikasi'] = value
#                         elif header == "SB":
#                             row_data['skor_pembuktian'] = value
#                         elif header == "H":
#                             row_data['evaluasi_harga/biaya'] = value
#                         elif header == "P":
#                             row_data['pemenang'] = value
#                         elif header == "PK":
#                             row_data['pemenang_berkontrak'] = value
#                         elif header == "B":
#                             row_data['pembuktian_kualifikasi'] = value
#                         else:
#                             row_data[header.lower()] = value

#                     tender_hasil.append(row_data)
#         collected_data['hasil_evaluasi'] = tender_hasil

#         url = response.url.replace('hasil', 'pemenang').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_pemenang, headers=self.headers, cookies=self.cookies, meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )

#     def tender_pemenang(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']

#         tables = response.css('#main > div > table')
#         pemenang = []
#         for row in tables:
#             nama_tender = row.css('tr:nth-child(1) > td::text').get()
#             jenis_pengadaan = row.css('tr:nth-child(2) > td::text').get()
#             klpd_dan_instansi_lainnya = row.css('tr:nth-child(3) > td::text').get()
#             satuan_kerja = row.css('tr:nth-child(4) > td::text').get()
#             pagu = row.css('tr:nth-child(5) > td::text').get()
#             hps = row.css('tr:nth-child(6) > td::text').get()

#             pemenang_data = {
#                 'nama_tender': nama_tender,
#                 'jenis_pengadaan': jenis_pengadaan,
#                 'klpd_dan_instansi_lainnya': klpd_dan_instansi_lainnya,
#                 'satuan_kerja': satuan_kerja,
#                 'pagu': pagu,
#                 'hps': hps
#             }

#             table_2 = row.css('tr:nth-child(7) > td > table > tr:nth-child(2)')
#             detail_pemenang = []
#             for row2 in table_2:
#                 nama_tender = row2.css('td:nth-child(1)::text').get()
#                 alamat = row2.css('td:nth-child(2) *::text').getall()
#                 npwp = row2.css('td:nth-child(3)::text').get()
#                 harga_penawaran = row2.css('td:nth-child(4)::text').get()
#                 harga_koreksi = row2.css('td:nth-child(5)::text').get()
#                 harga_negoisasi = row2.css('td:nth-child(6)::text').get()

#                 detail_pemenang_data = {
#                     'nama_tender': nama_tender,
#                     'alamat': alamat,
#                     'npwp': npwp,
#                     'harga_penawaran': harga_penawaran,
#                     'harga_koreksi': harga_koreksi,
#                     'harga_negoisasi': harga_negoisasi
#                 }
#                 detail_pemenang.append(detail_pemenang_data)

                

#             pemenang_data['detail_pemenang'] = detail_pemenang
#             pemenang.append(pemenang_data)

#         collected_data['pemenang'] = pemenang
        

#         url = response.url.replace('pemenang','pemenangberkontrak').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_pemenang_berkontrak, headers=self.headers, cookies=self.cookies, meta={'collected_data':collected_data.copy(), 'kode_api':kode_api } )

#     def tender_pemenang_berkontrak(self, response):
#         # ss = response.css('#main > div > table > tr:nth-child(1) > td::text').get()
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
        


#         tables = response.css('#main > div > table')
#         pemenang_berkontrak = []
#         for row in tables:
#             nama_tender = row.css('tr:nth-child(1) > td::text').get()
#             jenis_pengadaan = row.css('tr:nth-child(2) > td::text').get()
#             klpd_dan_instansi_lainnya = row.css('tr:nth-child(3) > td::text').get()
#             satuan_kerja = row.css('tr:nth-child(4) > td::text').get()
#             pagu = row.css('tr:nth-child(5) > td::text').get()
#             hps = row.css('tr:nth-child(6) > td::text').get()

#             pemenang_berkontrak_data = {
#                 'nama_tender': nama_tender,
#                 'jenis_pengadaan': jenis_pengadaan,
#                 'klpd_dan_instansi_lainnya': klpd_dan_instansi_lainnya,
#                 'satuan_kerja': satuan_kerja,
#                 'pagu': pagu,
#                 'hps': hps
#             }

#             table_2 = row.css('tr:nth-child(7) > td > table > tr:nth-child(2)')
#             detail_pemenang_berkontrak = []
#             for row2 in table_2:
#                 nama_pemenang = row2.css('td:nth-child(1)::text').get()
#                 alamat = row2.css('td:nth-child(2) *::text').getall()
#                 npwp = row2.css('td:nth-child(3)::text').get()
#                 harga_kontrak = row2.css('td:nth-child(4)::text').get()
#                 nilai_pdn = row2.css('td:nth-child(5)::text').get()
#                 nilai_umk = row2.css('td:nth-child(6)::text').get()

#                 detail_pemenang_berkontrak_data = {
#                     'nama_pemenang': nama_pemenang,
#                     'alamat': alamat,
#                     'npwp': npwp,
#                     'harga_kontrak': harga_kontrak,
#                     'nilai_pdn': nilai_pdn,
#                     'nilai_umk': nilai_umk
#                 }
#                 detail_pemenang_berkontrak.append(detail_pemenang_berkontrak_data)

#             pemenang_berkontrak_data['detail_pemenang_berkontrak'] = detail_pemenang_berkontrak
#             pemenang_berkontrak.append(pemenang_berkontrak_data)

#         collected_data['pemenang_berkontrak'] = pemenang_berkontrak

#         dir_raw = 'data'
#         os.makedirs(dir_raw ,exist_ok=True)
#         filename = f'{kode_api}.json'
#         save_json(collected_data, os.path.join(dir_raw, filename))














# import json
# import os
# from typing import Iterable
# from scrapy.http import Response
# import requests
# import scrapy
# import scrapy.resolver
# import sys
# sys.path.append('../../../../')
# from datetime import datetime
# from tools.save_json.save import save_json
# import copy


# class SpiderSpider(scrapy.Spider):
#     name = "main"

#     headers = {
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/125.0.0.0 Safari/537.36",
#         'Accept': 'application/json, text/javascript, */*; q=0.01',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Connection': 'keep-alive',
#         'Referer': 'https://www.lpse.kemenkeu.go.id/',
#         'X-Requested-With': 'XMLHttpRequest'
#     }

#     cookies = {
#         '_gid': 'GA1.3.875731840.1717572748',
#         '_ga_4P3N4EF554': 'GS1.3.1717644744.10.1.1717645010.0.0.0',
#         '_ga_91P6C1LWGZ': 'GS1.1.1717643425.5.1.1717645011.0.0.0',
#         '_ga': 'GA1.1.786936201.1716261060'
#     }

#     def start_requests(self):
#         yield scrapy.Request(url='https://www.google.com/', callback=self.get_api)

#     def get_server_time(self):
#         server_time_url = 'https://www.lpse.kemenkeu.go.id/eproc4/json/getservertime'
#         server_time_response = requests.get(server_time_url)
#         print("Server Time Response:", server_time_response.status_code, server_time_response.text)

#     def get_server_time_and_access_target_page(self, target_url):
#         headers = {
#             'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/125.0.0.0 Safari/537.36",
#             'Accept': 'application/json, text/javascript, */*; q=0.01',
#             'Accept-Language': 'en-US,en;q=0.9',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Connection': 'keep-alive',
#             'Referer': 'https://www.lpse.kemenkeu.go.id/',
#             'X-Requested-With': 'XMLHttpRequest'
#         }

#         cookies = {
#             '_gid': 'GA1.3.875731840.1717572748',
#             '_ga_4P3N4EF554': 'GS1.3.1717644744.10.1.1717645010.0.0.0',
#             '_ga_91P6C1LWGZ': 'GS1.1.1717643425.5.1.1717645011.0.0.0',
#             '_ga': 'GA1.1.786936201.1716261060'
#         }


#         server_time_response = requests.get('https://www.lpse.kemenkeu.go.id/eproc4/json/getservertime', headers=headers, cookies=cookies)
#         print("Server Time Response:", server_time_response.status_code, server_time_response.text)

#         response = requests.get(target_url, headers=headers, cookies=cookies)
#         print("Target Page Response:", response.status_code)
#         print(response.text) 


#     def get_api(self, response):

#         cookies = {
#             'SPSE_SESSION': '7926403d8378ab1b0f1b07ece1eba9963ce41af6-___AT=a61963776b1eb3b86e75628ceac6ffdb564c80b1&___TS=1717767077354&___ID=6f3bba91-897a-40f1-a38c-2ea0acd94e65',
#         }

#         headers = {
#             'accept': 'application/json, text/javascript, */*; q=0.01',
#             'accept-language': 'en-US,en;q=0.9,id;q=0.8',
#             'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#             # 'cookie': 'SPSE_SESSION=7926403d8378ab1b0f1b07ece1eba9963ce41af6-___AT=a61963776b1eb3b86e75628ceac6ffdb564c80b1&___TS=1717767077354&___ID=6f3bba91-897a-40f1-a38c-2ea0acd94e65',
#             'origin': 'https://www.lpse.kemenkeu.go.id',
#             'priority': 'u=1, i',
#             'referer': 'https://www.lpse.kemenkeu.go.id/eproc4/lelang?kategoriId=&tahun=&instansiId=L32&rekanan=&kontrak_status=&kontrak_tipe=',
#             'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
#             'x-requested-with': 'XMLHttpRequest',
#         }

#         params = {
#             'rekanan': '',
#             'instansiId': 'L32',
#         }

#         data = {
#             'draw': '2',
#             'columns[0][data]': '0',
#             'columns[0][name]': '',
#             'columns[0][searchable]': 'true',
#             'columns[0][orderable]': 'true',
#             'columns[0][search][value]': '',
#             'columns[0][search][regex]': 'false',
#             'columns[1][data]': '1',
#             'columns[1][name]': '',
#             'columns[1][searchable]': 'true',
#             'columns[1][orderable]': 'true',
#             'columns[1][search][value]': '',
#             'columns[1][search][regex]': 'false',
#             'columns[2][data]': '2',
#             'columns[2][name]': '',
#             'columns[2][searchable]': 'true',
#             'columns[2][orderable]': 'true',
#             'columns[2][search][value]': '',
#             'columns[2][search][regex]': 'false',
#             'columns[3][data]': '3',
#             'columns[3][name]': '',
#             'columns[3][searchable]': 'false',
#             'columns[3][orderable]': 'false',
#             'columns[3][search][value]': '',
#             'columns[3][search][regex]': 'false',
#             'columns[4][data]': '4',
#             'columns[4][name]': '',
#             'columns[4][searchable]': 'true',
#             'columns[4][orderable]': 'true',
#             'columns[4][search][value]': '',
#             'columns[4][search][regex]': 'false',
#             'columns[5][data]': '5',
#             'columns[5][name]': '',
#             'columns[5][searchable]': 'true',
#             'columns[5][orderable]': 'true',
#             'columns[5][search][value]': '',
#             'columns[5][search][regex]': 'false',
#             'order[0][column]': '5',
#             'order[0][dir]': 'desc',
#             'start': '0',
#             'length': '-1',
#             'search[value]': '',
#             'search[regex]': 'false',
#             'authenticityToken': 'a61963776b1eb3b86e75628ceac6ffdb564c80b1',
#         }

#         response = requests.post(
#             'https://www.lpse.kemenkeu.go.id/eproc4/dt/lelang',
#             params=params,
#             cookies=cookies,
#             headers=headers,
#             data=data,
#         )

#         print(response.status_code)
#         datas = response.json()
#         value_raw = datas['data']
#         for item in value_raw:
#             kode = item[0]
#             nama_paket = [
#                 item[5],
#                 item[6],
#                 item[7],
#                 item[8],
#             ]
#             k_l_p_d_instansi_lainnya= item[2]
#             tahapan = item[3]
#             hps = item[4]   
            
#             spse_raw = item[9]
#             if spse_raw == '1':
#                 spse = '3'
#             elif spse_raw == '2':
#                 spse = '4'
#             elif spse_raw == '3':
#                 spse = '4.3'
#             elif spse_raw == '4':
#                 spse = '4.4'
#             elif spse_raw == '5':
#                 spse = '4.5'

#             nilai_kontrak = item[10]

#             tahapan_url = f'https://www.lpse.kemenkeu.go.id/eproc4/lelang/{kode}/pengumumanlelang'


#             self.collected_data = {
#                     'link' : 'https://www.lpse.kemenkeu.go.id/eproc4/lelang?kategoriId=&tahun=&instansiId=L32&rekanan=&kontrak_status=&kontrak_tipe=',
#                     'domain' : 'lpse.kemenkeu.go.id',
#                     'crawling_time' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                     'crawling_time_epoch' : int(datetime.now().timestamp()),
#                     # 'path_data_raw' : path_s3,
#                     'path_data_clean' : None,
#                     'kode':int(kode),
#                     'nama_paket': nama_paket,
#                     'klpd_dan_instansi_lainnya': k_l_p_d_instansi_lainnya,
#                     'tahapan': tahapan,
#                     'hps': hps,
#                     'spse': spse,
#                     'nilai_kontrak': nilai_kontrak,
#                 }
#             if tahapan_url:
#                 yield scrapy.Request(
#                 tahapan_url,
#                 callback=self.tender_pengumuman,
#                 headers=self.headers,
#                 cookies=self.cookies,
#                 meta={'collected_data': self.collected_data.copy(), 'kode_api':kode }, 
#                 )


#     def tender_pengumuman(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
#         pengumuman = []
#         table = response.xpath('//*[@id="main"]/div/table')
#         for row in table.xpath('.//tr'):
#             header = row.xpath('.//th/text()').get()
#             value = row.xpath('.//td//text()').getall()
#             if header and value:
#                 header = header.strip()
#                 value = [val.strip() for val in value if val.strip()]  # Filter value kosong
#                 pengumuman.append({header: value})

#         collected_data['pengumuman'] = pengumuman


#         url = response.url.replace('pengumumanlelang', 'peserta')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_peserta, headers=self.headers, cookies=self.cookies, 
#                                     meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )


#     def tender_peserta(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
#         rows = response.css('#main > div > table > tbody > tr')
#         peserta=[]
#         for row in rows:
#             no = row.css('td:nth-child(1)::text').get()
#             nama_peserta = row.css('td:nth-child(2)::text').get().strip()
#             npwp = row.css('td:nth-child(3)::text').get()
#             harga_penawaran = row.css('td:nth-child(4)::text').get()
#             harga_terkoreksi = row.css('td:nth-child(5)::text').get()

#             peserta.append({
#                 'no': no,
#                 'nama_peserta': nama_peserta,
#                 'npwp': npwp,
#                 'harga_penawaran': harga_penawaran,
#                 'harga_terkoreksi': harga_terkoreksi
#             })

#         collected_data['peserta']=peserta
            


#         url = response.url.replace('peserta', 'hasil').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_hasil, headers=self.headers, cookies=self.cookies,meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )

#     def tender_hasil(self, response):
#         ee = response.css('#main > div > table > tbody > tr:nth-child(1) > td:nth-child(2)::text').get()
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']

#         tender_hasil = []
#         rows = response.xpath('//table[@class="table table-sm"]/tbody/tr')
#         for row in rows:
#             item = {}
#             cells = row.xpath('.//td')
#             for index, cell in enumerate(cells, start=1):
#                 header = response.xpath(f'//table[@class="table table-sm"]/thead/tr/th[{index}]//text()').get()
#                 value = cell.xpath('.//text()').get()
#                 img_src = cell.xpath('.//img/@src').get()
#                 i_class = cell.xpath('.//i/@class').get()
#                 # //*[@id="main"]/div/table/tbody/tr[2]/td[3]/i
#                 #! mendaptkan class i nya
#                 #*
#                 if img_src:
#                     value = img_src  
#                 if header == 'P' and img_src and 'star' in img_src:
#                     header = 'P_img'
#                 elif header == "A":
#                     header = 'evaluasi_administrasi'
#                 elif header == "T":
#                     header = 'evaluasi_teknis'
#                 elif header == "ST":
#                     header = 'skor_teknis'
#                 elif header == "P":
#                     header = 'penawaran'
#                 elif header == "PT":
#                     header = 'penawaran_terkoreksi'
#                 elif header == "HN":
#                     header = 'hasil_negosiasi'
#                 elif header == "SH":
#                     header = 'skor_harga'
#                 elif header == "SA":
#                     header = 'skor_akhir'
#                 elif header == "K":
#                     header = 'evaluasi_kualifikasi'
#                 elif header == "SK":
#                     header = 'skor_kualifikasi'
#                 elif header == "SB":
#                     header = 'skor_pembuktian'
#                 elif header == "H":
#                     header = 'evaluasi_harga/biaya'
#                 elif header == "PK":
#                     header = 'pemenang_berkontrak'
#                 elif header == "B":
#                     header = 'pembuktian_kualifikasi'
                
#                 item[header] = value
            
#             yield item

#         collected_data['hasil_evaluasi'] = tender_hasil
        
#         #     for tbody_row in row.css('tbody > tr'):
#         #         values = tbody_row.css('td::text, td > i::attr(class), td > img::attr(src)').getall()
#         #         values = [value.strip() for value in values]
#         #         values = [value for value in values if value]
#         #         if not values:
#         #             continue
#         #         if len(headers) == len(values):
#         #             row_data = dict(zip(headers, values))
#         #             tender_hasil.appe nd(row_data)
#         #         else:
#         #             row_data = {}
#         #             for header, value in zip(headers, values):
#         #                 if values == '/eproc4/public/images/star.gif':
#         #                     header = 'pemenang'
#                 #         elif header == "A":
#                 #             row_data['evaluasi_administrasi'] = value
#                 #         elif header == "T":
#                 #             row_data['evaluasi_teknis'] = value
#                 #         elif header == "ST":
#                 #             row_data['skor_teknis'] = value
#                 #         # elif header == "P":
#                 #         #     row_data['penawaran'] = value
#                 #         elif header == "PT":
#                 #             row_data['penawaran_terkoreksi'] = value
#                 #         elif header == "HN":
#                 #             row_data['hasil_negosiasi'] = value
#                 #         elif header == "SH":
#                 #             row_data['skor_harga'] = value
#                 #         elif header == "SA":
#                 #             row_data['skor_akhir'] = value
#                 #         elif header == "K":
#                 #             row_data['evaluasi_kualifikasi'] = value
#                 #         elif header == "SK":
#                 #             row_data['skor_kualifikasi'] = value
#                 #         elif header == "SB":
#                 #             row_data['skor_pembuktian'] = value
#                 #         elif header == "H":
#                 #             row_data['evaluasi_harga/biaya'] = value
#                 #         # elif header == "P":
#                 #         #     row_data['pemenang'] = value
#                 #         elif header == "PK":
#                 #             row_data['pemenang_berkontrak'] = value
#                 #         elif header == "B":
#                 #             row_data['pembuktian_kualifikasi'] = value
#                     #     else:
#                     #         row_data[header.lower()] = value

#                     # tender_hasil.append(row_data)
#         collected_data['hasil_evaluasi'] = tender_hasil

#         url = response.url.replace('hasil', 'pemenang').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_pemenang, headers=self.headers, cookies=self.cookies, meta={'collected_data': collected_data.copy(), 'kode_api':kode_api } )

#     def tender_pemenang(self, response):
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']

#         tables = response.css('#main > div > table')
#         pemenang = []
#         for row in tables:
#             nama_tender = row.css('tr:nth-child(1) > td::text').get()
#             jenis_pengadaan = row.css('tr:nth-child(2) > td::text').get()
#             klpd_dan_instansi_lainnya = row.css('tr:nth-child(3) > td::text').get()
#             satuan_kerja = row.css('tr:nth-child(4) > td::text').get()
#             pagu = row.css('tr:nth-child(5) > td::text').get()
#             hps = row.css('tr:nth-child(6) > td::text').get()

#             pemenang_data = {
#                 'nama_tender': nama_tender,
#                 'jenis_pengadaan': jenis_pengadaan,
#                 'klpd_dan_instansi_lainnya': klpd_dan_instansi_lainnya,
#                 'satuan_kerja': satuan_kerja,
#                 'pagu': pagu,
#                 'hps': hps
#             }

#             table_2 = row.css('tr:nth-child(7) > td > table > tr:nth-child(2)')
#             detail_pemenang = []
#             for row2 in table_2:
#                 nama_tender = row2.css('td:nth-child(1)::text').get()
#                 alamat = row2.css('td:nth-child(2) *::text').getall()
#                 npwp = row2.css('td:nth-child(3)::text').get()
#                 harga_penawaran = row2.css('td:nth-child(4)::text').get()
#                 harga_koreksi = row2.css('td:nth-child(5)::text').get()
#                 harga_negoisasi = row2.css('td:nth-child(6)::text').get()

#                 detail_pemenang_data = {
#                     'nama_tender': nama_tender.strip(),
#                     'alamat': alamat,
#                     'npwp': npwp,
#                     'harga_penawaran': harga_penawaran,
#                     'harga_koreksi': harga_koreksi,
#                     'harga_negoisasi': harga_negoisasi
#                 }
#                 detail_pemenang.append(detail_pemenang_data)

                

#             pemenang_data['detail_pemenang'] = detail_pemenang
#             pemenang.append(pemenang_data)

#         collected_data['pemenang'] = pemenang
        

#         url = response.url.replace('pemenang','pemenangberkontrak').replace('lelang','evaluasi')
#         if url:
#             yield scrapy.Request(url, callback=self.tender_pemenang_berkontrak, headers=self.headers, cookies=self.cookies, meta={'collected_data':collected_data.copy(), 'kode_api':kode_api } )

#     def tender_pemenang_berkontrak(self, response):
#         # ss = response.css('#main > div > table > tr:nth-child(1) > td::text').get()
#         kode_api = response.meta['kode_api']
#         collected_data = response.meta['collected_data']
        


#         tables = response.css('#main > div > table')
#         pemenang_berkontrak = []
#         for row in tables:
#             nama_tender = row.css('tr:nth-child(1) > td::text').get()
#             jenis_pengadaan = row.css('tr:nth-child(2) > td::text').get()
#             klpd_dan_instansi_lainnya = row.css('tr:nth-child(3) > td::text').get()
#             satuan_kerja = row.css('tr:nth-child(4) > td::text').get()
#             pagu = row.css('tr:nth-child(5) > td::text').get()
#             hps = row.css('tr:nth-child(6) > td::text').get()

#             pemenang_berkontrak_data = {
#                 'nama_tender': nama_tender,
#                 'jenis_pengadaan': jenis_pengadaan,
#                 'klpd_dan_instansi_lainnya': klpd_dan_instansi_lainnya,
#                 'satuan_kerja': satuan_kerja,
#                 'pagu': pagu,
#                 'hps': hps
#             }

#             table_2 = row.css('tr:nth-child(7) > td > table > tr:nth-child(2)')
#             detail_pemenang_berkontrak = []
#             for row2 in table_2:
#                 nama_pemenang = row2.css('td:nth-child(1)::text').get()
#                 alamat = row2.css('td:nth-child(2) *::text').getall()
#                 npwp = row2.css('td:nth-child(3)::text').get()
#                 harga_kontrak = row2.css('td:nth-child(4)::text').get()
#                 nilai_pdn = row2.css('td:nth-child(5)::text').get()
#                 nilai_umk = row2.css('td:nth-child(6)::text').get()

#                 detail_pemenang_berkontrak_data = {
#                     'nama_pemenang': nama_pemenang.strip(),
#                     'alamat': alamat,
#                     'npwp': npwp,
#                     'harga_kontrak': harga_kontrak,
#                     'nilai_pdn': nilai_pdn,
#                     'nilai_umk': nilai_umk
#                 }
#                 detail_pemenang_berkontrak.append(detail_pemenang_berkontrak_data)

#             pemenang_berkontrak_data['detail_pemenang_berkontrak'] = detail_pemenang_berkontrak
#             pemenang_berkontrak.append(pemenang_berkontrak_data)

#         collected_data['pemenang_berkontrak'] = pemenang_berkontrak

#         dir_raw = 'data'
#         os.makedirs(dir_raw ,exist_ok=True)
#         filename = f'{kode_api}.json'
#         save_json(collected_data, os.path.join(dir_raw, filename))