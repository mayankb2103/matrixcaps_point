##### Download the dataset

`python modelnet40_downloader.py` 
##### Start training
`python train.py modelnet40`

### Questions
1) Why exponential decay of learning rate?
2) Does extracting 2048 points instead of 1024 can help?
3) Why spread loss increases after every epoch and decreases within an epoch? 
   - Does it has something to do with shuffling of data. But code doesn't seems to shuffle after ever epoch and even if it does, it shouldn't work like that
   - Will Removing decoder network make network learn anything? Removing decoder network, reduces parmater by 1/6th(4.8L to 0.8L). Decoder work as heavy_penalty for high_loss.
   - What can be alternative for decoder for 3d Point cloud?


UPDATE @ 1pm: Decoder network removed. Network also doesn't seem to learn anything.

Training going on my 2GB GPU -_-. Abhishek sir ne unke tanthe khade kar diye hai.

As for right now, I am officially stuck and will read papers of cudenet and 3d point capsnet for some ideas. 

https://lectures.quantecon.org/jl/orth_proj.html

