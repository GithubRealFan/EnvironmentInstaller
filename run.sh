#!/bin/bash

# btcli regen_coldkeypub --ss58 5DxyxnZM6aqJT4HQAogmf3esE5fFvsokBjpZugg3HD1zyuAs --wallet.name alice
# btcli regen_hotkey --wallet.name alice --wallet.hotkey 1 --mnemonic stool link heart swallow dilemma wild design kingdom multiply own detect rack

for no in $(seq 1 25); 
    do btcli register --subtensor.network finney --netuid 1 --wallet.name alice --wallet.hotkey $no --cuda.TPB 512 --cuda.update_interval 800000 --cuda.dev_id 0 1 2 3 4 5 6 7 --cuda.use_cuda  --logging.debug --no_prompt;
done