#Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators, including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.

#Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.

fh=open('SP500.txt','r')
txt=fh.readlines()
fh.close()
#should be average
mean_SP=float('0')
sp_counter=0
sp_total=float('0')
#should be highest
max_interest=float('0')
sp500_col=0
ltir_col=0
header=txt.pop(0).strip().split(',')
for word in header:
    if word=='SP500':
        sp500_col=header.index(word)
        print('SP500 Column is:',sp500_col)
    elif word=='Long Interest Rate':
        ltir_col=header.index(word)
        print('Long Interest Rate Column is:',ltir_col)
max_interest=float(txt[0].strip().split(',')[ltir_col])

for line in txt:
    if ((int(line.strip().split(',')[0].split('/')[0])>=6 and int(line.strip().split(',')[0].split('/')[2])==2016) or (int(line.strip().split(',')[0].split('/')[0])<=5 and int(line.strip().split(',')[0].split('/')[2])==2017)):
        sp_counter+=1
        sp_total=sp_total+float(line.strip().split(',')[sp500_col])
        if float(line.strip().split(',')[ltir_col])>max_interest:
            max_interest=float(line.strip().split(',')[ltir_col])
mean_SP=sp_total/sp_counter
print('SP500 Average is:',mean_SP)
print('Long Interest Rate Max is:',max_interest)
