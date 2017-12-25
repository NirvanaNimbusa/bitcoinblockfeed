# bitcoinblockfeed

Telegram Channel to get notifications about each Bitcoin block found and lowest fee trx in the block.

<p align="center"> <img src="https://github.com/prayank23/bitcoinblockfeed/blob/master/screenshot.jpg?raw=true" width="300" height="450"/> </p>

Steps:

1. Create a telegram bot using @BotFather, get the API key
2. Create a public telegram channel, add the bot as administrator in channel which can post messages
3. The code uses APIs from "blocktrail" and "blockchair", sign up on blocktrail to get the API key
4. Copy all the files to your linux machine and run the blockfeed.py file after making necessary changes in it like adding your API keys, telegram channel username etc.
5. The script needs to run every 7 seconds automatically to check if a new block is found so you need to run the blockcron.sh in the background which will run py file every 7 seconds. 
<pre>chmod +x ./blockcron.sh
nohup ./blockcron.sh &</pre>
6. There is also a text file lastblock.txt which is used to saved the block height of the last block found and compare it when the script runs next time
7. Lowest fee transaction in the block is selected based on transactions sorted in ascending order by "fees per kb". 

Blockchair APIs are not reliable and may not work with 100% uptime. You can check with them about any issues related to API. Feel free to contact me if any questions: Telegram: @prayankgahlot Twitter: @prayankgahlot
