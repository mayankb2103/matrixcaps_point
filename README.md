##### Download the dataset

`python modelnet40_downloader.py` 
##### Start training
`python train.py modelnet40`

###Questions
1) Why exponential learning rate decay?
2) Does extracting 2048 point instead of 1024 can help?
3) Why spread loss increases after every epoch and decreases within an epoch? 
   - Does it has something to do with shuffling of data. But code doesn't seems to shuffle after ever epoch and even if it does, it shouldn't work like that
   - Will Removing decoder network make network learn anything?


UPDATE @ 1pm: Decoder network removed. Network also doesnt seem to learn anything

Training going on my 2GB GPU -_-. Abhishek sir ne unke tanthe khade kar diye hai.

As for Right now, I am officially stuck.


   
    

