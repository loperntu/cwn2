tsv=read.table(file='ratings.tsv',header=FALSE,sep=' ')
plot(tsv$V1,xlab='merged sense',ylab='5-point Likert scale',type='l')
lines(tsv$V2,col='red',lty=2)
lines(tsv$V3,col='blue',lty=3)