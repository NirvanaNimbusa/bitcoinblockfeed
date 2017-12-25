from pathlib import Path
import requests
import json

file_info = Path('lastblock.txt').read_text()

blockres = requests.get("https://api.blocktrail.com/v1/btc/block/latest?api_key=[YOUR API KEY HERE]")
newblock_json = json.loads(blockres.text)

block_id = str(newblock_json['height'])

if block_id > file_info:
 with open("lastblock.txt", "w") as text_file:
  print(block_id, file=text_file)
else:
 exit()

block_info = requests.get("https://api.blockchair.com/bitcoin/blocks?q=id(%s)"%(block_id))
bi_json = json.loads(block_info.text)

mining_pool = str( newblock_json['miningpool_name'])
block_height = str( bi_json['data'][0]['id'])
block_hash = str( bi_json['data'][0]['hash'])
block_size = str (format((int(bi_json['data'][0]['size']))/1024, '.2f'))
block_trx =  str (bi_json['data'][0]['transaction_count'])
block_time = str (bi_json['data'][0]['time'])

trxfee_info = requests.get("https://api.blockchair.com/bitcoin/mempool/transactions?q=block_id(%s)&s=fee_per_kb(asc)"%(block_id))
tf_json = json.loads(trxfee_info.text)

try:
 trx_id = str(tf_json['data'][1]['hash'])
 trx_fee = str('{:f}'.format(int(tf_json['data'][1]['fee'])/100000000))
 trx_fpb = str(int(tf_json['data'][1]['fee_per_kb'])/1000)
 
 url_block = "https://api.telegram.org/bot[TELEGRAM BOT API KEY]/sendMessage?chat_id=@[USERNAME OF TELEGRAM CHANNEL]&text=<pre>New block mined!</pre>\n\n<code>Mining Pool: %s\nHeight: %s\nHash: %s\nSize(KB): %s\nTransactions: %s\nTime: %s UTC</code>&parse_mode=HTML"%(mining_pool,block_height,block_hash,block_size,block_trx,block_time)
 post_msg1 = requests.get(url_block)

 url_trx = "https://api.telegram.org/bot[TELEGRAM BOT API KEY]/sendMessage?chat_id=@[USERNAME OF TELEGRAM CHANNEL]&text=<pre>Lowest fee transaction in block %s:</pre>\n\n<code>Tx ID: %s\nFees: %s BTC\nFees per byte: %s sat/byte</code>&parse_mode=HTML"%(block_height,trx_id,trx_fee,trx_fpb)
 post_msg2 = requests.get(url_trx)
 
#Exception for handling the blocks with only 1 transaction i.e. empty blocks

except:
 trx_id = str(tf_json['data'][0]['hash'])
 trx_fee = str('{:f}'.format(int(tf_json['data'][0]['fee'])/100000000))
 trx_fpb = str(int(tf_json['data'][0]['fee_per_kb'])/1000)
 
 url_block = "https://api.telegram.org/bot[TELEGRAM BOT API KEY]/sendMessage?chat_id=@[USERNAME OF TELEGRAM CHANNEL]&text=<pre>New block mined!</pre>\n\n<code>Mining Pool: %s\nHeight: %s\nHash: %s\nSize(KB): %s\nTransactions: %s\nTime: %s UTC</code>&parse_mode=HTML"%(mining_pool,block_height,block_hash,block_size,block_trx,block_time)
 post_msg1 = requests.get(url_block)

 url_trx = "https://api.telegram.org/bot[TELEGRAM BOT API KEY]/sendMessage?chat_id=@[USERNAME OF TELEGRAM CHANNEL]&text=<pre>Lowest fee transaction in block %s:</pre>\n\n<code>Tx ID: %s\nFees: %s BTC\nFees per byte: %s sat/byte</code>&parse_mode=HTML"%(block_height,trx_id,trx_fee,trx_fpb)
 post_msg2 = requests.get(url_trx)
