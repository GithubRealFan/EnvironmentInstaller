for no in $(seq 1 15); 
    do btcli register --subtensor.network finney --netuid 1 --wallet.name WALLETNAME --wallet.hotkey $no --cuda.TPB 512 --cuda.update_interval 800000 --cuda.dev_id 0 1 2 3 4 5 6 7 --cuda.use_cuda  --logging.debug --no_prompt; 
done